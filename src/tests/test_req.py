from flask import Flask

from app.routes import configure_routes


def test_get():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/fgh'

    response = client.get(url)
    assert response.status_code == 200


def test_post():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/nfg'

    response = client.post(url)
    assert response.status_code == 200


def test_delete():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/nfg'

    response = client.delete(url)
    assert response.status_code == 200
