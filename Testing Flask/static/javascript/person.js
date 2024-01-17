import {savetoarray} from './registration_handling.js'



export let data2=
[
            {
                id:'User01',
                userName:'Hitanshu Tandon',
                phonNo:9005177421,
                alternatePhoneno:400000000,
                Latitude: 26.8466937 ,
                Longitude: 80.946166,
                pincode:'226003',
                email:'random@gmail.com',
                ipAddress:156161
            }
]
        
const temp= savetoarray()
console.log(temp)
if(temp!=null)data2=temp;
console.log(data2)

       