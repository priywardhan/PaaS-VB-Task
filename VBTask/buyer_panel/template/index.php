<?php
    $firstname = $_POST['firstname'];
    $lastname = $_POST['lastname'];

    //Database connection
 $conn = new mysqli('localhost','root','','test');
 die('Connection Failed : '.$conn->connect_error);
}else{
  $stmt = $conn->>prepare("insert into registration(firstName, lastName) values(?,?)");
 $stmt->bind_param("ss", ,$firstName, $lastName);
 $stmt->execute();
  echo "registration SUccessfully...";
 $stmt->close();
 $conn->close ();

?>
