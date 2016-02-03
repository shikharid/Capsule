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
    $_SESSION['code'] = $branch.$year;
?>

    <html lang="en">

    <head>
        <meta http-equiv="content-type" content="text/html; charset=UTF-8">
        <meta charset="utf-8">
        <title>Dashboard</title>
        <?php require 'php_inc/head_inc.php'; ?>
            <!-- page specific gets appended after this one -->
    </head>



    <script type="text/javascript">
        $(window).load(function () {
            $(".se-pre-con").delay(1000);
            $(".se-pre-con").fadeOut(3000);

        });
    </script>

    <body>
        <?php $color = array("green", "orange", "yellow", "teal");?>
            <div class="se-pre-con"></div>
            <?php 
              $query = new ParseQuery("JUNCTION");
              $query->equalTo("code", $_SESSION['code']);
              $results = $query->find();
             for ($i = 0; $i < count($results); $i++) {
                     $object = $results[$i];
             $subjectcount = $object->get("subjectcount");
             $subjectlist = $object->get("subjectlist");}
             list($subject[0], $subject[1], $subject[2], $subject[3] ) = explode(',', $subjectlist);
              ?>

                <?php require 'php_inc/navbar.php'; ?>
                    <!-- navbar | do not fiddle! SPECIALY SWAPPY :@ :P -->
                    <div class='row'>
                        <?php require 'php_inc/sidebar.php'; ?>
                            <!-- sidebar | do not fiddle! SPECIALY SWAPPY :@ :P-->
                            <div class="col s10 white">
                                <div id="main">
                                    <div class="col s12 m12 l12" style='margin-left:12%;'>
                                        <div class="row">
                                            <?php for ($i = 0; $i < $subjectcount; $i++) { ?>
                                                <div class="col s12 m6" class="z-depth-2">
                                                    <div class="card-panel  <?php echo $color[$i]; ?> accent-4" id="limiter">
                                                        <span class="white-text center">
                          <h5><?php echo $subject[$i]; ?></h5>
                          <p>Last Updated:</p>
                            <div class="center qstn "><a class="waves-effect waves-light btn <?php  echo $color[$i]; ?> darken-3"  href='questions.php'><i class="mdi-action-find-in-page right "></i>View</a></div>

                      </span>
                                                    </div>
                                                </div>
                                                <?php } ?>

                                                 <?php if(!($i%2==0)) { ?>
                                                <div class="col s12 m6" >
                                                    <div class="card-panel  grey accent-4" id="limiter">
                                                        <span class="white-text center">
                                                          <h5><?php if($i==1){echo "Just 1 Lab";} if($i==3){echo "Only 3 Labs";} ?></h5>
                                                          <p>This semester</p>           
                                                        </span>
                                                    </div>
                                                </div>
                                                <?php } ?>

                                        </div>
                                    </div>
                                    <div class="col s12 m12 l12 blue z-depth-2" style="margin-left:12%;max-height:29.5%;overflow: hidden;">
                                        <span class='white-text center'><h5>Resources</h5><hr></span>
                                        <div style="max-height:29.5%;overflow-y: scroll; padding-bottom:20px;" id="feeder">
                                            <span class='white-text'>
                  <p><i class="mdi-communication-email"></i> USe this to share display the resorces that the faculty shall share.. use a blog kind of a thing! but do not make it personnal.</p>
                  <p><i class="mdi-communication-email"></i> Lorem ipsum dolor sit amet, curabitur gravida ut tincidunt, nobis tortor ante neque.</p>
                  <p><i class="mdi-communication-email"></i> Lorem ipsum dolor sit amet, curabitur gravida ut tincidunt, nobis tortor ante neque.</p>
                  <p><i class="mdi-communication-email"></i> Lorem ipsum dolor sit amet, curabitur gravida ut tincidunt, nobis tortor ante neque.</p>
                  <p><i class="mdi-communication-email"></i> Lorem ipsum dolor sit amet, curabitur gravida ut tincidunt, nobis tortor ante neque.</p>
                  <p><i class="mdi-communication-email"></i> Lorem ipsum dolor sit amet, curabitur gravida ut tincidunt, nobis tortor ante neque.</p>
                  <p><i class="mdi-communication-email"></i> Lorem ipsum dolor sit amet, curabitur gravida ut tincidunt, nobis tortor ante neque.</p>
                  <p><i class="mdi-communication-email"></i> Lorem ipsum dolor sit amet, curabitur gravida ut tincidunt, nobis tortor ante neque.</p>
                  </span></div>
                                    </div>
                                </div>
                            </div>

                    </div>
                    <?php require 'php_inc/footer.php'; ?>
                        <?php require 'php_inc/editor_package.php' ?>

    </body>
    <script type="text/javascript">
    </script>

    </html>


    <?php } else { header("location: re-index.php"); } ?>