'use strict';

angular.module('userApp').controller('LogoutController', ['URLS', '$location', 'Authentication',
    function(URLS, $location, Authentication){
        activate();
        function activate(){
            if(Authentication.isAuthenticated()){
                Authentication.deleteSession();
            }
        }
        $location.url(URLS.LOGIN);
    }
]);
