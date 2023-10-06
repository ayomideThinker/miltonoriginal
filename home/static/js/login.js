let signupBtn = document.getElementById("signupBtn");
let signinBtn = document.getElementById("signinBtn");
let nameField = document.getElementById("nameField");
let cpassword = document.getElementById("cpassword");
let forgot = document.getElementById("forgot");
let title = document.getElementById("title");

signinBtn.onclick = function(){
    nameField.style.maxHeight = "0";
    cpassword.style.height = "0";
    title.innerHTML = "Login";
    signupBtn.classList.add("disable");
    signinBtn.classList.remove("disable");
}

signupBtn.onclick = function(){
    nameField.style.maxHeight = "60px";
    title.innerHTML = "Register";
    cpassword.style.height = "3.5rem";
    signupBtn.classList.remove("disable");
    signinBtn.classList.add("disable");
}