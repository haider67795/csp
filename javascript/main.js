let click = new Audio("/media/click2.mp3");

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
  document.body.style.backgroundColor = "rgb(224, 181, 161)";
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
  document.body.style.backgroundColor = "rgb(170, 158, 146)";
}

function picChangeToFord() {
  click.play();
  let currentPic = document.getElementById("picTest");
  currentPic.src = "/media/ford.jpg";
  currentPic.alt = "A picture of Ford";
  document.getElementById("cap").innerHTML = "Ford";
  document.getElementById("fb3").style.backgroundColor = "rgb(50,50,50)";
  document.getElementById("fb1").style.backgroundColor =
    document.getElementById("fb2").style.backgroundColor =
    document.getElementById("fb4").style.backgroundColor =
      "";
  document.body.style.backgroundColor = "rgb(93, 88, 78)";
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
  document.body.style.backgroundColor = "";
}

function add(num) {
  let display = document.getElementById("display");
  display.value += num;
}

// function deleteAdd(num) {
//   let display = document.getElementById("display");
//   display.value.toString().slice(0, -1);
// }

function clearD() {
  let display = document.getElementById("display");
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
      let answer = listOfNums[i] * listOfNums[i + 2];
      console.log(answer);
      let display = document.getElementById("display");

      display.value = answer;
    } else if (listOfNums[i + 1] == "-") {
      let answer = listOfNums[i] - listOfNums[i + 2];
      console.log(answer);
      let display = document.getElementById("display");

      display.value = answer;
    } else if (listOfNums[i + 1] == "+") {
      let answer = parseInt(listOfNums[i]) + parseInt(listOfNums[i + 2]);
      console.log(answer);
      let display = document.getElementById("display");

      display.value = answer;
    } else if (listOfNums[i + 1] == "/") {
      let answer = listOfNums[i] / listOfNums[i + 2];
      console.log(answer);
      let display = document.getElementById("display");

      display.value = answer;
    }
  }

  listOfNums = [];
}

function clearAll() {
  clearD();
  listOfNums = [];
}
