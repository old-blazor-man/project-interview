<script>
    import {onMount, createEventDispatcher} from "svelte";
    const dispatch = createEventDispatcher();
    
    let ordername;
    let orderdate = new Date();
    let ordertotal;
    let cus_id;
    let customers = [];
    let keeptrack = [];
    onMount(async() => {
        var response = await fetch("/api/v1/customers");
        var results = await response.json();
        if(results) {
            customers = results;
        }
    });
    function handleSubmit() {
        var form = new FormData();
        form.append("orders", JSON.stringify(keeptrack));
        
        fetch("/api/v1/add/orders", {
            method: 'post',
            body: form,
        }).then(()=>{
            dispatch("refresh");
        });

    }

    function addOrders(){
        
        keeptrack = [...keeptrack, {"customerid" : cus_id,"orderdate": formatDate(orderdate), "ordername" : ordername, "ordertotal" : ordertotal}];
        ordername = "";
        ordertotal = 0;
       
    }

    function formatDate(date){
        if(date instanceof Date) {
            var year = date.getFullYear();
            var month = (date.getMonth() + 1 < 10) ? `0${date.getMonth() + 1}` : date.getMonth();
            var day = (date.getDate() < 10) ? `0${date.getDate()}` : date.getDate();
            return `${year}-${month}-${day}`;
        }
        return date;
    }

    function changeTab(){
        var docid = this.hash.replace("#", "");
        var element = document.getElementById(docid);
        var li = document.getElementById(`${docid}li`);

        var actives = document.querySelectorAll(".active");
        actives.forEach(ele => {
            if(ele.tagName == "DIV"){
                ele.style.display = "none";
            }
            ele.classList.remove("active"); 
        });
        li.classList.add("active");
        element.style.display = "";
        element.classList.add("active");
    }
    function removeOrder(index) {
        keeptrack.splice(index, 1);
        keeptrack = keeptrack;
    }


</script>
<style>
    .window{
        position: absolute;
        width: 600px;
        height: 640px;
        top: 50%;
        left: 50%;
        margin-left: -300px;
        margin-top: -320px;
    }
    .window-content {
        overflow: auto;
    }



</style>
<div class="window">
    <div class="window-caption">
        <span class="icon mif-cart"></span>
        <span class="title">Add Order</span>
        <div class="buttons">
            <span on:click="{()=>{dispatch("close", false)}}" class="btn-close"></span>
        </div>
    </div>
    <div class="window-content p-2">
        <button on:click={handleSubmit} class="button w-100 primary">Submit Data</button>
        <div class="tabs tabs-wrapper top tabs-expand" >
            <ul class="tabs-list">
                <li id="addli" class="active">
                    <a on:click|preventDefault={changeTab} href="#add">Home</a></li>
                <li id="ordersli">
                    <a on:click|preventDefault={changeTab} href="#orders">Orders</a></li>
            </ul>
        </div>
        
    <div class="border bd-default no-border-top p-2">
        <div id="add" class="active">
            <form>
                    <select bind:value={cus_id}>
                            <option value="-1">Select Customer</option>
                        {#each customers as {customerid, first_name, last_name}, i}
                            <option value={customerid}>{`${first_name} ${last_name}`}</option>
                        {/each}
                    </select>
                    <br/>
                    <h2>Add Orders</h2>
                    <div class="form-group">
                        <label>Order Name</label>
                        <input bind:value={ordername} type="text" placeholder="Enter First Name"/>
                    </div>
                    <div class="form-group">
                        <label>Order Total</label>
                        <input bind:value={ordertotal} type="text" placeholder="Enter Middle Name"/>
                    </div>
                    <div class="form-group">
                        <label>Order Date: {formatDate(orderdate)}</label>
                        
                    </div>


                    
                    <div class="form-group">
                        <button on:click|preventDefault={addOrders} class="button success">Add Order</button>
                        <input on:click="{()=>{dispatch("close", false)}}" type="button" class="button" value="Cancel">
                    </div>
            </form>
        </div>
        <div style="display: none;" id="orders">
           
            <table class="table compact">
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Order Name</th>
                        <th>Order Total</th>
                        <th>Order Date</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody> 
                    {#each keeptrack as {orderdate, ordername, ordertotal}, i}
                         <tr>
                            <td>{(i + 1)}</td>
                            <td>{ordername}</td>
                            <td>{ordertotal}</td>
                            <td>{orderdate}</td>
                            <td><button on:click="{()=>{removeOrder(i)}}" class="button alert">DELETE</button></td>
                         </tr>
                    {/each}
                
                </tbody>
            </table>
        </div>
    </div>


        
    </div>
</div>
