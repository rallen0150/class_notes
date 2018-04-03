<?php
  function checkBalancedBrackets($str) {
    $check = [
      '{' => '}',
      '[' => ']',
      '(' => ')'
    ];
    if ($str == "") {
      return true;
    }
    $stack = [];
    for ($i=0; $i < strlen($str); $i++) {
      if ($str[$i]=='{' || $str[$i]=='[' || $str[$i]=='(') {
        array_push($stack, $str[$i]);
      }
      else {
        $last = array_pop($stack);
        if ($str[$i] !== $check[$last]) {
          return false;
        }
      }
    }
    if ($sizeof($stack) < 0) {
      return false;
    }
    return true;
  }

if (checkBalancedBrackets('[{}]')) {
  echo "True";
} else {
  echo "False";
}

https://www.glassdoor.com/Interview/The-most-difficult-question-I-received-was-to-explain-in-detail-exactly-what-happened-once-you-enter-a-url-in-your-browser-QTN_633408.htm
https://www.glassdoor.com/Interview/Wayfair-Interview-Questions-E134525_P2.htm?sort.sortType=RD&sort.ascending=false&filter.jobTitleFTS=Software+Engineer
?>
