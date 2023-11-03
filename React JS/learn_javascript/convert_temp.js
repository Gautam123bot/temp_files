let celcius=document.getElementById("celsius");
let fahrenheit=document.getElementById("fahrenheit");

function celToFar(){
    let output=(parseFloat(celsius.value)*9/5)+32;
    fahrenheit.value=parseFloat=parseFloat(output.toFixed(2));
    console.log(output);
}

function farToCel(){
    let output=(parseFloat(fahrenheit.value)-32)*5/9;
    celcius.value=parseFloat(output.toFixed(2));
    console.log(output);
}