var page = require("webpage").create(),
    system = require("system"),
    t,
    address;

if(system.args.length === 1){
    console.log('Usage: loadspeed.js <some url>');
    phantom.exit();
}

t = Date.now();
address = system.args[1];
page.open(address,function(status){
    console.log('status:'+status);
    if(status !== 'success'){
        console.log('fail to load page');
    }else{
        t = Date.now() - t;
        console.log("load " + address);
        console.log('load cost ' + t + " msec");

    }
    phantom.exit();
});
