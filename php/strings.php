<?php

  $sentence = "hello world. I am the tiger!";

  // ucfirst is for capitalize like a sentence
  echo ucfirst($sentence) . "\n";
  // ucwords is like Python title
  echo ucwords($sentence . "\n");
  // For all uppercase
  echo strtoupper($sentence) . "\n";
  // For all lowercase
  echo strtolower($sentence) . "\n";
  // Reverses a string
  echo strrev($sentence) . "\n";
  // Returns the length of a string
  echo strlen($sentence) . "\n";
  // Counts how many words in the string
  echo str_word_count($sentence) . "\n";
  // Shuffle words
  echo str_shuffle($sentence) . "\n";
  // How to replace a word
  echo str_replace("world", "Robbie", $sentence) . "\n";
?>
