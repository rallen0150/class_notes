<?php
  // Must set the timezone to EST
  date_default_timezone_set('America/New_York');

  echo "3 different ways to write the date\n";
  echo date("Y/m/d") . "\n";
  echo date("m-d-y"). " --> note that the year is abbr" . "\n\n";

  echo "The time is: " . date("H:i:s") . "\n";
  echo "Military time: " . date("h:i:s") . "\n";
  echo "The time with either AM/PM: " . date("H:i:s A") . "\n\n";

  echo "The Month right now is ".date("M")."\n";
  echo "The Day of the Week right now is ".date("D")."\n";
  echo "The Day of the Week right now is ".date("l")." -> Non abbreviated\n\n";

  $d=strtotime("10:30pm April 5 2014");
  echo "Created date is " . date("m/d/Y h:i", $d)."\n\n";

  $d=strtotime("tomorrow");
  echo "Tommorow's date is ".date("m/d/Y h:i:sa", $d)."\n";
  $d=strtotime("next Saturday");
  echo "Next Saturday's date is ".date("m-d-Y h:i:sa", $d)."\n";
  $d=strtotime("+3 Months");
  echo "3 months from now is ".date("M d/Y h:i:sa", $d)."\n\n";

  $d=mktime(18, 14, 18, 8, 12, 2014); //mktime(hour,minute,second,month,day,year)
  echo "Created date is " . date("m-d-Y h:i:sa", $d)." -> Right now converting military time, but doesn't have to be military time\n";
?>
