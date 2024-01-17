// console.log("hello")
import {data2 as da} from './person.js'



export function update_registration()
{
    console.log(da)
    console.log('helloworld')
  const name=document.getElementById('name')
  // console.log(name.value)
  const phone=document.getElementById('phone')
  // console.log(phone.value)
  const altPhone=document.getElementById('altPhone')
  // console.log(altPhone.value)
  const latitude=document.getElementById('latitude')
  // console.log(latitude.value)
  const longitude=document.getElementById('longitude')
  // console.log(longitude.value)
  const pincode=document.getElementById('pincode')
  // console.log(pincode.value)
  const email=document.getElementById('email')
  // console.log(email.value)
  const ipAddress=document.getElementById('ipAddress')
  // console.log(ipAddress.value)
  let temp
  if (!da ){temp=0}
    
  else
  {temp=da.length}




    temp++;
  da.push({
        id:'User'+temp,
        userName:name.value,
        phonNo:phone.value,
        alternatePhoneno:altPhone.value,
        Latitude:latitude.value,
        Longitude:longitude.value,
        pincode:pincode.value,
        email:email.value,
        ipAddress:ipAddress.value
  })
  console.log(da)
  valuesupdated()
  
}
function saveToStorage() {
  localStorage.setItem('cart', JSON.stringify(da));
  
}
export function savetoarray()
{
  
  return JSON.parse(localStorage.getItem('cart'))
}
function valuesupdated()
{
  
  
  //localStorage.clear()
  saveToStorage()
  
}


