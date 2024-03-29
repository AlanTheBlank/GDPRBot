import discord
from discord.ext import commands
import asyncio
import datetime

client = commands.Bot(max_messages=1000000, status=discord.Status.offline, command_prefix="\\")

with open("../token.txt) as f:
	token = f.readline()
	f.close()

@client.command()
async def test(ctx):
	await ctx.send("test")

@client.command(pass_context=True)
async def compile(ctx, arg):
	await ctx.send("compiling...")
	f = open("" + arg + "_data.txt", "a+")
	f.close()
	for guild in client.guilds:
		for channel in guild.channels:
			try:
				print(channel.name)
				if channel.type == discord.ChannelType.text:
					async for message in channel.history(limit=None):
						for users in message.mentions:
							if arg == str(users.id):
								f = open("" + arg + "_data.txt", "a+")
								f.write("Author: " + str(message.author.id) + "\nServer: " + str(message.guild.name) + "\nChannel: "+ str(message.channel.name) + "\nMessage: " + str(message.content) + "\n\n---------------------------------------" + "\n\n")
								f.close()
						if arg in str(message):
							f = open("" + arg + "_data.txt", "a+")
							f.write("Author: " + str(message.author.id) + "\nServer: " + str(message.guild.name) + "\nChannel: "+ str(message.channel.name) + "\nMessage: " + str(message.content) + "\n\n---------------------------------------" + "\n\n")
							f.close()
						if len(message.attachments) > 0 and arg in str(message):
							f = open("" + arg + "_data.txt", "a+")
							f.write("Author: " + str(message.author.id) + "\nServer: " + str(message.guild.name) + "\nChannel: "+ str(message.channel.name) + "\nMessage: " + str(message.content) + "\nAttachments: " + str(message.attachments) +"\n\n---------------------------------------" + "\n\n")
							f.close()
			except:
				print("unable to read " + channel.name)
				pass
	await ctx.send("done!")

@client.command(pass_context=True)
async def delete(ctx, arg):
	await ctx.send("Deleting...")
	for guild in client.guilds:
		for channel in guild.channels:
			try:
				print(channel.name)
				if channel.type == discord.ChannelType.text:
					async for message in channel.history(limit=None):
						for users in message.mentions:
							if arg == str(users.id):
								await message.delete()
						if arg in str(message):
							await message.delete()
			except:
				pass
	await ctx.send("done!")
			
	

client.run(token)


