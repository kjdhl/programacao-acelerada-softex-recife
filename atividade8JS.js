function sinais (){
    return ['+','-','*','/']
}
const op=sinais()
const calc = (op,num1, num2) => eval(`${num1} ${op} ${num2}`);


function resultado(op,num){
  let string = `(${op}):Resultado = ${num.toFixed(2)}`;
  return string;

}
//realizando as 4 operações fundamentais com 10 e 1.5
console.log(resultado(op[0],calc(op[0], 10, 1.5)));
console.log(resultado(op[1],calc(op[1], 10, 1.5)));
console.log(resultado(op[2],calc(op[2], 10, 1.5)));
console.log(resultado(op[3],calc(op[3], 10, 1.5)));