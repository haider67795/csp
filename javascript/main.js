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
