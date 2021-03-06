"""
    The modules package
    ===================

    This package contains the modules of the application. Modules enable logical resource
    separation.

"""


def init_app(app, **kwargs):
    from . import ledgerlink

    # Initializes sub-modules.
    for module in (ledgerlink, ):
        module.init_app(app, **kwargs)

    # Initializes the special "dev" submodule if applicable.
    if app.debug:
        from . import dev
        dev.init_app(app)
