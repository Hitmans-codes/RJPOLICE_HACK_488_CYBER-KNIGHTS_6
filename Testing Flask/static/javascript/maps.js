import { data2 as data} from "./person.js";

function initMap() {
    // Initialize the map centered at a default location
    const map = new google.maps.Map(document.getElementById('map'), {
      center: { lat:26.8466937 , lng: 80.946166}, // Default to New York, NY
      zoom: 12
    });

    // Function to show the map based on user input
    // window.showMap = function () {
    //   const latitude = parseFloat(document.getElementById('latitude').value);
    //   const longitude = parseFloat(document.getElementById('longitude').value);

    //   // Validate latitude and longitude
    //   if (isNaN(latitude) || isNaN(longitude)) {
    //     alert('Please enter valid latitude and longitude.');
    //     return;
    //   }

    //   // Center the map on the user-inputted location
    //   map.setCenter({ lat: latitude, lng: longitude });

    //   // Add a marker at the specified location
    //   const marker = new google.maps.Marker({
    //     position: { lat: latitude, lng: longitude },
    //     map: map,
    //     title: 'Selected Location'
    //   });
    // };
    window.showMap = function () {
      for (let i = 0; i < data.length; i++){
        const marker= new google.maps.Marker({position:{lat:Number(data[i].Latitude),lng:Number(data[i].Longitude)},
        map:map,
        
  
        });}
    };

    // Function to show the location based on pincode
    window.showLocationByPincode = function () {
      const pincode = document.getElementById('pincode').value;
      // const pincode = document.getElementById('pincode').value;

      // // Validate pincode
      // if (!pincode) {
      //   alert('Please enter a pincode.');
      //   return;
      // }

      // Use Geocoding API to get location coordinates from pincode
      const geocoder = new google.maps.Geocoder();
      
      for(let i=0;i<data.length;i++){

         console.log(Number(data[i].pincode))
         if(pincode===data[i].pincode){
        geocoder.geocode({ address:data[i].pincode }, (results, status) => {
        if (status === 'OK' && results[0].geometry) {
          const location = results[0].geometry.location;
          map.setCenter(location);

          // Add a marker at the specified location
          const marker = new google.maps.Marker({
            position: location,
            map: map,
            title: data[i].pincode
          });
        } else {
          alert('Unable to find location for the provided pincode.');
        }
      });}
    }
      
    };
}
initMap()

  