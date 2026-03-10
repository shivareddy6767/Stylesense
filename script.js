document.querySelector("#styleForm").addEventListener("submit", async function(event){

event.preventDefault();

let gender = document.getElementById("gender").value;
let occasion = document.getElementById("occasion").value;
let color = document.getElementById("color").value;
let image = document.getElementById("image").files[0];

let formData = new FormData();

formData.append("gender", gender);
formData.append("occasion", occasion);
formData.append("color", color);
formData.append("image", image);

let response = await fetch("http://127.0.0.1:8000/recommend",{
method:"POST",
body:formData
});

let data = await response.json();

let resultDiv = document.getElementById("result");

/* REMOVE OLD IMAGES */
resultDiv.innerHTML = "";

data.outfits.forEach(img => {

let imageElement = document.createElement("img");
imageElement.src = img;
imageElement.className = "outfit-img";

resultDiv.appendChild(imageElement);

});

});