// Calcolatrice JavaScript

function somma(a, b) {
    return a + b;
}

function sottrazione(a, b) {
    return a - b;
}

function moltiplicazione(a, b) {
    return a * b;
}

function divisione(a, b) {
    if (b !== 0) {
        return a / b;
    } else {
        return "Errore: divisione per zero!";
    }
}

// Test
const x = 100;
const y = 25;

console.log("🧮 CALCOLATRICE JAVASCRIPT");
console.log("=".repeat(40));
console.log(`Numero 1: ${x}`);
console.log(`Numero 2: ${y}`);
console.log("");
console.log(`${x} + ${y} = ${somma(x, y)}`);
console.log(`${x} - ${y} = ${sottrazione(x, y)}`);
console.log(`${x} × ${y} = ${moltiplicazione(x, y)}`);
console.log(`${x} ÷ ${y} = ${divisione(x, y)}`);
console.log("");
console.log("✅ Calcolatrice funziona!");