// Il mio primo programma Node.js
console.log("🚀 Hello from Node.js!");
console.log("================================");

// Variabili (come in Python)
const nome = "Mario";
const eta = 25;

console.log(`Mi chiamo ${nome} e ho ${eta} anni.`);

// Array (come liste Python)
const numeri = [1, 2, 3, 4, 5];
console.log("\nNumeri:", numeri);

// Funzione (come def in Python)
function somma(a, b) {
    return a + b;
}

const risultato = somma(10, 20);
console.log(`\n10 + 20 = ${risultato}`);

// Loop (come for in Python)
console.log("\nTabellina del 5:");
for (let i = 1; i <= 5; i++) {
    console.log(`5 × ${i} = ${5 * i}`);
}

console.log("\n✅ Node.js funziona perfettamente!");