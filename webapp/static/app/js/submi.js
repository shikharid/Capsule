jQuery(document).ready(function($) {
	var sId = 0;
    var finish = false;
    var result;
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
	    		if(!finish){
	    			if(data['status'] != 0){
	    				alert(sId);
		    			setTimeout(load, 1000);
	    			} else {
	    				finish = true;
	    				setTimeout(load, 1);
		    		}
	    		} else {

	    			$('#language').text(data['langName']);
	    			$('#time').text(data['time']);
	    			$('#memory').text(data['memory']);
	    			$('#result').text(data['result']);
	    			$('#output').text(data['output']);
	    			$('#response-container').openModal();

	    		}
	    	},
	    	error: function(data){
	    	}
    	});
    	
    }
		    
    $(document).on('click', '#but-sub', function(){
    	var url = 'http://api.compilers.sphere-engine.com/api/3/submissions/?access_token=14753b7df6bf36810009cc037ee4d7c1';
	    var data = {
	    	'sourceCode': submit(), 
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
	    		alert(sId);
	    		load();
	    	},
	    	error: function(data){
	    	}
    	});
    });

   });