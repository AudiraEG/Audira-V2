import sys,base64,re,json,urllib.parse,os
sys.path.insert(0,'/downloads/audira_brand'); os.chdir('/downloads/audira_brand')
from lib import *
os.chdir('/downloads/audira_site')
b64=lambda p:base64.b64encode(open(p,'rb').read()).decode()
F='/downloads/audira_brand/fonts/'
WA='https://wa.me/20XXXXXXXXXX'
def wa(t): return WA+'?text='+urllib.parse.quote(t)
LG=('<span class="lg-d">'+wm('#F3F1EC',GD,22)+'</span><span class="lg-l">'+wm(INK,GL,22)+'</span>')
LGF=('<span class="lg-d">'+wm('#F3F1EC',GD,30)+'</span><span class="lg-l">'+wm(INK,GL,30)+'</span>')
fav='data:image/svg+xml;base64,'+base64.b64encode(icon(64,GM,NAVY,16).encode()).decode()

CSS=r'''
:root,:root[data-theme=dark]{--bg:#0A0E1A;--bg2:#0E1424;--ink:#F3F1EC;--mut:#9AA3B5;--ac:#D9B24E;--acf:#C79B2F;--onac:#0B1020;--ln:rgba(159,179,200,.18);--card:rgba(255,255,255,.04);--cardh:rgba(255,255,255,.07);--sh:0 20px 50px rgba(0,0,0,.45);--cvt:159,179,200;--cvA:217,178,78;--cvb:199,155,47;--cvn:255,244,214;--cvi:243,241,236;color-scheme:dark}
:root[data-theme=light]{--bg:#FFFFFF;--bg2:#F5F6F8;--ink:#0B1020;--mut:#555B66;--ac:#A87F1C;--acf:#A87F1C;--onac:#fff;--ln:rgba(11,16,32,.15);--card:#fff;--cardh:#fff;--sh:0 18px 44px rgba(11,16,32,.14);--cvt:85,91,102;--cvA:168,127,28;--cvb:168,127,28;--cvn:11,16,32;--cvi:11,16,32;color-scheme:light}
*{box-sizing:border-box;margin:0}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--ink);font-family:Barlow,Cairo,Tahoma,system-ui,sans-serif;line-height:1.8;overflow-x:hidden;transition:background .4s,color .4s}
a{color:inherit}
.lg-l{display:none}.lg-d{display:inline-flex}
:root[data-theme=light] .lg-l{display:inline-flex}:root[data-theme=light] .lg-d{display:none}
#track{height:640vh;position:relative}
.stage{position:sticky;top:0;height:100vh;height:100svh;overflow:hidden}
canvas{position:absolute;inset:0;width:100%;height:100%}
.glow{position:absolute;left:-10vw;bottom:-20vh;width:60vw;height:60vw;background:radial-gradient(closest-side,rgba(217,178,78,.12),transparent);pointer-events:none}
:root[data-theme=light] .glow{background:radial-gradient(closest-side,rgba(168,127,28,.10),transparent)}
.bar{position:absolute;top:0;left:0;right:0;display:flex;justify-content:space-between;align-items:center;padding:18px 6vw;z-index:3;gap:14px}
.logo{display:flex;align-items:center;gap:14px;direction:ltr}
.logo small{color:var(--mut);font-size:12px;direction:rtl;border-left:1px solid var(--ln);padding-left:14px}
.nav{display:flex;align-items:center;gap:22px;font-size:14px}
.nav a.l{text-decoration:none;color:var(--mut);transition:.2s}.nav a.l:hover{color:var(--ac)}
.pill{font-size:13px;text-decoration:none;border:1px solid var(--ac);color:var(--ac);padding:6px 16px;border-radius:99px;transition:.3s;white-space:nowrap}
.pill:hover{background:var(--ac);color:var(--onac)}
.tg{width:36px;height:36px;border-radius:50%;border:1px solid var(--ln);background:var(--card);color:var(--ink);display:grid;place-items:center;cursor:pointer;transition:.3s}
.tg:hover{border-color:var(--ac);color:var(--ac)}
.tg svg{width:18px;height:18px}.tg .sun{display:none}
:root[data-theme=light] .tg .sun{display:block}:root[data-theme=light] .tg .moon{display:none}
.caps{position:absolute;right:6vw;top:50%;width:min(30vw,400px);height:0;z-index:2}
.cap{position:absolute;top:0;opacity:0;transform:translateY(calc(-50% + 16px));transition:opacity .7s,transform .7s;pointer-events:none}
.cap.on{opacity:1;transform:translateY(-50%);pointer-events:auto}
.tag{display:flex;align-items:center;gap:10px;color:var(--ac);font-size:12.5px;margin-bottom:14px;font-weight:600}
.tag::before{content:"";width:28px;height:1px;background:currentColor}
.cap h2{font-size:clamp(1.5rem,2.6vw,2.2rem);font-weight:800;line-height:1.4;margin-bottom:12px}
.cap h1{font-size:clamp(1.9rem,3.6vw,3.2rem);font-weight:800;line-height:1.35;margin-bottom:16px}
.cap h1 em{font-style:normal;color:var(--ac);position:relative;display:inline-block}
.cap h1 em svg{position:absolute;left:-2%;bottom:-10px;width:104%;height:12px;overflow:visible}
.cap p{color:var(--mut);font-size:clamp(.95rem,1.2vw,1.05rem)}
.hint{position:absolute;bottom:22px;left:50%;transform:translateX(-50%);font-size:12px;color:var(--mut);display:flex;flex-direction:column;align-items:center;gap:8px;transition:opacity .5s;z-index:2}
.hint::after{content:"";width:1px;height:28px;background:linear-gradient(var(--mut),transparent);animation:dr 1.8s infinite}
@keyframes dr{0%{transform:scaleY(0);transform-origin:top}60%{transform:scaleY(1);transform-origin:top}100%{transform:scaleY(1);transform-origin:bottom;opacity:0}}
.dots{position:absolute;left:22px;top:50%;transform:translateY(-50%);display:flex;flex-direction:column;gap:12px;z-index:2}
.dots i{width:4px;height:4px;border-radius:9px;background:var(--ln);transition:.4s}
.dots i.on{height:22px;background:var(--ac)}
.sec{position:relative;padding:120px 6vw}
.wrap{max-width:1180px;margin:0 auto}
.k{font-weight:700;font-size:13.5px;color:var(--ac);margin-bottom:16px;display:flex;align-items:center;gap:12px}
.k b{font:600 13px Barlow;letter-spacing:.2em;opacity:.7;direction:ltr}
.big{font-size:clamp(1.8rem,4vw,3.2rem);font-weight:800;line-height:1.35}
.lead{color:var(--mut);font-size:clamp(1rem,1.4vw,1.15rem);max-width:54ch;margin-top:20px}
.rv{opacity:0;transform:translateY(26px);transition:opacity .9s,transform .9s}.rv.v{opacity:1;transform:none}
/* academy */
.acad{display:grid;grid-template-columns:1.1fr .9fr;gap:60px;align-items:end}
.chips{display:flex;flex-wrap:wrap;gap:10px;direction:ltr;justify-content:flex-start}
.chips span{border:1px solid var(--ln);background:var(--card);padding:8px 18px;border-radius:99px;font-size:1.05rem}
.chips span:nth-child(3n+1){transform:rotate(-1.5deg)}.chips span:nth-child(3n){transform:rotate(1deg);border-color:var(--ac);color:var(--ac)}
.sheet{background:var(--bg2);border-block:1px solid var(--ln)}
/* dashboard */
.dsh{display:grid;grid-template-columns:1.25fr .75fr;gap:50px;align-items:center}
.stack{position:relative;padding:0 0 70px 40px}
.win{background:var(--bg);border:1px solid var(--ln);border-radius:16px;box-shadow:var(--sh);overflow:hidden;direction:rtl;transform:rotate(-1.2deg)}
.sheet .win{background:var(--bg)}
.wb{display:flex;align-items:center;gap:6px;padding:11px 16px;border-bottom:1px solid var(--ln);font-size:12px;color:var(--mut)}
.wb i{width:9px;height:9px;border-radius:50%;background:var(--ln)}.wb i:first-child{background:var(--ac)}
.wb span{margin-right:auto;margin-left:0}
.kp{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;padding:16px}
.kp div{border:1px solid var(--ln);border-radius:10px;padding:12px 14px}
.kp small{display:block;color:var(--mut);font-size:11.5px}.kp b{font:600 22px Barlow;direction:ltr;display:block;text-align:right}
.kp b.up{color:var(--ac)}
.chart{padding:4px 16px 8px}.chart svg{width:100%;height:auto;display:block}
.ledger{position:absolute;left:0;bottom:0;width:260px;background:#F3F1EC;color:#0B1020;border-radius:6px;padding:16px 16px 14px;box-shadow:var(--sh);transform:rotate(3.2deg);font-size:12px}
.ledger h6{font:700 11px Barlow;letter-spacing:.18em;color:#A87F1C;margin-bottom:8px}
.ledger div{display:flex;justify-content:space-between;border-bottom:1px solid #0b102022;padding:5px 0}
.ledger div b{font:600 12.5px Barlow;direction:ltr}
.stamp{position:absolute;left:14px;top:-18px;transform:rotate(-8deg);border:2px solid #A87F1C;color:#A87F1C;border-radius:8px;padding:2px 10px;font-weight:800;font-size:12px;background:#F3F1EC}
.pts{display:grid;gap:26px}
.pts div{border-right:2px solid var(--ac);padding-right:18px}
.pts h4{font-size:1.2rem;font-weight:800}.pts p{color:var(--mut);font-size:.98rem}
.cap-note{font-size:12px;color:var(--mut);margin-top:12px}
/* about */
.about{display:grid;grid-template-columns:.8fr 1.2fr;gap:70px}
.pq{font-size:clamp(1.6rem,3vw,2.5rem);font-weight:800;line-height:1.5;position:relative;padding-top:42px}
.pq::before{content:"”";position:absolute;top:-26px;right:-4px;font:800 120px/1 Barlow;color:var(--ac);opacity:.9}
.about p{color:var(--mut);margin-bottom:16px;font-size:1.05rem}
.about p.f{color:var(--ink)}
.vals{display:flex;gap:14px;margin-top:26px;flex-wrap:wrap}
.vals div{flex:1 1 150px;border:1px solid var(--ln);background:var(--card);border-radius:12px;padding:16px}
.vals div:nth-child(2){margin-top:22px}
.vals b{display:block;font-size:1.05rem;color:var(--ac)}.vals span{font-size:.9rem;color:var(--mut)}
/* badges */
.badge{display:inline-block;font-size:12px;color:var(--onac);background:var(--ac);border-radius:99px;padding:2px 12px;font-weight:700}
/* packages */
.pk{display:grid;grid-template-columns:1fr 1.08fr 1fr;gap:20px;align-items:start;margin-top:50px}
.pc{border:1px solid var(--ln);background:var(--card);border-radius:18px;padding:30px 26px;position:relative}
.pc.mid{background:var(--ink);color:var(--bg);margin-top:-26px;border:none;box-shadow:var(--sh)}
.pc.mid .pn,.pc.mid li{color:var(--bg)}.pc.mid li::before{color:var(--ac)}
:root[data-theme=dark] .pc.mid li::before{color:#A87F1C}
.pc h3{font-size:1.4rem;font-weight:800}.pn{color:var(--mut);font-size:.95rem;margin-top:4px}
.pr{margin:22px 0 18px;direction:ltr;text-align:right;font:600 44px/1 Barlow;color:var(--ac)}
.pc.mid .pr{color:#A87F1C}:root[data-theme=light] .pc.mid .pr{color:#D9B24E}
.pr small{font:400 14px Cairo;opacity:.7;margin-right:6px}
.pc ul{list-style:none;padding:0;display:grid;gap:10px}
.pc li{font-size:.97rem;color:var(--mut);padding-right:24px;position:relative}
.pc li::before{content:"✓";position:absolute;right:0;color:var(--ac);font-weight:800}
.pc .tagm{position:absolute;top:-13px;right:24px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;margin-top:24px;background:linear-gradient(135deg,#D9B24E,#C79B2F);color:#0B1020;font-weight:800;text-decoration:none;padding:13px 30px;border-radius:99px;font-size:1rem;transition:.3s;border:0;cursor:pointer;font-family:inherit}
:root[data-theme=light] .btn{background:#A87F1C;color:#fff}
.btn:hover{transform:translateY(-2px);box-shadow:0 10px 30px rgba(217,178,78,.3)}
.btn.o{background:transparent!important;border:1px solid var(--ln);color:var(--ink)!important}.btn.o:hover{border-color:var(--ac);color:var(--ac)!important;box-shadow:none}
.pc .btn{width:100%}
.pc.mid .btn.o{border-color:#0b102044;color:var(--bg)!important}
/* proof */
.stats{display:flex;flex-wrap:wrap;gap:0;margin-top:44px;border-block:1px solid var(--ln)}
.st{flex:1 1 200px;padding:26px 24px;border-left:1px solid var(--ln);position:relative}
.st:last-child{border-left:0}
.st b{display:block;font:600 clamp(2.4rem,4.4vw,3.6rem)/1 Barlow;color:var(--ac);direction:ltr;text-align:right}
.st span{display:block;margin-top:10px;color:var(--mut);font-size:.95rem}
.st i{position:absolute;top:8px;left:12px;font-style:normal;font-size:10.5px;color:var(--mut)}
.quotes{display:grid;grid-template-columns:1.3fr 1fr 1fr;gap:18px;margin-top:30px;align-items:start}
.q{border:1px dashed var(--ac);border-radius:14px;padding:24px}
.q:nth-child(2){margin-top:30px}.q:nth-child(3){margin-top:12px}
.q p{line-height:1.9}.q small{display:block;margin-top:14px;color:var(--mut);font-size:13px}
.note{margin-top:20px;font-size:12.5px;color:var(--mut)}
/* faq */
.faqw{display:grid;grid-template-columns:.7fr 1.3fr;gap:70px}
details{border-bottom:1px solid var(--ln);padding:20px 0}
details summary{cursor:pointer;font-weight:700;font-size:1.1rem;list-style:none;display:flex;justify-content:space-between;gap:16px}
details summary::-webkit-details-marker{display:none}
details summary::after{content:"+";font:400 28px/1 Barlow;color:var(--ac);transition:.3s}
details[open] summary::after{transform:rotate(45deg)}
details p{color:var(--mut);margin-top:12px;max-width:60ch}
/* contact */
.ct{display:grid;grid-template-columns:.9fr 1.1fr;gap:60px}
.cards{display:grid;gap:14px;margin-top:30px}
.cc{display:flex;gap:16px;align-items:center;border:1px solid var(--ln);background:var(--card);border-radius:14px;padding:16px 20px;text-decoration:none;transition:.3s}
.cc:hover{border-color:var(--ac);transform:translateX(-4px)}
.cc small{display:block;color:var(--mut);font-size:12.5px}.cc b{font-size:1.05rem}
.cc .ic{width:42px;height:42px;border-radius:12px;background:var(--ac);color:var(--onac);display:grid;place-items:center;font-weight:800;flex:none}
.cc b.ltr{direction:ltr;display:block;text-align:right}
.form{background:var(--card);border:1px solid var(--ln);border-radius:20px;padding:30px;box-shadow:var(--sh)}
.form label{display:block;font-size:13px;color:var(--mut);margin:0 0 6px}
.form input,.form select,.form textarea{width:100%;background:var(--bg);color:var(--ink);border:1px solid var(--ln);border-radius:10px;padding:12px 14px;font:inherit;margin-bottom:16px;outline:none;transition:.2s}
.form input:focus,.form select:focus,.form textarea:focus{border-color:var(--ac)}
.form textarea{min-height:110px;resize:vertical}
.fr{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.form .acts{display:flex;gap:12px;flex-wrap:wrap;align-items:center}.form .btn{margin-top:4px}
/* footer */
footer{border-top:1px solid var(--ln);padding:70px 6vw 34px;background:var(--bg2)}
.fg{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:40px}
footer h5{font-size:13px;color:var(--ac);margin-bottom:14px;letter-spacing:.04em}
footer a{display:block;text-decoration:none;color:var(--mut);font-size:.95rem;margin-bottom:8px}footer a:hover{color:var(--ac)}
footer .ab{color:var(--mut);margin-top:16px;font-size:.95rem;max-width:34ch}
.fb{display:flex;justify-content:space-between;flex-wrap:wrap;gap:10px;margin-top:50px;padding-top:22px;border-top:1px solid var(--ln);font-size:12.5px;color:var(--mut)}
@media(max-width:900px){.acad,.dsh,.about,.faqw,.ct{grid-template-columns:1fr;gap:40px}.pk{grid-template-columns:1fr}.pc.mid{margin-top:0}.quotes{grid-template-columns:1fr}.q:nth-child(n){margin-top:0}.fg{grid-template-columns:1fr 1fr}.stack{padding-left:0}.ledger{position:relative;margin:-30px 0 0 0;left:auto;width:230px}.nav a.l{display:none}.sec{padding:84px 6vw}.fr{grid-template-columns:1fr}}
@media(max-width:760px){.caps{right:6vw;left:6vw;width:auto;top:auto;bottom:6vh}.cap{top:auto;bottom:0;transform:translateY(16px)}.cap.on{transform:none}.dots,.hint{display:none}.logo small{display:none}}
@media(max-width:560px){.fg{grid-template-columns:1fr}.st{border-left:0;border-bottom:1px solid var(--ln)}}

/* services */
.svcs{display:grid;grid-template-columns:repeat(12,1fr);gap:20px;margin-top:54px}
.sv{border:1px solid var(--ln);background:var(--card);border-radius:20px;padding:30px 28px;position:relative;overflow:hidden}
.sv .no{font:600 64px/1 Barlow;color:var(--ac);opacity:.9;direction:ltr;text-align:right;margin-bottom:6px}
.sv h3{font-size:1.35rem;font-weight:800;margin-bottom:8px}
.sv .si{color:var(--mut);font-size:.98rem;margin-bottom:16px}
.sv ul{list-style:none;padding:0;display:grid;gap:8px}
.sv li{font-size:.95rem;padding-right:20px;position:relative}
.sv li::before{content:"";position:absolute;right:0;top:.8em;width:10px;height:1px;background:var(--ac)}
.sv.a{grid-column:span 7}.sv.b{grid-column:span 5;margin-top:44px}
.sv.c{grid-column:span 5}.sv.d{grid-column:span 7;margin-top:0;background:var(--ink);color:var(--bg);border:none}
.sv.d .si,.sv.d li{color:var(--bg)}.sv.d .no{color:#A87F1C}:root[data-theme=light] .sv.d .no{color:#D9B24E}
.sv.e{grid-column:span 6}.sv.f{grid-column:span 6;margin-top:30px}
.sv.d li::before{background:#A87F1C}
.rg{margin-top:18px;font-size:12.5px;color:var(--mut);border-top:1px dashed var(--ln);padding-top:12px}
.sv.d .rg{color:var(--bg);opacity:.75;border-color:#0b102033}
.tools{display:flex;flex-wrap:wrap;gap:8px;margin-top:16px;direction:ltr}
.tools span{border:1px solid currentColor;border-radius:99px;padding:2px 12px;font-size:13px;opacity:.85}
.pdfn{margin-top:26px;font-size:13px;color:var(--mut)}
/* team and models */
.team{margin-top:26px;border:1px solid var(--ln);background:var(--card);border-radius:16px;padding:22px 24px}
.team h4{color:var(--ac);font-size:1rem;margin-bottom:10px}
.team ul{list-style:none;padding:0;display:grid;gap:8px;margin-bottom:14px}
.team li{padding-right:20px;position:relative;color:var(--mut);font-size:.97rem}
.team li::before{content:"";position:absolute;right:0;top:.8em;width:10px;height:1px;background:var(--ac)}
.quals{display:flex;gap:10px;direction:ltr;flex-wrap:wrap;margin-top:8px}
.quals b{font:700 20px Barlow;letter-spacing:.08em;border:1px solid var(--ac);color:var(--ac);border-radius:10px;padding:4px 16px}
.quals b:nth-child(2){transform:translateY(5px)}
.mods{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:50px;align-items:start}
.md{border:1px solid var(--ln);background:var(--card);border-radius:18px;padding:26px 22px;position:relative}
.md:nth-child(2){margin-top:26px}.md:nth-child(3){margin-top:-12px}.md:nth-child(4){margin-top:14px}
.md i{font:600 13px Barlow;color:var(--ac);letter-spacing:.2em;font-style:normal;display:block;margin-bottom:12px}
.md h3{font-size:1.2rem;font-weight:800;margin-bottom:6px}.md p{color:var(--mut);font-size:.95rem}
.md .pr{font-size:28px;margin:16px 0 0}
.follow{margin-top:34px;border-right:2px solid var(--ac);padding:4px 20px 4px 0;max-width:70ch}
.follow h4{font-size:1.1rem;font-weight:800}.follow p{color:var(--mut)}
/* sectors */
.secs{display:flex;flex-wrap:wrap;gap:12px;margin-top:40px}
.secs span{border:1px solid var(--ln);background:var(--card);padding:10px 22px;border-radius:99px;font-size:1.02rem}
.secs span:nth-child(4n+1){border-color:var(--ac);color:var(--ac)}
.secs span:nth-child(3n){transform:translateY(6px)}
@media(max-width:900px){.svcs{grid-template-columns:1fr}.sv.a,.sv.b,.sv.c,.sv.d,.sv.e,.sv.f{grid-column:auto;margin-top:0}.mods{grid-template-columns:1fr 1fr}.md:nth-child(n){margin-top:0}}
@media(max-width:560px){.mods{grid-template-columns:1fr}}

/* v4 editorial */
.ph{display:block;width:100%;height:100%;object-fit:cover;transform:scale(1.12);transition:transform 1.4s cubic-bezier(.2,.7,.2,1);will-change:transform}
.pf{position:relative;isolation:isolate}
.pf::after{content:"";position:absolute;inset:0;border:1px solid var(--ac);transform:translate(-16px,16px);z-index:-1;border-radius:3px;transition:transform .6s}
.pf:hover::after{transform:translate(-8px,8px)}
.pf:hover .ph{transform:scale(1.04)}
.pi{overflow:hidden;border-radius:3px;background:#2A4378;position:relative;height:100%}
.pi::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(5,8,19,0) 65%,rgba(5,8,19,.3));pointer-events:none}
:root[data-theme=dark] .ph{filter:brightness(.95)}
.cap2{position:absolute;bottom:14px;right:16px;color:#F1DC9C;font-size:12.5px;letter-spacing:.04em;z-index:2}
.disp{font-size:clamp(2.5rem,7.2vw,6.6rem);line-height:1.2;font-weight:800}
.disp em{font-style:normal;color:var(--ac)}
.rv{transition-delay:var(--d,0s)}
.tick{border-block:1px solid var(--ln);overflow:hidden;direction:ltr;background:var(--bg2);padding:16px 0}
.tick div{display:flex;width:max-content;gap:0;animation:tk 48s linear infinite}
.tick span{font:600 15px Barlow,Cairo;letter-spacing:.22em;text-transform:uppercase;white-space:nowrap;padding:0 28px;color:var(--mut);display:flex;align-items:center;gap:56px}
.tick span::after{content:"";width:6px;height:6px;background:var(--ac);transform:rotate(45deg)}
@keyframes tk{to{transform:translateX(-50%)}}
.tick:hover div{animation-play-state:paused}
.man{padding-top:140px}
.man-g{display:grid;grid-template-columns:1.25fr .75fr;gap:70px;margin-top:70px;align-items:start}
.man-g .big-ph{aspect-ratio:4/3}
.man-t .lead{margin-top:0;font-size:1.25rem;color:var(--ink);max-width:none}
.man-t p{color:var(--mut);margin-top:20px}
.man-t .pf{margin-top:44px;aspect-ratio:3/2;width:78%;margin-right:auto}
.svh{display:flex;justify-content:space-between;align-items:end;gap:40px;flex-wrap:wrap}
.sr{display:grid;grid-template-columns:5fr 7fr;gap:70px;padding:84px 0;border-top:1px solid var(--ln);align-items:start;position:relative}
.sr:last-child{border-bottom:1px solid var(--ln)}
.sr:nth-child(even) .sl{order:2}
.sn{font:600 clamp(5rem,12vw,10rem)/.9 Barlow;color:transparent;-webkit-text-stroke:1px var(--ac);direction:ltr;text-align:right;transition:color .5s;margin-bottom:18px}
.sr:hover .sn{color:var(--ac)}
.sl h3{font-size:clamp(1.8rem,3.4vw,2.9rem);font-weight:800;line-height:1.3;margin-bottom:16px}
.sl .si{color:var(--mut);font-size:1.06rem;max-width:44ch}
.sd .pf{aspect-ratio:16/9;margin-bottom:34px}
.sd ul{list-style:none;padding:0;columns:2;column-gap:36px}
.sd li{break-inside:avoid;padding:10px 24px 10px 0;position:relative;border-bottom:1px solid var(--ln);font-size:.98rem;transition:padding .3s,color .3s}
.sd li::before{content:"";position:absolute;right:0;top:1.35em;width:12px;height:1px;background:var(--ac);transition:width .3s}
.sd li:hover{color:var(--ac);padding-right:34px}.sd li:hover::before{width:24px}
.sd .rg{margin-top:20px;font-size:12.5px;color:var(--mut);border-right:2px solid var(--ac);padding-right:14px}
.sd .tools{direction:ltr;display:flex;gap:8px;flex-wrap:wrap;margin-top:20px}
.sd .tools span{border:1px solid var(--ac);color:var(--ac);border-radius:99px;padding:2px 14px;font-size:13px}
.sd .win{transform:none;margin-bottom:34px}.sd .stack{padding:0 0 60px 30px;margin-bottom:6px}.sd .stack .win{margin-bottom:0}
.band{position:relative;height:min(78vh,720px);overflow:hidden;display:flex;align-items:end;background:#050813}
.bimg{position:absolute;inset:-12% 0;}
.bimg .ph{transform:none;object-position:50% 88%;filter:none!important}
.band::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(18,30,66,.1),rgba(18,30,66,.55) 45%,rgba(18,30,66,.9));}
.bov{position:relative;z-index:2;width:100%;padding:0 6vw 70px;color:#F3F1EC}
.bov .k{color:#D9B24E}.bov p{margin-top:34px;font:500 1.1rem Barlow;letter-spacing:.3em;color:#D9B24E;direction:ltr;text-align:right}
.ab2{display:grid;grid-template-columns:1.1fr .9fr;gap:90px;align-items:start}
.ab2 .pq{font-size:clamp(1.9rem,3.6vw,3.2rem)}
.ab2 .f{font-size:1.15rem}
.ab2 .ph-col{position:relative;padding-bottom:90px}
.ab2 .tall{aspect-ratio:4/5}
.ab2 .small{position:absolute;width:52%;aspect-ratio:1;bottom:0;left:-8%}
.quals b{font-size:26px;padding:8px 22px;border-radius:4px;transition:.3s}.quals b:hover{background:var(--ac);color:var(--onac)}
.mods4{display:grid;grid-template-columns:repeat(4,1fr);margin-top:64px;border-top:1px solid var(--ln)}
.m4{padding:34px 26px 40px;border-left:1px solid var(--ln);position:relative;transition:background .4s}
.m4:last-child{border-left:0}
.m4:hover{background:var(--card)}
.m4 i{font:600 70px/1 Barlow;color:transparent;-webkit-text-stroke:1px var(--ac);display:block;margin-bottom:22px;font-style:normal;direction:ltr;text-align:right}
.m4:hover i{color:var(--ac)}
.m4 h3{font-size:1.4rem;font-weight:800}.m4 p{color:var(--mut);margin-top:6px}
.m4 .pr{font-size:30px;margin:26px 0 0}
.m4:nth-child(2){padding-top:70px}.m4:nth-child(4){padding-top:56px}
.sl2{margin-top:50px;border-top:1px solid var(--ln)}
.sl2 a,.sl2 div.r{display:flex;align-items:baseline;gap:28px;padding:22px 0;border-bottom:1px solid var(--ln);font-size:clamp(1.5rem,3.4vw,2.8rem);font-weight:800;transition:padding .4s,color .4s;cursor:default}
.sl2 div.r b{font:600 14px Barlow;color:var(--ac);letter-spacing:.2em;min-width:2.2em;direction:ltr}
.sl2 div.r:hover{padding-right:28px;color:var(--ac)}
.sl2.cols{display:grid;grid-template-columns:1fr 1fr;column-gap:70px}
.cta2{position:relative;overflow:hidden;border-radius:6px;margin:0 6vw 120px}
.cta2 .bg{position:absolute;inset:-10% 0}.cta2 .bg .ph{transform:none;filter:brightness(.45)!important}
.cta2 .in{position:relative;z-index:2;padding:90px 6vw;color:#F3F1EC;display:flex;justify-content:space-between;gap:40px;flex-wrap:wrap;align-items:end}
.cta2::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(11,16,32,.9),rgba(11,16,32,.4))}
.cta2 .in{z-index:3}
.cta2 .disp{font-size:clamp(2rem,5vw,4.4rem);max-width:14ch}
.cta2 .btn{margin:0}
.fbig{direction:ltr;text-align:right;margin-bottom:22px}
@media(max-width:900px){.man-g,.ab2,.sr{grid-template-columns:1fr;gap:40px}.sr{padding:56px 0}.sr:nth-child(even) .sl{order:0}.sd ul{columns:1}.mods4{grid-template-columns:1fr 1fr}.m4:nth-child(n){padding-top:30px}.sl2.cols{grid-template-columns:1fr}.ab2 .small{left:0}.man-t .pf{width:100%}.pf::after{transform:translate(-8px,8px)}}
@media(max-width:560px){.mods4{grid-template-columns:1fr}.m4{border-left:0;border-bottom:1px solid var(--ln)}.band{height:60vh}.cta2{margin:0 4vw 80px}.disp{font-size:clamp(2.2rem,11vw,3.2rem)}}
@media(prefers-reduced-motion:reduce){.tick div{animation:none}.ph{transition:none}}
'''

