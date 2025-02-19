# Kidney Disease Classification

![Kidney Disease Classification](https://github.com/PriyanshuDey23/Kidney_Disease_Classification/blob/main/Output.jpg)

## Overview
The **Kidney Disease Classification** project aims to predict whether a kidney is **healthy** or affected by a **tumor** using deep learning techniques. The model is built using the **Keras VGG16** architecture and leverages **MLflow** and **DAGsHub** for experiment tracking and version control.

## Workflows
To ensure smooth execution, follow these steps:

1. **Update `config.yaml`** - Define configurations.
2. **Update `secrets.yaml`** (Optional) - Store sensitive credentials.
3. **Update `params.yaml`** - Modify hyperparameters.
4. **Update the entity** - Ensure the correct entity structure.
5. **Update the configuration manager in `src/config`** - Manage configurations.
6. **Update the components** - Implement core functionalities.
7. **Update the pipeline** - Integrate components.
8. **Update `main.py`** - Execute the pipeline.
9. **Update `dvc.yaml`** - Track changes with DVC.
10. **Update `app.py`** - Deploy the model as an API or web app.

## How to Run?
### Steps to Execute:

#### **Step 1: Clone the Repository**
```bash
https://github.com/PriyanshuDey23/Kidney_Disease_Classification.git
```

#### **Step 2: Create and Activate Conda Environment**
```bash
conda create -n cnncls python=3.8 -y
conda activate cnncls
```

#### **Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

#### **Step 4: Run the Application**
##### **Backend**
```bash
python app.py
```
##### **Frontend**
```bash
streamlit run streamlit_app.py
```

## MLflow Tracking
MLflow is used for logging experiments and tracking models.

#### **Start MLflow UI**
```bash
mlflow ui
```

#### **Logging with MLflow**
```python
import mlflow

with mlflow.start_run():
    mlflow.log_param("parameter_name", "value")
    mlflow.log_metric("metric_name", 1)
```

## DAGsHub Integration
[DAGsHub](https://dagshub.com/) is used for experiment versioning and collaboration.

#### **Initialize DAGsHub**
```python
import dagshub

dagshub.init(repo_owner="", repo_name="", mlflow=True)
```

## DVC (Data Version Control)
DVC is used for lightweight experiment tracking and pipeline orchestration.

#### **DVC Commands**
```bash
dvc init
dvc repro
dvc dag
```

## MLflow & DVC Comparison
| Feature  | MLflow | DVC |
|----------|--------|-----|
| **Use Case** | Production-grade tracking | Lightweight POC tracking |
| **Capabilities** | Logging, tagging, and tracing experiments | Orchestration & pipeline management |
| **Strength** | Robust experiment management | Lightweight version control |

---
This project integrates **state-of-the-art deep learning** with **efficient experiment tracking**, making it a **scalable** and **reproducible** kidney disease classification system.

