alert('Olá mundo!')
console.log('Olá')
var my_var;
my_var = 'Olá, pessoal';
alert(my_var)
my_var = 5;
alert(my_var)
my_var = [1, 10, 'Olá', true];
alert(my_var)


if (my_var%2 == 0){
    alert('Número par');
}
else if (my_var%2 == 1){
    alert('Número ímpar');
}
else{
    alert('Valor inválido');
}


var i;
for (i = 0; i < 4; i++){
    alert(i)
}
var i;
i = 0;
while (i < 4){
    alert(i)
    i++
}

var nome = prompt("Digite seu nome: ");
alert("Olá " + nome);