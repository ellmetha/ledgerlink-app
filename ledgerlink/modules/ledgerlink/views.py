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

    try:
        result = client.contract(
            current_app.config.get('LEDGERLINK_CONTRACT_SCRIPT_HASH')).getURL(code)
    except ConnectionError:
        return redirect(url_for('ledgerlink.home', neodown='yes'))

    try:
        url = result['stack'][0]['value']
        url = url.decode('utf-8')
        assert url
    except (KeyError, IndexError, AssertionError):
        abort(404)

    return redirect(url)
