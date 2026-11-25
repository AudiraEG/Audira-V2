import React, { useEffect } from 'react';
import { BODY } from './body.html';
import { init } from './site';
import cairo from './fonts/Cairo.ttf';
import barlow4 from './fonts/Barlow-Regular.ttf';
import barlow6 from './fonts/Barlow-SemiBold.ttf';
import img_about from './img/about.jpg';
import img_cairo from './img/cairo.jpg';
import img_cta from './img/cta.jpg';
import img_gulf from './img/gulf.jpg';
import img_hero from './img/hero.jpg';
import img_s1 from './img/s1.jpg';
import img_s2 from './img/s2.jpg';
import img_s3 from './img/s3.jpg';
import img_s4 from './img/s4.jpg';
import img_s5 from './img/s5.jpg';
import img_s6 from './img/s6.jpg';

const IMG: Record<string, string> = { about: img_about,cairo: img_cairo,cta: img_cta,gulf: img_gulf,hero: img_hero,s1: img_s1,s2: img_s2,s3: img_s3,s4: img_s4,s5: img_s5,s6: img_s6 };
const A = (u: string) => { const sc = document.querySelector('script[src*="main.js"]') as HTMLScriptElement | null; return sc ? sc.src.replace('main.js', u.replace(/^\.\//, '')) : u; };

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
