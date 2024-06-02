# Entidades del Sistema (Inventario)

## product

- id (UNIQUE): **INTEGER** **(PK)**
- name (UNIQUE): **VARCHAR (100)**
- description: **TEXT**
- quantity: **INTEGER**
- category_id: **INTEGER** **(FK)** R: 1 -> 1
- subcategory_id: **INTEGER** **(FK)** R: 1 -> 1

## product_category **(Catálogo)**

- id (UNIQUE): **INTEGER** **(PK)**
- name (UNIQUE): **VARCHAR (100)**

## product_subcategory **(Catálogo)**

- id (UNIQUE):: **INTEGER** **(PK)**
- category_id: **INTEGER** **(FK)** R: 1 -> 1
- name (UNIQUE):: **VARCHAR (100)**

## product_history

- id (UNIQUE):: **INTEGER** **(PK)**
- datetime: **DATETIME**
- description: **TEXT**
- entry: **BOOLEAN**
- product_id: **INTEGER** **(FK)** R: 1 -> 1
- quantity: **INTEGER**
