const global = {}

global.baseAddress="http://123.57.167.155:5000/";

global.request=function(address){
    return this.baseAddress+address;
};

export default global