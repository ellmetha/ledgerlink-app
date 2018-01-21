"""
    The ledgerlink application
    ==========================

    Ledgerlink (or ledgr.link) is a URL shortener service that uses the NEO blockchain as a mean to
    store irreplaceable / unfalsifiable short URLs. Such shortened URLs are protected against any
    third party interferences because they cannot be changed by anybody - they will live forever on
    the NEO blockchain. Thus the NEO blockchain is used as a source of trust, ensuring that the
    shortened links always lead to where they are supposed to.

"""

from flask import Flask

from config import config

from . import extensions
from . import modules


def create_app(config_name):
    config_obj = config[config_name]()
    app = Flask(
        __name__, static_url_path='/static',
        static_folder='static/build' if not config_obj.DEBUG else 'static/build_dev')

    # Initializes configuration values.
    app.config.from_object(config_obj)

    # Configure SSL if the current platform supports it.
    if not app.debug and not app.testing and not app.config['SSL_DISABLE']:
        from flask.ext.sslify import SSLify
        SSLify(app)

    # Initializes Flask extensions.
    extensions.init_app(app)

    # Initializes modules.
    modules.init_app(app)

    return app
