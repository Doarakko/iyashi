import io
import os
from time import time

import requests
import torch
import torch.nn as nn
import torchvision
from PIL import Image
from torch.nn import functional as F
from torchvision import transforms

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

CLASS_NAMES = ["cat", "chinchilla", "dog", "hedgehog", "owl"]


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


model = torchvision.models.resnet18()
model.fc = nn.Linear(model.fc.in_features, len(CLASS_NAMES))
model.load_state_dict(torch.load("model.pth"))
model.eval()


transformer = transforms.Compose(
    [
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
    ]
)


def predict(url):
    try:
        responce = requests.get(
            url,
            headers={"Authorization": f'Bearer {os.environ["SLACK_BOT_TOKEN"]}'},
            stream=True,
            timeout=5,
        )
        img = Image.open(io.BytesIO(responce.content)).convert("RGB")

        return _predict(img)
    except Exception as e:
        print(e)


def _predict(img):
    inputs = transformer(img)
    inputs = inputs.unsqueeze(0).to("cpu")

    outputs = model(inputs)

    batch_probs = F.softmax(outputs, dim=1)
    batch_probs, batch_indices = batch_probs.sort(dim=1, descending=True)

    return CLASS_NAMES[batch_indices[0][0]]
