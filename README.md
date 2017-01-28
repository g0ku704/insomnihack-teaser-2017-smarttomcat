# InsomniHack Teaser 2017 SmartTomCat WriteUp

The question was like following:

Normal, regular cats are so 2000 and late, I decided to buy this allegedly smart tomcat robot Now the damn thing has attacked me and flew away. I can't even seem to track it down on the broken search interface... Can you help me ?
<br/>
<a href="http://smarttomcat.teaser.insomnihack.ch">Search interface</a>
<br/>
<br/>
<br/>
![alt tag](https://github.com/rustempasha/insomnihack-teaser-2017-smarttomcat/blob/master/tomcat/scrensht.png)
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
<br/>
![alt tag](https://github.com/rustempasha/insomnihack-teaser-2017-smarttomcat/blob/master/tomcat/writeup.png)
<br/>
<br/>
In parameter, the X and Y parameters are sent with GET request to the local server on port 8080.
When I tried to send request without parameters I get the following response.
<br/>
![alt tag](https://github.com/rustempasha/insomnihack-teaser-2017-smarttomcat/blob/master/tomcat/burp2.png)
<br/>
<br/>
I only can send requests to the local server with X and Y included.
Then, I looked for web contents in the local server and I found something interesting.
<br/>
![alt tag](https://github.com/rustempasha/insomnihack-teaser-2017-smarttomcat/blob/master/tomcat/burp3.png)
<br/>
<br/>
Whoa! The smart 'tomcat' is actually Apache Tomcat server (Also the logo of Apache Tomcat is described in index page).
I wrote a small Python and Bash fuzzing script to discover web contents in Apache Tomcat using Tomcat dorks.
And then I found <b>'/manager/html'</b> directory exists but need authentication.
![alt tag](https://github.com/rustempasha/insomnihack-teaser-2017-smarttomcat/blob/master/tomcat/writeup2.png)
<br/>
<br/>
For HTTP basic authentication, I tried some default user:pass combination used in Apache Tomcat manager page and voila,
flag is given in response.
<br/>
![alt tag](https://github.com/rustempasha/insomnihack-teaser-2017-smarttomcat/blob/master/tomcat/writeup3.png)
<br/>
Flag: <b>INS{th1s_is_re4l_w0rld_pent3st}</b>


