# End-to-End Machine Learning pipeline

## Overview
This project is an end-to-end Machine Learning pipeline designed to automate the entire ML workflow, from data ingestion to model deployment. It also includes model tracking and versioning using **DagsHub** and **MLflow** to ensure reproducibility and performance monitoring.

## Pipeline Stages
The ML pipeline is structured into the following stages:

### 1. Data Ingestion
- Collects raw data..
- Splits the dataset into training and testing sets.
- Stores the ingested data for further processing.

### 2. Data Validation
- Checks data schema, missing values, and anomalies.
- Ensures data quality and consistency before transformation.
- Generates validation reports.

### 3. Data Transformation
- Handles missing values and outliers.
- Converts raw data into a format suitable for model training.

### 4. Model Training
- Trains ML models with ElasticNet.
- Stores trained models and logs experiments using MLflow.
- Saves the best model based on evaluation metrics.

### 5. Model Evaluation
- Tests the trained models on the test datasets.
- Generates performance metrics such as mean_sqaured_error,mean_absolute_error,r2_score.
- Logs evaluation results to DagsHub and MLflow for tracking.

## Model Tracking with DagsHub & MLflow
- **DagsHub**: Used for version control, collaboration, and tracking model artifacts.
- **MLflow**: Used for experiment tracking and model registry.
- All training runs, parameters, and performance metrics are stored and accessible for comparison.

## Installation
To set up the project, follow these steps:

```bash
# Clone the repository
git clone <repo_url>
cd <project_directory>

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

## Usage
### Train the Model
```bash
python main.py
```
### Run the Flask App
```bash
python app.py
```
### Track Experiments with MLflow
```bash
mlflow ui
```
Then open `http://localhost:8080` in a browser to view logs.

## Deployment
- The trained model can be deployed using **Flask/FastAPI**.
- API endpoints are created to receive input data and return predictions.
- The UI is built using HTML, CSS, and JavaScript for user interaction.

## Contributors
- **Atharv Mohan Jadhav**  

## License
This project is licensed under the GNU GENERAL PUBLIC LICENSE.

