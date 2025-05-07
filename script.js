function buscarReceita() {
    console.log("Passei por aqui")
    fetch("http://127.0.0.1:5000/receita")
        .then(response => response.json())
        .then(data => {
            // Exibir ingredientes
            document.getElementById("ingredientes").innerHTML =
                data.ingredientes.map(item => `<li>${item}</li>`).join("");

            // Exibir modo de preparo
            document.getElementById("modo").innerHTML =
                data.modo_de_preparo.map(passo => `<li>${passo}</li>`).join("");

            // Mostrar a seção da receita
            document.getElementById("receita").classList.remove("oculto");
        })
        .catch(() => alert("Erro ao buscar a receita! Certifique-se de que o servidor está rodando."));
}