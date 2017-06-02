<?php
  class User
  {
    public $name;
    public $age;

    public function Describe()
    {
        return $this->name . " is " . $this->age . " years old \n";
    }
  }

  $user = new User();
  $user->name = "John Doe";
  $user->age = 42;
  echo $user->Describe();
  $user->name = "Robbie Allen";
  $user->age = 24;
  echo $user->Describe();
?>
