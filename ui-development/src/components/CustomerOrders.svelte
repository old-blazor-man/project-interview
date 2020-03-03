<script>
    import Table from "./stats/Table.svelte";
    export let title = "TEST";
    let table;
    export function refresh(){
        table.refresh();
    }
</script>
<div class="panel mt4" >
        <div class="panel-content" >
            <Table bind:this={table} /> 
        </div>
        <div class="panel-title">
            <span class="caption">{title}</span>
            <span class="mif-apps icon"></span>
            <span class="dropdown-toggle marker-center active-toggle"></span>
        </div>
</div>