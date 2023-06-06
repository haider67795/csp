let click = new Audio("/media/click2.mp3");

function playAudio() {
  click.play();
}

function picChangeToIvan() {
  click.play();
  let currentPic = document.getElementById("picTest");
  currentPic.src = "/media/ivan.jpg";
  currentPic.alt = "A picture of Ivan";
  document.getElementById("cap").innerHTML = "Ivan";
  document.getElementById("fb1").style.backgroundColor = "rgb(50,50,50)";
  document.getElementById("fb2").style.backgroundColor =
    document.getElementById("fb3").style.backgroundColor =
    document.getElementById("fb4").style.backgroundColor =
      "";

  let imgContainer = document.getElementsByClassName("imgContainer");
  imgContainer[0].style.background = "";
  imgContainer[0].style.backgroundColor = "rgb(224, 181, 161)";
}

function picChangeToBen() {
  click.play();
  let currentPic = document.getElementById("picTest");
  currentPic.src = "/media/ben.jpg";
  currentPic.alt = "A picture of Ben";
  document.getElementById("cap").innerHTML = "Ben";
  document.getElementById("fb2").style.backgroundColor = "rgb(50,50,50)";
  document.getElementById("fb1").style.backgroundColor =
    document.getElementById("fb3").style.backgroundColor =
    document.getElementById("fb4").style.backgroundColor =
      "";
  let imgContainer = document.getElementsByClassName("imgContainer");
  imgContainer[0].style.background = "";
  imgContainer[0].style.backgroundColor = "rgb(170, 158, 146)";
}

function picChangeToFord() {
  click.play();
  let currentPic = document.getElementById("picTest");
  currentPic.src = "/media/ford.jpg";
  currentPic.alt = "A picture of Ford";
  document.getElementById("cap").innerHTML = "Ford";
  document.getElementById("fb3").style.background = "rgb(50,50,50)";
  document.getElementById("fb1").style.backgroundColor =
    document.getElementById("fb2").style.backgroundColor =
    document.getElementById("fb4").style.backgroundColor =
      "";
  let imgContainer = document.getElementsByClassName("imgContainer");

  imgContainer[0].style.background =
    "linear-gradient(0deg, rgba(91,206,250,1) 0%, rgba(149,192,225,1) 14%, rgba(245,169,184,1) 14%, rgba(245,169,184,1) 36%, rgba(255,255,255,1) 36%, rgba(255,255,255,1) 59%, rgba(245,169,184,1) 59%, rgba(221,175,194,1) 80%, rgba(157,190,222,1) 80%, rgba(91,206,250,1) 100%)";
}

function picChangeToDefault() {
  click.play();
  let currentPic = document.getElementById("picTest");
  currentPic.src = "/media/default.jpg";
  currentPic.alt = "No One Selected Yet";
  document.getElementById("cap").innerHTML = "No One Selected Yet";
  document.getElementById("fb1").style.backgroundColor =
    document.getElementById("fb2").style.backgroundColor =
    document.getElementById("fb3").style.backgroundColor =
      "";

  let imgContainer = document.getElementsByClassName("imgContainer");
  imgContainer[0].style.background = "";
  imgContainer[0].style.backgroundColor = "";
}

function currentHistory() {
  let display2 = document.getElementById("display2");
  for (let i = 0; i < listOfNums.length; i++) {
    display2.value += listOfNums[i];
  }
}

function add(num) {
  let display = document.getElementById("display");
  display.value += num;
}

function clearD() {
  let display = document.getElementById("display");
  display.value = "";
  clearD2();
  currentHistory();
}
function clearD2() {
  let display = document.getElementById("display2");
  display.value = "";
}
function multiplyNum() {
  let display = document.getElementById("display");
  currentVal = display.value;
  addToList("*");
  clearD();
}

function subNum() {
  let display = document.getElementById("display");
  currentVal = display.value;
  addToList("-");
  clearD();
}
function addNum() {
  let display = document.getElementById("display");
  currentVal = display.value;
  addToList("+");
  clearD();
}
function divideNum() {
  let display = document.getElementById("display");
  currentVal = display.value;
  addToList("/");
  clearD();
}

let listOfNums = [];
function addToList(operation) {
  num = document.getElementById("display").value;
  listOfNums.push(num);
  listOfNums.push(operation);
  console.log(listOfNums);
}

function solve() {
  addToList("");

  for (i = 0; i < listOfNums.length; i += 2) {
    if (listOfNums[i + 1] == "*") {
      let answer = parseFloat(listOfNums[i]) * parseFloat(listOfNums[i + 2]);
      console.log(answer);
      let display = document.getElementById("display");

      display.value = answer;
    } else if (listOfNums[i + 1] == "-") {
      let answer = parseFloat(listOfNums[i]) - parseFloat(listOfNums[i + 2]);
      console.log(answer);
      let display = document.getElementById("display");

      display.value = answer;
    } else if (listOfNums[i + 1] == "+") {
      let answer = parseFloat(listOfNums[i]) + parseFloat(listOfNums[i + 2]);
      console.log(answer);
      let display = document.getElementById("display");

      display.value = answer;
    } else if (listOfNums[i + 1] == "/") {
      let answer = parseFloat(listOfNums[i]) / parseFloat(listOfNums[i + 2]);
      console.log(answer);
      let display = document.getElementById("display");

      display.value = answer;
    }
  }

  listOfNums = [];
  clearD2();
}

function clearAll() {
  clearD();
  clearD2();
  listOfNums = [];
}
