function Banco(conta, saldo, tipoConta, agencia)
{
    this.conta=conta;
    this.saldo=parseFloat(saldo);
    this.tipoConta=tipoConta;
    this.agencia=agencia;

    //metodo que retorna o saldo da conta:nomeDoObjeto.buscarSaldo()
    this.buscarSaldo = ()=>{return`Saldo:${this.saldo} R$`};
    
    //metodo para fazer um deposito na conta, como paramentro o valor a ser depositado:nomeDoObjeto.deposito(valor)
    this.deposito = (valor)=>{
        this.saldo+=parseFloat(valor)
        return `Novo saldo da conta:${this.saldo} R$`
    };
    
    //metodo para fazer um saque na conta, como paramentro o valor a ser sacado:nomeDoObjeto.saque(valor)
    this.saque = (valor)=>{
        if(parseFloat(valor)>this.saldo){
            return `Operação invalida, valor desejado superior ao saldo disponivel`
        }else{
            this.saldo-=parseFloat(valor);
            return `Saque de ${valor} R$ realizado. Novo saldo:${this.saldo} R$`
        } 
    }

    //metodo que retorna o numero da conta:nomeDoObjeto.numeroConta()
    this.numeroConta = () =>{return`O numero da conta é: ${this.conta} R$`}
}
    

//criando o objeto:  let novoBanco = new Banco(conta,saldo,tipoDeConta, agencia)
