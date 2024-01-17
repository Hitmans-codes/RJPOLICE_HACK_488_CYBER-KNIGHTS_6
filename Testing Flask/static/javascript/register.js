import { update_registration } from "./registration_handling.js";
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        alert("Geolocation is not supported by this browser.");
    }
  }
  
  function showPosition(position) {
    document.getElementById("latitude").value = position.coords.latitude 
    document.getElementById("longitude").value = position.coords.longitude;
  }

function backToHome(){
  window.location.replace("index.html");

}
var home=document.querySelector('.js-registrationToHome')
var buttonHtml=document.querySelector('.js-register-button')
var getLo=document.querySelector('.getLocation')
home.addEventListener('click',backToHome)
getLo.addEventListener('click',getLocation);
buttonHtml.addEventListener('click',update_registration);