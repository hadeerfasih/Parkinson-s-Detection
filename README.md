# Parkinson's Detection

This repository contains the code and documentation for the project on Parkinson's disease detection using a clinical decision support system.

## Project Overview
The project focuses on investigating the use of sketching behavior as a fine motor symptom for differentiating individuals affected by Parkinson's disease (PD) from a healthy control group. The goal is to develop a clinical decision support system using deep learning algorithms, particularly Convolutional Neural Networks (CNNs), to classify sketched images and accurately detect PD.

## Methods
### Literature Review
The project begins with an extensive literature review of existing research on Parkinson's disease detection. Two key papers are reviewed:

1. "Parkinson’s Disease Detection Using ResNet50 with Transfer Learning" - This paper presents a computational system that utilizes Convolutional Neural Networks (CNNs) and the ResNet50 model for classifying spiral drawings to distinguish between individuals with Parkinson's disease and healthy subjects. The system achieved a commendable accuracy rate of 96.67%.

2. "Deep Transfer Learning Based Parkinson’s Disease Detection Using Optimized Feature Selection" - This paper introduces a novel approach for accurately detecting Parkinson's disease using handwritten records. Transfer learning models such as ResNet, VGG19, and InceptionV3 are employed, and feature optimization is performed using a genetic algorithm. The proposed model achieved a detection accuracy exceeding 95% and outperformed state-of-the-art approaches.

### Dataset
The dataset used in the project is the Parkinson's Drawings dataset obtained from Kaggle. It consists of 204 sketches, including 102 spiral sketches and 102 wave sketches. The dataset is divided into training and testing categories, with a balanced distribution of healthy and Parkinson's sketches.

### Preprocessing
Several preprocessing methods and algorithms are applied to the dataset:
- Keras' ImageDataGenerator is used for image augmentation and preprocessing, including scaling pixel values, adjusting colors, and brightness.
- The Zhang-Suen thinning algorithm is implemented to reduce the width of objects in the image.
- Gaussian blur is applied as a data augmentation technique to reduce image noise and detail.
- Otsu thresholding is used for image thresholding to separate foreground and background.

### Model Development
The project employs Convolutional Neural Networks (CNNs) and transfer learning techniques to develop the Parkinson's detection system. Various CNN models, including VGG, ResNet50, and InceptionV3, are utilized. The models are trained on the training sketches and evaluated on the testing sketches. The objective is to achieve high accuracy in differentiating between healthy and Parkinson's sketches.

## Results and Conclusion
The proposed system demonstrates promising results in detecting Parkinson's disease based on sketching behavior. The VGG model achieves an accuracy of 86.67% specifically when analyzing spiral sketches. The project validates the effectiveness of deep learning algorithms and transfer learning in Parkinson's disease detection.

Overall, this project contributes to the development of a clinical decision support system for Parkinson's disease diagnosis based on sketching behavior. The achieved results showcase the potential of using deep learning algorithms and image analysis techniques for early detection and intervention in Parkinson's disease.

For more details, please refer to the full report in the Report.pdf file.

