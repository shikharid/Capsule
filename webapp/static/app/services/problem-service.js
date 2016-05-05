'use strict';

angular.module('capsuleApp').factory('Problem', ['Restangular',
function(Restangular){
    var Problem = Restangular.all('capsule');
    return {
        getProblemList: getProblemList
    };

    function getProblemList(id){
        return Restangular.one('capsule').post('get-problem-list/', {'assignment_id': id});
    }
}]);
