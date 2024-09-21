document.addEventListener("DOMContentLoaded", function () {
  var openModalBtn0 = document.getElementById("botaoFase0");
  var openModalBtn1 = document.getElementById("botaoFase1");

  var modal0 = document.getElementById("modal0");
  var modal1 = document.getElementById("modal1");

  var closeModalSpan0 = document.getElementsByClassName("close")[0];
  var closeModalSpan1 = document.getElementsByClassName("close")[1];

  openModalBtn0.addEventListener("click", function () {
    modal0.style.display = "block";
  });

  openModalBtn1.addEventListener("click", function () {
    modal1.style.display = "block";
  });

  closeModalSpan0.addEventListener("click", function () {
    modal0.style.display = "none";
  });

  closeModalSpan1.addEventListener("click", function () {
    modal1.style.display = "none";
  });

  window.addEventListener("click", function (event) {
    if (event.target == modal0) {
      modal0.style.display = "none";
    }

    if (event.target == modal1) {
      modal1.style.display = "none";
    }
  });
});
