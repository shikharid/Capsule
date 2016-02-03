<!-- editor modal-->
 <div id="editor-container" class="modal">
    <div class="modal-content" style='overflow:hidden;' >
          <div id='buttons'>
             <input type='text' id='sherlock' placeholder="Search" style='margin-top:-10px;'>
            <input type='button' id='but-sea' onClick='find();' title="Search">
            <input type='button' id='but-ref' onClick='flush();' title="Reset">
            <input type='button' id='but-sub'  title="Submit">
            <a href="#!" class="modal-action modal-close waves-effect waves-green btn-flat " style='margin-left:53%;'><img src="images/close.png"></a>
          </div>
        
        <div id="texty">
          <pre id="editor"><code></code></pre>

          <script src="ace/ace.js" type="text/javascript" charset="utf-8"></script>
            <script>
            var editor = ace.edit("editor");
            editor.setTheme("ace/theme/chaos");
            editor.session.setMode("ace/mode/c_cpp");
            editor.setAutoScrollEditorIntoView(true);
            editor.setOption("showPrintMargin", false);

           </script>
    </div>
         <hr style='margin-top:2px;'>
       <div class="modal-footer" style='background-color: #000000;'>
     <div id='console-io' style=' height:100%;'>
            <textarea id="stdin" style="width: 100%; height: 90%; display:inline-block;color:red; outline:none; border:none;"></textarea>
        </div>
        <div id="cmlogo" >
          <img class="bottom"  src="images/mini-bw.png" />
          <img class="top"     src="images/mini-col.png"/>
        </div>
    </div>

  </div>
 
    

    </div>

 <!--response modal-->
  <div id="response-container" class="modal">
    <div class="modal-content" style='overflow:hidden;' >
       <h4 class="modal-title" id="myModalLabel" style='text-align:center;'> Submission Sheet </h4>
       <hr>
       <div class="modal-body">
             <label>Language: </label> <span id = "language"></span> <br>
             <label>Time: </label><span id = "time"> </span> <br>
             <label>Memory: </label><span id = "memory"></span> <br>
             <label>Result: </label><span id = "result"></span> <br>
             <label>Output: </label><span id = "output"></span> 
        </div>
        
  <div class="input-field col s6 m6 l6 center">
            <p class="margin medium-small btn"><a href="#!" class=" modal-action modal-close waves-effect waves-blue btn-flat">Close</a></p>
          </div>   

    </div>
  </div>

<script type="text/javascript">
  $('.modal-trigger').leanModal({
      dismissible: false, 
      opacity: .5, 
      in_duration: 300, 
      out_duration: 200, 
      
    }
  );
</script>