InsomniHack Teaser 2017 SmartTomCat WriteUp

The question was like following:

Normal, regular cats are so 2000 and late, I decided to buy this allegedly smart tomcat robot Now the damn thing has attacked me and flew away. I can't even seem to track it down on the broken search interface... Can you help me ?
<br/>
Search interface
<br/>
<br/>
First, in page source, the lattitue (X) and longitude (Y) parameters are posted like following
</br>
```javascript
...
    var cat_coords = 'http://localhost:8080/index.jsp?x=' + parseFloat($('#xcoord').val()) + '&y=' + parseFloat($('#ycoord').val());
    var $form = $(this);
    var $inputs = $form.find('input, select, button, textarea');
    $inputs.prop('disabled', true);

    request = $.ajax({
        url: '/index.php',
        type: 'post',
        success: function(data) {
          markers.clearMarkers();
          while(map.popups.length) {map.removePopup(map.popups[0]);}
          var y = parseFloat($('#ycoord').val());
          var x = parseFloat($('#xcoord').val());
          if (isNaN(y) || isNaN(x)) {y = 15.2833; x = -4.2667;}
          lonlat = new OpenLayers.LonLat(y,x).transform(new OpenLayers.Projection("EPSG:4326"),map.getProjectionObject());
          center_marker = new OpenLayers.Marker(lonlat);
          markers.addMarker(center_marker);
          popup = new OpenLayers.Popup.FramedCloud("popup",
                   lonlat,
                   null,
                   data, null,
                   true);
          map.addPopup(popup);
          map.setCenter(lonlat,zoom);
        },
        data: {
		u: cat_coords
	}
...
```
Next, I sent the request to Repeater and get the following response.

![alt tag](https://github.com/rustempasha/insomnihack-teaser-2017-smarttomcat/blob/master/tomcat/writeup.png)

In parameter, the X and Y parameters are sent with GET request to the local server on port 8080.
When I tried to send request without parameters I get the following response.

![alt tag](https://github.com/rustempasha/insomnihack-teaser-2017-smarttomcat/blob/master/tomcat/burp2.png)





