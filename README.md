# SWGCV-backend

Backend para Sistema Web de Gestión Comercial para Vivero

## Configuración del proyecto

- Crear un archivo `.env` con lo siguiente:

```
SECRET_KEY=<your-secret-key>
DEBUG=True
SERVER=http://127.0.0.1:8000/
```

- Crear las migraciones

```bash
python manage.py makemigrations
```

- Hacer las migraciones

```bash
python manage.py migrate
```
