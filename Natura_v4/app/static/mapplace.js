// The map
var longitude = document.getElementById('longitude').value
var latitude = document.getElementById('latitude').value
mapboxgl.accessToken =
    'pk.eyJ1IjoiaGFubmlsczk4IiwiYSI6ImNrOGgxNGs1ejAydG8zaGxmcjFhNGc3MmsifQ.bmfahnTIFCFL9n9WJAGsYw';
var map = new mapboxgl.Map({
    container: 'map', // container id
    style: 'mapbox://styles/hannils98/ck8hfxoua1ftp1ioi5jjggbyj', // stylesheet location
    center: [longitude, latitude], // starting position [lng, lat]
    zoom: 20, // starting zoom
    minZoom: 7,
    maxZoom: 16
});

// Add geolocate control to the map.
map.addControl(
    new mapboxgl.GeolocateControl({
        positionOptions: {
            enableHighAccuracy: true
        },
        trackUserLocation: true
    })
);

// Add zoom and rotation controls to the map.
map.addControl(new mapboxgl.NavigationControl());
