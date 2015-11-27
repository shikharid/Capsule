

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
    <link rel="stylesheet" type="text/css" href="css/subject.css">

    <script src="js/jquery.js"></script>
    <script src="js/typed.js"></script>
    <script src="//code.jquery.com/ui/1.11.4/jquery-ui.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/scripts.js"></script>

<script>
  $(function() {
    $( "#accordion" ).accordion({
      event: "click hoverintent"
    });
  });
 
  /*
   * hoverIntent | Copyright 2011 Brian Cherne
   * http://cherne.net/brian/resources/jquery.hoverIntent.html
   * modified by the jQuery UI team
   */
  $.event.special.hoverintent = {
    setup: function() {
      $( this ).bind( "mouseover", jQuery.event.special.hoverintent.handler );
    },
    teardown: function() {
      $( this ).unbind( "mouseover", jQuery.event.special.hoverintent.handler );
    },
    handler: function( event ) {
      var currentX, currentY, timeout,
        args = arguments,
        target = $( event.target ),
        previousX = event.pageX,
        previousY = event.pageY;
 
      function track( event ) {
        currentX = event.pageX;
        currentY = event.pageY;
      };
 
      function clear() {
        target
          .unbind( "mousemove", track )
          .unbind( "mouseout", clear );
        clearTimeout( timeout );
      }
 
      function handler() {
        var prop,
          orig = event;
 
        if ( ( Math.abs( previousX - currentX ) +
            Math.abs( previousY - currentY ) ) < 7 ) {
          clear();
 
          event = $.Event( "hoverintent" );
          for ( prop in orig ) {
            if ( !( prop in event ) ) {
              event[ prop ] = orig[ prop ];
            }
          }
          // Prevent accessing the original event since the new event
          // is fired asynchronously and the old event is no longer
          // usable (#6028)
          delete event.originalEvent;
 
          target.trigger( event );
        } else {
          previousX = currentX;
          previousY = currentY;
          timeout = setTimeout( handler, 100 );
        }
      }
 
      timeout = setTimeout( handler, 100 );
      target.bind({
        mousemove: track,
        mouseout: clear
      });
    }
  };
  </script>



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
            <legend>Subject Name</legend>
          </fieldset>
          <div id="accordion">
  <h3>Question 1</h3>
  <div>
    <p>
    	Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras libero lorem, mollis at commodo sed, malesuada at lacus. Maecenas consectetur eleifend tempor. Nullam consequat consectetur ipsum, id venenatis dui fringilla in. Suspendisse ut metus eu diam pretium ultricies. Duis gravida velit risus, in commodo nulla fringilla eget. In ac massa.

   Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras libero lorem, mollis at commodo sed, malesuada at lacus. Maecenas consectetur eleifend tempor. Nullam consequat consectetur ipsum, id venenatis dui fringilla in. Suspendisse ut metus eu diam pretium ultricies. Duis gravida velit risus, in commodo nulla fringilla eget. In ac massa.
    </p>
  </div>
  <h3>Question 2</h3>
  <div>
    <p>
    Sed non urna. Donec et ante. Phasellus eu ligula. Vestibulum sit amet
    purus. Vivamus hendrerit, dolor at aliquet laoreet, mauris turpis porttitor
    velit, faucibus interdum tellus libero ac justo. Vivamus non quam. In
    suscipit faucibus urna.
    </p>
  </div>
  <h3>Question 3</h3>
  <div>
    <p>
    Nam enim risus, molestie et, porta ac, aliquam ac, risus. Quisque lobortis.
    Phasellus pellentesque purus in massa. Aenean in pede. Phasellus ac libero
    ac tellus pellentesque semper. Sed ac felis. Sed commodo, magna quis
    lacinia ornare, quam ante aliquam nisi, eu iaculis leo purus venenatis dui.
    </p>
    <ul>
      <li>List item one</li>
      <li>List item two</li>
      <li>List item three</li>
    </ul>
  </div>
  <h3>Question 4</h3>
  <div>
    <p>
    Cras dictum. Pellentesque habitant morbi tristique senectus et netus
    et malesuada fames ac turpis egestas. Vestibulum ante ipsum primis in
    faucibus orci luctus et ultrices posuere cubilia Curae; Aenean lacinia
    mauris vel est.
    </p>
    <p>
    Suspendisse eu nisl. Nullam ut libero. Integer dignissim consequat lectus.
    Class aptent taciti sociosqu ad litora torquent per conubia nostra, per
    inceptos himenaeos.
    </p>
  </div>
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