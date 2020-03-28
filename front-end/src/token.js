const token = {}

token.getToken=function(n) {
    let token = localStorage.getItem('t');
    let t = window.decodeURIComponent(window.atob(token));
    if (n == 0) return token;
    if (n == 1) return t;
};

token.storeToken=function(token){
    let t=window.btoa(window.encodeURIComponent(token));
    localStorage.setItem("t",t);
};

export default token