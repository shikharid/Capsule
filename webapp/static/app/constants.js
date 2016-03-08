'use strict';

angular.module('capsuleApp').constant("URLS",{
    "INDEX": "/",
    "LOGIN": "/login",
    "EDITOR": "/editor",
    "PENDING": "/pending-assignment",
    "PENDING_PROBLEMS": "/pending-assignment/:id",
    "LOGOUT": "/logout",
    "BASE_URL": "http://127.0.0.1:8000/api/"
});

angular.module('capsuleApp').constant("PARTIALS",{
    "INDEX": "/static/app/partials/dashboard.html",
    "EDITOR": "/static/app/partials/editor.html",
    "PENDING": "/static/app/partials/pending-assignment.html",
    "PROBLEM_LIST": "/static/app/partials/problem-list.html",
    "LOGIN": "/static/app/partials/login.html",
    "LOGOUT": "/static/app/partials/500.html"
});

angular.module('capsuleApp').constant("API",{
    "UPDATE": "/user/info/",
    "LOGOUT": "/user/logout/",
    "LOGIN": "/user/login/",
    "PENDING": "/problem/get-pending-assignment-list/",
    "PROBLEM_LIST": "/problem/get-problem-list/"
});

angular.module('capsuleApp').constant("SPOJ", {
    "BASE": "api/3/",
    "SUBMIT": "submissions/?access_token=14753b7df6bf36810009cc037ee4d7c1",
    "RESULT": "api/3/submissions/",
    "TOKEN": "14753b7df6bf36810009cc037ee4d7c1"
});