'use strict';

angular.module('capsuleApp').controller('assignmentFacultyController', ['ADMIN', 'Authentication', '$location', '$scope', 'FacultyAssignment',
function(ADMIN, Authentication, $location, $scope, FacultyAssignment){
    activate();
    function activate(){
        Authentication.isAuthenticated().then(
            function(data){
                if(!data.loggedIn) {
                    $location.url(URLS.LOGIN);
                }
                else{
                    FacultyAssignment.getFacultyAssignmentList().then(
                        function (data) {
                            $scope.assignment = data;
                        },
                        function(data) {
                            $scope.error = 'Error loading assignments';
                        }
                    );
                }
            },
            function(data){
                $scope.error = 'Error connecting to server.Retry.';
            }
        );
    }

    $scope.gotoAssignment = function(index){
        $location.url(ADMIN.LIVE_A + '/' + $scope.assignment[index].id);
    }
}]);

angular.module('capsuleApp').controller('reviewAssignmentListController', ['ADMIN', 'Authentication', '$location', '$scope', 'FacultyAssignment',
function(ADMIN, Authentication, $location, $scope, FacultyAssignment){
    activate();
    function activate(){
        Authentication.isAuthenticated().then(
            function(data){
                if(!data.loggedIn) {
                    $location.url(URLS.LOGIN);
                }
                else{
                    FacultyAssignment.getCompletedAssignmentList().then(
                        function (data) {
                            $scope.assignment = data;
                        },
                        function(data) {
                            $scope.error = data;
                        }
                    );
                }
            },
            function(data){
                $scope.error = 'Error connecting to server.Retry.';
            }
        );
    }

    $scope.gotoAssignment = function(index) {
        $location.url(ADMIN.COMPLETE_A + '/' + $scope.assignment[index].id);
    }
}]);

angular.module('capsuleApp').controller('reviewAssignmentController', ['ADMIN', 'Authentication', '$mdDialog', '$location', '$scope', '$routeParams', '$interval', 'FacultyAssignment',
function(ADMIN, Authentication, $mdDialog, $location, $scope, $routeParams, $interval, FacultyAssignment){
    activate();
    var assignmentID;
    $scope.plagCheckCompleted = false;
    $scope.plagCheckProgress = false;
    var checkPlagStatus = function () {
        FacultyAssignment.getPlagCheckStatus(assignmentID).then(
            function (data) {
                if(data.status === "success" && data.state) {
                    $scope.plagCheckCompleted = true;
                    $scope.plagCheckProgress = false;
                    $interval.cancel(checkStatus);
                }
                else if(data.status === "success") {
                    $scope.plagCheckCompleted = false;
                    $scope.plagCheckProgress = true;
                }
            },
            function (data) {
                $scope.plagCheckCompleted = false;
                $scope.plagCheckProgress = false;
                $scope.error = data;
            }
        );
    };
    function activate(){
        window.scroll(0, 0);
        assignmentID = $routeParams.assignmentID;
        $scope.assignment = assignmentID;
        Authentication.isAuthenticated().then(
            function(data){
                if(!data.loggedIn) {
                    $location.url(URLS.LOGIN);
                }
                else{
                    FacultyAssignment.getStudentList(assignmentID).then(
                        function (data) {
                            $scope.student = data;
                        },
                        function(data) {
                            $scope.error = data;
                        }
                    );
                    checkPlagStatus();

                }
            },
            function(data){
                $scope.error = 'Error connecting to server.Retry.';
            }
        );
    }
    var checkStatus;
    $scope.gotoStudentAssignment = function(index){
        $location.url(ADMIN.COMPLETE_A + '/' + assignmentID + '/' + $scope.student[index].member_id);
    };

    $scope.markReviewDone = function (ev) {
        var confirm = $mdDialog.confirm()
            .title('Are you sure to mark review complete')
            .textContent('Pressing Yes will mark review complete and will calculate scores and review reports.You wont be able to edit them after that.')
            .ariaLabel('Confirm')
            .targetEvent(ev)
            .ok('Yes')
            .cancel('No');
            $mdDialog.show(confirm).then(function() {
                FacultyAssignment.markReviewDone(assignmentID).then(
                    function(data) {
                        $location.url(ADMIN.COMPLETE_A);
                    },
                    function (data) {
                        $scope.error = data;
                    }
                )
            });
    };
    $scope.sendPlagiarismCheckRequest = function () {
        FacultyAssignment.sendPlagiarismCheckRequest(assignmentID).then(
            function (data) {
                $scope.message = data;
                checkStatus = $interval(checkPlagStatus, 100);
            },
            function (data) {
                $scope.error = data;
            }
        )
    };
}]);

