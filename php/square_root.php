<?php
  function square_root($x){
    $ans = sqrt($x);
    $ans = round($ans, 3);
    echo "$ans\n";
  }
  
  print_r(square_root(16));
  print_r(square_root(24));
  print_r(square_root(36));
?>
