# DiscordTool
簡単にWebhookのスパムや一斉参加、退出等の基本動作ができます。

# 特徴
- 軽量
- 多機能
- わかりやすいUI
- Proxyをサポート
- SelfBotをサポート
- エラーメッセージあり

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

# DiscordToolAPI
Coming Soon
