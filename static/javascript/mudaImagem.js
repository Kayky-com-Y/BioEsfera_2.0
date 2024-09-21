let indiceImagem = 0;
const imagens = ['../assets/images/RabanetoBuriti.gif', 'assets/images/baoba.png', 'img3.jpg'];

export function proximaImagem() {
    indiceImagem++;
    if (indiceImagem >= imagens.length) {
        indiceImagem = 0;
    }
    document.getElementById('minhaImagem').src = imagens[indiceImagem];
}

export function imagemAnterior() {
    indiceImagem--;
    if (indiceImagem < 0) {
        indiceImagem = imagens.length - 1;
    }
    document.getElementById('minhaImagem').src = imagens[indiceImagem];
}