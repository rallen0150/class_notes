<?php
  $nums = array(11,103,645,34,3,632,100, -453234);
  $floatnums = array(23.55645,10.553534,50.324682,67.83328,76.905525,6.034682);

  sort($nums);
  foreach ($nums as $x) {
    echo $x.", ";
  }
  echo "\n";

  sort($floatnums);
  foreach ($floatnums as $s) {
    echo $s.", ";
  }
  echo "\n";
  echo "\n";

  echo max($nums)."\n";
  echo min($nums)."\n";

  echo "\n";

  foreach ($floatnums as $x) {
    echo round($x, 2)."\n";
  }
?>
