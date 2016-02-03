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
    $codehandler = $currentUser->get('snip');
?>



    <html lang="en">

    <head>
        <meta http-equiv="content-type" content="text/html; charset=UTF-8">
        <meta charset="utf-8">
        <title>Codepad</title>
        <?php require 'php_inc/head_inc.php'; ?>
            <!-- page specific gets appended after this one -->
            <link rel="stylesheet" type="text/css" href="css/codepad.css">

    </head>



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


                                <!-- editor modal-->



                                <div id="texty">
                                    <pre id="editor"><code><?php echo $codehandler; ?></code></pre>

                                    <script src="ace/ace.js" type="text/javascript" charset="utf-8"></script>
                                    <script>
                                        var editor = ace.edit("editor");
                                        editor.setTheme("ace/theme/chaos");
                                        editor.session.setMode("ace/mode/c_cpp");
                                        editor.setAutoScrollEditorIntoView(true);
                                        editor.setOption("showPrintMargin", false);

                                    </script>
                                </div>

                                <div class="modal-footer" style='background-color: #000000;'>

                                    <div id="cmlogo">
                                        <img class="bottom" src="images/mini-bw.png" />
                                        <img class="top" src="images/mini-col.png" />
                                    </div>
                                </div>
                                <div style='margin-left:30%;'>
                                    <a class="waves-effect waves-light btn amber" onClick='flush();'>Reset</a>
                                    <a class="waves-effect waves-light btn green" onClick='saver();'>Save</a>
                                    <a class="waves-effect waves-light btn red disabled" onClick='alert("Coming Soon!");'>View</a>
                                </div>
                            </div>



                        </div>




                </div>
                </div>
                </div>


                <?php require 'php_inc/footer.php'; ?>

        </body>



     

    </html>
   
<?php
    
} else {
   header("location: re-index.php");
}
 ?>