# dashboard chart svg
CSS=CSS+open('/downloads/audira_site/nc.css',encoding='utf8').read()+open('/downloads/audira_site/nc2.css',encoding='utf8').read()+open('/downloads/audira_site/nc3.css',encoding='utf8').read()
bars=[38,46,41,55,52,63,58,70,66,78,74,88]
svg='<svg viewBox="0 0 360 120" xmlns="http://www.w3.org/2000/svg" direction="ltr">'
for i in range(5): svg+=f'<line x1="0" x2="360" y1="{10+i*25}" y2="{10+i*25}" stroke="var(--ln)" stroke-width="1"/>'
pts=[]
for i,v in enumerate(bars):
    x=8+i*29;h=v*1.0;y=112-h
    svg+=f'<rect x="{x}" y="{y}" width="18" height="{h}" rx="3" fill="var(--acf)" opacity="{.55+.04*i:.2f}"/>'
    pts.append(f'{x+9},{y-10-(i%3)*3}')
svg+=f'<polyline points="{" ".join(pts)}" fill="none" stroke="var(--ink)" stroke-width="1.6" stroke-dasharray="3 3" opacity=".7"/></svg>'

STORY=r'''<section id="track"><div class="stage"><div class="glow"></div><canvas id="pf" aria-hidden="true"></canvas><canvas id="cv"></canvas>
<div class="bar"><div class="logo">%LG%<small>الذكاء المالي والتكنولوجيا</small></div>
<div class="nav"><a class="l" href="#services">خدماتنا</a><a class="l" href="#about">من نحن</a><a class="l" href="#models">التعاون</a><a class="l" href="#faq">الأسئلة</a><a class="pill" href="#contact">احجز استشارة مجانية</a><button class="lgb" type="button" id="lgb" aria-label="Language">EN</button><button class="tg" type="button" aria-label="تبديل الوضع الليلي والنهاري" title="الوضع الليلي / النهاري"><svg class="moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M20 14.5A8 8 0 0 1 9.5 4 8 8 0 1 0 20 14.5z"/></svg><svg class="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M5 5l1.5 1.5M17.5 17.5L19 19M5 19l1.5-1.5M17.5 6.5L19 5"/></svg></button></div></div>
<div class="caps">
<div class="cap on"><div class="tag">AUDIRA · أوديرا</div><h1>الأرقام كثيرة.<br><em>الوضوح<svg viewBox="0 0 100 12" preserveAspectRatio="none"><path d="M1 8 C 18 1, 30 11, 48 5 S 80 2, 99 7" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg></em> هو الناقص.</h1><p>نساعد الشركات على تنظيم الإدارة المالية، وفهم البيانات، وتطوير الحلول التقنية، وتوظيف الذكاء الاصطناعي لدعم الأداء واتخاذ القرار. مصر ودول مجلس التعاون الخليجي.</p></div>
<div class="cap"><div class="tag">01 · الإدارة المالية والمحاسبية</div><h2>نظام مالي منظم</h2><p>إدارة وتنظيم العمليات والسجلات المالية، والتقارير، والتدفقات النقدية، والرقابة.</p></div>
<div class="cap"><div class="tag">02 · الخدمات والاستشارات الضريبية</div><h2>التزامات في موعدها</h2><p>إعداد الإقرارات ومتابعة الالتزامات والإجراءات الضريبية وفق المتطلبات المحلية.</p></div>
<div class="cap"><div class="tag">03 · تحليل البيانات وذكاء الأعمال</div><h2>بيانات تتحول إلى رؤية</h2><p>تقارير ولوحات معلومات ومؤشرات تدعم الإدارة في متابعة الأداء وفهم الاتجاهات.</p></div>
<div class="cap"><div class="tag">04 · التطبيقات والحلول المخصصة</div><h2>تطبيق مصمم لشركتك</h2><p>تقارير وتنبيهات بالتغيرات المهمة، ومساعد ذكي يجيب عن أسئلتك بلغتك.</p></div>
<div class="cap"><div class="tag">05 + 06 · التدريب والتخطيط</div><h2>فرق أقوى وخطط أوضح</h2><p><b>05 التدريب والتطوير:</b> برامج منظمة بشهادات إتمام وتدريب عملي مخصص للشركات.</p><p style="margin-top:8px"><b>06 الموازنات والتخطيط المالي:</b> تقدير الإيرادات والمصروفات وتحليل الانحرافات.</p><p style="margin-top:14px;color:var(--ac)">نخدم مصر ودول مجلس التعاون الخليجي.</p></div>
</div><div class="hint" id="hint">مرّر للأسفل</div><div class="dots"><i class="on"></i><i></i><i></i><i></i><i></i><i></i></div></div></section>'''.replace('%LG%',LG)

