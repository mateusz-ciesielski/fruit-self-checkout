#!/usr/bin/env python3

import json

import frontend
from fastapi import FastAPI, Request

app = FastAPI()


@app.post('/inference_ingest')
async def inference_ingest(request: Request):

    prices = {
        'orange': 10,
        'pear': 20,
        #'peach': 5
    }

    icons = {
        'orange': '🍊',
        #'peach': '🍑',
        'pear': '🍐'
    }

    inference_body = await request.body()
    print(request.headers)
    print(f'{inference_body=}')
    try:
        inference_json = await request.json()
        print(f'{inference_json=}')
        frontend.current_items = [
    {'name': f'{icons.get(label["name"], "")} {label["name"]}', 'price': prices.get(label["name"], 10)}
        for annotation in inference_json.get("annotations", []) for label in annotation.get("labels", [])]
    except Exception:
        print('Failed to parse inference request as json')


@app.post('/current_items')
async def current_items(request: Request):
    items = await request.body()
    items = json.loads(items)
    print(items)
    frontend.current_items = items


frontend.init(app)

if __name__ == '__main__':
    print('Please start the app with the "uvicorn" command as shown in the start.sh script')
