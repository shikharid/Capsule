function toll()
{ var email= document.getElementById('emailer').value;
	var pass = document.getElementById('wrd').value;
	if((email.length!=0)&&(pass.length!=0))
	{if (email.indexOf('@whatthetech.in', email.length - '@whatthetech.in'.length) !== -1) 
			{return true;}
     else {swal({   title: "Error!",   timer: 2000,  text: "Only 'abc@whatthetech.in' emails are allowed",animation: "slide-from-top",   imageUrl: "images/error.png", showConfirmButton: false }); return false;}} 
	else { swal({   title: "Error!",  timer: 2000,  text: "Inavlid Email or Password.", animation: "slide-from-top",   imageUrl: "images/error.png",showConfirmButton: false }); return false; }
};



@font-face { font-family: Handwritten; src: url(../fonts/handwritten.ttf); } /* special symbols are not visible */




body{
	background-image: url('../images/background.png');
}


.helper{
	font-family: Handwritten;
	font-size: 48px;
	margin-left: 325px;
	margin-top: 100px;
}



/*credits section */
#credit-text-header{
	-webkit-transform: rotate(8deg);
    position: absolute;
    margin-top: 24%;
    margin-left: 75.5%;
    font-size: 16px;
	font-family: Handwritten;
	color: #000000;
	}

#credit-text-lower{
	-webkit-transform: rotate(8deg);
	 word-wrap: break-word;
	 width: 350px;
    position: absolute;
    margin-top: 27%;
    margin-left: 69%;
    font-size: 14px;
	font-family: Handwritten;
	color: #000000;
	}
	
#credit-text-footer{
	-webkit-transform: rotate(8deg);
    position: absolute;
    margin-top: 34%;
    margin-left: 68%;
    font-size: 14px;
	font-family: Handwritten;
	color: #000000;
	}



/*logo-control*/
.logo-main{ margin-left: 75%; margin-top: 9%; -webkit-transform: rotate(8deg);position: absolute;}
.logo-main img{position:absolute;  -webkit-transition: opacity 1s ease-in-out; -moz-transition: opacity 1s ease-in-out; -o-transition: opacity 1s ease-in-out; transition: opacity 1s ease-in-out;}
.logo-main img.top:hover{opacity:0;}@keyframes cmlogoFadeInOut{0%{opacity:1;}45%{opacity:1;}55%{opacity:0;}100%{opacity:0;}}
.logo-main img.top{animation-name: cmlogoFadeInOut;animation-timing-function: ease-in-out;animation-iteration-count: infinite;animation-duration: 5s;animation-direction: alternate;}


/* arrow control */
.arrow-spread{
	margin-left: 350px;
	margin-top: -30px;
}

/*login-panel-controls*/

.login-container{
	-webkit-transform: rotate(338deg);
    position: absolute;
    margin-top: 9%;
    margin-left: 24.5%;

}

.login-container: hover{
	display: block;
	-webkit-transform: rotate(338deg);
    position: absolute;
    margin-top: 10%;
    margin-left: 24.5%;
}

.handler{
	border: none;
	outline: none;
	width:175px;
	margin-left: 1px;
	padding-left: 2px;
	margin-top: 3%;
	background: transparent;
	text-align: center;
	font-family: cursive;
	color:#ff5356;

}

.sub-but{
	margin-left:1px;
	margin-top: 3%;
	width:175px;
  height: 30px;
  padding: 0;
  font-size: 18px;
  color: white;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.25);
  background: #4D9EE1;
  border: 0;
  border-bottom: 2px solid #2a8bcc;
  cursor: pointer;
  -webkit-box-shadow: inset 0 -2px #2a8bcc;
  box-shadow: inset 0 -2px #2a8bcc;
}

.sub-but:active {
  top: 1px;
  outline: none;
  -webkit-box-shadow: none;
  box-shadow: none;
}

.reg-but{
	margin-left: 1px;
	margin-top: -9px;
	outline: #3CB35A;
 width:175px;
  height: 30px;
  padding: 0;
  font-size: 18px;
  color: white;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.25);
  background: #6BF178;
  border: 0;
  border-bottom: 2px solid #3CB35A;
  cursor: pointer;
  -webkit-box-shadow: inset 0 -2px #3CB35A;
  box-shadow: inset 0 -2px #3CB35A;
}

.reg-but:active {
  top: 1px;
  outline: none;
  -webkit-box-shadow: none;
  box-shadow: none;
}