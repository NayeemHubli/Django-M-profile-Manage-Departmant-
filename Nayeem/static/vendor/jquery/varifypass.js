function verifyPassword() {
  var pw = document.getElementById("password").value;
  var cpw = document.getElementById("Cpassword").value;    
  if(pw != cpw) {
     
     return alert("Incorrect Confirm-password !");
  } 

 //check empty password field
  if(pw == "") {
     document.getElementById("message").innerHTML = "**Fill the password please!";
     return alert("Fill the password please!");
  }
 
 //minimum password length validation
  if(pw.length < 8) {
     document.getElementById("message").innerHTML = "**Password length must be atleast 8 characters";
     return alert("Password length must be atleast 8 characters");
  }
}
