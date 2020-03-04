<script>
    //This Component handles all the total customers 
    //Display Quick Stats..
    import {onMount, createEventDispatcher} from "svelte";

    let total = 0;
    
    const dispatch = createEventDispatcher();
    onMount( ()=>{
        download();
        
    });

    async function download(){
        const response = await fetch("/api/v1/total/customers")
        const results = await response.json();
        if(results){
            total = results['total'];
        }
    }

    export function refresh(){
        download();
    }

</script>
<div class="more-info-box bg-green fg-white">
            <div class="content">
                <h2 class="text-bold mb-0">{total}</h2>
                <div>Total Customers</div>
            </div>
            <div class="icon">
               <span class="mif-user-check"></span>
            </div>
            <a on:click|preventDefault="{()=>{dispatch('customers',true)}}" href="#test" class="more"> More info <span class="mif-arrow-right"></span></a>
</div>