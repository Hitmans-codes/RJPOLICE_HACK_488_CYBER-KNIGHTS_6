import { data2 as data} from "./person.js";

let clienthtml=''

clienthtml+=`<p><strong>UserId:</strong>${data[0].id} <br>
<strong>Name:</strong>${data[0].userName} <br>
<strong>Phone Number:</strong>${data[0].phonNo} <br>
<strong>Alternate Phone Number:</strong>${data[0].alternatePhoneno} <br>
<strong>Email:</strong>${data[0].email} <br>
<strong>UserId:</strong>${data[0].id} <br></p>`
console.log(clienthtml)
document.getElementById('clientinfo').innerHTML=clienthtml;

console.log(clienthtml)