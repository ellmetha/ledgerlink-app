"""
    Ledgerlink client
    =================

    This module defines a convenient ``get_client`` function allowing to initialize a JSON-RPC
    client that will be used to interact with the NEO blockchain in order to redirect users.

"""

from flask import current_app
from neojsonrpc import Client


_client = None


def get_client(reset=False):
    """ Returns a NeoJsonRPC client instance allowing to interact with the NEO blockchain. """
    global _client
    if _client is None or reset:
        _client = Client(
            host=current_app.config.get('LEDGERLINK_NEO_JSONRPC_HOST'),
            port=current_app.config.get('LEDGERLINK_NEO_JSONRPC_PORT'))
    return _client
