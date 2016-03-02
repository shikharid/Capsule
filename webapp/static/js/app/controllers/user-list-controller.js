'use strict';

angular.module('userApp').controller('UserListController', ['$scope', 'userList', 'Authentication', 'URLS', '$location',
    function($scope, userList, Authentication, URLS, $location){

        activate();
        function activate(){
            if(Authentication.isAuthenticated()){
                userList.userList().then(
                    function(data){
                        $scope.listError = false;
                        $scope.userList = data;
                    },
                    function(data){
                        $scope.listError = true;
                    }
                )
            }
            else{
                $location.url(URLS.INDEX);
            }
        }
    }
]);