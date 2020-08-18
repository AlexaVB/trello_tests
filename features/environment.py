from behaving import environment as benv
from behaving.web.steps import *
from selenium import webdriver
import requests
import os
import json
import code
import env

def call_trello_api(method, path, query={}):
    base_api_url = 'https://api.trello.com/1'

    full_query = dict({
        'key': os.environ['TRELLO_KEY'],
        'token': os.environ['TRELLO_TOKEN']
    })
    full_query.update(query)

    headers = {
        "Accept": "application/json"
    }

    return requests.request(
        method,
        base_api_url + path,
        params=full_query,
        headers=headers
    )

def before_all(context):
    benv.before_all(context)

def before_scenario(context, scenario):
    query = {
        'name': 'My Trello board'
    }

    response = call_trello_api(
        "POST",
        '/boards',
        query
    )

    global board_id
    board_id = json.loads(response.text)['id']

    response = call_trello_api(
        "GET",
        f"/boards/{board_id}/lists"
    )

    list_id = json.loads(response.text)[0]['id']

    for card_number in range(3):
        query = {
            'idList': list_id,
            'name': f'Card {card_number + 1}'
        }
        card_number += 1

        response = call_trello_api(
            "POST",
            "/cards",
            query
        )

        global card_id
        card_id = json.loads(response.text)['id']
    
    context.add_desc = add_desc
    context.delete_card = delete_card
    context.add_comment = add_comment

def add_desc():
    query = {
        'desc': 'This is the card description'
    }

    call_trello_api(
        "PUT",
        f"/cards/{card_id}",
        query
    )

def delete_card():
    call_trello_api(
        "DELETE",
        f"/cards/{card_id}"
    )

def add_comment():
    query = {
        'text': 'This is the card comment'
    }

    call_trello_api(
        "POST",
        f"/cards/{card_id}/actions/comments",
        query
    )

def after_scenario(context, scenario):
    call_trello_api(
        "DELETE",
        f"/boards/{board_id}"
    )
    benv.after_scenario(context, scenario)
