<?php
  $arr = array(100,110,40,10,80,200,2);
  $new = $arr;

  for ($i=0; $i < count($arr); $i++) {
    for ($j=0; $j < count($arr)-1; $j++) {
      if ($arr[$j] > $arr[$j+1]) {
        $temp = $arr[$j+1];
        $arr[$j+1] = $arr[$j];
        $arr[$j] = $temp;
      }
    }
  }

  for ($i=0; $i < count($new); $i++) {
    for ($j=0; $j < count($new)-1; $j++) {
      if ($new[$j] < $new[$j+1]) {
        $temp = $new[$j+1];
        $new[$j+1] = $new[$j];
        $new[$j] = $temp;
      }
    }
  }

  print_r($arr);
  print_r($new);

  // or just sort() or rsort()
?>
