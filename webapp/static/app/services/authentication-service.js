'use strict';

angular.module('capsuleApp').factory('Authentication', ['Restangular',
function(Restangular){
    var User = Restangular.all('user');
    return {
        isAuthenticated: isAuthenticated,
        login: login,
        logout: logout
    };

    function isAuthenticated() {
        return User.get('authentication/');
    }

    function login(user) {
        return Restangular.one('user').post('login/',{member_id: user.member_id,
            password: user.password});
    }

    function logout() {
        return User.get('logout/');
    }
}]);
