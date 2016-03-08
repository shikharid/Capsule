'use strict';

angular.module('capsuleApp').factory('Assignment', ['Restangular',
function(Restangular){
    var Problem = Restangular.all('problem');
    return {
        getStudentAssignmentList: getStudentAssignmentList
    };

    function getStudentAssignmentList(){
        return Problem.get('get-pending-assignment-list/');
    }
}]);
