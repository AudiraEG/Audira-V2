;(function(){try{var d=document.documentElement,el=document.getElementById('intro');if(!el)return;
if(window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches){el.remove();return}
d.classList.add('introing');var done=false,T=[];
function fin(){if(done)return;done=true;T.forEach(clearTimeout);el.classList.add('out');d.classList.remove('introing');setTimeout(function(){el.remove()},800)}
el.addEventListener('click',fin);
function an(n,kf,o){var e=document.getElementById(n);if(e&&e.animate)e.animate(kf,Object.assign({fill:'both',easing:'cubic-bezier(.2,.7,.2,1)'},o))}
an('il5',[{opacity:0,transform:'translate(-14.8px,2.3px)'},{opacity:1,transform:'translate(-14.8px,0)'}],{duration:800,delay:200});
an('il5',[{transform:'translate(-14.8px,0)'},{transform:'translate(0,0)'}],{duration:700,delay:1100,composite:'replace'});
for(var i=0;i<5;i++)an('il'+i,[{opacity:0,transform:'translateY(1.6px)'},{opacity:1,transform:'translateY(0)'}],{duration:600,delay:1600+160*i});
var sb=el.querySelector('.isub');if(sb&&sb.animate)sb.animate([{opacity:0,transform:'translateY(8px)'},{opacity:1,transform:'none'}],{duration:700,delay:2900,fill:'both',easing:'ease-out'});
var lg=el.querySelector('svg');if(lg&&lg.animate)for(var b=0;b<4;b++)lg.animate([{transform:'scale(1)',opacity:1},{transform:'scale(1.028)',opacity:1,offset:.18},{transform:'scale(1.004)',offset:.34},{transform:'scale(1.016)',offset:.5},{transform:'scale(1)',opacity:1}],{duration:900,delay:2300+900*b,easing:'ease-in-out',fill:'none'});
T.push(setTimeout(fin,6100));
}catch(e){try{console.warn("audira",e)}catch(_){}}})();
;(function(){try{var sp=document.createElement('div');sp.id='sp';sp.setAttribute('aria-hidden','true');document.body.appendChild(sp);var tk=false,vt=0,mv=0,hm=false,box=null,docH=0,vis={},S=16,io=null;
function hosted(){var de=document.documentElement;return (function(){try{return window.top!==window}catch(e){return true}})()&&innerHeight>1500&&de.scrollHeight-innerHeight<150}
function build(){var de=document.documentElement;if(box){box.remove();if(io)io.disconnect()}vis={};docH=de.scrollHeight;box=document.createElement('div');box.setAttribute('aria-hidden','true');box.style.cssText='position:absolute;left:0;top:0;width:1px;height:'+docH+'px;pointer-events:none;visibility:hidden;overflow:hidden';var n=Math.ceil(docH/S),fr=document.createDocumentFragment();io=new IntersectionObserver(function(es){es.forEach(function(e){var k=e.target.__k;if(e.isIntersecting)vis[k]=e.intersectionRect;else delete vis[k]});var t=1e9,b=0;for(var k in vis){var r=vis[k];if(r.top<t)t=r.top;if(r.bottom>b)b=r.bottom}if(t<1e9){vt=t;mv=Math.max(mv,b-t);r2()}},{threshold:[0,1]});for(var i=0;i<n;i++){var d=document.createElement('div');d.style.cssText='position:absolute;left:0;width:1px;height:'+S+'px;top:'+i*S+'px';d.__k=i;fr.appendChild(d)}box.appendChild(fr);document.body.appendChild(box);[].forEach.call(box.children,function(d){io.observe(d)})}
function u(){tk=false;window.__hm=hm;window.__vt=vt;var de=document.documentElement,y,m;if(hm){y=vt;m=Math.max(1,docH-Math.max(mv,300))}else{y=window.pageYOffset||de.scrollTop||0;m=(de.scrollHeight-innerHeight)||1}
var p=Math.max(0,Math.min(1,y/m));sp.style.transform='scaleX('+p+')';var b=document.querySelector('.bar');if(b)b.classList.toggle('sc',y>30);
if(hm){var ty=(y>2?Math.round(y)+62:0)+'px';sp.style.top=ty;if(b)b.style.top=ty}}
function r2(){if(!tk){tk=true;requestAnimationFrame(u)}}
function chk(){var h=hosted();if(h&&(!hm||Math.abs(document.documentElement.scrollHeight-docH)>40)){if(!hm){hm=true;document.documentElement.classList.add('hm')}build()}r2()}
addEventListener('scroll',r2,{passive:true});addEventListener('resize',chk);setInterval(chk,1500);chk();u()}catch(e){try{console.warn("audira",e)}catch(_){}}})();
;(function(){try{var c=document.getElementById('pf');if(!c||!c.getContext)return;document.body.appendChild(c);var x=c.getContext('2d'),P=[],W=0,H=0,dpr=Math.min(2,devicePixelRatio||1),mx=-9e3,my=-9e3,mt=0,coarse=matchMedia('(pointer:coarse)').matches,rm=matchMedia('(prefers-reduced-motion: reduce)').matches;
function init(){W=innerWidth;H=window.__hm?Math.min(Math.max(screen.height||900,700),1200):innerHeight;c.style.width=W+'px';c.style.height=H+'px';c.width=W*dpr;c.height=H*dpr;x.setTransform(dpr,0,0,dpr,0,0);P=[];var g=W<700?84:86,cols=Math.ceil(W/g)+1,rows=Math.ceil(H/g)+1;for(var i=0;i<cols;i++)for(var j=0;j<rows;j++){var hx=i*g+(Math.random()-.5)*g*.95,hy=j*g+(Math.random()-.5)*g*.95;P.push({hx:hx,hy:hy,x:hx,y:hy,vx:0,vy:0,s:.9+Math.random()*1,a:.3+Math.random()*.3})}}
function pos(e){var r=c.getBoundingClientRect();mx=e.clientX-r.left;my=e.clientY-r.top;mt=performance.now()}
addEventListener('mousemove',pos);
addEventListener('touchmove',function(e){if(e.touches[0])pos(e.touches[0])},{passive:true});
addEventListener('resize',init);
function col(){return document.documentElement.getAttribute('data-theme')==='light'?'168,127,28':'217,178,78'}
var R=150,t0=performance.now(),lt=-1;
function f(now){requestAnimationFrame(f);if(document.hidden||document.getElementById('intro'))return;
if(window.__hm){var ty=Math.max(0,Math.round(window.__vt||0))+(window.__vt>2?62:0);if(ty!==lt){c.style.top=ty+'px';lt=ty}}
var cc=col(),px=mx,py=my;
if(now-mt>2500){var t=(now-t0)/1000;px=W*(.5+.32*Math.sin(t*.35));py=H*(.5+.28*Math.cos(t*.27));R=coarse?110:90}else R=150;
x.clearRect(0,0,W,H);
for(var i=0;i<P.length;i++){var p=P[i],dx=p.x-px,dy=p.y-py,d2=dx*dx+dy*dy;if(d2<R*R&&d2>.01){var d=Math.sqrt(d2),k=(1-d/R);k=k*k*7;p.vx+=dx/d*k;p.vy+=dy/d*k}
p.vx+=(p.hx-p.x)*.035;p.vy+=(p.hy-p.y)*.035;p.vx*=.86;p.vy*=.86;p.x+=p.vx;p.y+=p.vy;
if(p.y<76&&!window.__hm)continue;var dsp=Math.min(1,Math.hypot(p.x-p.hx,p.y-p.hy)/40);x.fillStyle='rgba('+cc+','+(p.a+dsp*.3)+')';x.beginPath();x.arc(p.x,p.y,p.s*(1+dsp*.4),0,6.283);x.fill()}}
init();setTimeout(init,1800);if(rm){x.fillStyle='rgba('+col()+',.3)';P.forEach(function(p){x.beginPath();x.arc(p.x,p.y,p.s,0,6.283);x.fill()})}else requestAnimationFrame(f)}catch(e){try{console.warn("audira",e)}catch(_){}}})();
;(function(){try{function ease(t){return t<.5?4*t*t*t:1-Math.pow(-2*t+2,3)/2}
document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[href^="#"]');if(!a||window.__hm)return;var id=a.getAttribute('href').slice(1);var el=id&&document.getElementById(id);if(!el)return;e.preventDefault();var y0=window.pageYOffset,y1=el.getBoundingClientRect().top+y0-70,dist=y1-y0,dur=Math.min(1500,Math.max(700,Math.abs(dist)*.35)),t0=performance.now();
(function st(n){var k=Math.min(1,(n-t0)/dur);window.scrollTo(0,y0+dist*ease(k));if(k<1)requestAnimationFrame(st)})(t0)})}catch(e){}})();
