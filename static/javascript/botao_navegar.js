document.addEventListener("DOMContentLoaded", function () {
  var botoesNavegacao = document.querySelectorAll(".btn-navegacao");

  botoesNavegacao.forEach(function (botao) {
    botao.addEventListener("click", function () {
      botao.classList.add("clicked");
      setTimeout(function () {
        botao.classList.remove("clicked");
      }, 300);
      var destinoTela = botao.dataset.destino;

      // Redirecionar para a tela desejada
      window.location.href = destinoTela;
    });
  });
});
