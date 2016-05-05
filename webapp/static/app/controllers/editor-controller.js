'use strict';

angular.module('capsuleApp').controller('editorController', ['spojService', 'Authentication', '$scope', '$interval',
    function(spojService, Authentication, $scope, $interval) {
        $scope.code = {};
        $scope.code.language = 1;

        activate();
        function activate(){
            Authentication.isAuthenticated().then(
                function(data){
                    if(!data.loggedIn) {
                        $location.url(URLS.LOGIN);
                    }
                },
                function(data){
                    $scope.serverError = 'Error connecting to server.Retry.';
                }
            );
        }

        $scope.submit = function(){
            $scope.code.sourceCode = editor.getValue();
            $scope.processing = true;
            if($scope.result)
                delete $scope.result;
            if($scope.error)
                delete $scope.error;
            spojService.submit($scope.code).then(
                function(data){

                    var submissionID = data.id;
                    var stop = $interval(function(){
                                    spojService.status(submissionID).then(
                                        function(data){
                                            if(data.status == 0){
                                                $interval.cancel(stop);
                                                spojService.fetch(submissionID).then(
                                                    function(data){
                                                        $scope.result = {
                                                            small: {
                                                                Language: data.langName,
                                                                Memory: data.memory,
                                                                Time: data.time
                                                            },
                                                            error: data.cmpinfo,
                                                            large: {
                                                                Input: data.input,
                                                                Output: data.output
                                                            }
                                                        };
                                                        $scope.processing = false;
                                                    },
                                                    function(data){
                                                        $scope.processing = false;
                                                        delete $scope.result;

                                                        $scope.error = 'Error in fetching result.Retry';
                                                        console.log($scope.error);
                                                    }
                                                );
                                            }
                                        },
                                        function(data){
                                        }
                                )
                    }, 2000);

                },
                function(data){
                    $scope.processing = false;
                    delete $scope.result;
                    $scope.error = 'Error in submission.Retry';
                    console.log($scope.error);
                }
            )
        }
    }
]);