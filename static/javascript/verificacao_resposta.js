document.addEventListener("DOMContentLoaded", function () {
  
  document.querySelector("form").addEventListener("submit", function (event) {
    event.preventDefault();
    verificarRespostas();
  });
});

function verificarRespostas() {
  // Função auxiliar para verificar uma pergunta individual
  function verificarPergunta(nome, respostaCorreta, indicePergunta) {
    var opcoes = document.getElementsByName(nome);
    var respostaUsuario = null;

    // Itera sobre as opções para encontrar a resposta selecionada
    for (var i = 0; i < opcoes.length; i++) {
      if (opcoes[i].checked) {
        respostaUsuario = opcoes[i].value;
        break;
      }
    }

    // Verifica se a resposta do usuário é correta
    var mensagemFeedback = document.getElementById(
      "mensagemFeedback" + indicePergunta
    );
    if (respostaUsuario === respostaCorreta) {
      mensagemFeedback.innerHTML =
        "Resposta correta para a pergunta " + indicePergunta;
    } else {
      mensagemFeedback.innerHTML =
        "Resposta incorreta para está pergunta ";
    }
  }

  verificarPergunta("q1", "1", 1);
  verificarPergunta("q2", "1", 2); 
  verificarPergunta("q3", "1", 3);
}
