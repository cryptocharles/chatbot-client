import sys
import json
import click
from two1.commands.config import Config
from two1.wallet import Wallet
from two1.bitrequests import BitTransferRequests

wallet = Wallet()
username = Config().username
requests = BitTransferRequests(wallet, username)
server_url = 'http://10.244.195.170:7766/'

@click.command()
@click.argument('username')
@click.argument('message')
def cli(username, message):
    json_logs = json.loads(json.dumps(dict(username=username, message=message)))
    click.echo(json.loads(requests.post(url=server_url, json=json).text))
