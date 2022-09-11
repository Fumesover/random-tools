#! /usr/bin/env python3

import json
import requests
import os
import sys
from PIL import Image
from typing import Generator, Iterator, Any


def fetch_1(uuid: str) -> Any:
    response = requests.get('https://widgetviewer.api.photoconnector.net/' + uuid)
    response.raise_for_status()
    return response.json()


def fetch_all(uuid: str) -> Iterator[str]:
    os.makedirs(uuid, exist_ok=True)
    for idx, url in enumerate(fetch_1(uuid)['pages']):
        filename = url.split('?')[0].split('/')[-1]

        if filename == 'flysheet.jpg':
            continue

        print(f'Fetching {filename} ...')

        response = requests.get(url)
        response.raise_for_status()

        with open(f'{uuid}/{filename}', 'wb') as f:
            f.write(response.content)

        yield f'{uuid}/{filename}'


def to_pdf(uuid: str) -> str:
    pics_list = fetch_all(uuid)

    path = f'{uuid}.pdf'
    print(f"Generating {path}...")

    pics = list(map(lambda path: Image.open(path).convert('RGB'), pics_list))

    header = pics.pop(0)
    header.save(path, save_all=True, append_images=pics)

    return path


if __name__ == '__main__':
    for uuid in sys.argv[1:]:
        path = to_pdf(uuid)
        print(f"File {path} created.")
