const heading = document.getElementsByTagName("p");
let div = heading[1];
div.textContent = "ECE";

const para = document.getElementsByTagName("p");
console.log(para);
for (let i = 0; i < para.length; i++) {
  para[i].style.fontStyle = "italic";
}

const newDiv = document.createElement("p");
newDiv.textContent = "AIML";
newDiv.classList.add("p");
const parent = document.getElementById("data");
parent.appendChild(newDiv);
console.log(newDiv);

const button = document.querySelector("#button1");
button.addEventListener("mouseover", () => {
  button.style.backgroundColor = "green";
  button.style.scale = 1.2;
});

button.addEventListener("mouseout", () => {
  button.style.backgroundColor = "white";
  button.style.scale = 0.9;
});

button.addEventListener("click", () => {
  const newH1 = document.createElement("h1");
  console.log();
  newH1.textContent = document.getElementById("input").value;
  document.getElementById("data").appendChild(newH1);
});
