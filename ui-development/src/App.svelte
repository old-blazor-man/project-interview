<script>
  //Main COMPONENT...
  //LOAD THE QUICK STATS...
  import TotalOrders from "./components/stats/TotalOrders.svelte";
  import TotalCustomers from "./components/stats/TotalCustomers.svelte";
  import AppBar from "./components/Header/AppBar.svelte";
  import CustomerOrders from "./components/CustomerOrders.svelte";
  import CustomersInfo from "./components/CustomersInfo.svelte";
  import AddUser from "./components/popUp/AddUser.svelte";
  import AddOrders from "./components/popUp/AddOrder.svelte";
  import EditItem from "./components/popUp/EditItem.svelte";
  import EditUser from "./components/popUp/EditUser.svelte";


  let title = "Starbucks Store";
  let displayCustomer = false;
  let displayOrder = false;
  let displayEditItem = false;
  let displayEditUser = false;
  let viewCustomers = false;

  let customer;
  let totalOrders;
  let totalCustomers;
  let user;
  let item;

  function handleRefresh() {
      displayCustomer = false;
      displayEditUser = false;
      customer.refresh();
      totalOrders.refresh();
      totalCustomers.refresh();

  }

  function handleEditUser(e) {
      displayEditUser = true;
      user = e.detail;
  }

  function handleEditItem(e){
      displayEditItem = true;
      item = e.detail;
  }

  function handleCustomers(e){
      viewCustomers = e.detail;

  }

</script>
<div data-role="navview" data-toggle="#paneToggle" data-expanded="xl" data-compact="lg" data-active-state="true" class="navview compact-lg expanded-xl" data-role-navview="true">
    <div class="navview-pane">
        <div class="bg-cyan d-flex flex-align-center">
            <button class="pull-button m-0 bg-darkCyan-hover">
                <span class="mif-menu fg-white"></span>
            </button>
            <h2 class="text-light m-0 fg-white pl-7" style="line-height: 52px">{title}</h2>
        </div>

        <div class="suggest-box">
            <div class="data-box">
                <img alt="ICON" src="https://metroui.org.ua/themes/pandora/images/jek_vorobey.jpg" class="avatar">
                <div class="ml-4 avatar-title flex-column">
                    <a href="#quite" class="d-block fg-white text-medium no-decor"><span class="reduce-1">Jack Sparrow</span></a>
                    <p class="m-0"><span class="fg-green mr-2">●</span><span class="text-small">online</span></p>
                </div>
            </div>
            <img alt="ICON" src="https://metroui.org.ua/themes/pandora/images/jek_vorobey.jpg" class="avatar holder ml-2">
        </div>

        
        <div class="w-100 text-center text-small data-box p-2 border-top bd-grayMouse" style="position: absolute; bottom: 0">
            <div>© 2019 <a href="mailto:sergey@pimenov.com.ua" class="text-muted fg-white-hover no-decor">Sergey Pimenov</a></div>
            <div>Created with <a href="https://metroui.org.ua" class="text-muted fg-white-hover no-decor">Metro 4</a></div>
        </div>
    </div>

    <div class="navview-content h-100">
       <AppBar on:addorder="{(e) =>{displayOrder = e.detail;}}" on:adduser="{(e) =>{displayCustomer = e.detail;}}" />

        <div id="content-wrapper" class="content-inner h-100" style="overflow-y: auto"><div class="row border-bottom bd-lightGray m-3">
            <div class="cell-md-4 text-center text-left-md">
                <h3 class="dashboard-section-title">{title} <small>Version 1.0</small></h3>
            </div>

    <div class="cell-md-8 d-flex flex-justify-center flex-justify-end-md">
        <ul class="breadcrumbs bg-transparent">
            <li class="page-item"><a href="#test" class="page-link"><span class="mif-meter"></span></a></li>
            <li class="page-item"><a on:click|preventDefault="{()=>{viewCustomers = false;}}" href="#test" class="page-link">Dashboard</a></li>
        </ul>
    </div>
</div>

<div class="m-3">
    <div class="row mt-2">
    
    </div>

<div class="row">
    <div class="cell">
        <TotalOrders bind:this={totalOrders} />
    </div>
    <div class="cell">
        <TotalCustomers on:customers={handleCustomers} bind:this={totalCustomers} />
    </div>
</div>
    {#if viewCustomers}
         <CustomersInfo on:edit="{handleEditUser}" on:refresh={handleRefresh} title="Customers" bind:this={customer} />
    {:else}
        <CustomerOrders on:edit="{handleEditUser}" on:eitem={handleEditItem} on:refresh={handleRefresh} bind:this={customer} title="Customer/Orders" />
    {/if}
    
</div>
</div>
    </div>
</div>



{#if displayCustomer}
     <AddUser on:refresh={handleRefresh} on:close="{(e)=>{displayCustomer = e.detail;}}" />
{:else if  displayOrder}
      <AddOrders on:refresh={handleRefresh} on:close="{(e)=>{displayOrder = e.detail;}}" />
{:else if displayEditItem}
    <EditItem {item} on:refresh={handleRefresh} on:close="{(e)=>{displayEditItem = e.detail}}" />
{:else if displayEditUser}
    <EditUser on:refresh={handleRefresh} on:close="{(e)=>{displayEditUser = e.detail}}" {user} />
{/if}