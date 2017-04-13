<?php
  // Must set the timezone to EST
  date_default_timezone_set('America/New_York');

  echo "3 different ways to write the date\n";
  echo date("Y/m/d") . "\n";
  echo date("m-d-y"). " --> note that the year is abbr" . "\n\n";

  echo "The time is: " . date("H:i:s") . "\n";
  echo "Military time: " . date("h:i:s") . "\n";
  echo "The time with either AM/PM: " . date("H:i:s A") . "\n\n";

  // //See the different time zones
  // $tzlist=timezone_abbreviations_list();
  // print_r($tzlist);

?>
