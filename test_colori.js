// Importa chalk
const chalk = require('chalk');

// Testo colorato!
console.log(chalk.blue('Questo testo è BLU! 🔵'));
console.log(chalk.red('Questo testo è ROSSO! 🔴'));
console.log(chalk.green('Questo testo è VERDE! 🟢'));
console.log(chalk.yellow('Questo testo è GIALLO! 🟡'));

// Combinazioni
console.log(chalk.bold.bgGreen.black(' SUCCESSO! '));
console.log(chalk.underline.cyan('Testo sottolineato azzurro'));

// Emoji + colori
console.log(chalk.magenta('🎨 npm e Node.js funzionano alla perfezione!'));