'use strict';

angular.module('userApp').directive('userListDirective', ['PARTIALS', function (PARTIALS) {
    return{
        restrict: 'E',
        templateUrl: PARTIALS.LIST
    }
}]);

