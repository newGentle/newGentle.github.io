(()=>{
'use strict';
const hero=document.querySelector('.hero'),canvas=document.getElementById('executive-globe');
if(!hero||!canvas)return;
const ctx=canvas.getContext('2d',{alpha:true});if(!ctx)return;
const pref=window.matchMedia('(prefers-reduced-motion: reduce)');
const TAU=Math.PI*2;
const vertices=[],edges=[];
const nlat=19,nlon=32;
for(let y=0;y<=nlat;y++){const lat=-Math.PI/2+Math.PI*y/nlat;for(let x=0;x<nlon;x++){
 const lon=TAU*x/nlon;vertices.push({lat,lon,x,y,amber:(x*7+y*11)%27===0,bright:(x*13+y*3)%31===0});
}}
for(let y=0;y<=nlat;y++)for(let x=0;x<nlon;x++){
 const i=y*nlon+x;if(y<nlat)edges.push([i,(y+1)*nlon+x]);edges.push([i,y*nlon+(x+1)%nlon]);
}
let w=0,h=0,dpr=1,frame=0,request=0,active=true,start=performance.now(),latest=0;
function fit(){
 const r=hero.getBoundingClientRect();w=Math.max(1,Math.round(r.width));h=Math.max(1,Math.round(r.height));dpr=Math.min(devicePixelRatio||1,1.8);
 canvas.width=Math.round(w*dpr);canvas.height=Math.round(h*dpr);canvas.style.width=w+'px';canvas.style.height=h+'px';ctx.setTransform(dpr,0,0,dpr,0,0);
}
function paint(t){
 request=0;if(!active)return;
 if(t-latest<32){request=requestAnimationFrame(paint);return;}latest=t;
 ctx.clearRect(0,0,w,h);
 const mobile=w<700, radius=Math.min(w*(mobile?.60:.30),h*(mobile?.36:.49));
 const centerX=w*(mobile?.62:.76),centerY=h*(mobile?.42:.49);
 const angle=frame*.0028+.12,tilt=-.23;
 const positions=vertices.map(p=>{
   const c=Math.cos(p.lat);let X=c*Math.cos(p.lon+angle),Z=c*Math.sin(p.lon+angle),Y=Math.sin(p.lat);
   const yr=Y*Math.cos(tilt)-Z*Math.sin(tilt),zr=Y*Math.sin(tilt)+Z*Math.cos(tilt);
   const scale=1+.13*zr;
   return{x:centerX+X*radius*scale,y:centerY+yr*radius*scale,z:zr,vis:zr>-.23,amber:p.amber,bright:p.bright};
 });
 ctx.save();ctx.globalCompositeOperation='screen';
 let glow=ctx.createRadialGradient(centerX,centerY,0,centerX,centerY,radius*1.35);
 glow.addColorStop(0,'rgba(5,45,63,.10)');glow.addColorStop(.55,'rgba(2,31,48,.11)');glow.addColorStop(1,'rgba(1,8,18,0)');
 ctx.fillStyle=glow;ctx.fillRect(centerX-radius*1.4,centerY-radius*1.4,radius*2.8,radius*2.8);
 const sorted=edges.map(([a,b])=>[positions[a],positions[b]]).sort((a,b)=>(a[0].z+a[1].z)-(b[0].z+b[1].z));
 for(const [a,b] of sorted){const za=(a.z+b.z)/2;const strength=Math.max(.02,Math.min(.35,(za+1)*.17));ctx.strokeStyle='rgba(21,191,214,'+strength.toFixed(3)+')';ctx.lineWidth=za>0?.95:.45;ctx.beginPath();ctx.moveTo(a.x,a.y);ctx.lineTo(b.x,b.y);ctx.stroke();}
 for(const p of positions){
  const strength=Math.max(.1,Math.min(.95,(p.z+1)*.58));const hot=p.amber&&p.z>.0,bright=p.bright&&p.z>0;
  if(hot||bright){const rr=hot?10:7;const halo=ctx.createRadialGradient(p.x,p.y,0,p.x,p.y,rr);halo.addColorStop(0,hot?'rgba(231,109,54,.7)':'rgba(32,211,229,.7)');halo.addColorStop(1,'rgba(0,0,0,0)');ctx.fillStyle=halo;ctx.beginPath();ctx.arc(p.x,p.y,rr,0,TAU);ctx.fill();}
  ctx.fillStyle=hot?'rgba(249,128,67,.95)':'rgba(24,201,226,'+strength.toFixed(3)+')';ctx.beginPath();ctx.arc(p.x,p.y,hot?2.65:bright?2.1:1.15,0,TAU);ctx.fill();
 }
 ctx.restore();frame++;if(!pref.matches)request=requestAnimationFrame(paint);
}
function update(){if(request){cancelAnimationFrame(request);request=0;}fit();active=!document.hidden;request=requestAnimationFrame(paint)}
const ro=new ResizeObserver(update);ro.observe(hero);
const observer=new IntersectionObserver(es=>{active=es[0].isIntersecting&&!document.hidden;if(active&&!request)request=requestAnimationFrame(paint);if(!active&&request){cancelAnimationFrame(request);request=0;}},{threshold:0});observer.observe(hero);
document.addEventListener('visibilitychange',()=>{active=!document.hidden;if(active&&!request)request=requestAnimationFrame(paint)});
pref.addEventListener('change',update);
fit();request=requestAnimationFrame(paint);
})();
