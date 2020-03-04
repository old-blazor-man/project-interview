<script>
    import {onMount, createEventDispatcher} from "svelte";
    let total = 0;
    const dispatch = createEventDispatcher();
    onMount(()=>{
        download();
    });
    async function download() {
        const response = await fetch("/api/v1/total/orders/Year");
        const results = await response.json();
        if(results){
          
            total = results['total']
        }
    }
    export function refresh(){
        download();
    }

</script>
<div class="more-info-box bg-cyan fg-white">
            <div class="content">
                <h2 class="text-bold mb-0">{total}</h2>
                <div>Total Orders By Year</div>
            </div>
            <div class="icon">
                <span class="mif-cart"></span>
            </div>
            <a  on:click|preventDefault="{()=>{dispatch('orders',true)}}" href="#Hello" class="more"> More info <span class="mif-arrow-right"></span></a>
</div>