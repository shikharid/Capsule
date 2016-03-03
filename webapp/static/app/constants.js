'use strict';

angular.module('capsuleApp').constant("URLS",{
    "INDEX": "/",
    "LOGIN": "/login",
    "LOGOUT": "/logout",
    "BASE_URL": "http://127.0.0.1:8000/api/"
});

angular.module('capsuleApp').constant("PARTIALS",{
    "INDEX": "/static/app/partials/dashboard.html",
    "LOGIN": "/static/app/partials/login.html",
    "LOGOUT": "/static/app/partials/500.html"
});

angular.module('capsuleApp').constant("API",{
    "UPDATE": "/api/user/info/",
    "LOGOUT": "/api/user/logout/",
    "LOGIN": "/api/user/login/"
});