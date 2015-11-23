<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Capsule | Group #54</title>

    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/style.css" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="css/overrides.css">
    <link rel="stylesheet" type="text/css" href="css/index.css">

    <script src="js/jquery.js"></script>
    <script src="js/typed.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/scripts.js"></script>
  </head>

  <body>

    <div class="container-fluid">
	<div class="row no-gutter" >
		<div class="col-md-12"  id='top-mast'>
      
		</div>
	</div>

	<div class="row" id='backgr'>
    <div class="col-md-4 col-md-offset-5" id='logo-hold'><img src="images/logo-small.png"></div>
    <div class="col-md-3 col-md-offset-4" id='login-pane-1'>
       <div class="col-md-12-elem" id='botface'><p style='text-align: center; color:#fff'>Please wait while the bot arrives.</p></div>
    </div>
    <div class="col-md-3 col-md-offset-4" id='login-pane-2'>

       <div class="col-md-12">
        <div id='main-form'>
          <form name='login' onsubmit='passw();' action='login.php' method=POST>
            <input type='text' id='holder'> <input type="submit" value='' id='clicker'>
          </form>
            </div>
        </div>
       </div>
    </div>
	



	<div class="row">
		<div class="col-md-12-foot" id='bottom-mast'>
      <p>Capsule-ACG | B.Tech(CSE) Final Year Project 2015-2016| Group Number 54 | <i> email: capsule@whatthetech.in</i></p>
		</div>
	</div>
</div>

<script>
 $(document).ready(function(){
      $(".col-md-12-elem").typed({
        strings: ["@Botfather: ^1000 Hi! Please enter your username in the command box below."],
        startDelay: 3000,
        showCursor: false,
        contentType: 'text',
        typeSpeed: 0
      });
});
</script>

   
  </body>
</html>