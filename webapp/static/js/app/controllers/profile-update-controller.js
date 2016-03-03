'use strict';

angular.module('userApp').controller('ProfileUpdateController', ['URLS', '$scope', '$location', 'Authentication',
function(URLS, $scope, $location, Authentication){
    $scope.user = {};

    activate();

    function activate(){
        if(Authentication.isAuthenticated()){
            Authentication.getInfo().then(function(data) {
                    for (var key in data.data)
                        $scope.user[key] = data.data[key];
                }
        );}
        else{
            $location.url(URLS.INDEX);
        }
    }

    $scope.update = function() {
        $scope.formState = '';
        Authentication.update($scope.user).then(
            function(data){
                for(var key in data.data)
                    $scope.user[key] = data.data[key];
                $scope.formState = "Successfully Updated Info";
        },
        function(data){
            for(var key in data.data){
                if ((key in $scope.form)) {
                    $scope.form[key].$invalid = true;
                    $scope.form[key].error = data.data[key][0];
                } else $scope.formState = data.data[key];
            }
        });
    }
}]);