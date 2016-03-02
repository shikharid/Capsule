'use strict';

angular.module('userApp').factory('userList' , ['Restangular', 'API',
    function(Restangular, API){
        return {
            userList: userList
        };
        function userList(){
            return Restangular.one(API.LIST).get();
        }
    }]);
