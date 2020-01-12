function addToUsers(user, pass, phone){
  
  fetch("https://chubb.api.stdlib.com/http-project@dev/?username="+user+"&password="+pass+"&phoneNum="+phone+"");

}
