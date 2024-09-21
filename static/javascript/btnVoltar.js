// Obtém o botão por ID
var btnVoltar = document.getElementById("BtnV");

// Adiciona um ouvinte de evento para o clique no botão
btnVoltar.addEventListener("click", function() {
    // Volta para a página anterior no histórico do navegador
    window.history.back();
});