import discord
from discord import app_commands
import os

TESTING_GUILD = discord.Guild(id=989025229781205002)

intents = discord.Intents.default()

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
  game = discord.Game("Games")
  await client.change_presence(status=discord.Status.online, activity=game)
  for i in os.listdir("cogs"):
    if i[-3:] == ".py" and i[0] != "-":
      print(f"Loading cogs.{i[:-3]} ...")
      await client.load_extension(f"cogs.{i[:-3]}")
  print(f"Logged in as {client.user} (ID: {client.user.id})")


if __name__ == "__main__":
  with open("bottoken.gmv", "r") as f:
    bottoken = f.read()
  client.run(bottoken)