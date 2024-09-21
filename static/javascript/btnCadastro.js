// Obtém o botão por ID
var meuBotao = document.getElementById("Btn1");
var meuBotaIndex = document.getElementById("Btn_cadastro");

// Adiciona um ouvinte de evento para o clique no botão
if (meuBotao) {
  meuBotao.addEventListener("click", function () {
    meuBotao.classList.add("clicked");
    setTimeout(function () {
        btnVoltar.classList.remove("clicked");
      }, 300);
    // Redireciona para outra página
    window.location.href = "cadastro.html";
    
  });
}
if (meuBotaIndex) {
  meuBotaIndex.addEventListener("click", function () {
    meuBotaIndex.classList.add("clicked");
    setTimeout(function () {
        btnVoltar.classList.remove("clicked");
      }, 300);
    // Redireciona para outra página
    window.location.href = "cadastro.html";
  });
}
