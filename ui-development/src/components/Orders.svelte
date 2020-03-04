<script>
    import {onMount} from "svelte";
    import TableOrders from "./stats/TableOrders.svelte";
    export let title = "TEST";
    let table;
    let orders;

    onMount(() =>{
        download();
    });

    async function download(){
        const response = await fetch('/api/v1/orders');
        const results = await response.json();
        if(results) {

            results.forEach(order => {
                order['order_date'] = formatDate(order['order_date'])
            });
            orders = results;
        }
    }

    export function refresh(){
        download();
    }

     function formatDate(date){
        var dte = new Date(Date.parse(date));
        dte.setDate(dte.getDate() + 1);
        var year = dte.getFullYear();
        var month = (dte.getMonth() + 1 < 10) ? `0${dte.getMonth() + 1}` : dte.getMonth() + 1;
        var day = (dte.getDate() < 10) ? `0${dte.getDate()}` : dte.getDate();

        return `${year}-${month}-${day}`;
    }

    function handleResults(e) {
        orders = e.detail;
    }
    function handleKeyDown(e) {
        //console.log(e);
        //On Enter Search the information...
        //Get the html element so we can get the value...
        var input = e.target || e.srcElement;
        if(e.keyCode == 13){
            
            var value = input.value.toLowerCase();
           
            orders = orders.filter(order => 
                order['order_name'].toLowerCase().includes(value) 
                || order['order_date'].toLowerCase().includes(value)
                || order['order_total'].toString().includes(value)
            );

            
            
        }else if(e.keyCode == 8 || input.value.length == 0){
            download();
        }
    }
</script>
<div class="panel mt4" >
        <div class="panel-content" >
            <TableOrders {orders} on:eitem on:refresh on:results={handleResults} bind:this={table} /> 
        </div>
        <div class="panel-title">
            
            <span class="caption">{title}
                <div style="position: absolute;top: 2px;width: 70%;left: 188px;" class="input">
                    <input on:keydown={handleKeyDown} placeholder="Search Customers" type="text" />
                </div>
            </span>
            <span class="mif-apps icon"></span>
            <span class="dropdown-toggle marker-center active-toggle"></span>
            
        </div>
</div>