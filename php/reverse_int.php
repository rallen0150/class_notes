<?php
// One way to do it
  $n = 3456;
  $reverse = 0;
  while ($n > 0) {
    $reverse = $reverse * 10; // Multiply by 10 first
    $reverse = $reverse + $n%10; // Then get the modulus of the last last number first, then next, then next
    $n = (int)($n/10);
  }
  echo $reverse . "\n";

  // Another way to do it
  function reverse_integer($n)
  {
      $reverse = 0;
      while ($n > 0)
        {
          $reverse = $reverse * 10;
          $reverse = $reverse + $n % 10;
          $n = (int)($n/10);
        }
       return $reverse;
  }
  echo reverse_integer(1234)."\n";
  echo reverse_integer(23)."\n";
?>
