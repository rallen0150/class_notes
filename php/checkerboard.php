<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Checkerboard</title>
  </head>
  <body>
    <table width="550px" cellspacing="0px" cellpadding="0px" border="1px">
      <?php
        for ($row=0; $row<= 8; $row++) {
          echo "<tr>";
          for ($col=0; $col<=8 ; $col++) {
            $total = $row + $col;
            if ($total%2==0) {
              echo "<td height=55px width=55px bgcolor=#FFFFFF></td>";
            }
            else {
              echo "<td height=55px width=55px bgcolor=#000000></td>";
            }
          }
          echo "</tr>";
        }
      ?>
    </table>
  </body>
</html>
