/*! For license information please see index.69349a2f.js.LICENSE.txt */
(function(){var e,t,a,r,i,n,s={2451:function(e,t,a){"use strict";e.exports=a.p+"static/font/IBMPlexSans-Bold.974f44a1.woff2"},3829:function(e,t,a){"use strict";e.exports=a.p+"static/font/IBMPlexSerif-Regular.e0f81e90.woff2"},6629:function(e,t,a){"use strict";e.exports=a.p+"static/image/shavkat.a72885ce.png"},5955:function(e,t,a){"use strict";a.r(t);var r=a("5893");a("6285");var i=a("4151");t.default=()=>(0,r.jsx)(i.default,{})},2189:function(e,t,a){"use strict";a.r(t);var r=a("5893");a("7294");var i=a("2693");t.default=()=>(0,r.jsx)(r.Fragment,{children:(0,r.jsx)("div",{className:i.pager,children:"CV"})})},771:function(e,t,a){"use strict";a.r(t);var r=a("5893");a("7294");t.default=()=>(0,r.jsx)("div",{children:"Experience"})},3478:function(e,t,a){"use strict";a.r(t);var r=a("5893");a("7294");var i=a("6647"),n=a("1145"),s=a("9903");t.default=()=>(0,r.jsxs)(r.Fragment,{children:[(0,r.jsxs)("div",{className:i.imagePart,children:[(0,r.jsx)("div",{className:i.img}),(0,r.jsx)("h1",{children:"SHAVKAT JABBOROV"}),(0,r.jsx)("span",{children:"Teacher in Business Disciplines"})]}),(0,r.jsxs)("div",{className:i.infoPart,children:[(0,r.jsxs)("div",{className:i.contacts,children:[(0,r.jsx)(n.default,{}),(0,r.jsx)("span",{children:"+998 99 999 99 99"})]}),(0,r.jsxs)("div",{className:i.contacts,children:[(0,r.jsx)(s.default,{}),(0,r.jsx)("span",{children:"shjabborov@gmail.com"})]}),(0,r.jsx)("div",{className:i.shortText,children:"Lorem ipsum dolor sit amet consectetur adipisicing elit. Vel deleniti hic, non quae facere aliquam laborum quos. Itaque, debitis delectus? Eius quas vitae magni cum corrupti corporis ullam temporibus cupiditate? Sit, nobis maxime at reiciendis animi harum! Totam alias veritatis porro doloremque. Fuga, in quod, dignissimos consectetur recusandae exercitationem odio ipsa reiciendis laudantium beatae aspernatur! A est officia fuga sed! Nesciunt tempore ipsum recusandae temporibus at dicta impedit cumque soluta, facere nobis, doloribus nam dolore quis aspernatur pariatur voluptatem in commodi ipsa molestiae esse architecto! Magnam delectus atque dicta culpa?"})]})]})},4151:function(e,t,a){"use strict";a.r(t);var r=a("5893"),i=a("7294"),n=a("8538"),s=a("3478"),o=a("2189"),c=a("771"),u=a("5647"),l=a("3873");t.default=()=>{let[e,t]=(0,i.useState)("about"),a=(0,l.useSpring)({transform:"about"===e?"scale(1)":"scale(0.8)",opacity:"about"===e?1:0,width:"100vw",height:"100vh",display:"about"===e?"flex":"none",gap:"100px",padding:"60px",flexGrow:1}),d=(0,l.useSpring)({transform:"cv"===e?"scale(1)":"scale(0.8)",opacity:"cv"===e?1:0,width:"100vw",height:"100vh",display:"cv"===e?"flex":"none",gap:"100px",padding:"60px",flexGrow:1}),f=(0,l.useSpring)({transform:"experience"===e?"scale(1)":"scale(0.8)",opacity:"experience"===e?1:0,width:"100vw",height:"100vh",display:"experience"===e?"flex":"none",gap:"100px",padding:"60px",flexGrow:1});return(0,r.jsxs)("div",{className:u.main,children:[(0,r.jsx)(n.default,{onMenuClick:e=>{t(e)}}),(0,r.jsx)(l.animated.div,{style:a,children:(0,r.jsx)(s.default,{})}),(0,r.jsx)(l.animated.div,{style:d,children:(0,r.jsx)(o.default,{})}),(0,r.jsx)(l.animated.div,{style:f,children:(0,r.jsx)(c.default,{})})]})}},8538:function(e,t,a){"use strict";a.r(t),a("7640"),a("9924");var r=a("5893"),i=a("7294"),n=a("8005"),s=a("5128"),o=a("802"),c=a("1003"),u=a("2702");t.default=e=>{let{onMenuClick:t}=e,{t:a}=(0,u.useTranslation)(),{i18n:l}=(0,u.useTranslation)(),d=["about","cv","experience","skills","works"],f=["uz","ru","en"],[p,m]=(0,i.useState)(d[0]),[x,v]=(0,i.useState)(f[0]),h=e=>{l.changeLanguage(e)};return(0,r.jsxs)("div",{className:c.container,children:[(0,r.jsx)("h2",{className:c.logo,children:"SH. J."}),(0,r.jsx)("ul",{className:c.navbar,children:d.map((e,i)=>(0,r.jsx)("li",{className:p===e?c.active:"",onClick:()=>{t(e),m(e)},children:(0,r.jsx)("span",{children:a(`${e}`)})},i))}),(0,r.jsx)("div",{className:c.languages,children:(0,r.jsx)("ul",{children:f.map((e,t)=>(0,r.jsx)("li",{className:x===e?c.active_lang:"",onClick:()=>{v(e),h(`${e}`)},children:e.toUpperCase()},t))})}),(0,r.jsxs)("div",{className:c.bottom,children:[(0,r.jsxs)("div",{className:c.socials,children:[(0,r.jsx)(n.default,{}),(0,r.jsx)(s.default,{}),(0,r.jsx)(o.default,{})]}),(0,r.jsxs)("p",{children:["Copyright \xa9 2024 ",(0,r.jsx)("br",{})," All right reserved."]})]})]})}},6233:function(e,t,a){"use strict";a.r(t);var r=a("994"),i=a("2702"),n=a("2792"),s=a("6030"),o=a("7035");r.default.use(i.initReactI18next).init({resources:{en:{translation:n},uz:{translation:s},ru:{translation:o}},lng:"uz",fallbackLng:"ru",interpolation:{escapeValue:!1}}),r.default},5688:function(e,t,a){"use strict";a.r(t);var r=a("5893");a("7294");var i=a("745"),n=a("5955");a("6233");var s=a("5905"),o=a("1722");i.createRoot(document.getElementById("root")).render((0,r.jsx)(o.Provider,{store:s.store,children:(0,r.jsx)(n.default,{})}))},5390:function(e,t,a){"use strict";a.r(t);var r=a("4226");let i=(0,r.createSlice)({name:"menu",initialState:{value:0},reducers:{setValue(e,t){e.value=t.payload}}}),{setValue:n}=i.actions;t.default=i.reducer},5905:function(e,t,a){"use strict";a.r(t),a.d(t,{store:function(){return n}});var r=a("4226"),i=a("5390");let n=(0,r.configureStore)({reducer:{state:i.default}})},2693:function(e){"use strict";e.exports={pager:"pager-_76c8a"}},6647:function(e){"use strict";e.exports={contacts:"contacts-_09483",imagePart:"imagePart-db1e71",img:"img-_2ae5d",infoPart:"infoPart-_04e72",shortText:"shortText-_5f715"}},5647:function(e){"use strict";e.exports={main:"main-aa286c"}},1003:function(e){"use strict";e.exports={active:"active-d90f0b",activeLang:"active_lang-_7f3a6",active_lang:"active_lang-_7f3a6",bottom:"bottom-_657cb",container:"container-a401a0",languages:"languages-c5bab4",logo:"logo-_1449f",navbar:"navbar-e844d0",socials:"socials-d69c0e"}},6285:function(e){},2792:function(e){"use strict";e.exports=JSON.parse('{"about":"about","experience":"experience"}')},7035:function(e){"use strict";e.exports=JSON.parse('{"about":"\u041E\u0431\u043E \u043C\u043D\u0435","experience":"\u0410\u043A\u0442\u0438\u0432\u043D\u043E\u0441\u0442\u044C"}')},6030:function(e){"use strict";e.exports=JSON.parse('{"about":"Men haqqimda","experience":"O`qituvchilik faoliyatim","skills":"Kasbiy (professional) faoliyatim","works":"Biznes faoliyatim"}')}},o={};function c(e){var t=o[e];if(void 0!==t)return t.exports;var a=o[e]={exports:{}};return s[e].call(a.exports,a,a.exports,c),a.exports}c.m=s,c.es=function(e,t){return Object.keys(e).forEach(function(a){"default"!==a&&!Object.prototype.hasOwnProperty.call(t,a)&&Object.defineProperty(t,a,{enumerable:!0,get:function(){return e[a]}})}),e},c.p="/",e=[],c.O=function(t,a,r,i){if(a){i=i||0;for(var n=e.length;n>0&&e[n-1][2]>i;n--)e[n]=e[n-1];e[n]=[a,r,i];return}for(var s=1/0,n=0;n<e.length;n++){for(var a=e[n][0],r=e[n][1],i=e[n][2],o=!0,u=0;u<a.length;u++)s>=i&&Object.keys(c.O).every(function(e){return c.O[e](a[u])})?a.splice(u--,1):(o=!1,i<s&&(s=i));if(o){e.splice(n--,1);var l=r();void 0!==l&&(t=l)}}return t},c.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||Function("return this")()}catch(e){if("object"==typeof window)return window}}(),c.d=function(e,t){for(var a in t)c.o(t,a)&&!c.o(e,a)&&Object.defineProperty(e,a,{enumerable:!0,get:t[a]})},c.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},c.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return c.d(t,{a:t}),t},a=Object.getPrototypeOf?function(e){return Object.getPrototypeOf(e)}:function(e){return e.__proto__},c.t=function(e,r){if(1&r&&(e=this(e)),8&r||"object"==typeof e&&e&&(4&r&&e.__esModule||16&r&&"function"==typeof e.then))return e;var i=Object.create(null);c.r(i);var n={};t=t||[null,a({}),a([]),a(a)];for(var s=2&r&&e;"object"==typeof s&&!~t.indexOf(s);s=a(s))Object.getOwnPropertyNames(s).forEach(function(t){n[t]=function(){return e[t]}});return n.default=function(){return e},c.d(i,n),i},c.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},r={980:0},c.O.j=function(e){return 0===r[e]},i=function(e,t){var a=t[0],i=t[1],n=t[2],s,o,u=0;if(a.some(function(e){return 0!==r[e]})){for(s in i)c.o(i,s)&&(c.m[s]=i[s]);if(n)var l=n(c)}for(e&&e(t);u<a.length;u++)o=a[u],c.o(r,o)&&r[o]&&r[o][0](),r[o]=0;return c.O(l)},(n=self.webpackChunkcv=self.webpackChunkcv||[]).forEach(i.bind(null,0)),n.push=i.bind(null,n.push.bind(n));var u=c.O(void 0,["126","361","674"],function(){return c("5688")});c.O(u)})();