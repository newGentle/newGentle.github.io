(()=>{
 const button=document.querySelector('[data-menu-button]'),nav=document.querySelector('[data-nav]'),bar=document.querySelector('[data-progress]');
 if(button&&nav){button.addEventListener('click',()=>{const open=nav.dataset.open!=='true';nav.dataset.open=String(open);button.setAttribute('aria-expanded',String(open));});nav.addEventListener('click',event=>{if(event.target.closest('a')){nav.dataset.open='false';button.setAttribute('aria-expanded','false');}});}
 const reduced=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
 const reveal=[...document.querySelectorAll('[data-reveal]')];
 if(!reduced&&'IntersectionObserver' in window){const obs=new IntersectionObserver(entries=>{for(const entry of entries)if(entry.isIntersecting){entry.target.classList.add('is-visible');obs.unobserve(entry.target);}},{rootMargin:'0px 0px -35px 0px',threshold:.05});for(const el of reveal)obs.observe(el);document.documentElement.classList.add('reveal-ready');for(const el of reveal)if(el.getBoundingClientRect().top<innerHeight*.9)el.classList.add('is-visible');}
 const navLinks=[...document.querySelectorAll('.nav-link')],targets=[...document.querySelectorAll('main section[id]')];
 let raf=false;function update(){raf=false;if(bar){const max=document.documentElement.scrollHeight-innerHeight;bar.style.width=(max>0?Math.min(100,scrollY/max*100):0)+'%';}let current='';for(const el of targets)if(el.getBoundingClientRect().top<Math.max(200,innerHeight*.34))current=el.id;for(const a of navLinks)a.classList.toggle('is-active',a.getAttribute('href')==='#'+current);}
 window.addEventListener('scroll',()=>{if(!raf){raf=true;requestAnimationFrame(update)}},{passive:true});update();
})();