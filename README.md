# Laboratorio DevOps – Integración continua con GitHub Actions

**Curso:** Virtualización – Universidad Rafael Landívar
**Estudiante:** Eduardo David Hernández Girón – 1156823

## Descripción

Aplicación Flask sencilla con dos endpoints y pruebas automáticas con Pytest. Cada vez que se hace `push` al repositorio, GitHub Actions instala las dependencias y ejecuta las pruebas para validar que la aplicación sigue funcionando.

| Endpoint | Respuesta |
| --- | --- |
| `/` | `{"mensaje": "Virtualizacion URL"}` |
| `/health` | `{"status": "ok"}` (código 200) |

## Herramientas utilizadas

- Python 3.12 (runner) / 3.11 (local)
- Flask
- Pytest
- Git y GitHub
- GitHub Actions
- Visual Studio Code

## Estructura

```
laboratorio-devops/
├── app.py
├── test_app.py
├── requirements.txt
├── .gitignore
├── docs/
│   └── Laboratorio_CICD_1156823_Eduardo_Hernandez.pdf
└── .github/
    └── workflows/
        └── ci.yml
```

## Instalación

```bash
git clone https://github.com/EduardoHG017/laboratorio-devops.git
cd laboratorio-devops
python -m venv .venv
source .venv/Scripts/activate      # Windows (Git Bash)
# source .venv/bin/activate        # Linux / macOS
python -m pip install -r requirements.txt
```

## Ejecución

```bash
python app.py
```

Abrir en el navegador:

- http://localhost:5000
- http://localhost:5000/health

## Pruebas

```bash
python -m pytest -v
```

Resultado esperado:

```
test_app.py::test_inicio PASSED
test_app.py::test_health PASSED
2 passed
```

## Integración continua (GitHub Actions)

El workflow `.github/workflows/ci.yml` (**CI Flask**) se ejecuta con `push`, `pull_request` o de forma manual (`workflow_dispatch`). Corre en `ubuntu-latest` y realiza estos pasos:

1. Descargar el repositorio (`actions/checkout@v4`)
2. Configurar Python 3.12 (`actions/setup-python@v5`)
3. Instalar dependencias
4. Ejecutar las pruebas con Pytest

## Evidencia del workflow

| Ejecución | Commit | Descripción | Resultado |
| --- | --- | --- | --- |
| #1 | `1b98151` | Agregar aplicacion Flask y pruebas | ✅ Satisfactoria |
| #2 | `c3b307d` | Modificar mensaje de inicio (error intencional) | ❌ Fallida: `test_inicio` |
| #3 | `7a5134f` | Corregir mensaje de inicio | ✅ Satisfactoria |

Historial completo en la pestaña [Actions](https://github.com/EduardoHG017/laboratorio-devops/actions). Las capturas están en `docs/Laboratorio_CICD_1156823_Eduardo_Hernandez.pdf`.