def plan(name,sub,items,mid=False,tag=''):
    li=''.join(f'<li>{x}</li>' for x in items)
    t=f'<span class="badge tagm">{tag}</span>' if tag else ''
    link=wa(f'مرحبًا أوديرا، مهتم بباقة «{name}».')
    return f'<div class="pc{" mid" if mid else ""}">{t}<h3>{name}</h3><div class="pn">{sub}</div><div class="pr">[XXX]<small>USD / شهريًا</small></div><ul>{li}</ul><a class="btn{"" if mid else " o"}" href="{link}" target="_blank" rel="noopener">اطلب هذه الباقة</a></div>'

faq=[('أين تعملون؟','نخدم الشركات في مصر ودول مجلس التعاون الخليجي.'),
('هل يمكن الاستفادة من خدمة واحدة فقط؟','نعم. خدماتنا مترابطة، ويمكن الاستفادة منها بشكل مستقل أو ضمن نطاق تعاون متكامل.'),
('ما الأدوات التي تعملون بها؟','<bdi>Excel</bdi> المتقدم، <bdi>Power BI</bdi>، <bdi>SQL</bdi>، <bdi>Python</bdi> وأدوات الذكاء الاصطناعي.'),
('هل التطبيق المخصص يعرض بياناتنا لحظة بلحظة؟','التطبيق يرتبط ببيانات الشركة بحسب إعدادات التكامل المتفق عليها. وتحديث البيانات الفوري يعتمد على مصادر البيانات والتكاملات وإعدادات النظام لديكم.'),
('هل تمثلونا أمام الجهات الضريبية؟','التمثيل يتم وفق التراخيص والاشتراطات المعمول بها في كل دولة. تقديم الخدمات الضريبية والتمثيل يخضع للقوانين ومتطلبات الترخيص والتفويض في الدولة المعنية.'),
('كيف تُحدَّد الأسعار؟','[نص تجريبي: يرجى تأكيده] نختار طريقة التعاون وفق نطاق العمل واحتياجاتك: اشتراك شهري أو مشروع محدد أو شراكة سنوية أو خدمات عند الطلب.')]
FAQ=''.join(f'<details{" open" if i==0 else ""}><summary>{q}</summary><p>{a}</p></details>' for i,(q,a) in enumerate(faq))

