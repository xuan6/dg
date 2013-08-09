
  var isMouseDown = false;
  var lastX = 0;
  var lastY = 0;
  var midX = 249;
  var midY = 249;
  
  function wheelMouseDown(e) {
  
	 var wheeldiv = document.getElementById("wheelcanvas");
    midX = wheeldiv.offsetLeft+wheelRadius+wheeldiv.offsetParent.offsetLeft;
	 midY = wheeldiv.offsetTop+wheelRadius+wheeldiv.offsetParent.offsetTop;
	 lastX=e.clientX;
	 lastY=e.clientY;
    isMouseDown = true;
  }
  function wheelMouseMove(e) {
	if (isMouseDown == true) {
	 var x = e.clientX+document.documentElement.scrollLeft+document.body.scrollLeft;
	 var y = e.clientY+document.documentElement.scrollTop+document.body.scrollTop;
	 //var moved = Math.abs(lastX - x) + Math.abs(lastY - y);
	 //var moved = ((lastX - x) + (lastY - y)) *0.01;
	 if (x > midX) {
		//alert(x+" , "+midX);
		if (y > midY) {
			startAngle += ((lastX - x) - (lastY - y)) *0.01;
		} else {
	 	 startAngle += (0-(lastX - x) - (lastY - y)) *0.01;
		}
	 } else {
	 	if (y > midY) {
			startAngle += ((lastX - x) + (lastY - y)) *0.01;
		} else {
	 	 startAngle += (0-(lastX - x) + (lastY - y)) *0.01;
		}
	 }
	 lastX=x;
	 lastY=y;
	 drawRouletteWheel();
	 }
  }
  function wheelMouseMove2(x,y) {
	if (isMouseDown == true) {
	 //var moved = Math.abs(lastX - x) + Math.abs(lastY - y);
	 //var moved = ((lastX - x) + (lastY - y)) *0.01;
	 if (x > midX) {
		//alert(x+" , "+midX);
		if (y > midY) {
			startAngle += ((lastX - x) - (lastY - y)) *0.01;
		} else {
	 	 startAngle += (0-(lastX - x) - (lastY - y)) *0.01;
		}
	 } else {
	 	if (y > midY) {
			startAngle += ((lastX - x) + (lastY - y)) *0.01;
		} else {
	 	 startAngle += (0-(lastX - x) + (lastY - y)) *0.01;
		}
	 }
	 lastX=x;
	 lastY=y;
	 drawRouletteWheel();
	 }
  }
  function wheelMouseUp(e) {
    isMouseDown = false;
	 //spin();
  }

var isMuted = false;
function playSound() {
 if (isMuted == false) {
	var audio = document.getElementById("wheelAudio");
	//audio.currentTime =0;
	audio.play();
 }
}

function toggleMute(button) {
 var audio = document.getElementById("wheelAudio");
 if (isMuted == true) {
	audio.volume = 1;
	button.value="Mute"; 
	button.src="images/unmute-button.png";
	isMuted = false;
 } else {
	audio.volume = 0;
	button.value="Unmute";
	button.src="images/mute-button.png";
	isMuted = true;
 }
}

var wheeldiv = document.getElementById("wheelcanvas");
wheeldiv.addEventListener('touchmove', function(e) {
    e.preventDefault();
    var touch = e.touches[0];
	 wheelMouseMove2(touch.pageX,touch.pageY);
    //alert(touch.pageX + " - " + touch.pageY);
}, false);

wheeldiv.addEventListener('touchstart', function(e) {
	//alert('touched');
    e.preventDefault();
    var touch = e.touches[0];
	 wheelMouseDown(touch);
    //alert(touch.pageX + " - " + touch.pageY);
}, false);

wheeldiv.addEventListener('touchend', function(e) {
    e.preventDefault();
    var touch = e.touches[0];
	 wheelMouseUp(touch);
	 spin();
    //alert(touch.pageX + " - " + touch.pageY);
}, false);

