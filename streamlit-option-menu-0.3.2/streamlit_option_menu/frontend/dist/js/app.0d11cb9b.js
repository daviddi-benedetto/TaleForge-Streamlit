(function(e){function t(t){for(var r,o,a=t[0],l=t[1],s=t[2],b=0,d=[];b<a.length;b++)o=a[b],Object.prototype.hasOwnProperty.call(c,o)&&c[o]&&d.push(c[o][0]),c[o]=0;for(r in l)Object.prototype.hasOwnProperty.call(l,r)&&(e[r]=l[r]);u&&u(t);while(d.length)d.shift()();return i.push.apply(i,s||[]),n()}function n(){for(var e,t=0;t<i.length;t++){for(var n=i[t],r=!0,a=1;a<n.length;a++){var l=n[a];0!==c[l]&&(r=!1)}r&&(i.splice(t--,1),e=o(o.s=n[0]))}return e}var r={},c={app:0},i=[];function o(t){if(r[t])return r[t].exports;var n=r[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,o),n.l=!0,n.exports}o.m=e,o.c=r,o.d=function(e,t,n){o.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},o.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},o.t=function(e,t){if(1&t&&(e=o(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(o.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var r in e)o.d(n,r,function(t){return e[t]}.bind(null,r));return n},o.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return o.d(t,"a",t),t},o.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},o.p="";var a=window["webpackJsonp"]=window["webpackJsonp"]||[],l=a.push.bind(a);a.push=t,a=a.slice();for(var s=0;s<a.length;s++)t(a[s]);var u=l;i.push([0,"chunk-vendors"]),n()})({0:function(e,t,n){e.exports=n("cd49")},"04d9":function(e,t,n){"use strict";n("b4b3")},"0796":function(e,t,n){},"1eca":function(e,t,n){},"293c":function(e,t,n){"use strict";n("0796")},"44dc":function(e,t,n){"use strict";n("1eca")},b4b3:function(e,t,n){},cd49:function(e,t,n){"use strict";n.r(t);n("e260"),n("e6cf"),n("cca6"),n("a79d");var r=n("830f"),c=n("5c40"),i={id:"app"};function o(e,t,n,r,o,a){var l=Object(c["w"])("MyComponent"),s=Object(c["w"])("WithStreamlitConnection");return Object(c["r"])(),Object(c["d"])("div",i,[Object(c["i"])(s,null,{default:Object(c["C"])((function(e){var t=e.args;return[Object(c["i"])(l,{args:t},null,8,["args"])]})),_:1})])}var a=n("9ff4"),l=Object(c["D"])("data-v-4323f8ce");Object(c["t"])("data-v-4323f8ce");var s={class:"menu"},u=Object(c["i"])("hr",null,null,-1);Object(c["s"])();var b=l((function(e,t,n,r,i,o){return Object(c["r"])(),Object(c["d"])("div",s,[Object(c["i"])("div",{class:["container-xxl d-flex flex-column flex-shrink-0",{"p-3":!e.isHorizontal,"p-h":e.isHorizontal,"nav-justified":e.isHorizontal}],style:e.styleObjectToString(e.styles["container"])},[e.menuTitle?(Object(c["r"])(),Object(c["d"])(c["b"],{key:0},[Object(c["i"])("a",{href:"#",class:"menu-title align-items-center mb-md-0 me-md-auto text-decoration-none",style:e.styleObjectToString(e.styles["menu-title"])},[Object(c["i"])("i",{class:["icon",e.menuIcon],style:e.styleObjectToString(e.styles["menu-icon"])},null,6),Object(c["h"])(" "+Object(a["F"])(e.menuTitle),1)],4),u],64)):Object(c["e"])("",!0),Object(c["i"])("ul",{class:["nav nav-pills mb-auto",{"flex-column":!e.isHorizontal,"nav-justified":e.isHorizontal}],style:e.styleObjectToString(e.styles["nav"])},[(Object(c["r"])(!0),Object(c["d"])(c["b"],null,Object(c["u"])(e.args.options,(function(t,n){return Object(c["r"])(),Object(c["d"])("li",{class:"nav-item",key:t,style:e.styleObjectToString(e.styles["nav-item"])},["---"===t?(Object(c["r"])(),Object(c["d"])("hr",{key:0,class:{vr:e.isHorizontal},style:e.styleObjectToString(e.styles["separator"])},null,6)):(Object(c["r"])(),Object(c["d"])("a",{key:1,href:"#",class:["nav-link",{active:n==e.selectedIndex,"nav-link-horizontal":e.isHorizontal}],onClick:function(r){return e.onClicked(n,t)},"aria-current":"page",style:e.styleObjectToString(e.styles["nav-link"])+e.styleObjectToString(e.styles["nav-link-selected"],n==e.selectedIndex)},[Object(c["i"])("i",{class:["icon",e.icons[n]],style:e.styleObjectToString(e.styles["icon"])},null,6),Object(c["h"])(" "+Object(a["F"])(t),1)],14,["onClick"]))],4)})),128))],6)],6)])})),d=(n("99af"),n("fb6a"),n("a1e9")),f=n("d092");function j(){Object(c["o"])((function(){f["a"].setFrameHeight()})),Object(c["q"])((function(){f["a"].setFrameHeight()}))}
/**
 * @license
 * Copyright 2018-2020 Streamlit Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */n("ab8b"),n("cd74");function O(e){return"bi-"!==e.slice(0,3)?"bi-"+e:e}var v={name:"MyComponent",props:["args"],setup:function(e){j();var t=Object(d["i"])(e.args.menuTitle),n="horizontal"==e.args.orientation,r=Object(d["i"])(e.args.menuIcon||"bi-menu-up");r.value=O(r.value);for(var c=Object(d["i"])(e.args.icons||[]),i=0;i<e.args.options.length;i++)c.value[i]||(c.value[i]="bi-caret-right"),c.value[i]=O(c.value[i]);var o=Object(d["i"])(e.args.defaultIndex),a=function(e,t){o.value=e,f["a"].setComponentValue(t)},l=function(e,t){if("undefined"===typeof t&&(t=!0),!t)return"";var n="";for(var r in e)n+="".concat(r,":").concat(e[r],";");return n},s=Object(d["i"])(e.args.styles||{});return{selectedIndex:o,menuTitle:t,menuIcon:r,icons:c,styles:s,onClicked:a,styleObjectToString:l,isHorizontal:n}}};n("293c");v.render=b,v.__scopeId="data-v-4323f8ce";var p=v,y=Object(c["D"])("data-v-bef81972");Object(c["t"])("data-v-bef81972");var m={key:0},g=Object(c["i"])("h1",{class:"err__title"},"Component Error",-1),h={class:"err__msg"};Object(c["s"])();var S=y((function(e,t,n,r,i,o){return Object(c["r"])(),Object(c["d"])("div",null,[""!=e.componentError?(Object(c["r"])(),Object(c["d"])("div",m,[g,Object(c["i"])("div",h,"Message: "+Object(a["F"])(e.componentError),1)])):null!=e.renderData?Object(c["v"])(e.$slots,"default",{key:1,args:e.renderData.args,disabled:e.renderData.disabled}):Object(c["e"])("",!0)])})),k=Object(c["j"])({name:"WithStreamlitConnection",setup:function(){var e=Object(d["i"])(void 0),t=Object(d["i"])(""),n=function(n){var r=n;e.value=r.detail,t.value=""};return Object(c["o"])((function(){f["a"].events.addEventListener(f["a"].RENDER_EVENT,n),f["a"].setComponentReady()})),Object(c["q"])((function(){""!=t.value&&f["a"].setFrameHeight()})),Object(c["p"])((function(){f["a"].events.removeEventListener(f["a"].RENDER_EVENT,n)})),Object(c["n"])((function(e){t.value=String(e)})),{renderData:e,componentError:t}}});n("44dc");k.render=S,k.__scopeId="data-v-bef81972";var T=k,x=Object(c["j"])({name:"App",components:{MyComponent:p,WithStreamlitConnection:T}});n("04d9");x.render=o;var _=x;Object(r["a"])(_).mount("#app")}});
//# sourceMappingURL=app.0d11cb9b.js.map