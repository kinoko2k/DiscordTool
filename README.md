# DiscordTool
簡単にWebhookのスパムや一斉参加、退出等の基本動作ができます。

# 動作環境
Python 3.8.9(Path登録済み)

# 特徴
- 軽量
- 多機能
- わかりやすいUI
- Proxyをサポート
- SelfBotをサポート
- エラーメッセージあり

# Tokenの設定方法
Tokenはtokens.txtに1行ずつ書いていってください。
Example:
```
abc
abc
abc
```
NG:
```
abcabcabc
```
そしてTokenはBotTokenではなくUserTokenである必要があります。
もしTokenの先端に「mfa」とついていたらそれも含めてください。
Example:
```
mfa.abc
```

# HTTPのProxy設定方法
ProxyのHTTPはhttp-proxy.txtに1行ずつ書いていってください。
Example:
```
http://111.111.111.111:80
```
必ず「http」と「:80」は入れてください。
「:80」はProxyのポート番号にしてください。
Example:
```
http://111.111.111.111:8080
```

#HTTPSのProxy設定方法
ProxyのHTTPSはHTTPとほぼ同じです。
httpをhttpsにして、ポートをそのProxyの物に変更するだけです。
ただhttps-proxy.txtに保存してください。


# 一斉参加の招待コード
NG例

```
discord.gg/example
```
OK例
```
example
```
「discord.gg/」以降のランダムなアルファベットのコード。

# できること
- Join flood
- Left flood
- Spam
- Webhook spam
- Token info view
- Nitro generate
- Nitro active check

# 必要ライブラリ
- discord.py
- requests
- string
- secrets
- random
- json
- time
- re
- rich

# ライブラリの役割
- discord.py = SpammerやLeave floodに使用(API使用)
- requests = Join floodやNitro checkerに使用(JsonAPI使用)
- string = Nitro generatorに使用
- secrets = Nitro generatorに使用
- random = Proxyのリスト変数の内容シャッフルに使用
- json = JsonAPIの内容を解析、jsonデータ取得に使用
- time = 数秒間の待機(10秒後にプログラムを終了させる際など)に使用
- re = replaceに使用
- rich = コンソール出力の色付け等に使用

# DiscordToolAPI - 使用準備
APIを使用するにはまずインポートする必要があります。
DiscordToolAPI.pyを同じディレクトリに入れてimportします。
```python
import DiscordToolAPI.py as DTAPI
```
これで使えるようになりました。
```python
as DTAPI
```
はDTAPIでpyファイルの関数等を呼び出せるようにするものです。

# DiscordToolAPI - InviteAPI
InviteAPIは招待リンクの情報を確認したりTokenを使いユーザーを参加させたりできます。
```python
DTAPI.join(code, token)
```
codeは招待リンクのコードです。
```
discord.gg/Example
```
この場合Exampleに当たります。
もしコードがExampleの情報を見たければ
```python
DTAPI.join(Example)

```
になります。
もしabcと言うTokenを持っている人にExampleと言うコードのサーバーに参加してほしい場合
```python
DTAPI.join(Example, abc)
```
となります。

# DiscordToolAPI - SendWebhook
Webhookをもっと簡単に送信できるようにします。
```python
wsend(url, data)
```
です。
データは自分で設定する必要があります。
構文は
```python
data = {
  "content": "test"
}
```
となります。
usernameやavatarの指定は
```python
"username": "name",
"avatar_url": "url"
```
となります。
最終的な構文は
```python
data = {
  "content": "Webhook Send API",
  "username": "Discord Tool"
}
wsend("discordapp.com/URL", data=data)
```
となります。

# DiscordToolAPI - TokenCheck
Tokenをチェックすることができます。
登録情報や基本的な情報まで!
```python
check(token)
```
簡単ですね。
例えばabcと言うtokenを調べたければ
```python
check("abc")
```
となります。

# DiscordToolAPI - DisableToken
簡単にTokenを無効にできます。
構文はこれも簡単で
```python
disable(invite, token)
```
です。
実はinvitecodeつまりjoin()と同じコードが必要になります。
例えば招待コードが
```
discord.gg/Example
```
であれば「Example」の部分がコードになります。
そしてTokenはUserTokenです。
なのでExampleと言う招待コードのサーバーでabcと言うTokenを無効にする場合
```python
disable(Example, abc)
```
となります。
ただ成功してもなんのレスポンスもないので注意。
