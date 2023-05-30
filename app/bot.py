import logging
import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

import animal
from db import Database
from file import File

logging.basicConfig(level=logging.WARNING)

app = App(token=os.environ["SLACK_BOT_TOKEN"])

NO_PICTURE_MESSAGE = f'Please post pictures on <#{os.environ["IMAGE_UPLOADED_CHANNEL"]}> and it will be registered automatically!'


@app.event("app_mention")
def mention(say):
    try:
        row = file.get_by_random()
        say(row.url)
    except Exception:
        say(NO_PICTURE_MESSAGE)


@app.message("^iyashi$")
def iyashi(say):
    try:
        row = file.get_by_random()
        say(row.url)
    except Exception:
        say(NO_PICTURE_MESSAGE)


@app.message("^(にゃーん|ニャーン)$")
def cat(say):
    try:
        row = file.get_by_animal(animal.CAT)
        say(row.url)
    except Exception:
        say(NO_PICTURE_MESSAGE)


@app.message("^(わんわん|ワンワン)$")
def dog(say):
    try:
        row = file.get_by_animal(animal.DOG)
        say(row.url)
    except Exception:
        say(NO_PICTURE_MESSAGE)


@app.message("^(チンチラ|ちんちら)$")
def chinchilla(say):
    try:
        row = file.get_by_animal(animal.CHINCHILLA)
        say(row.url)
    except Exception:
        say(NO_PICTURE_MESSAGE)


@app.message("^(ハリネズミ|はりねずみ)$")
def hedgehog(say):
    try:
        row = file.get_by_animal(animal.HEDGEHOG)
        say(row.url)
    except Exception:
        say(NO_PICTURE_MESSAGE)


@app.message("^(フクロウ|ふくろう|ほーほー|ホーホー)$")
def owl(say):
    try:
        row = file.get_by_animal(animal.OWL)
        say(row.url)
    except Exception:
        say(NO_PICTURE_MESSAGE)


@app.event("file_shared")
def post(body, client, say):
    channel_id = body["event"]["channel_id"]
    if channel_id != os.environ["IMAGE_UPLOADED_CHANNEL"]:
        return

    res = client.files_info(file=body["event"]["file_id"])
    label = animal.predict(res["file"]["url_private_download"])
    file.add(res["file"]["permalink"], label)

    shares = res["file"]["shares"]
    for i in shares["private"].keys():
        res = client.reactions_add(
                channel=channel_id,
                name=label,
                timestamp=shares["private"][i][0]["ts"]
        )


if __name__ == "__main__":
    Database.initialise()
    try:
        file = File()
        file.create_table()
    except Exception:
        pass

    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()
