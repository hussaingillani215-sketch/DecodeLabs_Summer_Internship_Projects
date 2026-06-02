# Project 2: Data Classification Using AI

## Internship Program
Decode Labs Summer Intensive Program 2026

## Project Overview
This project focuses on building a basic supervised learning classification model using the K-Nearest Neighbors algorithm. The main goal is to understand how a machine learning model learns patterns from labeled data and predicts the class of new data points.

## Dataset Used
The Iris dataset is used in this project. It is a small and well-known classification dataset containing flower measurements.

The dataset contains:
- 150 samples
- 4 input features
- 3 target classes

## Features
The input features are:
- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

## Classes
The model predicts one of the following Iris flower classes:
- Setosa
- Versicolor
- Virginica

## Algorithm Used
K-Nearest Neighbors Classifier

KNN is a supervised learning algorithm that classifies a new data point based on the majority class of its nearest neighbors.

## Project Workflow
The notebook follows these steps:

1. Import required libraries
2. Load the Iris dataset
3. Understand the dataset
4. Split the data into training and testing sets
5. Apply feature scaling using StandardScaler
6. Train the KNN classification model
7. Make predictions on test data
8. Evaluate the model using:
   - Accuracy Score
   - Confusion Matrix
   - Precision
   - Recall
   - F1 Score
9. Compare different K values
10. Test the model using custom input
11. Save the trained model

## Libraries Used
- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib

## Results
The model achieved high accuracy on the Iris dataset and successfully classified flower species using the KNN algorithm.

## How to Run the Project
1. Clone this repository.
2. Open the Jupyter Notebook.
3. Install the required libraries using:

```bash
pip install -r requirements.txt