# Detailed outline of specifications for the endpoints

---

### **1. `/predict` Endpoint Specification**

#### **Purpose**
This endpoint is designed to accept user input and return a prediction based on the machine learning model.

#### **Request Structure**
- **Method**: `POST`
- **Endpoint**: `/predict`
- **Request Body**:
  - **Content Type**: `application/json`
  - **Parameters**:
    - `smoker`: `bool` (required)
      - **Constraints**: Should be a boolean, where `True` indicates the person is a smoker and `False` indicates a non-smoker.
    - `bmi`: `float` (required)
      - **Constraints**: Should be a non-negative floating-point number, typically between 0 and 100. This represents the Body Mass Index.
    - `age`: `int` (required)
      - **Constraints**: Should be a positive integer, typically between 0 and 120, representing the age in years.
    - `children`: `int` (required)
      - **Constraints**: Should be a non-negative integer, representing the number of children the person has (e.g., 0, 1, 2).


#### **Response Structure**
- **Status Code**: `200 OK` (on success)
- **Response Body** (JSON): 
  - `cost_prediction`: `float`
    - **Description**: Predicted health insurance premiums cost
- **Error Responses**:
  - `400 Bad Request`: Returned if required fields are missing or invalid.
    - Example: `{"error": "Invalid age provided. Age must be a positive integer."}`


### **Example Request**:
**Request Method**: `POST`  
**Endpoint**: `/predict`  
**Request Body** (JSON):
```json
{
  "smoker": true,
  "bmi": 28.5,
  "age": 40,
  "children": 2
}
```

### **Example Response**:
**Response Status Code**: `200 OK`  
**Response Body** (JSON):
```json
{
  "cost_prediction": 3500.75
}
```

### **Example Error Response (Invalid Input)**:
If the request is missing a required parameter or contains invalid data:

**Response Status Code**: `400 Bad Request`  
**Response Body** (JSON):
```json
{
  "error": "Invalid age provided. Age must be a positive integer."
}
```

---

### **2. CRUD Endpoints for User Data**

#### **POST /users**
- **Purpose**: Create a new user record.
- **Request Structure**:
  - **Method**: `POST`
  - **Endpoint**: `/users`
  - **Request Body**:
    - `name`: `str` (required)
    - `email`: `str` (required, must be a valid email)
    - `age`: `int` (optional)
  - **Response**:
    - **Status Code**: `201 Created`
    - **Response Body**:
      ```json
      {
        "user_id": "generated_user_id",
        "message": "User created successfully."
      }
      ```

#### **GET /users/{user_id}**
- **Purpose**: Retrieve a user's information.
- **Response**:
  - **Status Code**: `200 OK`
  - **Response Body**:
    ```json
    {
      "user_id": "string",
      "name": "string",
      "email": "string",
      "age": "int"
    }
    ```
  - **Error**: `404 Not Found` if the user ID doesn’t exist.

#### **PUT /users/{user_id}**
- **Purpose**: Update user data.
- **Response**:
  - **Status Code**: `200 OK`
  - **Response Body**:
    ```json
    {
      "message": "User updated successfully."
    }
    ```
  - **Error**: `404 Not Found` if the user ID doesn’t exist.

#### **DELETE /users/{user_id}**
- **Purpose**: Delete a user’s information.
- **Response**:
  - **Status Code**: `200 OK`
  - **Response Body**:
    ```json
    {
      "message": "User deleted successfully."
    }
    ```

---