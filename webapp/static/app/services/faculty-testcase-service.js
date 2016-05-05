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
        return Restangular.one('capsule').one('assignment', assignmentID).one('problems', problemID)
            .one('testcase/').get();
    }

    function deleteTestcase(assignmentID, problemID, testcaseID) {
        return Restangular.one('capsule').one('assignment', assignmentID).one('problems', problemID)
            .one('testcase', testcaseID).one('delete/').remove();
    }

    function addTestcase(assignmentID, problemID, data) {
        var fd = new FormData();
        fd.append('input', data.input);
        fd.append('output', data.output);
        return Restangular.one('capsule').one('assignment', assignmentID).one('problems', problemID).one('testcase')
            .one('add/').withHttpConfig({transformRequest: angular.identity})
                    .customPOST(fd, '', undefined, {'Content-Type': undefined});
    }
}]);
