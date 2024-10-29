function somaNum() {
    var x = document.getElementById('n1');
    var y = document.getElementById('n2');

    soma = parseInt(x.value) + parseInt(y.value);
    alert( x.value + '+' + y.value + '=' + soma);
}

function subNum() {
    var x = document.getElementById('n1');
    var y = document.getElementById('n2');

    sub = parseInt(x.value) - parseInt(y.value);
    alert( x.value + '-' + y.value + '=' + sub);
}

function multNum() {
    var x = document.getElementById('n1');
    var y = document.getElementById('n2');

    mult = parseInt(x.value) * parseInt(y.value);
    alert( x.value + '*' + y.value + '=' + mult);
}

function divNum() {
    var x = document.getElementById('n1');
    var y = document.getElementById('n2');
    if (y.value == 0) {
        alert('impossivel dividir por 0')
    }
    else {
    div = parseInt(x.value) / parseInt(y.value);
    alert( x.value + '/' + y.value + '=' + div);
    }
}