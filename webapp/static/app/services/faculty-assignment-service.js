'use strict';

angular.module('capsuleApp').factory('FacultyAssignment', ['Restangular',
function(Restangular){
    var Problem = Restangular.all('capsule');
    return {
        getFacultyAssignmentList: getFacultyAssignmentList,
        addAssignment: addAssignment,
        editAssignment: editAssignment,
        getAssignment: getAssignment
    };

    function getFacultyAssignmentList() {
        return Problem.get('list-assignment/');
    }

    function addAssignment(data) {
        data.deadline = moment(data.deadline).format('YYYY-MM-DD');
        data = JSON.stringify(data);
        return Restangular.one('capsule').post('add-assignment/', data);
    }

    function getAssignment(assignmentID) {
        return Restangular.one('capsule').one('assignment', assignmentID).one('edit/').get();
    }

    function editAssignment(assignmentID, data) {
        data.deadline = moment(data.deadline).format('YYYY-MM-DD');
        data = JSON.stringify(data);
        return Restangular.one('capsule').one('assignment', assignmentID).one('edit/').customPUT(data);
    }
}]);
