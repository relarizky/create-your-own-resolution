def test_api_doc(client):
    """test api documentation page"""

    fetch = client.get("/api/doc/")

    assert b"Resolution API" in fetch.data


def test_api_add_resolution(client, resolution):
    """test add new resolution from API"""

    new_resolution = client.post(
        "/api/resolution/",
        json=resolution
    )
    response_json = new_resolution.get_json()
    response_status = response_json.get("status")
    response_message = response_json.get("message")

    assert response_status is True
    assert response_message == "successfully added new resolution"


def test_api_add_resolution_fail(client, resolution):
    """test add new resolution from API that causes fail"""

    new_resolution = client.post(
        "/api/resolution/",
        json={
            "percentage": resolution.get("percentage"),
            "description": resolution.get("description")
        }
    )
    response_json = new_resolution.get_json()
    response_status = response_json.get("status")
    response_message = response_json.get("message")

    assert response_status is False
    assert response_message == "fail to perform the action"


def test_api_fetch_multiple_row(client):
    """test fetch multiple row from API"""

    fetch = client.get("/api/resolution/")
    response = fetch.get_json()

    assert len(response) != 0


def test_api_fetch_single_row(client):
    """test fetch single row from API"""

    fetch = client.get("/api/resolution/1")
    response = fetch.get_json()
    response_data = response.get("data")
    response_status = response.get("status")

    assert response_status is True
    assert type(response_data) is dict


def test_api_fetch_single_row_fail(client):
    """test fetch unexisting single row from API"""

    fetch = client.get("/api/resolution/10")
    response = fetch.get_json()
    response_status = response.get("status")
    response_message = response.get("message")

    assert response_status is False
    assert response_message == "can't find resolution with the given id"


def test_api_update_resolution(client):
    """test update resolution row"""

    request = client.put(
        "/api/resolution/1",
        json={
            "resolution": "Learn JavaScript"
        }
    )
    response = request.get_json()
    response_status = response.get("status")
    response_message = response.get("message")

    resolution = client.get("/api/resolution/1").get_json()
    resolution_data = resolution.get("data")
    resolution_status = resolution.get("status")

    assert response_status is True
    assert response_message == "successfully updated resolution"
    assert resolution_status is True
    assert resolution_data.get("resolution") == "Learn JavaScript"


def test_api_update_resolution_fail(client):
    """test update resolution row that causes fail"""

    request = client.put(
        "/api/resolution/10",
        json={
            "resolution": "Learn JavaScript"
        }
    )
    response = request.get_json()
    response_status = response.get("status")
    response_message = response.get("message")

    resolution = client.get("/api/resolution/1").get_json()
    resolution_data = resolution.get("data")
    resolution_status = resolution.get("status")

    assert response_status is False
    assert response_message == "can't find resolution with the given id"


def test_api_delete_single_row(client):
    """test delete single row from API"""

    request = client.delete("/api/resolution/1")
    response = request.get_json()
    response_status = response.get("status")
    response_message = response.get("message")

    assert response_status is True
    assert response_message == "successfully deleted resolution"


def test_api_delete_single_row_fail(client):
    """test delete unexisting single row from API"""

    request = client.delete("/api/resolution/19")
    response = request.get_json()
    response_status = response.get("status")
    response_message = response.get("message")

    assert response_status is False
    assert response_message == "can't find resolution with the given id"
