<script>
    import Table from "./stats/Table.svelte";
    export let title = "TEST";
    let table;
    let results;
    export function refresh(){
        table.refresh();
    }

    function handleResults(e) {
        results = e.detail;
    }
</script>
<div class="panel mt4" >
        <div class="panel-content" >
            <Table on:refresh on:results={handleResults} bind:this={table} /> 
        </div>
        <div class="panel-title">
            
            <span class="caption">{title}
                <div style="position: absolute;top: 2px;width: 70%;left: 188px;" class="input">
                    <input placeholder="Search Customers" type="text" />
                </div>
            </span>
            <span class="mif-apps icon"></span>
            <span class="dropdown-toggle marker-center active-toggle"></span>
            
        </div>
</div>