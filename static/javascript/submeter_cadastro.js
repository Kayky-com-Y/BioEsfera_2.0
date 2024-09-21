document.getElementById('cadastrarBtn').addEventListener('click', function() {

    document.getElementById('cadastrarForm').addEventListener('submit', function(event) {
        event.preventDefault();
        // Lógica para submeter o formulário
    });
    document.getElementById('cadastrarForm').onsubmit = function() {
        var name = document.getElementById('nome')
        var username = document.getElementById('username')
        var email = document.getElementById('email')
        var senha = document.getElementById('senha').value;
        var confirmarSenha = document.getElementById('confirmarSenha').value;
        if(name === "" || username === "" || email ===  "" || senha === "" || confirmarSenha === ""  ){
            alert('Preencha todos os campos obrigatórios!!')
            return false;
        }
        if (senha !== confirmarSenha) {
            alert('A confirmação de senha é diferente da senha!');
            return false; // Impede o envio do formulário se as senhas não coincidirem
        }
    }; 
});


