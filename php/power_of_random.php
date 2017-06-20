<?php
  function power_of_random($x, $n){
    $power = $x;
    $num = $n;

    while($x%$n==0){
      $x /= $n;
    }
    if ($x == 1) {
      echo "$power is a power of $num!\n";
    }
    else {
      echo "$power is NOT a power of $num!\n";
    }
  }

  print_r(power_of_random(16, 2));
  print_r(power_of_random(25, 5));
  print_r(power_of_random(27, 3));
  print_r(power_of_random(62, 4));
?>
