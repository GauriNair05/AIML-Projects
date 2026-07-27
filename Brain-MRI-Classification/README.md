# Brain MRI Tumor Detection using CNN

A deep learning project that classifies brain MRI images into different tumor categories using a Convolutional Neural Network (CNN). The model analyzes MRI scans to identify tumor types and distinguish them from healthy brain images, demonstrating the application of deep learning in medical image classification.

## Dataset

*Dataset:* Brain Tumor MRI Dataset

The dataset consists of brain MRI images organized into four classes.

### Classes

- Glioma
- Meningioma
- Pituitary Tumor
- No Tumor

The dataset is divided into separate *Training* and *Testing* folders for model development and evaluation.

## Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

## Project Workflow

1. Load MRI images from the training and testing directories.
2. Resize and normalize the images for model training.
3. Build a Convolutional Neural Network (CNN).
4. Train the model on the MRI dataset.
5. Evaluate the trained model on unseen test images.
6. Generate predictions for brain MRI scans.
7. Visualize performance using accuracy and loss graphs.
8. Analyze results with a confusion matrix and classification report.

## CNN Architecture

The model consists of:

- Three Convolutional Layers
- Three Max Pooling Layers
- Flatten Layer
- Fully Connected Dense Layer
- Dropout Layer for regularization
- Softmax Output Layer with 4 classes

## Features

- Brain MRI image preprocessing
- Image normalization
- CNN-based tumor classification
- Model training and validation
- Accuracy and loss visualization
- Confusion Matrix
- Classification Report
- Single MRI image prediction

## Results

The CNN model successfully learns meaningful features from brain MRI images and classifies them into four categories. The trained model achieved approximately *90.25% test accuracy*, demonstrating effective performance for multi-class brain tumor classification. Performance is further evaluated using accuracy curves, loss curves, a confusion matrix, and a classification report.

## Repository Structure


Brain-MRI-Tumor-Detection/
│
├── brain_mri_tumor_detection.ipynb
├── README.md
└── results/


## Installation

Clone the repository:

bash
git clone https://github.com/your-username/Brain-MRI-Tumor-Detection.git


Install the required libraries:

bash
pip install tensorflow numpy matplotlib seaborn scikit-learn


Run the Jupyter Notebook:

bash
jupyter notebook brain_mri_tumor_detection.ipynb


## Conclusion

This project demonstrates the use of Convolutional Neural Networks for automated brain MRI tumor classification. It provides practical experience in medical image preprocessing, deep learning model development, evaluation, and visualization, highlighting the potential of AI-assisted medical image analysis for supporting diagnostic workflows.
