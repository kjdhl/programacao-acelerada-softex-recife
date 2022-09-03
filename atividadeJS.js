function listarPropriedades(objeto){
    for(let propriedades in objeto){
        console.log(`${propriedades}:${objeto[propriedades]}`);
    };
};
function listarElementos(array){
    for(let elementos of array){
        console.log(elementos);
    };
};



let carros = ["Ferrari", "Honda", "Ford", "Fiat"];

function pessoa(nome, idade, cidade, id){
    this.nome = nome;
    this.idade = idade;
    this.cidade = cidade;
    this.id = id
};
let novaPessoa = new pessoa("Karlos",23,"Petrolina", 123456789);

listarPropriedades(novaPessoa);
listarElementos(carros);