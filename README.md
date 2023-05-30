# iyashi

"iyashi" is a slack bot that randomly returns the pictures of animals you posted.

When you post a picture of an animal, it will be automatically classified and registered.

If you have a heroku account, you can use it without coding.

![example](./example.gif)

## What is "iyashi"

"iyashi" is a Japanese word meaning "soothing" or "healing" mentally and physically.

We need "iyashi", let's get "iyashi"!

## Requirements

- Heroku account
- Slack
- Microsoft Azure Custom Vision API

You need to invite slack bot to the channel you want "iyashi".

## Usage

Click "Deploy to Heroku" Button and enter your environment valiables.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Supported animals

- cat
  - cat
  - nyan
  - にゃーん
  - ニャーン
- chinchilla
  - chinchilla
  - チンチラ
  - ちんちら
- dog
  - dog
  - wanwan
  - わんわん
  - ワンワン
- hedgehog
  - hedgehog
  - ハリネズミ
  - はりねずみ
- owl
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
