<script>
    import {onMount} from "svelte";
    let customers = [];
    onMount(()=>{
        download();
    })
    async function download() {
        const response = await fetch("/api/v1/customers/orders");
        const results = await response.json();
        if(results){
            console.log(results);
            customers = results;
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
        {#each customers as customer, i}
             <tr>
                <td>{(i + 1)}</td>
                <td>{customer['first_name']}</td>
                <td>{customer['last_name']}</td>
                <td>{customer['dob']}</td>
                <td>{customer['address']}</td>
                <td>{customer['email']}</td>
                <td>{customer['date_registered']}</td>
                <td><button class="button">View Orders</button></td>
             </tr>
        {/each}
    </tbody>
</table>