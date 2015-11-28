<?php session_start(); ?>
<!DOCTYPE html>
<html lang="en">
  <head>
    <?php require 'php_includes/db_conx.php';?>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Capsule | Group #54</title>

    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/style.css" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="css/overrides.css">
    <link rel="stylesheet" type="text/css" href="css/dashboard.css">

    <script src="js/jquery.js"></script>
    <script src="js/typed.js"></script>
    <script src="//code.jquery.com/ui/1.11.4/jquery-ui.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/scripts.js"></script>
  </head>
                  
                  <?php
                      error_reporting(0);
                   $token=$_SESSION["email"];
                    $ticket="nhhggcttctc"; $name="";
                    $query  ="SELECT `Name`, `Pass`,`Userid` FROM `login` WHERE Email= '$token'"; 
                      if($result=mysqli_query($conn,$query))
                      { while ($row=mysqli_fetch_assoc($result))
                          { $ticket = $row["Pass"];
                            $name = $row["Name"];
                            $thumb = $row["Userid"];}
                            mysqli_free_result($result);}
                            mysqli_close($conn);  ?>      

  <body>


    <div class="container-fluid">
	<div class="row no-gutter" >
		<div class="col-md-12"  id='top-mast'>
      <div class="col-md-4 col-md-offset-0" id='logo-hold'><img src="images/sitewide-logo.png"></div>
      
		</div>
	</div>

         <?php if((isset($_POST['pwd'])&&($ticket==$_POST['pwd']))||isset($_SESSION['Userid']))
                                   { $_SESSION['Userid']= $thumb; ?>

	<div class="row" id='backgr'>

    <div class="row" id='active-frame'>
      <div class="col-md-4" >
        <div class="panel panel-default" style='border:none; outline: none;'>
          <div class="panel-heading" style="background-color: rgba(100,168,224,1);">
            <h3 class="panel-title" style='text-align:center;'>Notifications</h3>
          </div>
          <div class="panel-body"> 
            <div class='bullets'><p><img src="images/bullet.png">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p></div>
            <div class='bullets'><p><img src="images/bullet.png">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p></div>
            <div class='bullets'><p><img src="images/bullet.png">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p></div>
            <div class='bullets'><p><img src="images/bullet.png">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p></div>
            <div class='bullets'><p><img src="images/bullet.png">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p></div>
            <div class='bullets'><p><img src="images/bullet.png">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p></div>
            <div class='bullets'><p><img src="images/bullet.png">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p></div>
            <div class='bullets'><p><img src="images/bullet.png">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p></div>
            <div class='bullets'><p><img src="images/bullet.png">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p></div>
            <div class='bullets'><p><img src="images/bullet.png">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p></div>
            <div class='bullets'><p><img src="images/bullet.png">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p></div>
            <div class='bullets'><p><img src="images/bullet.png">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p></div>
            <div class='bullets'><p><img src="images/bullet.png">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p></div>
            <div class='bullets'><p><img src="images/bullet.png">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p></div>
            <div class='bullets'><p><img src="images/bullet.png">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p></div>
            <div class='bullets'><p><img src="images/bullet.png">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p></div>


          </div>
          <div class="panel-footer"><div id='botface'>
            <div id='name-holder' style='text-align: center;color:#fff;'><p><h4><?php echo $name; ?> </h4></p></div>
            <div id='upper-scorecase' style='color: #fff;'> <div id='usc-rank' style='display: inline; margin-left:12%; color:#ff5654; font-size: 35px;'>2</div><div id='usc-score' style='display: inline; margin-left:20%;color:#ff5654; font-size: 35px;'> 999</div> <div id='usc-subs' style='display: inline; margin-left:20%;color:#ff5654; font-size: 35px;'> -5</div> </div>
            <div id='lower-scorecase'> <div id='lsc-rank' style='display: inline; margin-left:8%; color: #fff; font-size: 20px;'>Rank</div><div id='lsc-score' style='display: inline; margin-left:18%;color: #fff; font-size: 20px;'> Rating</div> <div id='lsc-subs' style='display: inline; margin-left:12%;color: #fff; font-size: 20px;'> Submissions</div></div>
          </div></div>
        </div>
      </div>
      <div class="col-md-8 " >
        <ul class="nav nav-tabs" style="background-color: rgba(100,168,224,1);  border-top-right-radius: 5px; border-top-left-radius: 5px;">
          <li class="active"><a href="dashboard.php">Dashboard</a></li>
          <li><a href="notify.php">Submissions</a></li>
          <li ><a href="scoreboard.php">Scoreboard</a></li>
            <li class="dropdown pull-right"><a href="#" data-toggle="dropdown" class="dropdown-toggle">Tools<strong class="caret"></strong></a>
              <ul class="dropdown-menu">
                <li><a href="#">Settings</a></li>
                <li><a href="#">Requests</a></li>
                <li><a href="#">Something else here</a></li>
                <li class="divider"></li>
                <li><a href="php_includes/logout.php">Log Out</a></li>
              </ul>
            </li>
        </ul>
        
        <div class="col-md-12" id='page-cont'>
          <div><fieldset>
            <legend>Updates</legend>
          </fieldset>
          <?php  echo $thumb;?>
          <p>1. Added Subjects Tab | 2. Added Logout session | 3. Added Scorecard</p>
          </div>
          <br>
          <div>
           <fieldset>
            <legend>Subjects</legend>
          </fieldset>

              <div id='subjectpanel' style='margin-left: 5%;'>

                        <a href="subject.php" class="a-btn">
                            <span class="a-btn-text">Subject 1</span> 
                            <span class="a-btn-slide-text"><img src="images/updated.png" title="Last Updated"> 28-11-2015</span>
                            <span class="a-btn-icon-right"><span></span></span>
                      </a>
                       <a href="subject.php" class="a-btn">
                            <span class="a-btn-text">Subject 2</span> 
                            <span class="a-btn-slide-text"><img src="images/updated.png" title="Last Updated"> 27-11-2015</span>
                            <span class="a-btn-icon-right"><span></span></span>
                      </a>
                       <a href="subject.php" class="a-btn">
                            <span class="a-btn-text">Subject 3</span> 
                            <span class="a-btn-slide-text"><img src="images/updated.png" title="Last Updated"> 26-11-2015</span>
                            <span class="a-btn-icon-right"><span></span></span>
                      </a>
                       <a href="subject.php" class="a-btn">
                            <span class="a-btn-text">Subject 4</span> 
                            <span class="a-btn-slide-text"><img src="images/updated.png" title="Last Updated"> 25-11-2015</span>
                            <span class="a-btn-icon-right"><span></span></span>
                      </a>

               
              </div>
          </div>
        </div>
      </div>
    </div>

  </div>
<?php } else { ?>


    <div class="row" id='backgr'>
      <div class="row" id='active-frame' >
        

          <div id="cmlogo" ><img class="bottom" src="images/capsulebot.png" /><img class="top" src="images/capsulebot2.png" /></div>
          <div style='margin-left: 29%; margin-top:300px;'><h2>Invalid Credentials. Please login again.</h2></div>
          <div style='text-algin: center; margin-left: 47%;'><h6><a href="/index.php">Home</a></h6></div>
     

      </div>
    </div>




<?php } ?>
  

	<div class="row">
		<div class="col-md-12-foot" id='bottom-mast'>
      <p>Capsule-ACG | B.Tech(CSE) Final Year Project 2015-2016| Group Number 54 | <i> email: capsule@whatthetech.in</i></p>
		</div>
	</div>
</div>
   
    

  </body>
</html>