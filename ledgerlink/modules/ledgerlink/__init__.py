"""
    The ledgerlink module
    =====================

    This module defines the models allowing to manipulate information regarding links stored in the
    NEO blockchain.

"""


def init_app(app, **kwargs):
    # Register blueprints.
    from . import views
    app.register_blueprint(views.ledgerlink_blueprint)
