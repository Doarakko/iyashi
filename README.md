# iyashi

"iyashi" is a slack bot that randomly returns the pictures of animals you
posted.

When you post a picture of an animal, it will be automatically classified and
registered.

![example](./example.gif)

## What is "iyashi"

"iyashi" is a Japanese word meaning "soothing" or "healing" mentally and
physically.

We need "iyashi", let's get "iyashi"!

## Requirements

- Slack
- Microsoft Azure Custom Vision API

You need to invite slack bot to the channel you want "iyashi".

## Supported animals

- cat
  - にゃーん
  - ニャーン
- chinchilla
  - チンチラ
  - ちんちら
- dog
  - わんわん
  - ワンワン
- hedgehog
  - ハリネズミ
  - はりねずみ
- owl
  - フクロウ
  - ふくろう
  - ほーほー
  - ホーホー

Please create an issue if you have any animals you would like to see supported!

## Run on local

```sh
docker-compose up --build
```

### Add file manually

```sh
docker exec -it iyashi_app python scripts/add.py -a <animal> -u <image url>
```

### Delete file manually

```sh
docker exec -it iyashi_app python scripts/delete.py -u <image url>
```
