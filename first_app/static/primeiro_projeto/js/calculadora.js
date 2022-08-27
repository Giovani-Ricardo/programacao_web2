function calcular(texto) {
    let operadores = ['+', '-', '/', '*']
    let operador;
    let resultado;

    for (i in texto) {
        if (operadores.includes(texto[i])) {
            operador = texto[i];
        }
    }

    let op = texto.split(operador)
    console.log(operador)

    switch (operador) {
        case '+':
            resultado = parseFloat(op[0]) + parseFloat(op[1])
            break
        case '-':
            resultado = parseFloat(op[0]) - parseFloat(op[1])
            break
        case '*':
            resultado = parseFloat(op[0]) * parseFloat(op[1])
            break
        case '/':
            resultado = parseFloat(op[0]) / parseFloat(op[1])
            break
    }

    return resultado
}


function passaValor(tipo, valor) {

    if (tipo === 'operador') {
        let operadores = ['.', '+', '-', '*', '/', 'CE', 'C', '+/-'];
        /* 
        if(valor === 'c'){
          document.getElementById('resultado').value = ''
        }
        */
        let visor = document.getElementById('visor');

        if (valor === '=') {
            //var valor_campo = eval(visor.value)
            valor_campo = calcular(visor.value, operadores)
            visor.value = valor_campo
        } else if (!operadores.includes(valor)) {

            let ultima_letra = visor.value[visor.value.length - 1];

            if (!operadores.includes(ultima_letra)) {
                visor.value += valor
            }

        } else if (valor === '+/-') {

            visor.value = visor.value * -1;

        } else if (valor === 'backspace') {

            visor.value = visor.value.slice(0, -1)

        } else {

            visor.value = '0'
        }

        /*
        if(valor === '*' || valor === '-' || valor === '+' || valor === '/' || valor === '.'){
          document.getElementById('resultado').value += valor
        }

        if(valor === '='){
          var valor_campo = eval(document.getElementById('resultado').value)
          document.getElementById('resultado').value = valor_campo
        }
        */

    }
    if (tipo === 'valor') {
        let elemento = document.getElementById('visor');
        if (elemento.value === '0') {
            elemento.value = valor;
        } else if (!(elemento.value.includes('.') && valor === '.')) {
            elemento.value += valor;
        }

    }
}


document.addEventListener("keyup", function(e) {

    let valores = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']
    let operadores = ['/', '*', '-', '+', '.', 'Enter']
    tecla = e.key;

    let visor = document.getElementById('visor')

    if (valores.includes(tecla)) {
        passaValor('valor', tecla)
    } else if (operadores.includes(tecla)) {
        if (tecla === 'Enter') {
            console.log('entrou')
            tecla = '='
            passaValor('operador', tecla)
        } else {
            passaValor('valor', tecla)
        }

    }
})