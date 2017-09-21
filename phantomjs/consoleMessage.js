var page = require('webpage').create();
var url = 'https://www.baidu.com';
page.onConsoleMessage = function(msg){
    console.log("msg:" + msg);
}; 

page.open(url , function(status){
    page.evaluate(function(){
        console.log(document.title);
    });

    phantom.exit();
});