from nb import NEWBODY
INTRO='<div id="intro" aria-hidden="true">'+open('/downloads/audira_site/intro_svg.html').read()+'<div class="isub">الذكاء المالي والتكنولوجيا</div></div>'
BODY=INTRO+STORY+NEWBODY+f'''
<div><div class="k"><b>06</b>الأسئلة الشائعة</div><div class="big" style="font-size:clamp(1.6rem,3vw,2.5rem)">قبل أن تسأل، ربما تجد الجواب هنا</div></div>
<div>{FAQ}</div></div></section>

<div class="cta2 rv"><div class="bg"><img class="ph" data-ph="cta" alt="" loading="lazy"></div><div class="in"><div class="disp">لنبدأ بمحادثة.</div><a class="btn" href="{wa('مرحبًا أوديرا، أرغب في التواصل.')}" target="_blank" rel="noopener">راسلنا على واتساب</a></div></div>
<section class="sec" id="contact"><div class="wrap ct rv">
<div><div class="k"><b>07</b>تواصل معنا</div><div class="big">ابدأ بمحادثة، والباقي يتضح</div>
<p class="lead">أخبرنا عن شركتك وما تحتاجه، ونقترح عليك نطاق التعاون المناسب.</p>
<div class="cards"><a class="cc" href="{wa('مرحبًا أوديرا، أرغب في حجز استشارة مالية مجانية.')}" target="_blank" rel="noopener"><span class="ic">W</span><span><small>واتساب (الأسرع)</small><b class="ltr">+20 XXX XXX XXXX</b></span></a>
<a class="cc" href="mailto:info@audira-group.com?subject=%D8%B7%D9%84%D8%A8%20%D8%A7%D8%B3%D8%AA%D8%B4%D8%A7%D8%B1%D8%A9%20%D9%85%D8%A7%D9%84%D9%8A%D8%A9%20-%20AUDIRA"><span class="ic">@</span><span><small>البريد الإلكتروني</small><b class="ltr">info@audira-group.com</b></span></a>
<div class="cc"><span class="ic">◎</span><span><small>نخدم</small><b>مصر ودول مجلس التعاون الخليجي</b></span></div></div></div>
<div class="form"><div class="fr"><div><label for="f1">الاسم</label><input id="f1" type="text" placeholder="اسمك"></div><div><label for="f2">الشركة</label><input id="f2" type="text" placeholder="اسم الشركة"></div></div>
<div class="fr"><div><label for="f3">رقم الهاتف أو الإيميل</label><input id="f3" type="text" placeholder="للتواصل معك"></div><div><label for="f4">أحتاج إلى</label><select id="f4"><option>استشارة مالية</option><option>الإدارة المالية والمحاسبية</option><option>خدمات ضريبية</option><option>تحليل بيانات وذكاء أعمال</option><option>تطبيق أو حل مخصص</option><option>تدريب لفريقي</option><option>موازنات وتخطيط مالي</option></select></div></div>
<label for="f5">رسالتك</label><textarea id="f5" placeholder="اكتب نبذة قصيرة عن شركتك وما تحتاجه"></textarea>
<div class="acts"><a class="btn" id="fwa" href="{wa('مرحبًا أوديرا، أرغب في حجز استشارة مالية مجانية.')}" target="_blank" rel="noopener">احجز استشارتك المجانية عبر واتساب</a><a class="btn o" id="fml" href="mailto:info@audira-group.com">أو عبر البريد</a></div>
<p class="note">النموذج يجهّز رسالة جاهزة تفتح في واتساب أو البريد. لا يُحفظ شيء على الموقع.</p></div></div></section>

<footer><div class="wrap"><div class="fg">
<div><div class="fbig">{LGF}</div><p class="ab"><span dir="ltr" style="display:block;text-align:right;unicode-bidi:isolate">AUDIRA · Financial Intelligence &amp; Technology Group<br>Intelligence That Empowers Business</span><span style="display:block;margin-top:10px">خدمات مالية وتقنية لشركات مصر ودول مجلس التعاون الخليجي.</span></p></div>
<div><h5>الصفحة</h5><a href="#services">خدماتنا</a><a href="#about">من نحن</a><a href="#models">نماذج التعاون</a><a href="#sectors">القطاعات</a><a href="#faq">الأسئلة الشائعة</a></div>
<div><h5>الخدمات</h5><a href="#services">الإدارة المالية والمحاسبية</a><a href="#services">الخدمات الضريبية</a><a href="#services">تحليل البيانات وذكاء الأعمال</a><a href="#services">التطبيقات المخصصة</a><a href="#services">التدريب</a><a href="#services">الموازنات والتخطيط</a></div>
<div><h5>تواصل</h5><a href="#contact">احجز استشارة مجانية</a><a href="mailto:info@audira-group.com">info@audira-group.com</a><a>مصر ودول مجلس التعاون الخليجي</a></div></div>
<div class="fb"><span dir="ltr">AUDIRA · Financial Intelligence &amp; Technology Group © 2026</span><span>جميع الحقوق محفوظة</span></div></div></footer>'''