angular.module('capsuleApp').controller('reviewStudentSubmissionController', ['ADMIN', 'Authentication', '$mdDialog', '$location', '$scope', '$routeParams', '$interval', 'FacultyAssignment',
function(ADMIN, Authentication, $mdDialog, $location, $scope, $routeParams, $interval, FacultyAssignment){
    activate();
    var assignmentID, studentID, problemID, checkStatus;
    $scope.plagCheckCompleted = false;
    $scope.plagCheckProgress = false;
    var checkPlagStatus = function () {
        FacultyAssignment.getPlagCheckStatus(assignmentID).then(
            function (data) {
                if(data.status === "success" && data.state) {
                    $scope.plagCheckCompleted = true;
                    $scope.plagCheckProgress = false;
                    $interval.cancel(checkStatus);
                }
                else if(data.status === "success") {
                    $scope.plagCheckCompleted = false;
                    $scope.plagCheckProgress = true;
                }
            },
            function (data) {
                $scope.plagCheckCompleted = false;
                $scope.plagCheckProgress = false;
                $scope.error = data;
            }
        );
    };
    function activate(){
        window.scroll(0, 0);
        assignmentID = $routeParams.assignmentID;
        studentID = $routeParams.studentID;
        problemID = $routeParams.problemID;
        Authentication.isAuthenticated().then(
            function(data){
                if(!data.loggedIn) {
                    $location.url(URLS.LOGIN);
                }
                else{
                    FacultyAssignment.getSubmissionMatch(assignmentID, studentID, problemID).then(
                        function (data) {
                            $scope.res = data;
                            $scope.user = studentID;
                            $scope.assignment = assignmentID;
                            $scope.problem = problemID;
                            $scope.problemName = data.submission.problem_name;
                            $scope.score = parseInt(data.submission.score);
                            $scope.points = $scope.res.submission.points;
                            $scope.match = parseInt(Math.ceil(parseFloat(data.ratio) * 100));
                        },
                        function(data) {
                            $scope.error = data;
                        }
                    );
                    checkPlagStatus();
                }
            },
            function(data){
                $scope.error = 'Error connecting to server.Retry.';
            }
        );

    }

    $scope.sendSubmissionReview = function (ev) {
         var confirm = $mdDialog.prompt()
            .title('Write review for ' + studentID + ' for problem ID ' + problemID)
            .textContent('Add review comments in textbox. These review comments will be emailed to the student immediately.')
            .placeholder('Write Here')
            .ariaLabel('Review')
            .targetEvent(ev)
            .ok('Send')
            .cancel('Cancel');
        $mdDialog.show(confirm).then(function(review) {
            FacultyAssignment.sendSubmissionReview(assignmentID, studentID, problemID, review).then(
                function (data) {
                    $scope.message = data;
                },
                function (data) {
                    $scope.error = data;
                }
            )
        });
    };

    $scope.reduceProblemScore = function (scr) {
         var score = parseInt(scr);
         FacultyAssignment.reduceSubmissionScore(assignmentID, studentID, problemID, score).then(
            function (data) {
                $scope.message = data;
                $scope.score = score;
            },
            function (data) {
                $scope.error = data;
            }
        );
    };

    $scope.sendPlagiarismCheckRequest = function () {
        FacultyAssignment.sendPlagiarismCheckRequest(assignmentID).then(
            function (data) {
                $scope.message = data;
                checkStatus = $interval(checkPlagStatus, 100);
            },
            function (data) {
                $scope.error = data;
            }
        )
    }
}]);

angular.module('capsuleApp').controller('reviewStudentAssignmentController', ['ADMIN', 'Authentication', '$mdDialog', '$location', '$scope', '$routeParams', '$interval', 'FacultyAssignment',
function(ADMIN, Authentication, $mdDialog, $location, $scope, $routeParams, $interval, FacultyAssignment){
    activate();
    var assignmentID, studentID, checkStatus;
    $scope.plagCheckCompleted = false;
    $scope.plagCheckProgress = false;
    var checkPlagStatus = function () {
        FacultyAssignment.getPlagCheckStatus(assignmentID).then(
            function (data) {
                if(data.status === "success" && data.state) {
                    $scope.plagCheckCompleted = true;
                    $scope.plagCheckProgress = false;
                    $interval.cancel(checkStatus);
                }
                else if(data.status === "success") {
                    $scope.plagCheckCompleted = false;
                    $scope.plagCheckProgress = true;
                }
            },
            function (data) {
                $scope.plagCheckCompleted = false;
                $scope.plagCheckProgress = false;
                $scope.error = data;
            }
        );
    };
    function activate(){
        window.scroll(0, 0);
        assignmentID = $routeParams.assignmentID;
        studentID = $routeParams.studentID;
        Authentication.isAuthenticated().then(
            function(data){
                if(!data.loggedIn) {
                    $location.url(URLS.LOGIN);
                }
                else{
                    FacultyAssignment.getSubmissionList(assignmentID, studentID).then(
                        function (data) {
                            $scope.problem = data;
                            $scope.user = studentID;
                            $scope.assignment = assignmentID;
                        },
                        function(data) {
                            $scope.error = data;
                        }
                    );
                    checkPlagStatus();
                }
            },
            function(data){
                $scope.error = 'Error connecting to server.Retry.';
            }
        );

    }
    $scope.gotoStudentProblem = function(index){
        $location.url(ADMIN.COMPLETE_A + '/' + assignmentID + '/' + studentID + '/' + $scope.problem[index].problem_id);
    };

    $scope.sendAssignmentReview = function (ev) {
         var confirm = $mdDialog.prompt()
            .title('Write review for' + studentID)
            .textContent('Add review comments in textbox. These review comments will be emailed to the student once review is complete')
            .placeholder('Write Here')
            .ariaLabel('Review')
            .targetEvent(ev)
            .ok('Send')
            .cancel('Cancel');
        $mdDialog.show(confirm).then(function(review) {
            FacultyAssignment.sendAssignmentReview(assignmentID, studentID, review).then(
                function (data) {
                    $scope.message = data;
                },
                function (data) {
                    $scope.error = data;
                }
            )
        });
    };

    $scope.sendPlagiarismCheckRequest = function () {
        FacultyAssignment.sendPlagiarismCheckRequest(assignmentID).then(
            function (data) {
                $scope.message = data;
                checkStatus = $interval(checkPlagStatus, 100);
            },
            function (data) {
                $scope.error = data;
            }
        )
    }
}]);
