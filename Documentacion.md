# API Documentation

## Índice

1. [Register User](#register-user)
2. [Login User](#login-user)
3. [Test Token](#test-token)
4. [User Profile](#user-profile)
5. [View Users](#view-users)
6. [View User by ID](#view-user-by-id)
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

