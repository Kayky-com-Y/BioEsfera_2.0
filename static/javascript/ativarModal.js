document.addEventListener("DOMContentLoaded", function () {
  // Selecionar todos os botões e modais
  var botaoFases = document.querySelectorAll("[id^='botaoFase']");
  var modals = document.querySelectorAll(".modal");
  var closes = document.querySelectorAll(".close");

  // Adicionar event listeners aos botões para abrir os modais
  botaoFases.forEach(function (botao, index) {
    botao.addEventListener("click", function () {
      modals[index].style.display = "flex";  // Usar flex para centralização
      document.body.classList.add("modal-open");  // Desativar rolagem do body
    });
  });

  // Adicionar event listeners aos botões de fechar para fechar os modais
  closes.forEach(function (close, index) {
    close.addEventListener("click", function () {
      modals[index].style.display = "none";
      document.body.classList.remove("modal-open");  // Reativar rolagem do body
    });
  });

  // Fechar o modal ao clicar fora dele
  window.addEventListener("click", function (event) {
    modals.forEach(function (modal) {
      if (event.target == modal) {
        modal.style.display = "none";
        document.body.classList.remove("modal-open");  // Reativar rolagem do body
      }
    });
  });
});
