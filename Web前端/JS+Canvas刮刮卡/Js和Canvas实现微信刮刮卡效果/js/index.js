var canvas = document.getElementById("cas"),ctx = canvas.getContext("2d");
var x1,y1,a=30,timeout,totimes = 100,jiange = 30;
//创建图片对象
var img = new Image();
img.src = "images/涂层.jpg";
img.onload = function(){
	//绘制涂层图片
ctx.drawImage(img,0,0,canvas.width,canvas.height);
	//调用擦除方法
	otherClip();
}

//使用clip()方法来达到擦除效果
function otherClip(){
var tapstart ="mousedown",
	 tapmove = "mousemove",
	  tapend = "mouseup";

canvas.addEventListener(tapstart , function(e){
	
	x1 = e.clientX-canvas.offsetLeft;
	y1 = e.clientY-canvas.offsetTop;
	
	ctx.save();
	ctx.beginPath();
	ctx.arc(x1,y1,a,0,2*Math.PI);
	ctx.clip();
	ctx.clearRect(0,0,canvas.width,canvas.height);
	ctx.restore();
	//定义事件监听器，当触发鼠标移动事件时条用tapmoveHandler（）方法
	canvas.addEventListener(tapmove , tapmoveHandler);
	//当触发mouseup事件时执行
	canvas.addEventListener(tapend , function(){
		//删除鼠标移动事件的处理程序
		canvas.removeEventListener(tapmove , tapmoveHandler);
	});

	//鼠标移动处理器
	function tapmoveHandler(e){
		x2 = e.clientX-canvas.offsetLeft;
		y2 = e.clientY-canvas.offsetTop;
		
		var asin = a*Math.sin(Math.atan((y2-y1)/(x2-x1)));
		var acos = a*Math.cos(Math.atan((y2-y1)/(x2-x1)));
		var x3 = x1+asin;
		var y3 = y1-acos;
		var x4 = x1-asin;
		var y4 = y1+acos;
		var x5 = x2+asin;

		var y5 = y2-acos;
		var x6 = x2-asin;
		var y6 = y2+acos;
		
		ctx.save()
		ctx.beginPath()
		ctx.arc(x2,y2,a,0,2*Math.PI);
		ctx.clip()
		ctx.clearRect(0,0,canvas.width,canvas.height);
		ctx.restore();
		
		ctx.save()
		ctx.beginPath()
		ctx.moveTo(x3,y3);
		ctx.lineTo(x5,y5);
		ctx.lineTo(x6,y6);
		ctx.lineTo(x4,y4);
		ctx.closePath();
		ctx.clip()
		ctx.clearRect(0,0,canvas.width,canvas.height);
		ctx.restore();
		
		x1 = x2;
		y1 = y2;
	}
})
}
