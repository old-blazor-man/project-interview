<script>
    import {onMount, createEventDispatcher} from "svelte";
    import TableOrders from "./TableOrders.svelte";
    let customers = [];

    const dispatch = createEventDispatcher();
    onMount(()=>{
        download();
    })
    async function download() {
        const response = await fetch("/api/v1/customers");
        const results = await response.json();
        if(results){
           
            customers = results;
            
            dispatch("results", results);
        }
    }
    export function refresh(){
        download();
    }

    export function setCustomers(records) {
        customers = records;
    }

    function handlePrompt(user) {
        let response = confirm('Are you sure?');
        if(response) {
            var form = new FormData();
            form.append("customerid", user['customerid']);
        
            fetch("/api/v1/delete/customer",{
            method: 'post',
            body: form,
        }).then((response) =>{
                download();
                dispatch("refresh");
            });
        }
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
        {#each customers as user, i}
             <tr>
                <td>{(i + 1)}</td>
                <td>{user['first_name']}</td>
                <td>{user['last_name']}</td>
                <td>{user['dob']}</td>
                <td>{user['address']}</td>
                <td>{user['email']}</td>
                <td>{user['date_registered']}</td>
                <td>
                    <button on:click="{()=>{handlePrompt(user)}}" class="button alert">Delete User</button>
                    <button on:click="{()=>{dispatch("edit", user)}}" class="button">Edit User</button>
                </td>
                
             </tr>
        {/each}
    </tbody>
</table>