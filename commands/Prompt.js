const {SlashCommandBuilder} = require('discord.js');

const spawn = require("child_process").spawn;
const pythonProcess = spawn('python',['main.py','3D representation of a AIDS virus with blue background , 8-bit style.']);

module.exports = {
    data: new SlashCommandBuilder()
        .setName('createprompt')
        .setDescription('Creates a prompt'),
    async execute(interaction) {
        await interaction.reply('Prompt created!');
    }
}