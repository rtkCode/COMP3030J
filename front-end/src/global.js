const global = {}

global.baseAddress="http://127.0.0.1:5000/";

global.request=function(address){
    return this.baseAddress+address;
};

export default global