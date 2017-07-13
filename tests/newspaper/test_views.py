from newspaper import views


def test_healthcheck(rf):
    request = rf.get('/healthcheck/')
    response = views.healthcheck(request)
    assert response.status_code == 200
