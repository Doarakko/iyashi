import io
import os
from time import time

import requests

DOG = "dog"
CAT = "cat"
HEDGEHOG = "hedgehog"
OWL = "owl"
CHINCHILLA = "chinchilla"

DOG_EMOJI = "dog2"
CAT_EMOJI = "cat2"
HEDGEHOG_EMOJI = "hedgehog"
OWL_EMOJI = "owl"
CHINCHILLA_EMOJI = "mouse2"
UNDEFINED_EMOJI = "question"


def get_emoji(label=None):
    if label == DOG:
        return DOG_EMOJI
    elif label == CAT:
        return CAT_EMOJI
    elif label == CHINCHILLA:
        return CHINCHILLA_EMOJI
    elif label == HEDGEHOG:
        return HEDGEHOG_EMOJI
    elif label == OWL:
        return OWL_EMOJI
    else:
        return UNDEFINED_EMOJI


def predict(url):
    try:
        responce = requests.get(
            url,
            headers={"Authorization": f'Bearer {os.environ["SLACK_BOT_TOKEN"]}'},
            stream=True,
            timeout=5,
        )
        img = io.BytesIO(responce.content)

        return _predict(img)
    except Exception as e:
        print(e)


def _predict(img):
    try:
        responce = requests.post(
            os.environ["ANIMAL_PREDICTION_API"],
            headers={
                "Prediction-Key": os.environ["ANIMAL_PREDICTION_API_KEY"],
                "Content-Type": "application/octet-stream",
            },
            timeout=5,
            data=img,
        )
        json = responce.json()

        return json["predictions"][0]["tagName"]
    except Exception as e:
        print(e)
