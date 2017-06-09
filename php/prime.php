<?php
  function IsPrime($number){
    for ($x=2; $x < $number; $x++) {
      if ($number%$x == 0) {
        // echo $number. " is NOT a Prime Number...\n"; //For the $a part of the program
        return 0; //just to break out of the loop when just echoing above!
      }
    }
    // echo $number." IS a Prime Number...\n";
    return 1;
  }

  // $a = IsPrime(23);

  // Here shows what number is Prime and what number isn't prime
  $num = 100;
  echo "Your PRIME Numbers up to $num are:\n";
  for ($i=2; $i <= $num ; $i++) {
    $b = IsPrime($i);
    if ($b==1) {
      echo $i."\n";
    }
  }
?>
