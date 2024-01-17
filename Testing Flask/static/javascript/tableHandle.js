import { data2 as data} from "./person.js";

let tableHtml='';
let flag=0;
function displayTable(){
  
    
    data.forEach((datas)=>{
      tableHtml +=`<tr>
      <td>${datas.id}</td>
      <td>${datas.userName}</td>
      <td>${datas.Latitude}</td>
      <td>${datas.Longitude}</td>
      <td>${datas.pincode}</td>
      <td>${datas.phonNo}</td>
      <td>${datas.alternatePhoneno}</td>
      <td>${datas.email}</td>
      <td>${datas.ipAddress}</td>
       
    </tr>`;
    
    });
    document.querySelector('.table-content').innerHTML =tableHtml;
}


function searchByValue()
{
  tableHtml=``;
  console.log(pincodetosearch.value)
  data.forEach((datas)=>{
    console.log(datas.pincode)
    if(pincodetosearch.value==datas.pincode)
    {
      console.log('matched')
      tableHtml +=`<tr>
        <td>${datas.id}</td>
        <td>${datas.userName}</td>
        <td>${datas.Latitude}</td>
        <td>${datas.Longitude}</td>
        <td>${datas.pincode}</td>
        <td>${datas.phonNo}</td>
        <td>${datas.alternatePhoneno}</td>
        <td>${datas.email}</td>
        <td>${datas.ipAddress}</td>   
        </tr>`;
        

    }
    if(pincodetosearch.value==datas.id)
    {
      console.log('matched')
      tableHtml +=`<tr>
        <td>${datas.id}</td>
        <td>${datas.userName}</td>
        <td>${datas.Latitude}</td>
        <td>${datas.Longitude}</td>
        <td>${datas.pincode}</td>
        <td>${datas.phonNo}</td>
        <td>${datas.alternatePhoneno}</td>
        <td>${datas.email}</td>
        <td>${datas.ipAddress}</td>   
        </tr>`;
        

    }
  })
  
  flag=1;
  console.log(flag)
  document.querySelector('.table-content').innerHTML =tableHtml;
}

var pincodetosearch=document.getElementById('pincode')

var searchbutton = document.querySelector('.searchbypincode');
searchbutton.addEventListener('click',searchByValue);
console.log(tableHtml)
var showbutton= document.querySelector('.showTable')
showbutton.addEventListener('click',displayTable)






