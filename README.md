
# Insurance Charges Prediction API

This repository provides a FastAPI-based API that predicts insurance charges based on input features like age, BMI, number of children, and smoking status. The model is trained using polynomial regression, and the project includes Docker configuration for containerized deployment.

* Note: There are more detailed instructions and information in:
  * `app/api/README.md` for API endpoint specifications
  * `model/README.md` for training and model details

## Project Structure

```
app/
    api/                      # API endpoint implementations
    db_control/               # Database management and ORM files
    models/                   # Model and preprocessor files and needed moduls
         polynomial_regression_model.pkl
         polynomial_features.pkl
    schemas/                  # Pydantic schemas for request/response validation
    __init__.py
    main.py                   # Main FastAPI app instance
model/                        # Model training and evaluation
tests/                        # Pytest tests for the project
requirements.txt              # Python dependencies
Dockerfile                    # Docker configuration for building the container
README.md                     # Project documentation
```

## Getting Started

### Prerequisites

- Python 3.11.4
- Docker (for containerized deployment)

### Installation

1. **Clone or download the Repository**:

   ```bash
   git clone https://github.com/alirezashojaei/fastapi-ml-service.git
   cd fastapi-ml-service
   ```

2. **Install Dependencies**:

   Using `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application Locally**:

   ```bash
   uvicorn app.main:app --reload
   ```

   The app should now be accessible at `http://127.0.0.1:8000`.

### Using Docker

1. **Build the Docker Image**:

   ```bash
   docker build -t insurance-charges-api .
   ```

2. **Run the Docker Container**:

   ```bash
   docker run -p 8000:8000 insurance-charges-api
   ```

   The API will be available at `http://localhost:8000`.

## API Endpoints

* `app/api/README.md` for API endpoint specifications

- `POST /predict`: Predicts insurance charges based on provided input features.
   - **Input**: JSON object with `age`, `bmi`, `children`, and `smoker` fields.
   - **Output**: Predicted insurance charges.

### Example Request

```bash
curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d '{"age": 30, "bmi": 22.5, "children": 1, "smoker": "yes"}'
```

### Example Response

```json
{
  "predicted_charges": 13200.45
}
```

## Testing

Tests are written using `pytest` and include unit tests for model loading and prediction functionality.

To run tests:

```bash
pytest tests/
```

## Model and Data

The project uses a polynomial regression model to predict insurance charges based on features like `age`, `bmi`, `children`, and `smoker`. The model and polynomial transformer (`polynomial_regression_model.pkl` and `polynomial_features.pkl`) are located in `app/models/`.

### Dataset

* `model/README.md` for training and model details

The dataset for training includes information on individuals' age, BMI, number of children, smoking status, and insurance charges. Features were encoded and transformed before model training.

## License

This project is licensed under the MIT License.
