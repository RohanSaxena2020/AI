(this.webpackJsonpphoto=this.webpackJsonpphoto||[]).push([[0],{130:function(e,t,a){"use strict";a.r(t);var n=a(0),o=a.n(n),r=a(12),c=a.n(r),i=(a(95),a(5)),l=a(173),s=a(174),d=a(175),b=a(171),p=a(188),m=a(176),j=a(177),g=a(180),h=a(172),x=a(170),u=a(178),O=a(179),C=a(181),f=a(85),w=a(182),N=a(183),k=a(184),v=a(185),S=a(186),y=a(187),W=a.p+"static/media/cblogo.fcecc55f.PNG",F=a.p+"static/media/bg.d6836046.png",R=a(83),z=a(42),I=a(82),B=a.n(I),G=a(8);const P=Object(i.a)((e=>({root:{color:e.palette.getContrastText(z.a.white),backgroundColor:z.a.white,"&:hover":{backgroundColor:"#ffffff7a"}}})))(h.a),D=a(110).default,E=Object(l.a)((e=>({grow:{flexGrow:1},clearButton:{width:"-webkit-fill-available",borderRadius:"15px",padding:"15px 22px",color:"#000000a6",fontSize:"20px",fontWeight:900},root:{maxWidth:345,flexGrow:1},media:{height:400},paper:{padding:e.spacing(2),margin:"auto",maxWidth:500},gridContainer:{justifyContent:"center",padding:"4em 1em 0 1em"},mainContainer:{backgroundImage:"url(".concat(F,")"),backgroundRepeat:"no-repeat",backgroundPosition:"center",backgroundSize:"cover",height:"93vh",marginTop:"8px"},imageCard:{margin:"auto",maxWidth:400,height:500,backgroundColor:"transparent",boxShadow:"0px 9px 70px 0px rgb(0 0 0 / 30%) !important",borderRadius:"15px"},imageCardEmpty:{height:"auto"},noImage:{margin:"auto",width:400,height:"400 !important"},input:{display:"none"},uploadIcon:{background:"white"},tableContainer:{backgroundColor:"transparent !important",boxShadow:"none !important"},table:{backgroundColor:"transparent !important"},tableHead:{backgroundColor:"transparent !important"},tableRow:{backgroundColor:"transparent !important"},tableCell:{fontSize:"22px",backgroundColor:"transparent !important",borderColor:"transparent !important",color:"#000000a6 !important",fontWeight:"bolder",padding:"1px 24px 1px 16px"},tableCell1:{fontSize:"14px",backgroundColor:"transparent !important",borderColor:"transparent !important",color:"#000000a6 !important",fontWeight:"bolder",padding:"1px 24px 1px 16px"},tableBody:{backgroundColor:"transparent !important"},text:{color:"white !important",textAlign:"center"},buttonGrid:{maxWidth:"416px",width:"100%"},detail:{backgroundColor:"white",display:"flex",justifyContent:"center",flexDirection:"column",alignItems:"center"},appbar:{background:"#be6a77",boxShadow:"none",color:"white"},loader:{color:"#be6a77 !important"}}))),L=()=>{const e=E(),[t,a]=Object(n.useState)(),[r,c]=Object(n.useState)(),[i,l]=Object(n.useState)(),[h,F]=Object(n.useState)(!1),[z,I]=Object(n.useState)(!1);let L=0;Object(n.useEffect)((()=>{if(!t)return void c(void 0);const e=URL.createObjectURL(t);c(e)}),[t]),Object(n.useEffect)((()=>{r&&(I(!0),(async()=>{if(h){let e=new FormData;e.append("file",t);let a=await D({method:"post",url:"http://0.0.0.0:8000/predict",data:e});200===a.status&&l(a.data),I(!1)}})())}),[r]);return i&&(L=(100*parseFloat(i.confidence)).toFixed(2)),Object(G.jsxs)(o.a.Fragment,{children:[Object(G.jsx)(s.a,{position:"static",className:e.appbar,children:Object(G.jsxs)(d.a,{children:[Object(G.jsx)(b.a,{className:e.title,variant:"h6",noWrap:!0,children:"CodeBasics: Potato Disease Classification"}),Object(G.jsx)("div",{className:e.grow}),Object(G.jsx)(p.a,{src:W})]})}),Object(G.jsx)(m.a,{maxWidth:!1,className:e.mainContainer,disableGutters:!0,children:Object(G.jsxs)(x.a,{className:e.gridContainer,container:!0,direction:"row",justifyContent:"center",alignItems:"center",spacing:2,children:[Object(G.jsx)(x.a,{item:!0,xs:12,children:Object(G.jsxs)(j.a,{className:"".concat(e.imageCard," ").concat(h?"":e.imageCardEmpty),children:[h&&Object(G.jsx)(u.a,{children:Object(G.jsx)(O.a,{className:e.media,image:r,component:"image",title:"Contemplative Reptile"})}),!h&&Object(G.jsx)(g.a,{className:e.content,children:Object(G.jsx)(R.a,{acceptedFiles:["image/*"],dropzoneText:"Drag and drop an image of a potato plant leaf to process",onChange:e=>{if(!e||0===e.length)return a(void 0),F(!1),void l(void 0);a(e[0]),l(void 0),F(!0)}})}),i&&Object(G.jsx)(g.a,{className:e.detail,children:Object(G.jsx)(C.a,{component:f.a,className:e.tableContainer,children:Object(G.jsxs)(w.a,{className:e.table,size:"small","aria-label":"simple table",children:[Object(G.jsx)(N.a,{className:e.tableHead,children:Object(G.jsxs)(k.a,{className:e.tableRow,children:[Object(G.jsx)(v.a,{className:e.tableCell1,children:"Label:"}),Object(G.jsx)(v.a,{align:"right",className:e.tableCell1,children:"Confidence:"})]})}),Object(G.jsx)(S.a,{className:e.tableBody,children:Object(G.jsxs)(k.a,{className:e.tableRow,children:[Object(G.jsx)(v.a,{component:"th",scope:"row",className:e.tableCell,children:i.class}),Object(G.jsxs)(v.a,{align:"right",className:e.tableCell,children:[L,"%"]})]})})]})})}),z&&Object(G.jsxs)(g.a,{className:e.detail,children:[Object(G.jsx)(y.a,{color:"secondary",className:e.loader}),Object(G.jsx)(b.a,{className:e.title,variant:"h6",noWrap:!0,children:"Processing"})]})]})}),i&&Object(G.jsx)(x.a,{item:!0,className:e.buttonGrid,children:Object(G.jsx)(P,{variant:"contained",className:e.clearButton,color:"primary",component:"span",size:"large",onClick:()=>{l(null),F(!1),a(null),c(null)},startIcon:Object(G.jsx)(B.a,{fontSize:"large"}),children:"Clear"})})]})})]})};var T=function(){return Object(G.jsx)(L,{})};var H=e=>{e&&e instanceof Function&&a.e(3).then(a.bind(null,190)).then((({getCLS:t,getFID:a,getFCP:n,getLCP:o,getTTFB:r})=>{t(e),a(e),n(e),o(e),r(e)}))};c.a.render(Object(G.jsx)(o.a.StrictMode,{children:Object(G.jsx)(T,{})}),document.getElementById("root")),H()},95:function(e,t,a){}},[[130,1,2]]]);
//# sourceMappingURL=main.1f8a4228.chunk.js.map