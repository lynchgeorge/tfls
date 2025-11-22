from tfl.client import Client
from tfl.api_token import ApiToken
import os


def verify():
    return 'tfls is working!'


def get_client():
    token = ApiToken(
        os.getenv("app_id"),
        os.getenv("app_key")
    )
    return Client(token)


def get_line_ids():
    return [
        'victoria',
        'central',
        'northern',
        'bakerloo',
        'piccadilly',
        'dlr',
        'metropolitan',
        'jubilee',
        'circle',
        'district'
        # 'hammersmith & city'
        # 'waterloo & city',
    ]
