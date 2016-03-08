'use strict';

angular.module('capsuleApp').factory('Problem', ['Restangular',
function(Restangular){
    var Problem = Restangular.all('problem');
    return {
        getProblemList: getProblemList
    };

    function getProblemList(id){
        return Restangular.one('problem').post('get-problem-list/', {'assignment_id': id});
    }
}]);
