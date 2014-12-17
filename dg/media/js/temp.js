            var lat, lng;
            //$("#map-canvas").hide();
            navigator.geolocation.getCurrentPosition(function(position)
            { 
                lat = position.coords.latitude;
                lng = position.coords.longitude;
                console.log( lat + ":" + lng);
                //alert(lat + ":" + lng);
                jQuery("input#id_latitude").val(lat);
                jQuery("input#id_longitude").val(lng);
            });
