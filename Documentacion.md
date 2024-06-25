
# API Documentation

  

## Índice

  

1. [Register User](#register-user)

2. [Login User](#login-user)

3. [User Token](#user-token)

4. [User Profile](#user-profile)

5. [View Users](#view-users)

6. [View User by Email](#view-user-by-email)

7. [Change Password](#change-password)

8. [View Stock and Products by Category](#view-stock-and-products-by-category)

9. [View Document Types](#view-document-types)

10. [Create House](#create-house)

11. [Get Houses](#get-houses)

12. [Edit House](#edit-house)

13. [Get Directions](#get-directions)

14. [Create Direction](#create-direction)

15. [Get Specific Direction](#get-specific-direction)

16. [Edit Direction](#edit-direction)

17. [Delete User](#delete-user)

18. [Update User](#update-user)



## Register User


### URL

`/register/`
### Method

`POST`
### Description

Registers a new user.
  

### Parameters

- `nombre` (str, required): The first name of the user.

- `apellido` (str, required): The last name of the user.

- `nombreusuario` (str, required): The username of the user.

- `password` (str, required): The password for the user.

- `genero` (int, required): The gender of the user. (0: Male, 1: Female, 2: Unknown)

- `documento` (str, required): The document ID of the user.

- `telefono` (str, required): The phone number of the user.

- `email` (str, required): The email of the user.

- `id_direccion` (int, required): The ID of the user's address.

- `id_tipousuario` (int, required): The ID of the user type.

- `id_tipodocumento` (int, required): The ID of the document type.

### Request Body Example

```json
{
"nombre": "example",
"apellido": "example",
"nombreusuario": "example",
"password": "example",
"genero": 1,
"documento": "11111111",
"telefono": "3510000000",
"email": "example@gmail.com",
"id_direccion": 1,
"id_tipousuario": 1,
"id_tipodocumento": 1
}
```

  

### Possible Errors

  

#### 400 Bad Request

- **Invalid Data**: If any required field is missing or has invalid data.

- **Response Example**:

```json
{
"nombreusuario": ["This field is required."],
"password": ["This field is required."]
}
```

- **Cause**: One or more required fields (`nombreusuario`, `password`) are missing or empty.

  

- **Email Already Exists**: If a user with the same email already exists.

- **Response Example**:

```json
{
"email": ["A user with that email already exists."]
}
```

- **Cause**: The email provided is already associated with another user.

  

- **Username Already Exists**: If a user with the same username already exists.

- **Response Example**:

```json
{
"nombreusuario": ["A user with that username already exists."]
}
```

- **Cause**: The username provided is already associated with another user.

  

- **Validation Errors**: If any data provided does not meet the validation criteria.

- **Response Example**:

```json
{
"password": ["Ensure this field has at least 8 characters."]
}
```

- **Cause**: The password provided does not meet the minimum length requirement.

  

#### 409 Conflict

- **Duplicate Entry**: If there is a conflict with an existing entry (e.g., email or username already taken).

- **Response Example**:

```json
{
"error": "A user with this email or username already exists."
}
```

- **Cause**: An attempt to register with an email or username that is already taken by another user.

  

#### 500 Internal Server Error

- **Server Error**: If an unexpected error occurs on the server.

- **Response Example**:

```json
{
"error": "An unexpected error occurred. Please try again later."
}

```

- **Cause**: This can be due to a variety of reasons, such as database issues, server misconfigurations, etc.

  
## Login User

  
### URL

`/login/`
### Method

`POST`
### Description

User Login.

### Parameters


- `email` (str, required): The email of the user.
- 
- `password` (str, required): The password for the user.


### Request Body Example

```json
{
"email": "example@gmail.com",
"password": "example"
}
```

  

### Possible Errors

#### 400 Bad Request

- **Invalid Data**: If any required field is missing or has invalid data.

- **Response Example**:

```json
{
"email": ["This field is required."],
"password": ["This field is required."]
}
```

- **Cause**: One or more required fields (`email`, `password`) are missing or empty.

#### 401 Unauthorized

- **Wrong Password**: The password is not correct for that mail.

- **Response Example**:

```json
{
"error": "El usuario o la contraseña es incorrecta."
}
```

- **Cause**: An attempt to login with a password that is not correct.

  

#### 404 Not Found

- **Mail not found**: That mail doesn't exist.

- **Response Example**:

```json
{
"error": 'El usuario no fue encontrado'
}
```

- **Cause**:  An attempt to login with a mail that is not correct.
## User Token

  
### URL

`/userToken/<str:token>`
### Method

`GET`
### Description

User Login.

### Parameters


- `email` (str, required): The email of the user.

- `password` (str, required): The password for the user.

### Request Body Example

```json
{
"email": "example@gmail.com",
"password": "example"
}
```

  

### Possible Errors

#### 400 Bad Request

- **Invalid Data**: If any required field is missing or has invalid data.

- **Response Example**:

```json
{
"email": ["This field is required."],
"password": ["This field is required."]
}
```

- **Cause**: One or more required fields (`email`, `password`) are missing or empty.

#### 401 Unauthorized

- **Wrong Password**: The password is not correct for that mail.

- **Response Example**:

```json
{
"error": "El usuario o la contraseña es incorrecta."
}
```

- **Cause**: An attempt to login with a password that is not correct.

  

#### 404 Not Found

- **Mail not found**: That mail doesn't exist.

- **Response Example**:

```json
{
"error": 'El usuario no fue encontrado'
}
```

- **Cause**:  An attempt to login with a mail that is not correct.

## User Profile

  
### URL

`/profile/`
### Method

`GET`
### Description

Obtener la información del perfil del usuario autenticado.

### Parameters

Ninguno.

### Headers

- `Authorization` (str, requerido): Token de autenticación del usuario.

### Request Body Example

```json
{
 
}
```


### Possible Errors

#### 401 Unauthorized

- **Error de autenticación**: Token inválido o no proporcionado.

```json
{
  "detail": "Authentication credentials were not provided."
}
```
## View Users

  
### URL

`/user/`
### Method

`GET`
### Description

Obtener la lista de todos los usuarios. Necesitas estar autenticado.

### Parameters

Ninguno.

### Headers

- `Authorization` (str, requerido): Token de autenticación del usuario.

### Response Example

```json
[
    {
        "id": 1,
        "nombre": "John",
        "apellido": "Doe",
        "nombre_usuario": "johndoe",
        "documento": "12345678",
        "telefono": "3510000000",
        "email": "johndoe@example.com",
        "genero": 1,
        "fecha_union": "2023-01-01",
        "last_login": "2023-01-10",
        "is_superuser": false,
        "id_direccion": 1,
        "id_tipo_usuario": 1,
        "id_tipo_documento": 1
    }
]

```


### Possible Errors

#### 401 Unauthorized

- **Error de autenticación**: Token inválido o no proporcionado.

```json
{
  "detail": "Authentication credentials were not provided."
}
```

## View Users by Email

  
### URL

`/user/<str:email>`
### Method

`GET`
### Description

Obtener información de un usuario específico por su email.

### Parameters

- `email` (str, requerido): El email del usuario.

### Headers

- `Authorization` (str, requerido): Token de autenticación del usuario.

### Response Example

```json
{
    "id": 1,
    "nombre": "John",
    "apellido": "Doe",
    "nombre_usuario": "johndoe",
    "documento": "12345678",
    "telefono": "3510000000",
    "email": "johndoe@example.com",
    "genero": 1,
    "fecha_union": "2023-01-01",
    "last_login": "2023-01-10",
    "is_superuser": false,
    "id_direccion": 1,
    "id_tipo_usuario": 1,
    "id_tipo_documento": 1
}
```


### Possible Errors

#### 404 Not Found

- **Usuario no encontrado**: El email proporcionado no corresponde a ningún usuario.

```json
{
  "error": "El usuario no existe."
}
```

## Change Password

  
### URL

`/cambiar_contrasenia/`
### Method

`POST`
### Description

Cambiar la contraseña del usuario autenticado.

### Parameters

- `old_password` (str, requerido): La contraseña antigua del usuario.
- `new_password` (str, requerido): La nueva contraseña del usuario.
- `new_password_repeat` (str, requerido): Repetición de la nueva contraseña del usuario.

### Headers

- `Authorization` (str, requerido): Token de autenticación del usuario.

### Request Body Example

```json
{
    "old_password": "oldpass",
    "new_password": "newpass",
    "new_password_repeat": "newpass"
}
```


### Possible Errors

#### 400 Bad Request

- **Faltan datos**: No se proporcionaron los datos requeridos.

```json
{
  "error": "Por favor, proporcione la contraseña antigua, la nueva contraseña y la repetición de la nueva contraseña."
}
```

- **Las nuevas contraseñas no coinciden**: Las nuevas contraseñas proporcionadas no coinciden.

```json
{
    "error": "Las nuevas contraseñas no coinciden."
}
```

- **Contraseña antigua incorrecta**: La contraseña antigua proporcionada es incorrecta.

```json
{
    "error": "La contraseña antigua es incorrecta."
}
```

#### 401 Unauthorized

- **Error de autenticación**: Token inválido o no proporcionado.

```json
{
    "detail": "Las credenciales de autenticación no se proveyeron."
}
```


## View Stock and Products by Category

  
### URL

`/stock/<int:categoria_id>/
### Method

`GET`
### Description

Obtener los productos y el stock disponible de una categoría específica.

### Parameters

- `categoria_id` (int, requerido): El ID de la categoría de productos.

### Headers

- `Authorization` (str, requerido): Token de autenticación del usuario.
### Request Body Example

```json
[
    {
        "nombre_producto": "Producto 1",
        "descripcion": "Descripción del producto 1",
        "stock_disponible": 10
    },
    {
        "nombre_producto": "Producto 2",
        "descripcion": "Descripción del producto 2",
        "stock_disponible": 5
    }
]
```


### Possible Errors

#### 401 Unauthorized

- **Error de autenticación**: Token inválido o no proporcionado.

```json
{
  "detail": "Authentication credentials were not provided."
}
```

#### 404 Not Found

- **Error**: Id de categoria no proporcionado.

## View Document Types

  
### URL

`tipo_documento`
### Method

`GET`
### Description

Obtener todos los tipos de documentos disponibles.

### Parameters

Ninguno.

### Request Body Example

```json
[
    {
        "id": 1,
        "nombre": "DNI"
    },
    {
        "id": 2,
        "nombre": "Pasaporte"
    }
]

```


### Possible Errors

#### Ninguno
## Create House

  
### URL

`/crear_casa/`
### Method

`POST`
### Description

Crear una nueva casa.

### Parameters

- `nombre` (str, requerido): El nombre de la casa.
- `direccion` (str, requerido): La dirección de la casa.

### Headers

- `Authorization` (str, requerido): Token de autenticación del usuario.
### Request Body Example

```json
{
    "nombre": "Casa ejemplo",
    "descripcion": "Descripcion ejemplo",
    "id_organizacion": 1,
    "id_direccion": 1
}
```

### Response Example

```json
{
  "id_casa": 1,
  "nombre": "Casa ejemplo",
  "descripcion": "Descripcion ejemplo",
  "id_organizacion": 1,
  "id_direccion": 1
}
```

### Possible Errors

#### 400 Bad Request

- **Datos inválidos**: Si algún campo requerido falta o es inválido.
-
```json
{
  "detail": "Authentication credentials were not provided."
}
```

#### 404 Not Found

- **Error**: Id de categoria no proporcionado.

## Get Houses
  
### URL

`/casa/`
### Method

`GET`
### Description

Obtener la lista de todos las casas. Necesitas estar autenticado.

### Parameters

Ninguno.

### Headers

- `Authorization` (str, requerido): Token de autenticación del usuario.

### Response Example

```json
[
  {
    "id_casa": 1,
    "nombre": "Mama Antula",
    "descripcion": "Muy descriptiva :D",
    "id_organizacion": 1,
    "id_direccion": 1
  },
  {
    "id_casa": 2,
    "nombre": "El Aljibe",
    "descripcion": "Muy descriptiva :D",
    "id_organizacion": 1,
    "id_direccion": 2
  },
  {
    "id_casa": 3,
    "nombre": "La Casa de la Bondad",
    "descripcion": "Muy descriptiva :D x3",
    "id_organizacion": 1,
    "id_direccion": 3
  }
]
```

### Possible Errors

#### 401 Unauthorized

- **Error de autenticación**: Token inválido o no proporcionado.

```json
{
  "detail": "Authentication credentials were not provided."
}
```

## Edit House

### URL

`/editar_casa/<int:pk>/`
### Method

`PUT`
### Description

Editar una casa.

### Parameters

- `nombre` (str, requerido): El nombre de la casa.
- `direccion` (str, requerido): La dirección de la casa.

### Headers

- `Authorization` (str, requerido): Token de autenticación del usuario.
### Request Body Example

```json
{
    "nombre": "Casa ejemplo",
    "descripcion": "Descripcion ejemplo",
    "id_organizacion": 1,
    "id_direccion": 1
}
```

### Response Example

```json
{
  "id_casa": 1,
  "nombre": "Casa ejemplo",
  "descripcion": "Descripcion ejemplo",
  "id_organizacion": 1,
  "id_direccion": 1
}
```

### Possible Errors

#### 400 Bad Request

- **Datos inválidos**: Si algún campo requerido falta o es inválido.
-
```json
{
  "detail": "Authentication credentials were not provided."
}
```

#### 404 Not Found

- **Error**: Id de categoria no proporcionado.