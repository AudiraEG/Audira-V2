(function(){var EN=%EN%,ATTR=%ATTR%,d=document.documentElement,orig=new WeakMap(),ob=document.getElementById('lgb');EN['،']='،';EN['،']=',';
function texts(){var w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT,null),a=[],n;while(n=w.nextNode()){var p=n.parentNode;if(p&&!/^(SCRIPT|STYLE)$/.test(p.nodeName)&&n.nodeValue.trim())a.push(n)}return a}
function waEn(t){var m=t.match(/مهتم بباقة «(.*)»/);if(m)return 'Hello AUDIRA, I am interested in the "'+(EN[m[1]]||m[1])+'" plan.';if(t.indexOf('التواصل')>-1)return 'Hello AUDIRA, I would like to get in touch.';return 'Hello AUDIRA, I would like to book a free financial consultation.'}
function apply(l){var en=l==='en';
 texts().forEach(function(n){var o=orig.get(n);if(o===undefined){o=n.nodeValue;orig.set(n,o)}var k=o.trim();n.nodeValue=(en&&EN[k]!==undefined)?o.replace(k,function(){return EN[k]}):o});
 [].forEach.call(document.querySelectorAll('[placeholder],[aria-label],[title]'),function(e){['placeholder','aria-label','title'].forEach(function(a){if(!e.hasAttribute(a))return;var key='data-o-'+a;if(!e.hasAttribute(key))e.setAttribute(key,e.getAttribute(a));var o=e.getAttribute(key);e.setAttribute(a,en&&ATTR[o]?ATTR[o]:o)})});
 [].forEach.call(document.querySelectorAll('a[href^="https://wa.me"]'),function(a){if(a.id==='fwa')return;if(!a.hasAttribute('data-oh'))a.setAttribute('data-oh',a.getAttribute('href'));var o=a.getAttribute('data-oh');if(!en){a.setAttribute('href',o);return}var q=o.indexOf('?text=');var t=decodeURIComponent(o.slice(q+6));a.setAttribute('href',o.slice(0,q)+'?text='+encodeURIComponent(waEn(t)))});
 d.lang=en?'en':'ar';d.dir=en?'ltr':'rtl';if(ob){ob.textContent=en?'عربي':'EN';ob.setAttribute('aria-label',en?'التبديل إلى العربية':'Switch to English')}
 document.title=en?'AUDIRA | Financial Intelligence & Technology Group':'AUDIRA — Financial Intelligence & Technology Group';
 window.dispatchEvent(new Event('langchange'))}
function set(l){try{localStorage.setItem('audira-lang',l)}catch(e){}apply(l)}
if(ob)ob.addEventListener('click',function(){set(d.lang==='en'?'ar':'en')});
var s=null;try{s=localStorage.getItem('audira-lang')}catch(e){}
if(s==='en')apply('en');
})();
