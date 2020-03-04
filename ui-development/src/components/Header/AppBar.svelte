 <script>
    import {createEventDispatcher} from "svelte";

    const dispatch = createEventDispatcher();

 </script>
 <style>
    button{
        border: 1px solid white;
    }
 </style>
 <div  class="pos-absolute bg-darkCyan fg-white app-bar" >
            <button type="button" class="hamburger menu-down hidden" style="display: none;">
            <span class="line"></span><span class="line"></span>
            <span class="line"></span>
            </button>

            <a href="#test" class="app-bar-item d-block d-none-lg" id="paneToggle"><span class="mif-menu"></span></a>

            <div class="app-bar-container ml-auto">
                <a href="#test" class="app-bar-item">
                    <button on:click|preventDefault="{()=>{dispatch("adduser", true)}}" class="button primary">
                    
                    <span class="mif-user-plus"></span>
                    
                    </button>
                </a>
                <a href="#test" class="app-bar-item">
                    <button on:click|preventDefault="{()=>{dispatch("addorder", true)}}" class="button primary">
                        <span class="mif-cart"></span>
                    </button>
                </a>

                <div class="app-bar-container">
                    <a href="#t" class="app-bar-item">
                        <img alt="hello" src="https://metroui.org.ua/themes/pandora/images/jek_vorobey.jpg" class="avatar">
                        <span class="ml-2 app-bar-name">Hector Chapa</span>
                    </a>
                    <div class="user-block shadow-1" data-role="collapse" data-collapsed="true" data-role-collapse="true" style="display: none;">
                        <div class="bg-darkCyan fg-white p-2 text-center">
                            <img alt="" src="https://metroui.org.ua/themes/pandora/images/jek_vorobey.jpg" class="avatar">
                            <div class="h4 mb-0">Hector Chapa</div>
                            <div>Pirate captain</div>
                        </div>
                    </div>
                </div>
                <a href="#test" class="app-bar-item">
                    <span class="mif-cogs"></span>
                </a>
            </div>
        </div>