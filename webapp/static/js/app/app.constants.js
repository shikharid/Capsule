'use strict';
angular.module('userApp').constant("URLS",{
    "INDEX": "/",
    "LOGIN": "/login",
    "LOGOUT": "/logout",
    "UPDATE": "/update",
    "REGISTER": "/register",
    "LIST": "/list",
    "BASE_URL": "http://127.0.0.1:7000/api/"
});

angular.module('userApp').constant("PARTIALS",{
    "INDEX": "/static/js/app/partials/dashboard.html",
    "LOGIN": "/static/js/app/partials/login.html",
    "LOGOUT": "/static/js/app/partials/500.html",
    "UPDATE": "/static/js/app/partials/update.html",
    "REGISTER": "/static/js/app/partials/register.html",
    "LIST": "/static/js/app/partials/user-list.html",
    "LIST_TEMPLATE": "/static/js/app/partials/list-template.html"
});

angular.module('userApp').constant("API",{
    "REGISTER": "/api/user/create/",
    "UPDATE": "/api/user/update/",
    "LOGOUT": "/api/user/logout/",
    "LOGIN": "/api/user/login/",
    "LIST": "user/list/"
});