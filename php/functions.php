<?php
  function factorial_of_a_number($n){
    if($n ==0)
      {
         return 1;
      }
    else
      {
         return $n * factorial_of_a_number($n-1);
      }
  }
  print_r(factorial_of_a_number(4)."\n");
  echo "\n";

  function prime_number($x){
    for ($a == 2; $a<$x; $a++){
      if ($x%$a == 0){
        return 0;
      }
    }
      return 1;
  }
  $y = prime_number(5);
  if ($y == 0)
  echo "This is NOT a prime number!\n";
  else
  echo "This IS a prime number!\n"
?>
