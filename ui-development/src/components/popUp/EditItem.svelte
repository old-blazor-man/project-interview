<script>
    import {onMount, createEventDispatcher} from "svelte";
    const dispatch = createEventDispatcher();
    export let item;
    let oname;
    let ototal;
    let odate;
    let orderid;

    onMount(() => {
        
        oname = item.order_name;
        ototal = item.order_total;
        odate = item.order_date;
        orderid = item.orderid;
     
    })

    function handleSubmit() {
        var form = new FormData();
        form.append("oname", oname);
        form.append("ototal", ototal);
        form.append("odate", odate);
        form.append("orderid", orderid);
        fetch("/api/v1/update/order", {
            method: 'post',
            body: form,
        }).then(()=>{
            dispatch("refresh");
        });

    }


</script>
<style>
    .window{
        position: absolute;
        width: 600px;
        height: 350px;
        top: 50%;
        left: 50%;
        margin-left: -300px;
        margin-top: -125px;
    }
    .window-content {
        overflow: auto;
    }

</style>
<div class="window">
    <div class="window-caption">
        <span class="icon mif-cart"></span>
        <span class="title">Edit Item - {item['order_name']}</span>
        <div class="buttons">
          
            <span on:click="{()=>{dispatch("close", false)}}" class="btn-close"></span>
        </div>
    </div>
    <div class="window-content p-2">
        <form>
            <div class="form-group">
                <label>Order Name</label>
                <input bind:value={oname} type="text" placeholder="Enter First Name"/>
                
            </div>
            <div class="form-group">
                <label>Order Total</label>
                <input bind:value={ototal} type="number" placeholder="Enter Middle Name"/>
                
            </div>

            <div class="form-group">
                <label>order_date</label>
                <div class="input calendar-picker">
                      <input bind:value={odate} type="date" placeholder="Enter DOB"/>
                </div>
              
            </div>
           
            <div class="form-group">
                <button on:click|preventDefault={handleSubmit} class="button success">Update Order</button>
                <input on:click="{()=>{dispatch("close", false)}}" type="button" class="button" value="Cancel">
            </div>
        </form>
    </div>
</div>
