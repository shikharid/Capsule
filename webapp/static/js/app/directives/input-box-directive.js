'use strict';

angular.module('userApp').directive('myInput', function(){
    return{
        restrict: 'A',
        link: link
    };

    function link(scope, element, attr) {
        scope.$watch(attr.myInput, function(val){
           if(/^[0-9]*$/.test(val)){
               element.removeClass('has-error');
               element.addClass('has-success');
           }
           else{
               element.removeClass('has-success');
               element.addClass('has-error');
           }
        });
    }

});