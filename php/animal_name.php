<?php
  class Animal
  {
      public $name = "No-name animal";

      public function __construct($name)
      {
          echo "I'm alive! ";
          $this->name = $name;
      }

      public function __destruct()
      {
          echo " I'm dead now :( \n";
      }
  }

  $animal = new Animal("Bob");
  echo "Name of the animal: " . $animal->name ;
?>
