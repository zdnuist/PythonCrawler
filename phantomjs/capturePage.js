var page = require("webpage").create();
page.open("http://www.qq.com", function(status){
    console.log("status=" + status)
    if(status === "success"){
        page.render("qq.png");
    }
    phantom.exit();
});