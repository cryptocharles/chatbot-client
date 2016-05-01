import sys
import json
import click
from two1.commands.config import Config
from two1.wallet import Wallet
from two1.bitrequests import BitTransferRequests

wallet = Wallet()
username = Config().username
requests = BitTransferRequests(wallet, username)
server_url = 'http://10.244.30.174:7766/'

@click.command()
@click.argument('username')
@click.argument('message')
def cli(username, message):
    json_message = json.loads(json.dumps(dict(username=username, message=message)))
    response = requests.post(url=server_url, json=json_message).text
    click.echo(json.loads(response))
