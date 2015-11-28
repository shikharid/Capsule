<?php session_start(); ?>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Capsule | Group #54</title>

    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="css/overrides.css">
    <link rel="stylesheet" type="text/css" href="css/notify.css">
   <link rel="stylesheet" href="http://css-spinners.com/css/spinner/timer.css" type="text/css">
   <script type="test/javascript" src='js/jquery.min.js'></script>
   <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
   <script type="text/javascript" src='js/submi.js'></script>
   
  </head>


  <body oncontextmenu="return false">
    <noscript>
  <style type="text/css">
    #screen { display:none;}
  </style>

</noscript>
      


    <div class="container-fluid">
	<div class="row no-gutter" >
		<div class="col-md-12"  id='top-mast'>
      <div class="col-md-4 col-md-offset-0" id='logo-hold'><img src="images/sitewide-logo.png"></div>
		</div>
	</div>

 
 <?php error_reporting(0); if(isset($_SESSION['Userid'])) { ?>

	<div class="row" id='backgr'>
      <div class="col-md-12" id='screen' >
        <div id='controlbar'>
          <div id='buttons'>
            <input type='text' id='sherlock' placeholder="Search">
            <input type='button' id='but-sea' onClick='find();' title="Search">
            <input type='button' id='but-ref' onClick='flush();' title="Reset">
            <input type='button' id='but-sub' onClick='submit();' title="Submit">

            
          </div>
        </div>
        <div id="texty">
          <pre id="editor"><code>
          </code>
          </pre>

          <script src="ace/ace.js" type="text/javascript" charset="utf-8"></script>
            <script>
            var editor = ace.edit("editor");
            editor.setTheme("ace/theme/chaos");
            editor.session.setMode("ace/mode/c_cpp");
            editor.setAutoScrollEditorIntoView(true);
            editor.setOption("showPrintMargin", false);

           </script>
    </div>
        <hr style='margin-top:-2px;'>
        <div id='console-io'>
            <p>Stdin</p>
            <textarea id="stdin" style="width: 70%; height: 60%; display:inline-block;color:black;"></textarea>
        </div>
        
        <div id="cmlogo" >
          <img class="bottom" data-toggle="tooltip" title="Click Here to submit" src="images/mini-bw.png" id = "evaluate"//>
          <img class="top" data-toggle="tooltip" title="Click Here to submit" src="images/mini-col.png" id = "evaluate"/>
        </div>
        <div style='margin-top:-533px; margin-left: 1100px;'>  <a href="dashboard.php"><img src="images/close.png"></a> </div> <!-- back button buggy !-->

       </div>

  </div>

    <?php } else { ?>



    <div class="row" id='backgr'>
      <div class="row" id='active-frame'>
        

          <div id="cmlogo2" ><img class="bottom" src="images/capsulebot.png" /><img class="top" src="images/capsulebot2.png" /></div>
          <div style='margin-left: 39%; margin-top:300px;'><h2>Session Expired :( </h2></div>
          <div style='text-algin: center; margin-left: 46%;'><h6><a href="index.php">Home</a></h6></div>
     

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