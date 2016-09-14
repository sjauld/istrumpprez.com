from __future__ import print_function

import json
import datetime

print('Loading function')

def magic_number(raw_ip):
    try:
        safe_ip = map(lambda x: int(x) + 3, raw_ip.split('.'))
    except ValueError:
        safe_ip = [666]
    magic_number = reduce(lambda x, y: x * y, safe_ip)
    days = (datetime.date(2016, 11, 8) - datetime.date.today()).days
    if days > 0:
        return magic_number % ( days * 2 ) - days + 50
    else:
        return 50

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    return {'trump_chance': magic_number(event['client_ip'])}
