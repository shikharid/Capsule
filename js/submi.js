jQuery(document).ready(function($) {
	var sId = 0;
    var finish = false;

    var load = function(){
    	var extra = '';
    	if( finish ){
    		extra = '&withSource=1&withInput=1&withOutput=1&withStderr=1&withCmpinfo=1'
    	}
    	var url = 'http://api.compilers.sphere-engine.com/api/3/submissions/' + sId + '/?access_token=14753b7df6bf36810009cc037ee4d7c1' + extra;
    	$.ajax({url: url,
	    	type: 'get',
	    	dataType: 'json',
	    	success: function(data){
	    		//$("#status").html($(data['link'] + '<i class="fa fa-circle-o-notch fa-spin"></i>&nbsp;'));
	    		//load(data['link']);
	    		
	    		//console.log(data);
	    		//console.log($('#web-right-panel > ul > li:last-child'));
	    		//$('#web-right-panel > ul > li:last-child div.result').html(JSON.stringify(data));
	    		if(!finish){
	    			if(data['status'] != 0){
		    			setTimeout(load, 1000);
	    			} else {
	    				finish = true;
	    				setTimeout(load, 1);
		    		}
	    		} else {
	    			alert(JSON.stringify(data));
	    		}
	    	},
	    	error: function(data){
	    	}
    	});
    	
    }
		    
    $(document).on('click', '#evaluate', function(){
    	var url = 'http://api.compilers.sphere-engine.com/api/3/submissions/?access_token=14753b7df6bf36810009cc037ee4d7c1';
	    var data = {
	    	'sourceCode': editor.getValue(), 
	    	'language': 1,
	    	'input': $('#stdin').val()
	    };
	    sId = 0;
	    finish = false;
    	$.ajax({url: url,
	    	type: 'post',
	    	data: data,
	    	dataType: 'json',
	    	success: function(data){
	    		sId = data['id'];
	    		load();
	    	},
	    	error: function(data){
	    	}
    	});
    });

   });