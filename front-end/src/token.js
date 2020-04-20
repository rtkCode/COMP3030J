const token = {}

token.getToken=function(n) {
    let token = localStorage.getItem('t');
    let t = window.decodeURIComponent(window.atob(token));
    if (n == 0) return token;
    if (n == 1) return t;
};

token.isEmployee=function() {
    let e = localStorage.getItem('e');
    return e;
};

token.storeToken=function(token){
    let t=window.btoa(window.encodeURIComponent(token));
    localStorage.setItem("t",t);
    localStorage.setItem("e",false);
};

token.storeEmployeeToken=function(token){
    let t=window.btoa(window.encodeURIComponent(token));
    localStorage.setItem("t",t);
    localStorage.setItem("e",true);
};

token.hasToken=function(){
    let token=localStorage.getItem('t');
    if(token==null) return false;
    else return true;
};

token.removeToken=function(){
    localStorage.removeItem('t');
    localStorage.removeItem("e");
};

export default token