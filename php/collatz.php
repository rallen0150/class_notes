<?php
  function collatz($x) {
      $num_seq = [$x];
      if ($x <= 1) {
         return [];
      }
      while ($x > 1) {
         if ($x % 2 == 0) {
           $x = $x / 2;
         }
         else {
           $x = 3 * $x + 1;
         }
      # Added line
      array_push($num_seq, $x);
      }
    return $num_seq;
  }
  print_r(collatz(12));
  print_r(collatz(19));
?>
