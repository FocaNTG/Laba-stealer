//const { Client, IntentsBitField, CategoryChannel } = require('discord.js');
import { Client, IntentsBitField, CategoryChannel } from 'discord.js';
const client = new Client({
    intents: [
        IntentsBitField.Flags.Guilds,
        IntentsBitField.Flags.GuildMembers,
        IntentsBitField.Flags.MessageContent,
        IntentsBitField.Flags.GuildInvites,
        IntentsBitField.Flags.GuildEmojisAndStickers,
        IntentsBitField.Flags.DirectMessages,
        IntentsBitField.Flags.GuildMessages,
        IntentsBitField.Flags.AutoModerationExecution,
        IntentsBitField.Flags.AutoModerationConfiguration
    ]
})
import { config } from 'dotenv';
config();
console.log("Valid")

client.on('ready', () => {
    console.log(`${client.user.tag}としてログインしています`); // sa se stie ca a puscat botul
});

// stuff for when bot joins (setup for each server!)

const prefix = ',';

client.on('ready', () => {
  console.log(`commands initialized...`); // sa se stie ca a puscat pana aci ca aveam ceva probleme
});

client.on('messageCreate', (message) => {
  if (!message.content.startsWith(prefix) || message.author.bot) return;

  const args = message.content.slice(prefix.length).trim().split(/ +/);
  const command = args.shift().toLowerCase();

  if (command === 'ping') {
    message.channel.send('Pong!');
  } 
  else if (command === 'hello') {

  }
  else if (command === 'ban') {
    if (!message.member.permissions.has('BAN_MEMBERS')) {
      return message.channel.send('NO PERM AHAHH NYA NYA');
    }

    const member = message.mentions.members.first();
    if (!member) {
      return message.channel.send('mention a valid member nya');
    }

    if (!member.bannable) {
      return message.channel.send('member got big rank or sum idk');
    }

    member.ban()
      .then(() => {
        message.channel.send(`banned ${member.user.tag} (${member.user.id})`);
      })
      .catch((error) => {
        console.error(error);
        message.channel.send('didnt work');
      });
  }
  else if (command === 'kick') {
    if (!message.member.permissions.has('KICK_MEMBERS')) {
      return message.channel.send('NO PERM AHAHH NYA NYA');
    }

    const member = message.mentions.members.first();
    if (!member) {
      return message.channel.send('mention a valid member nya');
    }

    if (!member.kickable) {
      return message.channel.send('member got big rank or sum idk');
    }

    member.kick()
      .then(() => {
        message.channel.send(`kicked ${member.user.tag} (${member.user.id})`);
      })
      .catch((error) => {
        console.error(error);
        message.channel.send('didnt work');
      });
  }
  else if (command === 'hello') {
    message.channel.send('Hello there!');
  } else {
    message.channel.send('Command not found.');
  }
});
client.on('guildCreate', (TheServer) => {
    var ServerID = TheServer.id
    
});

client.on('guildMemberAdd', (TheMember) => {
    
});


// -------------------------------------------------------------------------------------------------------- \\ mai sus iti bagi codul tau frumos

client.login(process.env.DISCORD_TOKEN); // la final trebuie frumusetea asta :3
