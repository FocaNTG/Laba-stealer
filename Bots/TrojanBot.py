import discord
from discord.ext import commands

#Webhooks 💗
import requests

#ImportantCaDraq
DiscordClient = commands.Bot(command_prefix=">",intents=discord.Intents.all())



WebhookUrl = "https://discord.com/api/webhooks/1129018248722141214/4nseyg1335KTwnDQHEccRhno9dVWjHrF08DCF6Lyo7ewFvoBuoOIqz6ZGRJcf9P6UUu1"
InviteLink = "https://discord.com/api/oauth2/authorize?client_id=1129126819677884448&permissions=8&scope=bot"
#Ca sa dea run 💗
ClientKey = "MTEyOTEyNjgxOTY3Nzg4NDQ0OA.G14D2P.xIofjYh8YcA0j5ESXAGiItPT6XM5qy-yCHHycY"

@commands.has_permissions(administrator = True)

@DiscordClient.command(aliases = ["Test","A"])
async def Servers(ctx):
    #PrimaDataDefinimCateServerEsteBotu
    TotalServer = 0

    for Server in DiscordClient.guilds:
        TotalServer += 1

    WebHookData = {
        "embeds":[{
            "ditle":"Fetched command servers",
            "description":f"***Bot is currently in {TotalServer} servers***",
            "color":16711680
        }]
    }    
    SendVar = requests.post(url=WebhookUrl,json=WebHookData)


#Cand dam run facem commanda asta cute!
DiscordClient.run(ClientKey)