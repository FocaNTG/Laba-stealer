//const { Client, IntentsBitField, CategoryChannel } = require('discord.js');
import { Kawaii } from "kawaii-api";
import { Client, IntentsBitField, CategoryChannel, EmbedBuilder, Embed } from 'discord.js';
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
import { Server } from 'http';
import { NONAME } from "dns";
config();
console.log("Valid")

client.on('ready', () => {
    console.log(`${client.user.tag}としてログインしています`);
});

// stuff for when bot joins (setup for each server!)

const prefix = ';';
const api = new Kawaii("1091036373940699347.dzdBAc0zYEMcwnpvs5Fb");

client.on('ready', () => {
  console.log(`commands initialized...`);
});

client.on('messageCreate', (message) => {
  if (!message.content.startsWith(prefix) || message.author.bot) return;

  const args = message.content.slice(prefix.length).trim().split(/ +/);
  const command = args.shift().toLowerCase();

  const nopermmsg = "No permission."
  const invalidmember = "Invalid member."

  if (command === 'help') {
    message.channel.send('Pong!');
  } 

  if (command === 'ping') {
    message.channel.send('Pong!');
  } 

  else if (command === 'ban') {
    if (!message.member.permissions.has('BAN_MEMBERS')) {
      return message.channel.send(nopermmsg);
    }

    const member = message.mentions.members.first();
    if (!member) {
      return message.channel.send(invalidmember);
    }

    if (!member.bannable) {
      return message.channel.send('Member cannot be banned (maybe they are high in the hierarchy?)');
    }

    member.ban()
      .then(() => {
        message.channel.send(`banned ${member} (${member.user.id})`);
      })
      .catch((error) => {
        console.error(error);
        message.channel.send('Error (maybe i do not have permission?');
      });
  }
  else if (command === 'kick') {
    if (!message.member.permissions.has('KICK_MEMBERS')) {
      return message.channel.send(nopermmsg);
    }

    const member = message.mentions.members.first();
    if (!member) {
      return message.channel.send(invalidmember);
    }

    if (!member.kickable) {
      return message.channel.send('Member cannot be kicked (maybe they are high in the hierarchy?)');
    }

    member.kick()
      .then(() => {
        message.channel.send(`kicked ${member} (${member.user.id})`);
      })
      .catch((error) => {
        console.error(error);
        message.channel.send('Error (maybe i do not have permission?');
      });
  }
  else if (command === 'hello') {
    message.channel.send('Hello there!');
  } 

  else if (command === 'kiss') {
    const member = message.mentions.members.first();
    const mmbbrr = message.author
    if (!member) {
      return message.channel.send(invalidmember);
    }
    if (member) {
      const kissgif = '{response : }'
      api.get("gif", "kiss").then((result) => {
        // return message.channel.send(`*${mmbbrr} would kiss ${member} passionately and romantically for about 10 seconds.*${result}`);
        const embeddd = new EmbedBuilder()
	      .setTitle(`*${mmbbrr.username} kissed ${member.displayName} passionately for about 10 seconds.*`) // mmbbrr.displayName e retard la fel si member.username. la el display inseamna username...
	      .setDescription(' ')
	      .setImage(result)
        return message.channel.send({ embeds: [embeddd] });
      });
      api.endpoints("gif").then((result) => {

      });

    }
  
  else if (command === 'invite') {
    message.channel.send('https://discord.com/api/oauth2/authorize?client_id=1093504401261482025&permissions=8&scope=bot');
  } 
  else if (command === 'link') {
    message.channel.send('https://discord.com/api/oauth2/authorize?client_id=1093504401261482025&permissions=8&scope=bot');
  } 
  else if (command === 'invite link') {
    message.channel.send('https://discord.com/api/oauth2/authorize?client_id=1093504401261482025&permissions=8&scope=bot');
  }
  else if (command === 'inv') {
    message.channel.send('https://discord.com/api/oauth2/authorize?client_id=1093504401261482025&permissions=8&scope=bot');
  }


  else {
    message.channel.send('Command not found.');
  }
};
client.on('guildCreate', (TheServer) => {
  var serverid = TheServer.id
});

client.on('guildMemberAdd', (TheMember) => {
    var memberid = TheMember.id
});

});

// -------------------------------------------------------------------------------------------------------- \\

client.login(process.env.DISCORD_TOKEN);
