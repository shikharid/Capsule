function find(){
var key=document.getElementById("sherlock").value;
var editor=ace.edit("editor");
editor.find(key,{backwards: false, wrap: true, caseSensitive: false,wholeWord: false, regExp: false});
editor.findNext();editor.findPrevious();
}
function submit(){var editor=ace.edit("editor"); var hold=editor.getValue(); return(hold);}

function flush(){var editor=ace.edit("editor");editor.setValue("");}


function saver(){
	var editor=ace.edit("editor"); var hold=editor.getValue(); 

    $.post("php_inc/codesave.php",
    {
        cp: hold
    },
    function(data, status){ if(status=='success'){
        swal({
                        title: status,
                        timer: 2000,
                        text: data,
                        animation: "slide-from-top",
                        imageUrl: "images/tick.png",
                        showConfirmButton: false
                    });}
        else {
             swal({
                        title: status,
                        timer: 2000,
                        text: data,
                        animation: "slide-from-top",
                        imageUrl: "images/error.png",
                        showConfirmButton: false
                    });
        }

    



    });

}
