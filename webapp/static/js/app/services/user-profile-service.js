'use strict';

angular.module('userApp').factory('Authentication', ['$cookies', '$http', 'API',
    function($cookies, $http, API) {
        return {
            register: register,
            isAuthenticated: isAuthenticated,
            storeSession: storeSession,
            deleteSession: deleteSession,
            getInfo: getInfo,
            update: update,
            login: login
        };

        function register(user) {
            console.log(user);
            var resp = $http.post(API.REGISTER, {
            first_name: user.first_name,
            last_name: user.last_name,
            password: user.password,
            confirm_password: user.confirm_password,
            email: user.email
            });
            return resp;
        }

        function update(user) {
            var resp = $http.put(API.UPDATE, {
            first_name: user.first_name,
            last_name: user.last_name,
            password: user.password,
            confirm_password: user.confirm_password,
            });
            return resp;
        }

        function isAuthenticated(){
            return !!$cookies.get('loggedIn');
        }

        function storeSession(sessionInfo){
            $cookies.put('loggedIn', JSON.stringify(sessionInfo));
        }

        function deleteSession(){
            $http.get(API.LOGOUT);
            $cookies.remove('loggedIn');
        }

        function getInfo(){
            return $http.get(API.UPDATE);
        }

        function login(email, password) {
            var resp =  $http.post(API.LOGIN, {
            email: email, password: password
            }).then(loginSuccessCallback);


            function loginSuccessCallback(data){
                storeSession(data.data);
            }
            return resp;
        }
    }
]);

