<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Capsule | Group #54</title>

    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="css/overrides.css">
    <link rel="stylesheet" type="text/css" href="css/notify.css">
   <link rel="stylesheet" href="http://css-spinners.com/css/spinner/timer.css" type="text/css">

   <script type="text/javascript" src='js/scripts.js'></script>
    
  </head>
  <script type="text/javascript">
            <script language=JavaScript> var message="Function Disabled!"; function clickIE4(){ if (event.button==2){ alert(message); return false; } } function clickNS4(e){ if (document.layers||document.getElementById&&!document.all){ if (e.which==2||e.which==3){ alert(message); return false; } } } if (document.layers){ document.captureEvents(Event.MOUSEDOWN); document.onmousedown=clickNS4; } else if (document.all&&!document.getElementById){ document.onmousedown=clickIE4; } document.oncontextmenu=new Function("alert(message);return false") </script>
          </script>

  <body oncontextmenu="return false">

    <noscript>
  <style type="text/css">
    #screen { display:none;}
  </style>

</noscript>
      


    <div class="container-fluid">
	<div class="row no-gutter" >
		<div class="col-md-12"  id='top-mast'>
      <div class="col-md-4 col-md-offset-0" id='logo-hold'><img src="images/sitewide-logo.png"></div>
		</div>
	</div>


	<div class="row" id='backgr'>
      <div class="col-md-12" id='screen' >
        <div id='controlbar'>
          <div id='buttons'>
            <input type='text' id='sherlock' placeholder="Search">
            <input type='button' id='but-sea' onClick='find();' title="Search">
            <input type='button' id='but-ref' onClick='flush();' title="Reset">
            <input type='button' id='but-sub' onClick='submit();' title="Submit">
            
          </div>
        </div>
        <div id="texty">
          <pre id="editor"><code>
            using namespace std;
            char str[1000];
             
            int counter(char A)
            {if(A=='1') return 2;
            else if(A=='0' || A=='6' || A=='9') return 6;
            else if(A=='2' || A=='3' || A=='5') return 5;
            else if(A=='4') return 4;
            else if(A=='7') return 3;
            else if(A=='8') return 7;
            }
             
            int main()
            { int sum=0; int i=0;
             cin>>str;
              while(i strlen(str))
              {
                  sum=sum+counter(str[i]);
                  i++;
                //testing for search with 'return'
                }
              cout sum endl;
              return 0;
            }
          </code>
          </pre>

          <script src="ace/ace.js" type="text/javascript" charset="utf-8"></script>
            <script>
            var editor = ace.edit("editor");
            editor.setTheme("ace/theme/chaos");
            editor.session.setMode("ace/mode/c_cpp");
            editor.insert("under testing by tm \n");
            editor.setAutoScrollEditorIntoView(true);
            editor.setOption("showPrintMargin", false)
            editor.resize()

           </script>
        </div>
        <hr style='margin-top:-2px;'>
        <div id='console-io'>@Botfather: This area is for console messages | Under test by TM</div>
        <div id="cmlogo" >
          <img class="bottom" src="images/mini-bw.png" />
          <img class="top" src="images/mini-col.png" />
        </div>

       </div>

  </div>

	<div class="row">
		<div class="col-md-12-foot" id='bottom-mast'>
      <p>Capsule-ACG | B.Tech(CSE) Final Year Project 2015-2016| Group Number 54 | <i> email: capsule@whatthetech.in</i></p>
		</div>
	</div>
</div>




   
  </body>

 
</html>