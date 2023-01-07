




setTimeout(function(){
    //do what you need here


Object.keys(parsed[0]).forEach(function(key) {
    console.log('Key : ' + key + ', Value : ' + parsed[0][key])
    if (parsed[0][key] === 1)
         {
         document.getElementById(key).classList.remove("hidden");

         }

})}, 1000);