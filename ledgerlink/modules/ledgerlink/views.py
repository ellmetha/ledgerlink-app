"""
    Ledgerlink views
    ================

    This module defines views that will be used to browse link-related pages.

"""

from flask import Blueprint, abort, current_app, redirect, url_for
from requests.exceptions import ConnectionError

from .client import get_client


ledgerlink_blueprint = Blueprint('ledgerlink', __name__)


@ledgerlink_blueprint.route('/', methods=['GET', ])
def home():
    """ The main entrypoint of the ledgerlink URL-shortener service. """
    pass


@ledgerlink_blueprint.route('/<string:code>', methods=['GET', ])
def redirect_code(code):
    """ Redirects the user to the URL associated with considered code if applicable. """
    client = get_client()

    # Tries to get the corresponding URL by invoking the smart contract using the JSON-RPC client.
    # This will not result in a transaction being committed to the NEO blockchain because we are
    # using the 'invoke' JSON-RPC method: the getURL function will be run inside the NEO Virtual
    # Machine but the contract's storage won't be updated at all.
    try:
        result = client.contract(
            current_app.config.get('LEDGERLINK_CONTRACT_SCRIPT_HASH')).getURL(code)
    except ConnectionError:
        return redirect(url_for('ledgerlink.home', neodown='yes'))

    # Processes the response sent back by the NEO node and tries to get the URL corresponding to the
    # considered code if it was found in the contract's storage.
    try:
        url = result['stack'][0]['value']
        url = url.decode('utf-8')
        assert url
    except (KeyError, IndexError, AssertionError):
        abort(404)

    return redirect(url)
