# Iris Classifier Deployment with Docker and Kubernetes

This repository demonstrates how to train a simple machine learning model using scikit-learn and deploy it as a REST API using Flask, Docker, and Kubernetes.

## Overview

We use the classic Iris dataset to train a logistic regression classifier. The model is saved and served via a Flask API. The API is then containerized using Docker and deployed on a local Kubernetes cluster powered by Minikube.

## Project Structure

```
.
├── app.py                  # Flask REST API serving predictions
├── train_model.py          # Script to train and save the model
├── model.joblib            # Trained model file
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker image specification
└── kubernetes/
    ├── deployment.yaml     # Kubernetes Deployment definition
    └── service.yaml        # Kubernetes Service definition
```

## Setup Instructions

### 1. Train the Model

First, train the classifier and save it as `model.joblib`:

```bash
python train_model.py
```

### 2. Build the Docker Image

Build a Docker image for the Flask API:

```bash
docker build -t iris-flask:1.0 .
```

### 3. Run the API Locally (Optional Test)

You can test the API locally before deploying to Kubernetes:

```bash
docker run -d -p 5000:5000 --name iris_app iris-flask:1.0
```

Send a test request:

```bash
curl -X POST -H "Content-Type: application/json" \
     -d '{"features": [5.1, 3.5, 1.4, 0.2]}' \
     http://localhost:5000/predict
```

### 4. Load Docker Image into Minikube

If you're using Minikube locally, load the image into the Minikube environment:

```bash
minikube image load iris-flask:1.0
```

### 5. Deploy to Kubernetes

Apply the Kubernetes manifests to start the application:

```bash
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
```

### 6. Access the Service

To access the service from your browser or testing tool:

```bash
minikube service iris-service
```

Or alternatively, forward a port:

```bash
kubectl port-forward svc/iris-service 8080:80
```

Test with:

```bash
curl -X POST -H "Content-Type: application/json" \
     -d '{"features": [6.0, 2.9, 4.5, 1.5]}' \
     http://localhost:8080/predict
```

## Technologies Used

- Python
- scikit-learn
- Flask
- Docker
- Kubernetes
- Minikube

## Notes

- Make sure to install all dependencies listed in `requirements.txt`.
- The application expects the model file `model.joblib` to be in the same directory as `app.py`.
- This project is intended for educational and demonstration purposes.
