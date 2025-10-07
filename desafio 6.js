let valor = 5;
let elemento = document.getElementById("status");

if (valor === 10) {
    elemento.innerText = "A condição é sempre verdadeira! (Bug de Lógica)";
} else {
    elemento.innerText = "A condição é falsa.";
}