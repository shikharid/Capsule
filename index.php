
<?php session_start();?>

    <html>

    <head>
        <link rel="stylesheet" type="text/css" href="css/sweetalert.css">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.5/css/materialize.min.css">
        <link rel="stylesheet" type="text/css" href="css/index.css">
        <script src="JS/jquery.js"></script>
        <script src="js/sweetalert.js"></script>
        <script src="js/materialize.js"></script>
        <script src="js/scripts.js"></script>
        <script src="//www.parsecdn.com/js/parse-1.6.14.min.js"></script>

    </head>
        <script language="JavaScript">
            document.oncontextmenu =new Function("return false;")
        </script>    
    <body class='light-blue' onselectstart="return false">
        <div class='container-main'>
            <div id="login-page" class="row">
                <div class="col s12 z-depth-4 card-panel">
                    <form id='login' onSubmit='return validate();' action="php_inc/checkpoint.php" method='POST'>
                        <div class="row">
                            <div class="input-field col s12 center">
                                <img src="images/login-logo.png" alt="" class=" circle responsive-img valign profile-image-login">
                                <p class="center login-form-text">Capsule-Automatic Code Grader</p>
                            </div>
                        </div>
                        <div class="row margin text-red">
                            <div class="input-field col s12">
                                <i class="mdi-social-person-outline prefix"></i>
                                <input type='email' name='uid' id='uid'>
                                <label for="username" class="center-align">Login ID</label>
                            </div>
                        </div>
                        <div class="row margin">
                            <div class="input-field col s12">
                                <i class="mdi-action-lock-outline prefix"></i>
                                <input type='password' name='pwd' id='pwd'>
                                <label for="password">Password</label>
                            </div>
                        </div>
                        <div class="row">
                            <div class="input-field col s12">
                                <button type='Submit' class="btn waves-effect waves-light col s12 green">Login</button>
                            </div>
                        </div>
                        <div class="row">
                            <div class="input-field col s6 m6 l6 center">
                                <p class="margin medium-small"><a class="modal-trigger waves-effect waves-light btn" href="#modal1">Register Now!</a></p>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>

        <!--modal-->
        <div id="modal1" class="modal modal-fixed-footer">
            <div class="modal-content" style='overflow:hidden;'>
                <h4>Registeration Form</h4>
                <form id='login' onSubmit='return validate();' action="#" method='POST'>
                    <div class="row">
                        <div class="input-field col s12 center">
                            <input type='email' name='reg-uid' id='reg-uid'>
                            <label for="email" class="center-align">Email Address</label>
                        </div>
                    </div>
                    <div class="row">
                        <div class="input-field col s12 center">
                            <input type='text' name='reg-name' id='reg-name'>
                            <label for="name" class="center-align">Full Name</label>
                        </div>
                    </div>
                    <div class="row">
                        <div class="input-field col s6 center">
                            <input type='text' name='reg-year' id='year'>
                            <label for="year" class="center-align">Year</label>
                        </div>
                        <div class="input-field col s6 center">
                            <input type='text' name='reg-branch' id='branch'>
                            <label for="branch" class="center-align">Branch</label>
                        </div>
                        <div class="row">
                        <div class="input-field col s12 center">
                            <input type='password' name='reg-pwd' id='reg-pwd'>
                            <label for="pwd" class="center-align">Password</label>
                        </div>
                    </div>
                    </div>
                </form>
            </div>
            <div class="modal-footer">
                <a href="#!" class="modal-action modal-close waves-effect waves-green btn-flat ">Agree</a>
            </div>
        </div>


    </body>

    <script type="text/javascript">
        function validate() {
            var email = document.getElementById('uid').value;
            var pass = document.getElementById('pwd').value;
            if ((email.length != 0) && (pass.length != 0)) {
                if (email.indexOf('@whatthetech.in', email.length - '@whatthetech.in'.length) !== -1) {
                    return true;
                } else {
                    swal({
                        title: "Error!",
                        timer: 2000,
                        text: "Only 'abc@whatthetech.in' emails are allowed",
                        animation: "slide-from-top",
                        imageUrl: "images/error.png",
                        showConfirmButton: false
                    });
                    return false;
                }
            } else {
                swal({
                    title: "Error!",
                    timer: 2000,
                    text: "Inavlid Email or Password.",
                    animation: "slide-from-top",
                    imageUrl: "images/error.png",
                    showConfirmButton: false
                });
                return false;
            }
        };

    </script>

    <script type="text/javascript">
        $('.modal-trigger').leanModal({
            dismissible: false,
            opacity: .5,
            in_duration: 300,
            out_duration: 200,
            ready: function() {
                $('.container-main').fadeOut('fast', function() {
                    alert('opened');
                });
            },
            complete: function() {
                $('.container-main').fadeIn('slow', function() {
                    adduser();
                });
            }
        });

    </script>


    <script type="text/javascript">
    function adduser(){
        Parse.initialize("fc2VSBg5LxJTrGcmvZ7ZzlGAPL9BqDBepXkkXxy8", "BJgduXhMY0iIoLddFrY9puoJ9a73wFxbefav9I1k");
        var user = new Parse.User();
        user.set("username", document.getElementById('reg-uid').value);
        user.set("name", document.getElementById('reg-name').value);
        user.set("year", document.getElementById('year').value);
        user.set("branch", document.getElementById('branch').value);
        user.set("password", document.getElementById('reg-pwd').value );

        user.signUp(null, {
          success: function(user) {
           swal({
                        title: "Awesome!",
                        timer: 2000,
                        text: "Successfully added the user to database!",
                        animation: "slide-from-top",
                        imageUrl: "images/tick.png",
                        showConfirmButton: false
                    });
          },
          error: function(user, error) {
            var sys = "Reference Code-" + error.code + ": " + error.message;
           swal({
                        title: "Error!",
                        timer: 4000,
                        text: sys,
                        animation: "slide-from-top",
                        imageUrl: "images/error.png",
                        showConfirmButton: false
                    });
            
          }
        });
    }
    </script>

    </html>
