<?php
  // THIS IS TO REPLACE CHARACTERS IN A STRING
  $phrase = "$123,34.00A";
  // Got this from the internet
  $newString = preg_replace('/[^0-9,.]+/', '', $phrase) . "\n";
  echo $newString;

  $newPhrase = "ABC it's easy as 123 do rae me ABC123 baby you and m1e";
  $charSent = preg_replace('/[^a-zA-Z ]+/', '', $newPhrase) . "\n";
  echo $charSent;

  $alphanum = "ajbkjaoijofijae;j'fkajsdflknasdnfdnASDF?>:'FVBF':fdf;sf.sam<<>(09(*))(9f76#@$#)";
  $alpnum = preg_replace('/[^A-Za-z0-9 ]+/', '', $alphanum) . "\n";
  echo $alpnum;
?>
