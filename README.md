# Whale Sound Classifier

This project aims to classify whale species based on audio recordings using a Convolutional Neural Network (CNN). It includes Python scripts for data preprocessing, model training (using PyTorch), and model conversion to ONNX format. It's used in a Vue.js frontend application that allows users to listen to a sample whale sound, make a prediction, and see the model's classification performed directly in the browser using ONNX Runtime Web.

## Features

* **Audio Preprocessing:** Extracts Mel-Frequency Cepstral Coefficients (MFCCs) from `.wav` audio files using `librosa`.
* **CNN Model:** A PyTorch-based 1D CNN designed for audio classification.
* **Training & Validation:** Scripts for training the model, validating performance, and saving the best model weights. Includes early stopping.

## Model Architecture

The model is a 1D Convolutional Neural Network (CNN) implemented in PyTorch. It typically consists of:

* Input Layer: Expects MFCC data with shape `[batch_size, num_mfcc (13), time_frames (130)]`.
* Convolutional Layers: 1D convolutions (`nn.Conv1d`) with ReLU activations and Batch Normalization (`nn.BatchNorm1d`) to extract features along the time axis.
* Pooling Layers: Max Pooling (`nn.MaxPool1d`) to reduce dimensionality.
* Dropout Layers: To prevent overfitting.
* Flatten Layer: To prepare the features for the fully connected layers.
* Fully Connected Layers (`nn.Linear`): To perform the final classification.
* Output Layer: A linear layer with `num_classes` output neurons, producing raw logits for each class.

*(Refer to the `WhaleAudioCNN` class definition in `train_model.py` or `convert_to_onnx.py` for the exact architecture.)*