# JS
js=open('story.js',encoding='utf8').read()
for a in ['159,179,200','217,178,78','243,241,236','255,244,214','199,155,47']:
    key={'159,179,200':'t','217,178,78':'a','243,241,236':'i','255,244,214':'n','199,155,47':'b'}[a]
    js=js.replace(f'rgba({a},',f'rgba("+C.{key}+",')
assert 'rgba(' not in js.replace('rgba("+','')
js=js.replace("var calm=","var C={};function rc(){var cs=getComputedStyle(document.documentElement);C.t=cs.getPropertyValue('--cvt').trim();C.a=cs.getPropertyValue('--cvA').trim();C.b=cs.getPropertyValue('--cvb').trim();C.n=cs.getPropertyValue('--cvn').trim();C.i=cs.getPropertyValue('--cvi').trim()}rc();window.addEventListener('themechange',rc);var calm=",1)
js=js.replace("var pg=document.getElementById('prog');","")
js=re.sub(r"pg\.style\.width=[^;]*;","",js)
THEME='''(function(){var d=document.documentElement,t=null;try{t=localStorage.getItem('audira-theme')}catch(e){}
if(!t)t=(window.matchMedia&&matchMedia('(prefers-color-scheme: light)').matches)?'light':'dark';d.setAttribute('data-theme',t);
function set(v){d.setAttribute('data-theme',v);try{localStorage.setItem('audira-theme',v)}catch(e){}window.dispatchEvent(new Event('themechange'))}
[].forEach.call(document.querySelectorAll('.tg'),function(b){b.addEventListener('click',function(){set(d.getAttribute('data-theme')==='light'?'dark':'light')})});
var f=['f1','f2','f3','f4','f5'].map(function(i){return document.getElementById(i)}),w=document.getElementById('fwa'),m=document.getElementById('fml');
function up(){var n=f[0].value.trim(),c=f[1].value.trim(),k=f[2].value.trim(),s=f[3].value,x=f[4].value.trim();
var E=d.lang=='en';var lines=[E?'Hello AUDIRA,':'مرحبًا أوديرا،'];if(n)lines.push(E?('I am '+n+(c?' from '+c:'')+'.'):('أنا '+n+(c?' من '+c:'')+'.'));lines.push((E?'I need: ':'أحتاج إلى: ')+s+'.');if(x)lines.push(x);if(k)lines.push((E?'Contact: ':'للتواصل: ')+k);
var body=lines.join('\\n');w.href="%WA%?text="+encodeURIComponent(body);m.href='mailto:info@audira-group.com?subject='+encodeURIComponent((E?'Consultation request - ':'طلب استشارة - ')+s)+'&body='+encodeURIComponent(body)}
f.forEach(function(e){e.addEventListener('input',up);e.addEventListener('change',up)});window.addEventListener('langchange',up);up()})();'''.replace('%WA%',WA)
import i18n_en
I18N=open('/downloads/audira_site/i18n.js',encoding='utf8').read().replace('%EN%',json.dumps(i18n_en.EN,ensure_ascii=False)).replace('%ATTR%',json.dumps(i18n_en.ATTR,ensure_ascii=False))
INTROJS=open('/downloads/audira_site/intro.js',encoding='utf8').read()
THEME=THEME+'\n'+I18N+'\n'+INTROJS
FONTS=f"""@font-face{{font-family:Cairo;src:url(data:font/ttf;base64,{b64(F+'Cairo.ttf')}) format('truetype');font-weight:200 1000}}
@font-face{{font-family:Barlow;src:url(data:font/ttf;base64,{b64(F+'Barlow-Regular.ttf')}) format('truetype');font-weight:400}}
@font-face{{font-family:Barlow;src:url(data:font/ttf;base64,{b64(F+'Barlow-SemiBold.ttf')}) format('truetype');font-weight:600}}
"""
PRE="(function(){var t=null;try{t=localStorage.getItem('audira-theme')}catch(e){}if(!t)t=(window.matchMedia&&matchMedia('(prefers-color-scheme: light)').matches)?'light':'dark';document.documentElement.setAttribute('data-theme',t)})();"
# standalone
JS_ST=js.replace("var calm=","var pg=null;var calm=",1)
PX="(function(){if(innerWidth<700||matchMedia('(prefers-reduced-motion: reduce)').matches)return;var els=[].slice.call(document.querySelectorAll('[data-px]'));var t=false;function u(){t=false;var h=innerHeight;els.forEach(function(e){var r=e.parentNode.getBoundingClientRect();if(r.bottom<-300||r.top>h+300)return;var k=parseFloat(e.getAttribute('data-px'));var y=(r.top+r.height/2-h/2)*k,m=r.height*.06;y=Math.max(-m,Math.min(m,y));e.style.transform='translate3d(0,'+y.toFixed(1)+'px,0) scale(1.15)'})}function q(){if(!t){t=true;requestAnimationFrame(u)}}addEventListener('scroll',q,{passive:true});addEventListener('resize',q);u()})();"
BODY_ST=re.sub(r'data-ph="(\w+)"',lambda m:'src="data:image/jpeg;base64,'+b64('/downloads/audira_photos/nat/'+m.group(1)+'.jpg')+'"',BODY)
html=f'''<!DOCTYPE html><html lang="ar" dir="rtl" data-theme="dark"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"><link rel="icon" href="{fav}"><meta name="theme-color" content="#0A0E1A"><title>AUDIRA — Financial Intelligence &amp; Technology Group</title><script>{PRE}</script><style>{FONTS}{CSS}</style></head><body>{BODY_ST}<script>{js}</script><script>{THEME}</script><script>{PX}</script></body></html>'''
open('audira_site.html','w',encoding='utf8').write(html)
# hosted
jsh=js.replace("function prog(){var r=track.getBoundingClientRect();return Math.max(0,Math.min(1,-r.top/(r.height-window.innerHeight)))*5}",
"var step=0,last=0;function prog(){return step}\nfunction go(n){step=(n+6)%6;last=Date.now()}\nsetInterval(function(){if(Date.now()-last>9000)step=(step+1)%6},4800);\nvar stg=document.querySelector('.stage');stg.addEventListener('click',function(e){if(e.target.closest('a,button'))return;go(step+1)});dots.forEach(function(d,i){d.addEventListener('click',function(e){e.stopPropagation();go(i)})});")
assert 'function go' in jsh
jsh=jsh.replace("hint.style.opacity=cur>.25?0:1;","hint.style.opacity=last?0:1;").replace("if('IntersectionObserver'in window){","if(false){")
jsh=jsh.replace("cur=calm?tgt:cur+(tgt-cur)*.09","cur=calm?tgt:(tgt<cur-1?cur+(tgt-cur)*.18:cur+(tgt-cur)*.09)")
# the original rv observer removed in new js? check
HCSS=CSS+'''
#track{height:auto!important}
.stage{position:relative!important;height:740px!important;cursor:pointer}
@media(max-width:760px){.stage{height:620px!important}.caps{bottom:30px!important}.cap{bottom:0!important}}
.rv{opacity:1!important;transform:none!important}
.hint{display:flex}@media(max-width:760px){.hint{display:none!important}}
.dots i{cursor:pointer}
'''.replace('\n.hint{display:flex}@media','\n@media')
hbody=BODY.replace('مرّر للأسفل','اضغط للتالي')
A='/downloads/audira_site_app/src/'
open(A+'style.css','w',encoding='utf8').write(HCSS)
open(A+'site.ts','w',encoding='utf8').write('// @ts-nocheck\nexport function init(){\n'+jsh+'\n'+THEME+'\n}\n')
open(A+'body.html.ts','w',encoding='utf8').write('export const BODY = '+json.dumps(hbody,ensure_ascii=False)+';\n')
import shutil,glob
os.makedirs(A+'img',exist_ok=True)
names=[os.path.basename(f)[:-4] for f in sorted(glob.glob('/downloads/audira_photos/nat/*.jpg'))]
for n in names: shutil.copy(f'/downloads/audira_photos/nat/{n}.jpg',A+f'img/{n}.jpg')
imp=''.join(f"import img_{n} from './img/{n}.jpg';\n" for n in names)
mp=','.join(f"{n}: img_{n}" for n in names)
open(A+'App.tsx','w').write('''import React, { useEffect } from 'react';
import { BODY } from './body.html';
import { init } from './site';
import cairo from './fonts/Cairo.ttf';
import barlow4 from './fonts/Barlow-Regular.ttf';
import barlow6 from './fonts/Barlow-SemiBold.ttf';
'''+imp+'''
const IMG: Record<string, string> = { '''+mp+''' };
const A = (u: string) => { const sc = document.querySelector('script[src*="main.js"]') as HTMLScriptElement | null; return sc ? sc.src.replace('main.js', u.replace(/^\\.\\//, '')) : u; };

export function App() {
    useEffect(() => {
        const st = document.createElement('style');
        st.textContent = `@font-face{font-family:Cairo;src:url(${A(cairo)});font-weight:200 1000}@font-face{font-family:Barlow;src:url(${A(barlow4)});font-weight:400}@font-face{font-family:Barlow;src:url(${A(barlow6)});font-weight:600}`;
        document.head.appendChild(st);
        document.querySelectorAll('img[data-ph]').forEach((el) => {
            const k = el.getAttribute('data-ph') || '';
            (el as HTMLImageElement).loading = 'eager'; (el as HTMLImageElement).src = A(IMG[k]);
            el.removeAttribute('data-px');
            (el as HTMLElement).style.transform = 'none';
        });
        init();
    }, []);
    return <div dangerouslySetInnerHTML={{ __html: BODY }} />;
}
''')
print(len(html))
