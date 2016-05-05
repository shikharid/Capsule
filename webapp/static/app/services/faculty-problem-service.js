'use strict';

angular.module('capsuleApp').factory('FacultyProblem', ['Restangular',
function(Restangular){
    //var Problem = Restangular.one('capsule').one('assignment', assignmentID);
    return {
        listProblem: listProblem,
        deleteProblem: deleteProblem,
        editProblem: editProblem,
        addProblem: addProblem,
        getProblem: getProblem
    };

    function listProblem(assignmentID) {
        return Restangular.one('capsule').one('assignment', assignmentID).one('problems/').get();
    }

    function deleteProblem(assignmentID, problemID) {
        return Restangular.one('capsule').one('assignment', assignmentID).one('problems', problemID)
            .one('delete/').remove();
    }

    function getProblem(assignmentID, problemID) {
        return Restangular.one('capsule').one('assignment', assignmentID).one('problems', problemID)
            .one('edit/').get();
    }

    function editProblem(assignmentID, problemID, data) {
        return Restangular.one('capsule').one('assignment', assignmentID).one('problems', problemID)
            .one('edit/').customPUT(data);
    }

    function addProblem(assignmentID, data) {
        data = JSON.stringify(data);
        return Restangular.one('capsule').one('assignment', assignmentID).one('problems').post('add/', data);
    }
}]);
