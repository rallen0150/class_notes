<?php
  function array_sort($arr){
    for ($x=0; $x < count($arr); $x++) {
      $min = $x;
      for ($y=$x+1; $y < count($arr); $y++) {
        if ($arr[$y] < $arr[$min]) {
          $larger_value = $arr[$min]; //Sets the larger_value as the $x value
          $arr[$min] = $arr[$y]; //Changes the min value to the actual minimum value
          $arr[$y] = $larger_value; //Sets the $y value as the larger value
        }
      }
    }
    return $arr;
  }
  $a = array(51,14,1,21,-99, 109, 34.44);
  print_r(array_sort($a));
?>
