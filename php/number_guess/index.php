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
      <h1>Guess a Number Between <b>1</b> and <b>10</b>!</h1>
      <form class="" action="check.php" method="post">
        <p><input type="number" name="num_guess" max="10"></p>
        <p><input type="submit" name="" value="Guess"></p>
      </form>
    </div>

  </body>
</html>
