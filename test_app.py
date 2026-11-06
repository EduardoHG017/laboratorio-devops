from app import app


def test_inicio():
    cliente = app.test_client()
    respuesta = cliente.get("/")
    assert respuesta.status_code == 200
    datos = respuesta.get_json()
    assert datos["mensaje"] == "Virtualizacion URL"


def test_health():
    cliente = app.test_client()
    respuesta = cliente.get("/health")
    assert respuesta.status_code == 200
    datos = respuesta.get_json()
    assert datos["status"] == "ok"
