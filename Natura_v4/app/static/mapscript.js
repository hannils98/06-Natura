function indexMap() {
    // The map
    mapboxgl.accessToken = 'pk.eyJ1IjoiaGFubmlsczk4IiwiYSI6ImNrOGgxNGs1ejAydG8zaGxmcjFhNGc3MmsifQ.bmfahnTIFCFL9n9WJAGsYw';
    var map = new mapboxgl.Map({
        container: 'map', // container id
        style: 'mapbox://styles/hannils98/ck8hfxoua1ftp1ioi5jjggbyj', // stylesheet location
        center: [13.582728, 55.893180], // starting position [lng, lat]
        zoom: 7, // starting zoom
        minZoom: 7,
        maxZoom: 16
    });
    // Add pop-up
    map.on('click', function (e) {
        var features = map.queryRenderedFeatures(e.point, {
            layers: ['places']
        });
        if (!features.length) {
            return;
        }
        var feature = features[0];
        var popup = new mapboxgl.Popup({
                offset: [0, -15]
            })
            .setLngLat(feature.geometry.coordinates)
            .setHTML('<h3><a href="/' + feature.properties.name + '/' + feature.properties.id + '">' + feature.properties.name + '</a></h3><p>' + feature.properties.description + '</p>')
            .addTo(map);
    });

    // Add zoom and rotation controls to the map.
    map.addControl(new mapboxgl.NavigationControl());

}

function placeMap() {
    // The map
    var longitude = document.getElementById('longitude').value
    var latitude = document.getElementById('latitude').value
    mapboxgl.accessToken =
        'pk.eyJ1IjoiaGFubmlsczk4IiwiYSI6ImNrOGgxNGs1ejAydG8zaGxmcjFhNGc3MmsifQ.bmfahnTIFCFL9n9WJAGsYw';
    var map = new mapboxgl.Map({
        container: 'map', // container id
        style: 'mapbox://styles/hannils98/ck8hfxoua1ftp1ioi5jjggbyj', // stylesheet location
        center: [longitude, latitude], // starting position [lng, lat]
        zoom: 12, // starting zoom
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

}