'use strict';

angular.module('capsuleApp').factory('spojRestangular', ['Restangular',
    function(restangular) {
        return restangular.withConfig(function (RestangularConfigurer) {
            RestangularConfigurer.setBaseUrl("http://api.compilers.sphere-engine.com/")
            .setDefaultHeaders({"Content-Type": "application/x-www-form-urlencoded"});
        });
    }
]);

angular.module('capsuleApp').factory('spojService', ['spojRestangular', 'SPOJ', '$timeout',
    function(spojRestangular, SPOJ, $timeout){
        return {
            submit: submit,
            fetch: fetch,
            status: status
        };
        function submit(code){
            var data = 'sourceCode='+encodeURIComponent(code.sourceCode)
                        +'&language='+encodeURIComponent(code.language)
                        +'&input='+encodeURIComponent(code.input);
            return spojRestangular.one(SPOJ.BASE).post(SPOJ.SUBMIT, data);
        }

        function status(ID) {
            var url = ID + '/?access_token=' + SPOJ.TOKEN;
            return spojRestangular.one(SPOJ.RESULT).one(url).get().then();
        }
        function fetch(ID) {
            var url = ID + '/?access_token=' + SPOJ.TOKEN;
            url += '&withSource=1&withInput=1&withOutput=1&withStderr=1&withCmpinfo=1';
            return spojRestangular.one(SPOJ.RESULT).one(url).get();
        }
    }
]);