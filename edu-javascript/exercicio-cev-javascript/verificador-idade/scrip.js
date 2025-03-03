textoResult.innerHTML = ""

function verificar() {
    var anoAtual = new Date().getFullYear()
    var recebeData = document.getElementById('numtxt').value

    var textoResult = document.getElementById('resultado-text')
    var sexo = document.querySelector('input[name="radioes"]:checked')
    var imagem = document.getElementById('imagem')

    if (!recebeData || !sexo) {
        textoResult.innerHTML = "Por favor, insira os dados!"
        imagem.src = ""
        return
    }
    
    if (recebeData.length !== 4) {
        textoResult.innerHTML = "Só serão aceitos 4 números."
        imagem.src = ""
        return
    }

    var calculaIdade = anoAtual - recebeData
    
    if (calculaIdade < 0) {
        textoResult.innerHTML = "Por favor, Insira uma data válida"
        imagem.src = ""
        return
    }

    if (sexo.value === "Feminino" && calculaIdade <= 15) {
        textoResult.innerHTML = `Menina de ${calculaIdade} anos.`
        imagem.src = 'images-p/crianca-mulher.jpg'
    } else if (sexo.value === "Feminino" && calculaIdade > 15 && calculaIdade <= 25) {
        textoResult.innerHTML = `Adolescente de ${calculaIdade} anos.`
        imagem.src = 'images-p/jovem-mulher.jpg'
    } else if (sexo.value === "Feminino" && calculaIdade > 25 && calculaIdade <= 49) {
        textoResult.innerHTML = `Adulta de ${calculaIdade} anos.`
        imagem.src = 'images-p/adulto-mulher.jpg'
    } else if (sexo.value === "Feminino" && calculaIdade > 49 && calculaIdade <= 100) {
        textoResult.innerHTML = `Idosa ${calculaIdade} anos.`
        imagem.src = 'images-p/idosa-mulher.jpg'
    } else if (sexo.value === "Masculino" && calculaIdade <= 15) {
        textoResult.innerHTML = `Menino de ${calculaIdade} anos.`
        imagem.src = 'images-p/crianca-homem.jpg'
    } else if (sexo.value === "Masculino" && calculaIdade > 15 && calculaIdade <= 25) {
        textoResult.innerHTML = `Adolescente de ${calculaIdade} anos.`
        imagem.src = 'images-p/jovem-homem.jpg'
    } else if (sexo.value === "Masculino" && calculaIdade > 25 && calculaIdade <= 45) {
        textoResult.innerHTML = `Adulto de ${calculaIdade} anos.`
        imagem.src = 'images-p/adulto-homem.jpg'
    } else if (sexo.value === "Masculino" && calculaIdade > 45 && calculaIdade <= 100) {
        textoResult.innerHTML = `Idoso ${calculaIdade} anos.`
        imagem.src = 'images-p/idoso-homem.jpg'
    }
}

window.onload = verificar