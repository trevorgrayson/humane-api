import os
import http.client
from trello import TrelloClient

TRELLO_KEY = os.environment['TRELLO_KEY']
TRELLO_TOKEN = os.environment['TRELLO_TOKEN']

client = TrelloClient(
    api_key=TRELLO_KEY
    # api_secret='your-secret',
    token=TRELLO_TOKEN,
    # token_secret='your-oauth-token-secret'
)

curl "https://api.trello.com/1/members/me/boards?fields=name,url&key=$TRELLO_KEY&token=$TRELLO_TOKEN" | jq '.[] | .name,.id'
