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

  echo "\n";

  // From a website for another assignment
  $strings = array('KjgWZC', 'arf12');
  foreach ($strings as $testcase) {
      if (ctype_alpha($testcase)) {
          echo "The string $testcase consists of all letters.\n";
      } else {
          echo "The string $testcase does not consist of all letters.\n";
      }
  }

  echo "\n";

  $sent = "The quick brown fox is fast as lightning";
  // \s is for space like \n is for newline
  echo preg_replace('/\s+/', '', $sent) . "\n";

  echo "\n";

  // removes the final word
  $sent = "The quick brown fox";
  echo preg_replace("/\W\w+\s*(\W*)$/", '$1', $sent)."\n";
?>
