<<<<<<< HEAD
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Welcome <?php echo  $_POST['name'] ?><br></h1>

</body>
</html>
=======
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h3>Welcome <?php echo $_POST['name'] ?><br></h3>
    <h3>Your Email is <?php echo $_POST['email'] ?><br></h3>
    
</body>
</html>
<?php 
$conn=new mysqli("localhost","root","","cetmca");

if ($conn){
    $sql = "INSERT INTO user_data (Name,email) VALUES ('".$_POST['name']."','".$_POST['email']."')";
    $conn->query($sql);

    
}
else{
    echo "Connection failed";
    }
?>
>>>>>>> e805ffd07174b57e7462f8f7bc0bd6827c28b495
