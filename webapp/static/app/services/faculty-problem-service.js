'use strict';

angular.module('capsuleApp').factory('FacultyProblem', ['Restangular',
function(Restangular){
    var Problem = Restangular.all('capsule');
    return {
        listProblem: listProblem,
        deleteProblem: deleteProblem,
        editProblem: editProblem,
        addProblem: addProblem
    };

    function listProblem(assignmentID) {
        return Restangular.one('capsule').one('assignment', assignmentID).get('problems/');
    }

    function deleteProblem(assignmentID, problemID) {

    }

    function editProblem(assignmentID, problemID, data) {

    }

    function addProblem(assignmentID, data) {

    }
}]);
