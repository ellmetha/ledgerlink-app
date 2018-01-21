import pytest

from ledgerlink import create_app


@pytest.yield_fixture(scope='session')
def flask_app():
    """ Yields an instance of the Flask application. """
    app = create_app('testing')
    with app.app_context():
        yield app
