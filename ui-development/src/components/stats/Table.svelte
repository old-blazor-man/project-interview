<script>
    import {onMount, createEventDispatcher} from "svelte";
    import TableOrders from "./TableOrders.svelte";
    let customers = [];

    const dispatch = createEventDispatcher();
    onMount(()=>{
        download();
    })
    async function download() {
        const response = await fetch("/api/v1/customers/orders");
        const results = await response.json();
        if(results){
           
            customers = results;
            dispatch("results", results);
        }
    }
    export function refresh(){
        download();
    }

 
</script>
<table class="table compact">
    <thead>
    <tr>
        <th>#</th>
        <th>First Name</th>
        <th>Last Name</th>
        <th>Date Of Birth</th>
        <th>Address</th>
        <th>E-Mail</th>
        <th>Date Registered</th>
        <th></th>
    </tr>
    </thead>
    <tbody>
        {#each customers as {user}, i}
             <tr>
                <td>{(i + 1)}</td>
                <td>{user['first_name']}</td>
                <td>{user['last_name']}</td>
                <td>{user['dob']}</td>
                <td>{user['address']}</td>
                <td>{user['email']}</td>
                <td>{user['date_registered']}</td>
                <td><button on:click="{()=>{user['orderview'] = (user['orderview'] == 0) ? 1 : 0;}}" class="button">View Orders</button></td>
                
             </tr>
            {#if user['orderview'] == 1}
              <tr>
                <td>
                    <TableOrders on:refresh orders={user['orders']} />
                </td> 
              </tr>
            {/if}
        {/each}
    </tbody>
</table>