"""
    The dev module
    ==============

    This module defines context processors and views that are only used during developments.

"""


def init_app(app, **kwargs):
    # Register context processors
    from . import context_processors
    app.context_processor(context_processors.webpack)
