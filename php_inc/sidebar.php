<div class="col s2  grey lighten-3"> <!-- left panel -->
                <!-- START LEFT SIDEBAR NAV-->
            <aside id="left-sidebar-nav">
                <ul id="slide-out" class="side-nav fixed leftside-navigation">
                    <li class="user-details cyan darken-2" id='gradient'>
                        <div class="row">
                            <div class="col col s4 m4 l4">
                                <img src="images/avatar.png" alt="" class="circle responsive-img valign profile-image" >
                            </div>
                            <div class="col col s8 m8 l8">
                                <span class="btn-flat dropdown-button waves-effect waves-light white-text profile-btn" href="#" data-activates="profile-dropdown"><b> <?php echo($title);?> </b></span>
                                <p class="user-roal"> <?php echo "Sem/Branch:"." ".$year." | ".$branch ;?> </p>
                            </div>
                        </div>
                    </li>
                    <li class="bold active"><a href="dashboard.php" class="waves-effect waves-cyan"><i class="mdi-action-dashboard"></i>Desk</a>
                    </li>
                    <li class="bold"><a href="#editor-container" class="modal-trigger waves-effect waves-cyan"><i class="mdi-action-assignment"></i> Editor</a>
                    </li>
                    <li class="bold"><a href="#" class="waves-effect waves-cyan" onClick="alert('uploading soon');"><i class="mdi-editor-insert-chart"></i> Rankings</a>
                    </li>
                     <li class="bold"><a href="php_inc/logout.php" class="waves-effect waves-cyan" ><i class="material-icons dp48">power_settings_new</i>Logout</a>
                    </li>
                </ul>
            </aside>
        </div>
        