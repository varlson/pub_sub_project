const express = require("express");
const app = express();

app.get("/", (req, res) => {
  res.send({ message: "Ola Mundo" });
});

app.listen(7888, () => {
  console.log("Rodando na porta 7888");
});
