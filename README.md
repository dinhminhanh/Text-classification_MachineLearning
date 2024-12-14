# Text Classification with PCA and Naive Bayes

This project demonstrates how to perform text classification using machine learning techniques, including text preprocessing, dimensionality reduction using PCA (Principal Component Analysis), and training a Naive Bayes classifier.

## Table of Contents
1. [Overview](#overview)
2. [Dependencies](#dependencies)
3. [File Structure](#file-structure)
4. [Data Preprocessing](#data-preprocessing)
5. [Model Training and Evaluation](#model-training-and-evaluation)
6. [Results](#results)
7. [Usage](#usage)
8. [License](#license)

## Overview
This project implements a text classification system that processes Vietnamese language documents in JSON format, applies TF-IDF (Term Frequency-Inverse Document Frequency) to represent the text data, reduces the dimensionality of the feature space using PCA, and classifies the data using Naive Bayes classifiers. The goal is to predict the category (label) of each document.

The classification model is evaluated using accuracy scores for both training and test datasets.

## Dependencies
To run this project, you need the following Python libraries:

- `numpy`
- `scikit-learn`
- `pyvi`
- `json`
- `os`
- `matplotlib`
- `seaborn`

You can install the required dependencies using pip:

```bash
pip install numpy scikit-learn pyvi matplotlib seaborn

