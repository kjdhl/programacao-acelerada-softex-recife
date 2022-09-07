const Sequelize = require('sequelize');
const sequelize = new Sequelize('teste', 'root', '12345678', {
  host: 'localhost',
  dialect: 'mysql'
});

sequelize.authenticate().then(() => {
  console.log("Conexão realizada com sucesso");
}).catch((err) => {
  console.log("Erro:" +err);
});