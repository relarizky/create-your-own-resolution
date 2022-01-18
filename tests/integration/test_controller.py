def test_home_page(client):
    """test home page"""

    response = client.get("/")

    assert b"Create Your Own Resolution" in response.data
    assert b"Resolution List" in response.data


def test_statistic_page(client):
    """test statistic page"""

    response = client.get("/statistic")

    assert b"Create Your Own Resolution" in response.data
    assert b"Resolution Finishing Statistic" in response.data
