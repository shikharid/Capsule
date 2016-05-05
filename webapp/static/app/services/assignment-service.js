'use strict';

angular.module('capsuleApp').factory('Assignment', ['Restangular',
function(Restangular){
    var Problem = Restangular.all('capsule');
    return {
        getStudentAssignmentList: getStudentAssignmentList
    };

    function getStudentAssignmentList(){
        return Problem.get('get-pending-assignment-list/');
    }
}]);
