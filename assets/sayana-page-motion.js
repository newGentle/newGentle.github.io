(()=>{
 const reduce=window.matchMedia('(prefers-reduced-motion: reduce)');
 if(reduce.matches)return;
 const cv=document.createElement('canvas');cv.className='network-site-canvas';cv.setAttribute('aria-hidden','true');
 document.body.append(cv);
 const ctx=cv.getContext('2d',{alpha:true});if(!ctx)return;
 let w=0,h=0,scale=1,points=[],frameId=0,active=!document.hidden;
 const mod=(n,m)=>((n%m)+m)%m;
 function resize(){
   scale=Math.min(window.devicePixelRatio||1,2);w=innerWidth;h=innerHeight;cv.width=Math.round(w*scale);cv.height=Math.round(h*scale);
   ctx.setTransform(scale,0,0,scale,0,0);
   let n=Math.min(60,Math.max(22,Math.floor(w*h/27000)));
   points=Array.from({length:n},(_,i)=>({x:mod(i*271.3+53,997)/997*w,y:mod(i*379.1+105,997)/997*h,dx:Math.sin(i*2.31)*.19,dy:Math.cos(i*1.92)*.16,active:i%7===0,r:i%11===0?2.1:1.1}));
 }
 function paint(){
   frameId=0;if(!active)return;
   ctx.clearRect(0,0,w,h);
   const distance=145,max2=distance*distance;
   for(let i=0;i<points.length;i++){
      const p=points[i];p.x+=p.dx;p.y+=p.dy;if(p.x<0||p.x>w)p.dx*=-1;if(p.y<0||p.y>h)p.dy*=-1;
      for(let j=i+1;j<points.length;j++){
       const q=points[j],x=p.x-q.x,y=p.y-q.y,ds=x*x+y*y;
       if(ds<max2){ctx.strokeStyle='rgba(88,184,174,'+((1-Math.sqrt(ds)/distance)*.23)+')';ctx.lineWidth=.7;ctx.beginPath();ctx.moveTo(p.x,p.y);ctx.lineTo(q.x,q.y);ctx.stroke()}
      }
      ctx.beginPath();ctx.arc(p.x,p.y,p.r,0,Math.PI*2);ctx.fillStyle=p.active?'rgba(181,82,58,.73)':'rgba(88,184,174,.6)';ctx.fill();
   }
   frameId=requestAnimationFrame(paint);
 }
 function tick(){if(active&&!frameId)frameId=requestAnimationFrame(paint)}
 const io=new IntersectionObserver(()=>{active=!document.hidden&&!reduce.matches;tick()});
 io.observe(document.documentElement);
 document.addEventListener('visibilitychange',()=>{active=!document.hidden&&!reduce.matches;tick()});
 reduce.addEventListener('change',()=>{active=!reduce.matches&&!document.hidden;cv.style.display=reduce.matches?'none':'';tick()});
 window.addEventListener('resize',()=>{resize();tick()},{passive:true});resize();tick();
})();
