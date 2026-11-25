
(function(){
var cv=document.getElementById('cv'),ctx=cv.getContext('2d'),track=document.getElementById('track');
var caps=[].slice.call(document.querySelectorAll('.cap')),dots=[].slice.call(document.querySelectorAll('.dots i')),hint=document.getElementById('hint');
var pg=document.getElementById('prog');var calm=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
var V="128,400|37%|−1,310|15%|فاتورة|INV-0412|ذمم|كشف بنك|61,000|8.2%|ضريبة|−240|7,900|VAT|زكاة|3,150|عُهدة|12,640|5%|قيد|−85|41,200|تسوية|11%|9,870|فاتورة|−4,020|رواتب|1,205|WPS|86,300|−610|موردين|2,015|عملاء|340|IFRS|58,700|−1,980|IBAN|4,400|مصروفات|73,150|−90|إيرادات|19|6,260|نقد".split('|');
var VE=V.map(function(w){var M={"فاتورة":"Invoice","ذمم":"A/R","كشف بنك":"Bank stmt","ضريبة":"Tax","زكاة":"Zakat","عُهدة":"Petty cash","قيد":"Journal","تسوية":"Settlement","رواتب":"Payroll","موردين":"Vendors","عملاء":"Clients","مصروفات":"Expenses","إيرادات":"Revenue","نقد":"Cash"};return M[w]||w});
function LT(){return document.documentElement.dir=="ltr"}
var N=48,HT=[2,3,3,4,3,4,5,4,5,6,5,4],slots=[],ANOM=23;
HT.forEach(function(h,m){for(var k=0;k<h;k++)slots.push([m,k])});
var s=7;function rnd(){s=(s*16807)%2147483647;return s/2147483647}
var rp=[];for(var i=0;i<N;i++)rp.push([rnd(),rnd(),rnd()*6.28,.5+rnd()]);
var CITY=[["الرياض",.5,.42],["القاهرة",.1,.36],["مسقط",.9,.7],["الدوحة",.72,.5],["الكويت",.62,.14]],CITYE=["Riyadh","Cairo","Muscat","Doha","Kuwait"];
var W,H,R,T,BW,BH,narrow,base,cw,bh,dpr;
function layout(){
dpr=Math.min(window.devicePixelRatio||1,2);W=cv.clientWidth;H=cv.clientHeight;cv.width=W*dpr;cv.height=H*dpr;ctx.setTransform(dpr,0,0,dpr,0,0);
narrow=W<760;
R=narrow?{x:W*.07,y:H*.14,w:W*.86,h:H*.4}:{x:LT()?W*.37:W*.05,y:H*.17,w:W*.58,h:H*.66};var lt=LT(),cwid=Math.min(W*.3,400),capL=lt?W*.06+cwid+36:20,capR=lt?W-20:W-W*.06-cwid-36;
cw=R.w/12;bh=Math.min(R.h*.1,26);base=R.y+R.h*.88;
BW=[5,5,5,cw*.62,cw*.62,6];BH=[5,5,5,bh*.8,bh*.8,6];
T=[[],[],[],[],[],[]];
for(var i=0;i<N;i++){
var m=slots[i][0],k=slots[i][1],bx=lt?R.x+(m+.5)*cw:R.x+R.w-(m+.5)*cw;
T[0].push([narrow?rp[i][0]*W:capL+rp[i][0]*Math.max(40,capR-capL),rp[i][1]*H]);
T[1].push([lt?R.x+(i%6+.5)*R.w/6:R.x+R.w-(i%6+.5)*R.w/6,R.y+(Math.floor(i/6)+.5)*R.h/8]);
T[2].push([bx,R.y+R.h*.28+k*R.h*.11]);
T[3].push([bx,base-(k+.5)*bh]);
T[4].push([bx,base-(k+.5)*bh-(i==ANOM?bh*2.6:0)]);
var c=CITY[i%5],r=R.h*.035*(.4+(i%7)/7);
T[5].push([R.x+c[1]*R.w+Math.cos(i*2.4)*r,R.y+c[2]*R.h+Math.sin(i*2.4)*r]);
}}
function sm(x){x=Math.max(0,Math.min(1,x));return x*x*(3-2*x)}
var cur=0,tgt=0,active=-1;
function prog(){var r=track.getBoundingClientRect();return Math.max(0,Math.min(1,-r.top/(r.height-window.innerHeight)))*5}
function draw(t){
var lt=LT();
ctx.clearRect(0,0,W,H);
var a=Math.min(4,Math.floor(cur)),f=cur-a,e=sm(f);
function A(r){return r[a]+(r[a+1]-r[a])*e}
var fs=narrow?11:13,i,x,y,p,q;
var lineA=A([0,1,0,0,0,0]);
if(lineA>.01){ctx.strokeStyle="rgba(159,179,200,"+(.2*lineA)+")";ctx.lineWidth=1;for(i=0;i<=8;i++){y=R.y+i*R.h/8;ctx.beginPath();ctx.moveTo(R.x,y);ctx.lineTo(R.x+R.w,y);ctx.stroke()}}
var gA=A([0,0,0,1,.8,0]);
if(gA>.01){ctx.strokeStyle="rgba(159,179,200,"+(.35*gA)+")";ctx.beginPath();ctx.moveTo(R.x,base+3);ctx.lineTo(R.x+R.w,base+3);ctx.stroke()}
var mA=A([0,0,1,.8,.4,0]);
if(mA>.01){var ly=R.y+R.h*.16+(base+20-(R.y+R.h*.16))*sm(cur-2);ctx.fillStyle="rgba(159,179,200,"+mA+")";ctx.font="300 "+(narrow?9:11)+"px Barlow,Cairo,sans-serif";ctx.textAlign="center";
for(i=0;i<12;i++)ctx.fillText((i<9?"0":"")+(i+1),lt?R.x+(i+.5)*cw:R.x+R.w-(i+.5)*cw,ly)}
var nA=A([0,0,0,1,1,0]);
if(nA>.01){ctx.fillStyle="rgba(159,179,200,"+(.7*nA)+")";ctx.font="300 11px Barlow,Cairo,sans-serif";ctx.textAlign="center";ctx.fillText(lt?"Illustration only, not client data":"رسم توضيحي — وليس بيانات عميل",R.x+R.w/2,R.y+R.h+12)}
var cA=A([0,0,0,0,0,1]);
if(cA>.01){var C0=CITY[0];ctx.strokeStyle="rgba(217,178,78,"+(.35*cA)+")";
for(i=1;i<5;i++){ctx.beginPath();ctx.moveTo(R.x+C0[1]*R.w,R.y+C0[2]*R.h);ctx.lineTo(R.x+CITY[i][1]*R.w,R.y+CITY[i][2]*R.h);ctx.stroke()}
ctx.fillStyle="rgba(243,241,236,"+cA+")";ctx.font="500 "+(narrow?12:14)+"px Barlow,Cairo,sans-serif";ctx.textAlign="center";
for(i=0;i<5;i++)ctx.fillText(lt?CITYE[i]:CITY[i][0],R.x+CITY[i][1]*R.w,R.y+CITY[i][2]*R.h-R.h*.075)}
var amp=calm?0:A([18,2,0,0,0,0]),ta=A([.55,.85,.65,0,0,0])*(innerWidth<700?0:.62),ba=A([0,0,.4,1,1,.85]),bw=A(BW),bhh=A(BH);
var aw=sm(cur-3)*(1-sm(cur-4)),ax=0,ay=0;
for(i=0;i<N;i++){
p=T[a][i];q=T[a+1][i];x=p[0]+(q[0]-p[0])*e;y=p[1]+(q[1]-p[1])*e;
if(amp>.05){x+=Math.sin(t*rp[i][3]+rp[i][2])*amp;y+=Math.cos(t*rp[i][3]*.8+rp[i][2])*amp}
var an=i==ANOM,dim=an?1:1-.55*aw;
if(ta>.01&&(an||i%3!=2)){ctx.fillStyle="rgba("+"212,172,70,"+Math.min(1,ta*dim)+")";ctx.font="400 "+fs*(.85+rp[i][3]*.45)+"px Barlow,Cairo,sans-serif";ctx.textAlign="center";ctx.textBaseline="middle";ctx.fillText((lt?VE:V)[i],x,y)}
if(ba>.01){ctx.fillStyle=an&&aw>.02?"rgba(255,244,214,"+ba+")":"rgba(199,155,47,"+(ba*dim)+")";ctx.fillRect(x-bw/2,y-bhh/2,bw,bhh)}
if(an){ax=x;ay=y}
}
if(aw>.05){var pr=14+4*Math.sin(t*4);ctx.strokeStyle="rgba(255,244,214,"+(aw*.8)+")";ctx.lineWidth=1.5;ctx.beginPath();ctx.arc(ax,ay,pr,0,6.283);ctx.stroke();
ctx.fillStyle="rgba(255,244,214,"+aw+")";ctx.font="500 12px Barlow,Cairo,sans-serif";ctx.textAlign="center";ctx.fillText(lt?"Variance needs review":"انحراف يحتاج مراجعة",ax,ay-28)}
}
function frame(ms){
tgt=prog();cur=calm?tgt:cur+(tgt-cur)*.09;if(Math.abs(tgt-cur)<.0008)cur=tgt;
draw(ms/1000);
var n=Math.round(cur);
if(n!==active){active=n;caps.forEach(function(c,i){c.classList.toggle('on',i===n)});dots.forEach(function(d,i){d.classList.toggle('on',i===n)})}
hint.style.opacity=cur>.25?0:1;pg.style.width=(Math.min(1,window.scrollY/Math.max(1,document.documentElement.scrollHeight-innerHeight))*100)+'%';
requestAnimationFrame(frame)}
layout();window.addEventListener('resize',layout);window.addEventListener('langchange',layout);
requestAnimationFrame(frame);
if('IntersectionObserver'in window){var io=new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){en.target.classList.add('v');io.unobserve(en.target)}})},{threshold:.2});
[].forEach.call(document.querySelectorAll('.rv'),function(el){io.observe(el)})}else{[].forEach.call(document.querySelectorAll('.rv'),function(el){el.classList.add('v')})}
})();
