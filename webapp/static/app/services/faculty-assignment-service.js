'use strict';

angular.module('capsuleApp').factory('FacultyAssignment', ['Restangular',
function(Restangular){
    var Problem = Restangular.all('capsule');
    return {
        getFacultyAssignmentList: getFacultyAssignmentList,
        addAssignment: addAssignment,
        editAssignment: editAssignment,
        getAssignment: getAssignment,
        getCompletedAssignmentList: getCompletedAssignmentList,
        sendPlagiarismCheckRequest: sendPlagiarismCheckRequest,
        getPlagCheckStatus: getPlagCheckStatus,
        getStudentList: getStudentList,
        getSubmissionList: getSubmissionList,
        sendAssignmentReview: sendAssignmentReview,
        sendSubmissionReview: sendSubmissionReview,
        reduceSubmissionScore: reduceSubmissionScore,
        getSubmissionMatch: getSubmissionMatch,
        markReviewDone: markReviewDone
    };

    function getFacultyAssignmentList() {
        return Problem.get('list-assignment/');
    }

    function getSubmissionMatch(assignmentID, studentID, problemID) {
        return Restangular.one('capsule').one('review', assignmentID).one(studentID).one(problemID + '/').get();
    }

    function markReviewDone(assignmentID) {
        return Restangular.one('capsule').one('review', assignmentID).one('mark-review-done/').customPOST();
    }

    function sendAssignmentReview(assignmentID, studentID, review) {
        console.log("Here");
        return Restangular.one('capsule').one('review', assignmentID).one(studentID).one('mail/').customPOST({"review": review});
    }

    function sendSubmissionReview(assignmentID, studentID, problemID, review) {
        return Restangular.one('capsule').one('review', assignmentID).one(studentID).one(problemID).one('mail/').customPOST({"review": review});
    }

    function reduceSubmissionScore(assignmentID, studentID, problemID, score) {
        return Restangular.one('capsule').one('review', assignmentID).one(studentID).one(problemID).one('reduce/').customPOST({"points": score});
    }

    function getCompletedAssignmentList() {
        return Problem.get('review/assignment-list/');
    }

    function getStudentList(assignmentID) {
        return Restangular.one('capsule').one('review', assignmentID).one('student-list/').get();
    }

    function getSubmissionList(assignmentID, studentID) {
        return Restangular.one('capsule').one('review', assignmentID).one(studentID).one('code-list/').get();
    }

    function sendPlagiarismCheckRequest(assignmentID) {
        return Restangular.one('capsule').one('review', assignmentID).one('plagiarism-request/').customPOST();
    }


    function getPlagCheckStatus(assignmentID) {
        return Restangular.one('capsule').one('review', assignmentID).one('plagiarism-request-status/').get();
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
