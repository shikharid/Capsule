'use strict';

// TODO move this file to directives
angular.module('capsuleApp').directive('fileModel', ['$parse', function ($parse) {
return {
    restrict: 'A',
    link: function(scope, element, attrs) {
        var model = $parse(attrs.fileModel);
        var modelSetter = model.assign;

        element.bind('change', function(){
            scope.$apply(function(){
                modelSetter(scope, element[0].files[0]);
            });
        });
    }
};
}]);


angular.module('capsuleApp').controller('addProblemController', ['ADMIN', 'Authentication', '$location', '$scope', '$routeParams', 'FacultyProblem',
function(ADMIN, Authentication, $location, $scope, $routeParams, FacultyProblem) {
    activate();
    var assignmentID;
    function activate() {
        assignmentID = $routeParams.assignmentID;
        window.scroll(0, 0);
        Authentication.isAuthenticated().then(
            function(data) {
                if(!data.loggedIn) {
                    $location.url(URLS.LOGIN);
                }
            },
            function(data) {
                $scope.error = 'Error connecting to server.Retry.';
            }
        );
    }

    $scope.submit = function() {
        if($scope.form.$invalid)
            return;
        FacultyProblem.addProblem(assignmentID, $scope.problem).then(
            function(data) {
                $location.url('assignment/' + assignmentID);
            },
            function(data) {
                $scope.error = data;
            }
        )
    }
}]);

angular.module('capsuleApp').controller('editProblemController', ['ADMIN', 'PARTIALS', 'Authentication', '$mdDialog', '$location', '$scope', '$routeParams', 'FacultyProblem', 'FacultyTestcase',
function(ADMIN, PARTIALS, Authentication, $mdDialog, $location, $scope, $routeParams, FacultyProblem, FacultyTestCase) {
    activate();
    var assignmentID;
    var problemID;
    function activate() {
        assignmentID = $routeParams.assignmentID;
        problemID = $routeParams.problemID;
        window.scroll(0, 0);
        Authentication.isAuthenticated().then(
            function(data) {
                if(!data.loggedIn) {
                    $location.url(URLS.LOGIN);
                }
                else{
                    FacultyProblem.getProblem(assignmentID, problemID).then(
                        function(data) {
                            $scope.problem = data;
                            $scope.problem.time_limit = parseFloat($scope.problem.time_limit);
                        },
                        function(data) {
                            $scope.error = data;
                        }
                    );
                    FacultyTestCase.listTestcase(assignmentID, problemID).then(
                        function(data) {
                            $scope.testcase = data;
                        },
                        function(data) {
                            $scope.error = data;
                        }
                    );
                }
            },
            function(data) {
                $scope.error = 'Error connecting to server.Retry.';
            }
        );
    }

    $scope.updateProblem = function() {
        if($scope.form.$invalid)
            return;

        FacultyProblem.editProblem(assignmentID, problemID, $scope.problem).then(
            function(data) {
                $scope.problem = data;
            },
            function(data) {
                $scope.error = data;
            }
        )
    };

    $scope.addTestcase = function(ev) {
        $mdDialog.show({
            controller: DialogController,
            templateUrl: PARTIALS.TESTCASE_ADD,
            parent: angular.element(document.body),
            scope: $scope,
            preserveScope: true,
            clickOutsideToClose: true
        }).then(
            function(data) {
                window.scrollTo(0,document.body.scrollHeight);
                $scope.testcase.push(data);
            },
            function(data) {
                $scope.error = data;
            }
        );
    };

    $scope.uploadTestcase = function() {
        FacultyTestCase.addTestcase(assignmentID, problemID, $scope.newtestcase).then(
            function(data) {
                $mdDialog.hide(data);
            },
            function(data) {
                $scope.error = data;
                $mdDialog.hide();
            }
        );
    };
    $scope.deleteTestcase = function(index) {
        FacultyTestCase.deleteTestcase(assignmentID, problemID, $scope.testcase[index].id).then(
            function(data) {
                $scope.testcase.splice(index, 1);
            },
            function(data) {
                $scope.error = data;
            }
        )
    };

}]);

function DialogController($scope, $mdDialog) {
    $scope.hide = function() {
        $mdDialog.hide();
    };
    $scope.cancel = function() {
        $mdDialog.cancel();
    };
    $scope.answer = function(answer) {
        $mdDialog.hide(answer);
    };
}