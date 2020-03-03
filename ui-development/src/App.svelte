<script>
  //Main COMPONENT...
  //LOAD THE QUICK STATS...
  import TotalOrders from "./components/stats/TotalOrders.svelte";
  import TotalCustomers from "./components/stats/TotalCustomers.svelte";
  import AppBar from "./components/Header/AppBar.svelte";
  import CustomerOrders from "./components/CustomerOrders.svelte";
  import AddUser from "./components/popUp/AddUser.svelte";
  import AddOrders from "./components/popUp/AddOrder.svelte";
  import EditItem from "./components/popUp/EditItem.svelte";
  import EditUser from "./components/popUp/EditUser.svelte";


  let title = "Starbucks Store";
  let displayCustomer = false;
  let displayOrder = false;
  let displayEditItem = false;
  let displayEditUser = false;

  let customer;
  let totalOrders;
  let totalCustomers;
  let user;

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

        <ul class="navview-menu mt-4" id="side-menu" style="height: calc(100% - 225px);">
            <li class="item-header">MAIN NAVIGATION</li>
            <li class="active">
                <a href="#dashboard">
                    <span class="icon"><span class="mif-meter"></span></span>
                    <span class="caption">Dashboard</span>
                </a>
            </li>
            <li>
                <a href="#widgets">
                    <span class="icon"><span class="mif-widgets"></span></span>
                    <span class="caption">Widgets</span>
                </a>
            </li>
            <li>
                <a href="#" class="dropdown-toggle">
                    <span class="icon"><span class="mif-versions"></span></span>
                    <span class="caption">Sample Pages</span>
                </a>
                <ul class="navview-menu stay-open" data-role="dropdown" data-role-dropdown="true" style="display: none;">
                    <li class="item-header">Pages</li>
                    <li><a href="login.html">
                        <span class="icon"><span class="mif-lock"></span></span>
                        <span class="caption">Login</span>
                    </a></li>
                    <li><a href="register.html">
                        <span class="icon"><span class="mif-user-plus"></span></span>
                        <span class="caption">Register</span>
                    </a></li>
                    <li><a href="lockscreen.html">
                        <span class="icon"><span class="mif-key"></span></span>
                        <span class="caption">Lock screen</span>
                    </a></li>
                    <li><a href="#profile">
                        <span class="icon"><span class="mif-profile"></span></span>
                        <span class="caption">Profile</span>
                    </a></li>
                    <li><a href="preloader.html">
                        <span class="icon"><span class="mif-spinner"></span></span>
                        <span class="caption">Preloader</span>
                    </a></li>
                    <li><a href="404.html">
                        <span class="icon"><span class="mif-cancel"></span></span>
                        <span class="caption">404 Page</span>
                    </a></li>
                    <li><a href="500.html">
                        <span class="icon"><span class="mif-warning"></span></span>
                        <span class="caption">500 Page</span>
                    </a></li>
                    <li><a href="#product-list">
                        <span class="icon"><span class="mif-featured-play-list"></span></span>
                        <span class="caption">Product list</span>
                    </a></li>
                    <li><a href="#product">
                        <span class="icon"><span class="mif-rocket"></span></span>
                        <span class="caption">Product page</span>
                    </a></li>
                    <li><a href="#invoice">
                        <span class="icon"><span class="mif-open-book"></span></span>
                        <span class="caption">Invoice</span>
                    </a></li>
                    <li><a href="#orders">
                        <span class="icon"><span class="mif-table"></span></span>
                        <span class="caption">Orders</span>
                    </a></li>
                    <li><a href="#order-details">
                        <span class="icon"><span class="mif-library"></span></span>
                        <span class="caption">Order details</span>
                    </a></li>
                    <li><a href="#price-table">
                        <span class="icon"><span class="mif-table"></span></span>
                        <span class="caption">Price table</span>
                    </a></li>
                    <li><a href="maintenance.html">
                        <span class="icon"><span class="mif-cogs"></span></span>
                        <span class="caption">Maintenance</span>
                    </a></li>
                    <li><a href="coming-soon.html">
                        <span class="icon"><span class="mif-watch"></span></span>
                        <span class="caption">Coming soon</span>
                    </a></li>
                    <li>
                        <a href="help-center.html">
                            <span class="icon"><span class="mif-help"></span></span>
                            <span class="caption">Help center</span>
                        </a>
                    </li>
                </ul>
            </li>
            <li>
                <a href="#" class="dropdown-toggle">
                    <span class="icon"><span class="mif-devices"></span></span>
                    <span class="caption">Forms</span>
                </a>
                <ul class="navview-menu stay-open" data-role="dropdown" data-role-dropdown="true" style="display: none;">
                    <li class="item-header">Forms</li>
                    <li><a href="#forms-basic">
                        <span class="icon"><span class="mif-spinner2"></span></span>
                        <span class="caption">Basic elements</span>
                    </a></li>
                    <li><a href="#forms-extended">
                        <span class="icon"><span class="mif-spinner2"></span></span>
                        <span class="caption">Extended elements</span>
                    </a></li>
                    <li><a href="#forms-layouts">
                        <span class="icon"><span class="mif-spinner2"></span></span>
                        <span class="caption">Layouts</span>
                    </a></li>
                    <li><a href="#forms-validating">
                        <span class="icon"><span class="mif-spinner2"></span></span>
                        <span class="caption">Validating</span>
                    </a></li>
                </ul>
            </li>

            <li>
                <a href="#" class="dropdown-toggle">
                    <span class="icon"><span class="mif-table"></span></span>
                    <span class="caption">Tables</span>
                </a>
                <ul class="navview-menu stay-open" data-role="dropdown" data-role-dropdown="true" style="display: none;">
                    <li class="item-header">Tables</li>
                    <li><a href="#table-classes">
                        <span class="icon"><span class="mif-spinner2"></span></span>
                        <span class="caption">Table classes</span>
                    </a></li>
                    <li><a href="#table-component">
                        <span class="icon"><span class="mif-spinner2"></span></span>
                        <span class="caption">Table component</span>
                    </a></li>
                </ul>
            </li>

            <li>
                <a href="#" class="dropdown-toggle">
                    <span class="icon"><span class="mif-air"></span></span>
                    <span class="caption">UI Elements</span>
                </a>
                <ul class="navview-menu stay-open" data-role="dropdown" data-role-dropdown="true" style="display: none;">
                    <li class="item-header">UI Elements</li>
                    <li>
                        <a href="#colors">
                            <span class="icon"><span class="mif-paint"></span></span>
                            <span class="caption">Colors</span>
                        </a>
                    </li>
                    <li><a href="#typography">
                        <span class="icon"><span class="mif-bold"></span></span>
                        <span class="caption">Typography</span>
                    </a></li>
                    <li><a href="#buttons">
                        <span class="icon"><span class="mif-apps"></span></span>
                        <span class="caption">Buttons</span>
                    </a></li>
                    <li><a href="#tabs">
                        <span class="icon"><span class="mif-open-book"></span></span>
                        <span class="caption">Accordion &amp; Tabs</span>
                    </a></li>
                    <li><a href="#tiles">
                        <span class="icon"><span class="mif-dashboard"></span></span>
                        <span class="caption">Tiles</span>
                    </a></li>
                    <li><a href="#treeview">
                        <span class="icon"><span class="mif-tree"></span></span>
                        <span class="caption">TreeView</span>
                    </a></li>
                    <li><a href="#listview">
                        <span class="icon"><span class="mif-list"></span></span>
                        <span class="caption">ListView</span>
                    </a></li>
                    <li><a href="#progress">
                        <span class="icon"><span class="mif-spinner5"></span></span>
                        <span class="caption">Progress &amp; activities</span>
                    </a></li>
                    <li><a href="#list">
                        <span class="icon"><span class="mif-list2"></span></span>
                        <span class="caption">List component</span>
                    </a></li>
                    <li><a href="#splitter">
                        <span class="icon"><span class="mif-table"></span></span>
                        <span class="caption">Splitter</span>
                    </a></li>
                    <li><a href="#calendar">
                        <span class="icon"><span class="mif-calendar"></span></span>
                        <span class="caption">Calendar</span>
                    </a></li>
                    <li><a href="#countdown">
                        <span class="icon"><span class="mif-watch"></span></span>
                        <span class="caption">Countdown</span>
                    </a></li>
                </ul>
            </li>

            <li>
                <a href="#" class="dropdown-toggle">
                    <span class="icon"><span class="mif-play"></span></span>
                    <span class="caption">Media</span>
                </a>
                <ul class="navview-menu stay-open" data-role="dropdown" data-role-dropdown="true" style="display: none;">
                    <li class="item-header">Media</li>
                    <li><a href="#video">
                        <span class="icon"><span class="mif-spinner2"></span></span>
                        <span class="caption">Video player</span>
                    </a></li>
                    <li><a href="#audio">
                        <span class="icon"><span class="mif-spinner2"></span></span>
                        <span class="caption">Audio</span>
                    </a></li>
                </ul>
            </li>

            <li>
                <a href="#" class="dropdown-toggle">
                    <span class="icon"><span class="mif-comment"></span></span>
                    <span class="caption">Information</span>
                </a>
                <ul class="navview-menu stay-open" data-role="dropdown" data-role-dropdown="true" style="display: none;">
                    <li class="item-header">Information</li>
                    <li><a href="#windows">
                        <span class="icon"><span class="mif-spinner2"></span></span>
                        <span class="caption">Windows</span>
                    </a></li>
                    <li><a href="#dialogs">
                        <span class="icon"><span class="mif-spinner2"></span></span>
                        <span class="caption">Dialogs</span>
                    </a></li>
                    <li><a href="#info-boxes">
                        <span class="icon"><span class="mif-spinner2"></span></span>
                        <span class="caption">InfoBox</span>
                    </a></li>
                    <li><a href="#hints">
                        <span class="icon"><span class="mif-spinner2"></span></span>
                        <span class="caption">Hints</span>
                    </a></li>
                </ul>
            </li>

            <li>
                <a href="#" class="dropdown-toggle">
                    <span class="icon"><span class="mif-envelop"></span></span>
                    <span class="caption">Mailbox</span>
                    <span class="badges ml-auto mr-3">
                        <span class="badge inline bg-cyan fg-white">17</span>
                        <span class="badge inline bg-red fg-white">7</span>
                        <span class="badge inline bg-green fg-white">4</span>
                        <span class="badge inline bg-orange fg-white">3</span>
                    </span>
                </a>
                <ul class="navview-menu stay-open" data-role="dropdown" data-role-dropdown="true" style="display: none;">
                    <li class="item-header">Mailbox</li>
                    <li>
                        <a href="#inbox">
                            <span class="icon"><span class="mif-mail"></span></span>
                            <span class="caption">Inbox</span>
                        </a>
                    </li>
                    <li>
                        <a href="#inbox2">
                            <span class="icon"><span class="mif-mail"></span></span>
                            <span class="caption">Inbox2</span>
                        </a>
                    </li>
                    <li>
                        <a href="#compose">
                            <span class="icon"><span class="mif-mail-read"></span></span>
                            <span class="caption">Compose</span>
                        </a>
                    </li>
                    <li>
                        <a href="#read-email">
                            <span class="icon"><span class="mif-mail-read"></span></span>
                            <span class="caption">Read email</span>
                        </a>
                    </li>
                </ul>
            </li>

            <li>
                <a href="#chat">
                    <span class="icon"><span class="mif-bubbles"></span></span>
                    <span class="caption">Chat</span>
                    <span class="badges ml-auto mr-3">
                        <span class="badge inline bg-red fg-white">7</span>
                        <span class="badge inline bg-green fg-white">4</span>
                        <span class="badge inline bg-orange fg-white">3</span>
                    </span>
                </a>
            </li>

            <li>
                <a href="#" class="dropdown-toggle">
                    <span class="icon"><span class="mif-magic-wand"></span></span>
                    <span class="caption">Wizards</span>
                </a>
                <ul class="navview-menu stay-open" data-role="dropdown" data-role-dropdown="true" style="display: none;">
                    <li class="item-header">Wizards</li>
                    <li><a href="#master">
                        <span class="icon"><span class="mif-spinner2"></span></span>
                        <span class="caption">Master</span>
                    </a></li>
                    <li><a href="#wizard">
                        <span class="icon"><span class="mif-spinner2"></span></span>
                        <span class="caption">Wizard</span>
                    </a></li>
                </ul>
            </li>

            <li class="item-header">Documentation</li>
            <li>
                <a href="https://metroui.org.ua/intro.html">
                    <span class="icon"><span class="mif-brightness-auto fg-red"></span></span>
                    <span class="caption">Metro 4</span>
                </a>
            </li>
        </ul>

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
            <li class="page-item"><a href="#" class="page-link"><span class="mif-meter"></span></a></li>
            <li class="page-item"><a href="#" class="page-link">Dashboard</a></li>
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
        <TotalCustomers bind:this={totalCustomers} />
    </div>
</div>
    <CustomerOrders on:edit="{handleEditUser}" on:refresh={handleRefresh} bind:this={customer} title="Customer/Orders" />

</div>
</div>
    </div>
</div>



{#if displayCustomer}
     <AddUser on:refresh={handleRefresh} on:close="{(e)=>{displayCustomer = e.detail;}}" />
{:else if  displayOrder}
      <AddOrders on:refresh={handleRefresh} on:close="{(e)=>{displayOrder = e.detail;}}" />
{:else if displayEditItem}
    <EditItem />
{:else if displayEditUser}
    <EditUser on:refresh={handleRefresh} on:close="{(e)=>{displayEditUser = e.detail}}" {user} />
{/if}