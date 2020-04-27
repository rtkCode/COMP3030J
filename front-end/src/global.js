const global = {}

global.baseAddress="http://127.0.0.1:5000/";

global.request=function(address){
    return this.baseAddress+address;
};

global.resizeContent=function(){
    let bHeigh=document.documentElement.clientHeight;
    let header=document.querySelector("header").offsetHeight
    let footer=document.querySelector("footer").offsetHeight
    let content=document.querySelector(".content");
    content.style.minHeight=bHeigh-header-footer+"px";
};

global.minHeight=function(){
    let bHeigh=document.documentElement.clientHeight;
    let header=document.querySelector("header").offsetHeight
    let footer=document.querySelector("footer").offsetHeight
    return bHeigh-header-footer;
};

global.bg1={
    backgroundImage: "url(" + require("../public/img/index.jpeg") + ")",
    backgroundRepeat: "no-repeat",
    backgroundSize: "cover",
    backgroundPosition: "center"
};

global.bg2={
    backgroundImage: "url(" + require("../public/img/appointment.png") + ")",
    backgroundRepeat: "no-repeat",
    backgroundSize: "cover",
    backgroundPosition: "center",
    backgroundAttachment: "fixed",
};

export default global