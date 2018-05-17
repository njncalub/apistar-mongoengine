# import pytest

# from apistar import App, Route, TestClient


# from tests import app, client


# def no_parameter():
#     return None


# # routes = [
# #     Route(url='/sample/', method='GET', handler=no_parameter),
# # ]
# # app = App(routes=routes)
# # client = TestClient(app)


# def test_no_parameter(client):
#     response = client.get('/sample/')

#     assert response.status_code == 200
#     assert response.json() ==  {'hello': 'world'}
