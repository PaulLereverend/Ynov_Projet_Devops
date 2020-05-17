import pytest
from config import connect
import model.automate
import model.unite
from app import app

def test_conn_db():
    connect()

def test_app():
    return app

def test_automate():
    data = {'num_unite': '1'}
    with app.test_client() as c:
        response = c.get('/automates', query_string = data)
        assert response.status_code == 200

def test_automate_data():
    data = {
        'num_automate': '9',
        'date_fin': '1587741463',
        'unite_id': '3',
    }
    with app.test_client() as c:
        response = c.get('/automate/data', query_string = data)
        assert response.status_code == 200

def test_unite():
    with app.test_client() as c:
        response = c.get('/unites')
        assert response.status_code == 200