<?php
  function power_of_three($x){
    $orig = $x;

    while ($x%3==0) {
      $x /= 3;
    }
    if ($x == 1) {
      echo "$orig is a power of 3!\n";
    }
    else {
      echo "$orig is NOT a power of 3!\n";
    }
  }

  print_r(power_of_three(9));
  print_r(power_of_three(81));
  print_r(power_of_three(18));
?>
