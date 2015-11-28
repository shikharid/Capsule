<?php session_start(); ?>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Capsule | Group #54</title>
  
   <script type="text/javascript" src='js/jquery.js'></script>
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="css/overrides.css">
    <link rel="stylesheet" type="text/css" href="css/notify.css">
   <script type="text/javascript" src='js/bootstrap.min.js'></script>
   
  </head>


  <body oncontextmenu="return false">

   <script type="text/javascript" src='js/submi.js'></script>
    <noscript>
  <style type="text/css">
    #screen { display:none;}
  </style>

</noscript>
<div id='modalwrapper'>
                <div class="col-md-12">
      
      <div class="modal fade" id="modal-container" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
               
              <button type="button" class="close" data-dismiss="modal" aria-hidden="true">
                ×
              </button>
              <h4 class="modal-title" id="myModalLabel">
                Result
              </h4>
            </div>
            <div class="modal-body">
             <label>Language :</label> <p id = "language"></p>
             <label>Time :</label><p id = "time"> </p>
             <label>Memory :</label><p id = "memory"></p>
             <label>Result :</label><p id = "result"></p>
             <label>Output :</label><p id = "output"></p>
            </div>
            <div class="modal-footer">
               
              <button type="button" class="btn btn-default" data-dismiss="modal">
                Close
              </button> 
            </div>
          </div>
          
        </div>
        
      </div>
      
    </div>
      


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
            <input type='button' id='but-sub' title="Submit">

            
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
          <img class="bottom"  src="images/mini-bw.png" />
          <img class="top" src="images/mini-col.png"/>
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
 
 <!-- <div id="openModal" class="modal fade" role="dialog">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
           <a href="#close" title="Close" class="close">X</a>
          <h4 class="modal-title">Result</h4>
        </div>
        <div class="modal-body">
           <p id = "language"> </p>
           <p id = "time"> </p>
           <p id = "memory"> </p>
           <p id = "result"> </p>
           <p id = "output"> </p>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
        </div>
      </div>

    </div> !-->
    

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