<?php
require '../vendor/autoload.php';
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
ParseUser::logOut();
header('Location: ../index.php');
exit();
?>