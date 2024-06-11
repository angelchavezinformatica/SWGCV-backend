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

## Modelado de datos

### product

- id (UNIQUE): **INTEGER** **(PK)**
- name (UNIQUE): **VARCHAR (100)**
- description: **TEXT**
- price: **FLOAT**
- stock: **INTEGER**
- image: **VARCHAR (20)**
- category_id: **INTEGER** **(FK)** R: 1 -> 1
- subcategory_id: **INTEGER** **(FK)** R: 1 -> 1

### product_category **(Catálogo)**

- id (UNIQUE): **INTEGER** **(PK)**
- name (UNIQUE): **VARCHAR (100)**

### product_subcategory **(Catálogo)**

- id (UNIQUE): **INTEGER** **(PK)**
- category_id: **INTEGER** **(FK)** R: 1 -> 1
- name (UNIQUE): **VARCHAR (100)**

### client

- id (UNIQUE): **VARCHAR (36)** **PK**
- name: **VARCHAR (50)**
- last_name: **VARCHAR (50)**
- email: **VARCHAR (256)**
- phone_number: **VARCHAR (9)**

### sale

- id (UNIQUE):: **INTEGER** **PK**
- datetime: **DATETIME**
- id_client: **VARCHAR (36)** **FK**
- total: **FLOAT**

### sale_detail

- id (UNIQUE):: **INTEGER** **PK**
- id_sale: **INTEGER** **FK**
- id_product: **INTEGER** **FK**
- quantity: **INTEGER**
- price: **FLOAT**
- subtotal: **FLOAT**

![Diagrama entidad relación](./docs/DER.png)