var colors = [ "#047d0a", "#FFFFFF", "#047d0a", "#FFFFFF", "#047d0a", "#FFFFFF"];
var restaurants = ["Partner Page", "Discover Page", "About Us", "Team Members", "Featured Collection", "Tools"];
var urls = ["/connect", "/discover", "/about", "/about/team", "/discover/PRADAN/Jharkhand/Mundari/Sowing", "/tools"]
var choiceTextSize = [];
var numcolors = colors.length;
		
  var numoptions = restaurants.length;
  
  
  var startAngle = 0;
  //var arc = Math.PI / 6;
  var arc = Math.PI / (numoptions / 2);
  var spinTimeout = null;
  
  var spinArcStart = 10;
  var spinTime = 0;
  var spinTimeTotal = 0;
  
  var ctx;
  
  // Check available screen size so wheel doesn't go outside
  var maxHeight = window.screen.availHeight;
  var maxWidth = window.screen.availWidth;
  var wheelSize = 280;
  
  var canv = document.getElementById("wheelcanvas");
  if (maxWidth > 300 && maxHeight > 300) {
  
  var canvasWidth = 300;		canv.width = canvasWidth;
		canv.height = canvasWidth;
		wheelSize = canvasWidth-2;
		
		var context = canv.getContext('2d');
      var imageObj = new Image();

      imageObj.onload = function() {
        context.drawImage(imageObj, 0, 0, canvasWidth, canvasWidth);
      };
      imageObj.src = 'http://wheeldecide.com/images/transparent-circle-click.png';
		var wheelButtons = document.getElementById("wheelbuttons");
		wheelbuttons.style.marginLeft = "75%";
  }
  
  var wheelRadius = wheelSize * 0.5;
  var outsideRadius = wheelRadius;
  var textRadius = wheelRadius * 0.9;
  var insideRadius = wheelRadius *0.1;
  
  
  function draw() {
    setChoiceFontSizes();
    drawRouletteWheel();
  }
  
  function drawRouletteWheel() {
    var canvas = document.getElementById("wheelcanvas");
    if (canvas.getContext) {
    
      ctx = canvas.getContext("2d");
      ctx.clearRect(0,0,canv.width,canv.height);
      ctx.strokeStyle = "black";
      ctx.lineWidth = 2;
      
      ctx.font = 'bold 12px sans-serif';
      
      for(var i = 0; i < numoptions; i++) {
        var angle = startAngle + i * arc;
        ctx.fillStyle = colors[i%numcolors];
        
        ctx.beginPath();
        ctx.arc(wheelRadius+1, wheelRadius+1, outsideRadius, angle, angle + arc, false);
        ctx.arc(wheelRadius+1, wheelRadius+1, insideRadius, angle + arc, angle, true);
        ctx.stroke();
        ctx.fill();
        
        ctx.save();
		  
		  
		  ctx.fillStyle = "black";			var angHalfArc = angle + arc * 0.5 - 0.04;
        ctx.translate(wheelRadius + Math.cos(angHalfArc) * textRadius, wheelRadius + Math.sin(angHalfArc) * textRadius);
        ctx.rotate(angHalfArc + Math.PI);
        var text = restaurants[i];
		  
		  ctx.font = 'bold '+choiceTextSize[i]+'px sans-serif';

		  ctx.fillText(text, 0, 0);
        ctx.restore();
      } 
      
      //Arrow
      ctx.fillStyle = "black";
      ctx.beginPath();      
		// Left Side
		ctx.moveTo(0, wheelRadius + 5);
		ctx.lineTo(0, wheelRadius - 5);
      ctx.lineTo(13, wheelRadius );
      ctx.lineTo(0, wheelRadius + 5);
		
		ctx.fill();
    }
  }
  
  function spin() {
    var minTimeToSpin = 5; // 4
    var timeRange = 4; // 3
	 var minAngleToStartRotating = 20; // 10
	 var angleRange = 30; // 10
    spinAngleStart = Math.random() * angleRange + minAngleToStartRotating; 
    spinTime = 0;
    spinTimeTotal = minTimeToSpin * 1000; //Math.random() * timeRange * 1000 + minTimeToSpin * 1000; 
	 
    rotateWheel();
	 playSound();
  }
  
  function setChoiceFontSizes() {
  // get the font size of each choice
	 var canvas = document.getElementById("wheelcanvas");
    if (canvas.getContext) {
      ctx = canvas.getContext("2d");
		choiceTextSize = [];
		for(var i = 0; i < numoptions; i++) {
			var text = restaurants[i];
			ctx.font = 'bold 18px sans-serif'; 
			var textHWidth = ctx.measureText(text).width;
			if (textHWidth > textRadius - 30) {
				//ctx.font = 'bold 12px sans-serif'; 
				choiceTextSize.push("12");
			} else {
				choiceTextSize.push("18");
			}
		}
		
				  		
		
	}
  }
  
  function rotateWheel() {
    spinTime += 30;
    if(spinTime >= spinTimeTotal) {
      stopRotateWheel();
      return;
    }
    var spinAngle = spinAngleStart - easeOut(spinTime, 0, spinAngleStart, spinTimeTotal);
    startAngle += (spinAngle * Math.PI / 180);
    drawRouletteWheel();
    spinTimeout = setTimeout('rotateWheel()', 30);
  }
  
      
  function stopRotateWheel() {
    clearTimeout(spinTimeout);
    //var degrees = startAngle * 180 / Math.PI + 90;
	 var degrees = startAngle * 180 / Math.PI + 180; // left side, not top
    var arcd = arc * 180 / Math.PI;
    var index = Math.floor((360 - degrees % 360) / arcd);
	 var text = restaurants[index];
	   ctx.font = 'bold 30px sans-serif';
	 var textHWidth = ctx.measureText(text).width*0.5;
	 if (textHWidth > wheelRadius) {
	  ctx.font = 'bold 12px sans-serif';
	  textHWidth = ctx.measureText(text).width*0.5;
	 }
		ctx.fillStyle = "black";
      ctx.beginPath();      
		// Left Side
		ctx.moveTo(wheelRadius - textHWidth-5 , wheelRadius + 20);
		ctx.lineTo(wheelRadius - textHWidth-5, wheelRadius - 20);
      ctx.lineTo(wheelRadius + textHWidth+5, wheelRadius - 20);
      ctx.lineTo(wheelRadius + textHWidth+5 , wheelRadius + 20);		
      ctx.lineTo(wheelRadius - textHWidth-5 , wheelRadius + 20);
				
		
	 ctx.fill();
    ctx.save();
	 
	 //if (maxWidth > 300 && maxHeight > 300) {
	//	 var imageObj = new Image();
	//	 imageObj.src = 'http://wheeldecide.com/images/wheel-decision-gradient.png';
	//	 ctx.drawImage(imageObj, 0, 0);
	// }
	 
	 ctx.fillStyle = "white";
    //ctx.font = 'bold 30px sans-serif';

    ctx.fillText(text, wheelRadius - textHWidth, wheelRadius + 10);
	 
	 if (maxWidth > 300 && maxHeight > 300) {
		 var imageObj = new Image();

		 imageObj.onload = function() {
			  ctx.drawImage(imageObj, 0, 0, canvasWidth, canvasWidth);
			  ctx.fillStyle = "white";
				//ctx.font = 'bold 30px sans-serif';

			ctx.fillText(text, wheelRadius - textHWidth, wheelRadius + 10);
			//ctx.restore();
		 };
		 imageObj.src = 'http://wheeldecide.com/images/wheel-decision-gradient.png';
	 }
	 window.setTimeout(function(){window.location = urls[index]}, 3000);
	 
  }
  
  function easeOut(t, b, c, d) {
    var ts = (t/=d)*t;
    var tc = ts*t;
    return b+c*(tc + -3*ts + 3*t);
  }
draw();

