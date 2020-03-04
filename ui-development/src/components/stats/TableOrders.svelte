<script>
    import {createEventDispatcher} from "svelte";
    export let orders = [];
    const dispatch = createEventDispatcher();
    
    function removeOrder(index) {
  
        var form = new FormData();
        form.append("orderid", orders[index]['orderid']);
        
        fetch("/api/v1/delete/order", {
            method: 'post',
            body: form,
        }).then(()=>{
            dispatch("refresh");
        });
       
    }
</script>
<table class="table compact"  style="padding-left:100px;" cellspacing="0" cellpadding="5" border="0">
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
        {#each orders as  order, i}
             <tr >
                <td>{(i + 1)}</td>
                <td>{order['order_name']}</td>
                <td>{order['order_total']}</td>
                <td>{order['order_date']}</td>
                <td>
                    <button class="button" on:click="{()=>{removeOrder(i)}}">Delete</button>
                    <button class="button" on:click="{()=>{dispatch('eitem',order)}}">Edit Item</button>
                </td>
            </tr>
        {/each}
        
    </tbody>
</table>