function myName() {
    var name = document.getElementById('nome');
    name.value = name.value.toUpperCase();
    
}

function onlyLetters() {
    var name = document.getElementById('nome');
    var letters = /^[a-zA-Z\s]*$/;
    if(name.value.match(letters))
        {
        return true;
        }
    else
        {
        alert('Nomes devem conter apenas letras');
        name.value = ''
        return false;
        }
}

function minEight() {
    var idade = document.getElementById('idade');
    var numbers = /\b([1-9]|[1-9][0-9]|1[01][0-9]|12[0-0])\b/;
    if (idade.value.match(numbers)) {
        return true;
    } 
    else {
        idade.value = ''
        alert('Idade deve conter apenas números e ser menor que 120');
    }
}

function confirmarSenha(){
    var senha = document.getElementById('senha').value
    var confirma = document.getElementById('confsenha').value
    if (confirma.length != 0) {
        if(senha === confirma){
            return true
        } else{
            alert('Senhas diferentes')
            senha.value=''
            return false
        }
    }
}

function contarCaracteres(){
    var senha = document.getElementById('senha').value
    var tamanho = senha.length

    if (tamanho != 0 && tamanho < 8) {
        senha.value = ''
        alert('senha precisa ter no mínimo 8 caracteres')
    }
    else {
        return true
    }
}
