# CIFAR-10 Image Classification using CNN

A deep learning project that classifies color images from the CIFAR-10 dataset into one of ten object categories using a Convolutional Neural Network (CNN). The project demonstrates the complete image classification pipeline, including data preprocessing, model training, evaluation, and performance visualization using TensorFlow and Keras.

## Dataset

*Dataset:* CIFAR-10

The CIFAR-10 dataset contains *60,000 RGB images* of size *32 × 32 pixels* distributed across *10 classes*.

- Training Images: 50,000
- Testing Images: 10,000

### Classes

- Airplane
- Automobile
- Bird
- Cat
- Deer
- Dog
- Frog
- Horse
- Ship
- Truck

## Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

## Project Workflow

1. Load and preprocess the CIFAR-10 dataset.
2. Normalize pixel values to improve model training.
3. Build a Convolutional Neural Network (CNN).
4. Train the model on the training dataset.
5. Evaluate performance on the test dataset.
6. Generate predictions on unseen images.
7. Visualize results using accuracy and loss graphs.
8. Analyze model performance with a confusion matrix and classification report.

## CNN Architecture

The model consists of:

- Three Convolutional Layers
- Three Max Pooling Layers
- Flatten Layer
- Fully Connected Dense Layer
- Dropout Layer for regularization
- Softmax Output Layer with 10 classes

## Features

- Image preprocessing and normalization
- CNN-based image classification
- Model training and validation
- Accuracy and loss visualization
- Confusion Matrix
- Classification Report
- Single image prediction

## Results

The trained CNN successfully learns meaningful image features and achieves good classification performance on the CIFAR-10 dataset. Training and validation accuracy improve consistently while the loss decreases over successive epochs, demonstrating effective learning and generalization.

## Repository Structure


CIFAR-10-Image-Classification/
│
├── cifar10_classification.ipynb
├── README.md
└── results/


## Installation

Clone the repository:

bash
git clone https://github.com/your-username/CIFAR-10-Image-Classification.git


Install the required libraries:

bash
pip install tensorflow numpy matplotlib seaborn scikit-learn


Run the Jupyter Notebook:

bash
jupyter notebook cifar10_classification.ipynb


## Conclusion

This project demonstrates the application of Convolutional Neural Networks for multi-class image classification using the CIFAR-10 dataset. It provides hands-on experience with image preprocessing, CNN model development, training, evaluation, and visualization, serving as a strong foundation for more advanced computer vision tasks.
