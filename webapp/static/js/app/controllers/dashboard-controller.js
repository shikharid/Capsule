'use strict';

angular.module('userApp').controller('DashboardController', ['URLS', '$location', 'Authentication',
function(URLS, $location, Authentication){
    activate();
    function activate(){
            if(Authentication.isAuthenticated())
                $location.url(URLS.UPDATE);
            else
                $location.url(URLS.LOGIN);
        }
}]);