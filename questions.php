<?php 
    require 'vendor/autoload.php';
    use Parse\ParseClient;
    use Parse\ParseObject;
    use Parse\ParseQuery;
    use Parse\ParseACL;
    use Parse\ParsePush;
    use Parse\ParseUser;
    use Parse\ParseInstallation;
    use Parse\ParseException;
    use Parse\ParseAnalytics;
    use Parse\ParseFile;
    use Parse\ParseCloud;
    use Parse\ParseRole;
    use Parse\ParseSession;
     session_start();
ParseClient::initialize('fc2VSBg5LxJTrGcmvZ7ZzlGAPL9BqDBepXkkXxy8', 'RjKvcDha0vhoVcOfobtg1QMJrJh2ByyPEYyGpFzp', 'OKgYLQpO5SyXBFdM9ybSlZztvVsdN3MYAqtLgPlA'); 
   
    $currentUser = ParseUser::getCurrentUser();
if ($currentUser) {
    $title  = $currentUser->get('name');
    $year   = $currentUser->get('sem');
    $branch = $currentUser->get('branch');
?>


    <html lang="en">

    <head>
        <meta http-equiv="content-type" content="text/html; charset=UTF-8">
        <meta charset="utf-8">
        <title>
            <?php echo "Subject Name"; ?>
        </title>
        <?php require 'php_inc/head_inc.php'; ?>
            <!-- page specific gets appended after this one -->
    </head>

   <?php 
//if(isset($_SESSION['userkey'])){
?>



        <body>

          

            <noscript>
                <style type="text/css">
                    #screen {
                        display: none;
                    }
                </style>
            </noscript>


            <?php require 'php_inc/navbar.php'; ?>
                <!-- navbar | do not fiddle! SPECIALY SWAPPY :@ :P -->
                <div class='row'>
                    <?php require 'php_inc/sidebar.php'; ?>
                        <!-- sidebar | do not fiddle! SPECIALY SWAPPY :@ :P-->
                        <div class="col s12 white">
                            <div id="main">
                                <ul class="collapsible popout" data-collapsible="accordion">

                                    <?php for ($x = 0; $x < 4; $x++) { ?>
                                        <li>
                                            <div class="collapsible-header"><i class="material-icons"></i>
                                                <?php echo "Question #"." "; echo($x+1); ?>
                                            </div>
                                            <div class="collapsible-body">
                                                <p>
                                                    <?php echo "Lorem ipsum dolor sit amet, ei eros oporteat dissentiet vim, percipitur theophrastus duo cu. Pri vero offendit recteque ut. Graeco placerat te quo. Mea electram assueverit voluptatibus id, congue deleniti sea cu. Qui aperiam aliquando at, id posse munere sea, stet harum qui eu.

Quod vero appareat an duo, usu aliquam impedit tincidunt id. Bonorum appetere qui et, sit zril oportere in. No mea phaedrum scripserit dissentiunt, eam solet facete ne. Posse perfecto quaestio ex quo. Ea feugiat sadipscing pro. Mei vero omnesque id.

Eos eu accusata mnesarchum posidonium. Pro suas elit brute at, ei esse definitiones definitionem cum, dicit dolore pro ut. Magna atqui possit ex duo, consul laoreet cu per. Mea debet vulputate moderatius ea, nam ex assum decore reformidans. Mea nibh consequat inciderint at."; ?>
                                                </p>
                                                <p class="margin medium-small">
                                                    <a class="modal-trigger waves-effect waves-light btn blue" href="#editor-container">Attempt</a>
                                                </p>
                                            </div>
                                        </li>
                                        <?php } ?>

                                </ul>
                            </div>
                        </div>
                </div>


                <?php require 'php_inc/footer.php'; ?>
                    <?php require 'php_inc/editor_package.php' ?>
<?php
    
} else {
   header("location: re-index.php");
}
 ?>

        </body>



       

    </html>
