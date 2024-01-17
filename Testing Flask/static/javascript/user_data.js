import {sendtouserjs} from './registration_handling.js'

function saveToStorage() 
{
    localStorage.setItem('userdata', JSON.stringify(sendtouserjs));
}
saveToStorage()
data = JSON.parse(localStorage.getItem('userdata'));

console.log(data)