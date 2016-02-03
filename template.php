<?php session_start(); ?>
    <html lang="en">

    <head>
        <meta http-equiv="content-type" content="text/html; charset=UTF-8">
        <meta charset="utf-8">
        <title>Dashboard</title>
        <?php require 'php_inc/head_inc.php'; ?>
            <!-- page specific gets appended after this one -->
    </head>

    <?php if(isset($_SESSION["key"])){ ?>



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


                                everything important and page specific goes here bro! (Y)


                            </div>
                        </div>
                </div>


                <?php require 'php_inc/footer.php'; ?>
                    <?php require 'php_inc/editor_package.php' ?>
        </body>



        <?php } else { header('Location: re-index.php');} ?>

    </html>