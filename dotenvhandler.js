// module.exports = "MTA5MzUwNDQwMTI2MTQ4MjAyNQ.G-81qd.9dcRN0S4kqdipsnZ6t1FAFBkxfEo7CRMOSjVQc"

require("dotenv").config();

discordToken = process.env.DISCORD_TOKEN,
discordClientId = process.env.CLIENT_ID,
shouldCreateCommands = process.env.SHOULD_CREATE_COMMANDS === 'true',
dbHost = process.env.DB_HOST,
postgresUser = process.env.POSTGRES_USER,
postgresDb = process.env.POSTGRES_DB,
postgresPassword = process.env.POSTGRES_PASSWORD,
forceDbReset = process.env.FORCE_DB_RESET === 'false'

module.exports = {
  discordToken: process.env.DISCORD_TOKEN,
  discordClientId: process.env.CLIENT_ID,
  shouldCreateCommands: process.env.SHOULD_CREATE_COMMANDS === 'true',
  dbHost: process.env.DB_HOST,
  postgresUser: process.env.POSTGRES_USER,
  postgresDb: process.env.POSTGRES_DB,
  postgresPassword: process.env.POSTGRES_PASSWORD,
  forceDbReset: process.env.FORCE_DB_RESET === 'false'
};