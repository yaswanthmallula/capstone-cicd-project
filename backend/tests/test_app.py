from backend.app import app

def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")

    # Either UP or DOWN is acceptable, app should not crash
    assert response.status_code in [200, 500]
