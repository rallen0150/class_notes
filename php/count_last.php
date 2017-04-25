<?php
  function count_last($value) {
    $x = explode(" ", $value);
    foreach ($x as $i) {
      $str_count = strlen($i);
    }
    return $str_count;
  }
  echo count_last("I love working on PHP excercises")."\n"; // Return 10
  echo count_last("I love working on PHP")."\n"; // Return 3
  echo count_last("Python is my prefered language")."\n"; // Return 8
?>
