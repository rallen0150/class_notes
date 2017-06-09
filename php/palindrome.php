<?php
  function palindrome($string){
    $newString = strtolower($string);
    $newString = preg_replace('/\s+/', '', $newString);
    if ($newString==strrev($newString)) {
      echo "$string is a Palindrome!\n";
      return 0;
    }
    echo "$string is NOT a Palindrome!\n";
  }
  palindrome("Hello World!");
  palindrome("mAdaM");
  palindrome("Booya Hay oOB");
?>
