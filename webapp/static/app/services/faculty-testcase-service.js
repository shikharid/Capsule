'use strict';

angular.module('capsuleApp').factory('FacultyTestcase', ['Restangular',
function(Restangular){
    var Testcase = Restangular.all('capsule');
    return {
        listTestcase: listTestcase,
        deleteTestcase: deleteTestcase,
        addTestcase: addTestcase
    };

    function listTestcase(assignmentID, problemID) {

    }

    function deleteTestcase(assignmentID, problemID, testcaseID) {

    }

    function addTestcase(assignmentID, problemID, data) {

    }
}]);
