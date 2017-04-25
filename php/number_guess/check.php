<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Number Guess</title>

    <link rel="stylesheet" href="static/css/bootstrap.css" media="screen" title="no title">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

  </head>
  <body>
    <div class="container">
      <?php
        $num_guess = $_POST["num_guess"];
        $num = rand(1,10);
        if ($num_guess == $num) {
          echo "<h3>You are Correct!!! The correct number is <i><u>" . $num . "</u></i></h3>\n";
        }
        else {
          echo "<h3>So SORRY! The correct number is <i><u>" . $num . "</u></i></h3>\n";
        }
      ?>
      <br>
      <a href="index.php">Guess again</a>
    </div>
  </body>
</html>
