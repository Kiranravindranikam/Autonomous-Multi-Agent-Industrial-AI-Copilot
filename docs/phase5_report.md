# Phase 5 Report

## Dataset

NASA CMAPSS FD001

## Objective

Predict Remaining Useful Life (RUL) using LSTM.

## Data Preparation

* Cleaned NASA dataset used
* RUL feature generated
* Features normalized using MinMaxScaler
* Sequence length = 30 cycles

## Model Architecture

* LSTM (64)
* Dropout (0.2)
* LSTM (32)
* Dropout (0.2)
* Dense (16)
* Dense (1)

## Training

* Epochs: 10
* Batch Size: 64

## Evaluation

* Test Loss: 2924.92
* MAE: 39.75

## Output

Predicted Remaining Useful Life (RUL)

## Status Classification

* Healthy (RUL > 100)
* Warning (RUL 31–100)
* Critical (RUL ≤ 30)

## Model Saved

models/lstm_rul_model.keras

## Status

Phase 5 Completed Successfully
