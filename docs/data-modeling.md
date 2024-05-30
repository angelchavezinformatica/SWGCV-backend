# Entidades del Sistema (Inventario)

## product

- id (UNIQUE): **INTEGER** **(PK)**
- name (UNIQUE): **VARCHAR (50)**
- description: **TEXT**
- quantity: **INTEGER**
- id_category: **INTEGER** **(FK)** R: 1 -> 1
- id_subcategory: **INTEGER** **(FK)** R: 1 -> 1

## product_category **(Catálogo)**

- id (UNIQUE): **INTEGER** **(PK)**
- name (UNIQUE): **VARCHAR (20)**

## product_subcategory **(Catálogo)**

- id (UNIQUE):: **INTEGER** **(PK)**
- category_id: **INTEGER** **(FK)** R: 1 -> 1
- name (UNIQUE):: **VARCHAR (20)**

## product_history

- id (UNIQUE):: **INTEGER** **(PK)**
- datetime: **DATETIME**
- description: **TEXT**
- entry: **BOOLEAN**
- id_produto: **INTEGER** **(FK)** R: 1 -> 1
- quantity: **INTEGER**
