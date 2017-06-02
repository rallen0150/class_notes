<?php
  date_default_timezone_set('America/New_York');

  $odate = "2012-09-12";
  $newDate = date("M d,Y", strtotime($odate));
  echo $newDate."\n";
?>
