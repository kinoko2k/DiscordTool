import discord
import requests
import json
import time
import re

client = discord.Client()

def join(code, token):
	headers = {'authorization': f'{token}'}
	requests.post(f"https://discordapp.com/api/v6/invites/{code}", headers=headers)

def wspam(url, msg, name):
	data = {
		"username": f"{name}",
		"content": f"{msg}"
	}
	while True:
		requests.post(url, data=data)

def left(id, token):
	@client.event
	async def on_ready():
		guild = await client.fetch_guild(int(id))
		await guild.leave()
		exit()
	client.run(f"{token}", bot=False)

def spam(id, msg, token):
	@client.event
	async def on_ready():
		channel = await client.fetch_channel(int(id))
		await channel.send(f"{msg}")
	@client.event
	async def on_message(message):
		if message.content == str(msg):
			channel = await client.fetch_channel(int(id))
			await channel.send(f"{msg}")
	client.run(f"{token}", bot=False)

print("""
██████╗░██╗░██████╗░█████╗░░█████╗░██████╗░██████╗░  ████████╗░█████╗░░█████╗░██╗░░░░░
██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
██║░░██║██║╚█████╗░██║░░╚═╝██║░░██║██████╔╝██║░░██║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
██║░░██║██║░╚═══██╗██║░░██╗██║░░██║██╔══██╗██║░░██║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
██████╔╝██║██████╔╝╚█████╔╝╚█████╔╝██║░░██║██████╔╝  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗
╚═════╝░╚═╝╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝
""")

print("[1] Join flood")
print("[2] Left flood")
print("[3] Spammer")
print("[4] Webhook spammer")

select = input("> ")

if select == "1":
	invite_code = input("招待コード: ")
	tokens = open("tokens.txt", "r")
	for token in tokens:
		t = token.replace("\n", "")
		join(invite_code, t)
elif select == "2":
	guild_id = input("サーバーID: ")
	tokens = open("tokens.txt", "r")
	for token in tokens:
		t = token.replace("\n", "")
		left(guild_id, t)
elif select == "3":
	channel_id = input("チャンネルID: ")
	message = input("送信メッセージ: ")
	tokens = open("tokens.txt", "r")
	for token in tokens:
		t = token.replace("\n", "")
		spam(channel_id, message, t)
elif select == "4":
	webhook_url = input("WebhookURL: ")
	message = input("送信メッセージ: ")
	name = input("Webhookの名前: ")
	wspam(webhook_url, message, name)
else:
	print("番号が無効です。")
	print("10秒後にプログラムが終了します。")
	time.sleep(10)
	exit()