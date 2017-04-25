<?php
  function add_dig($value) {
    $x = str_split($value);
    $sum = 0;
    foreach ($x as $i) {
      $y = (int)$i;
      $sum = $sum + $y;
    }
    $a = new_add_dig($sum);
    return $a;
  }
  function new_add_dig($value) {
    $new_x = str_split($value);
    $new_sum = 0;
    foreach ($new_x as $i) {
      $b = (int)$i;
      $new_sum = $new_sum + $b;
    }
    return $new_sum;
  }
  echo add_dig(48) . "\n";
  echo add_dig(54) . "\n";
  echo add_dig(67) . "\n";
  echo add_dig(148) . "\n";
?>
