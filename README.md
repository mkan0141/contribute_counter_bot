# contribute_counter_bot
contribute_counter_botは1日のcontribute数とその月の総contribute数をつぶやいてくれるtwitter botです．

# 使い方

1. インストールする
```bash
git clone https://github.com/mkan0141/contribute_counter_bot
```

2. 設定ファイルを編集する
ディレクトリ構成は以下のようになっており，config.pyを編集してください．  twitter apiを叩くのでAPI Keyを取得してください．
```txt
├── README.md
├── __pycache__
│   └── config.cpython-36.pyc
├── config
│   ├── __init__.py
│   ├── __pycache__
│   └── config.py <- こいつを編集する
└── main.py
```

例

```python
CONSUMER_KEY = "FSjfkjafwelfjkwlafkhflekjfeawlfjelw"
CONSUMER_KEY_SECRET = "FjfjekfFjfwJFajffefaeafhljefs"
ACCESS_TOKEN = "4324832104898490248-fjfjwklejaeklwejklwsjl"
ACCESS_TOKEN_SECRET = "r23jrx3qporjx3oiqrpiwrwexjorij"

GITHUB_USER_ID="mkan0141"
```
