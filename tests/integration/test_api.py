def test_api_doc(client):
    """test api documentation page"""

    fetch = client.get("/api/doc/")

    assert b"Resolution API" in fetch.data


def test_api_add_resolution(client):
    """test add new resolution from API"""

    new_resolution = client.post(
        "/api/resolution/",
        json={
            "resolution": "Learn Test-Driven Development",
            "percentage": 40,
            "description": "it's still going on"
        }
    )
    response_json = new_resolution.get_json()
    response_status = response_json.get("status")
    response_message = response_json.get("message")

    assert response_status is True
    assert response_message == "successfully added new resolution"


def test_api_fetch_multiple_row(client):
    """test fetch multiple row from API"""

    fetch = client.get("/api/resolution/")
    response = fetch.get_json()

    assert len(response) != 0


def test_api_fetch_single_row(client):
    """test fetch single row from API"""

    fetch = client.get("/api/resolution/1")
    response = fetch.get_json()

    assert type(response) is dict
    assert response != {}


def test_api_delete_single_row(client):
    """test delete single row from API"""

    request = client.delete("/api/resolution/1")
    response = request.get_json()
    response_status = response.get("status")
    response_message = response.get("message")

    assert response_status is True
    assert response_message == "successfully deleted resolution"
