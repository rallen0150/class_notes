<?php
  function histogram($a){
    for ($i=0; $i <= $a; $i++) {
      for ($x=1; $x <=$i; $x++) {
        echo "#";
        if ($x<$i){
          echo "  ";
        }
      }
      echo "\n";
    }
    for ($i=$a; $i >= 0; $i--) {
      for ($x=1; $x <=$i; $x++) {
        echo "#";
        if ($x<$i){
          echo "  ";
        }
      }
      echo "\n";
    }
  }
  $his = 10;
  print_r(histogram($his)."\n");
  
  echo "MY TIMES TABLE!!!\n\n";
  for ($row=1; $row <= 10 ; $row++) {
    for ($col=1; $col <= 10 ; $col++) {
      $ans = $col * $row;
      echo $ans . " ";
    }
    echo " \n";
  }
?>
