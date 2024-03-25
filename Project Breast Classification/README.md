# Breast Cancer Diagnostic Classification 

## Project Description :computer:
The project aims to a build machine learning model that will classify breast cancer tumors as either benign or malignant based on various features.

## Dataset & Data Preprocessing :bookmark_tabs:
The dataset used for this project is the Breast Cancer Wisconsin (Diagnostic) Data Set found on Kaggle, which can be accessed <a href="https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data/data" target="_blank">here</a>. It contains features computed from a digitized image of a fine needle aspirate (FNA) of a breast mass. The data was preprocessed by handling missing values and scaling features.

## Models Architecture :gear:
#### Simple Model :pushpin:
Layers:

```
- Input Dense Layer (128 Neurons) with ReLU activation function.

- Dropout Layer with a dropout rate of 0.2.

- Dense Layer with 64 Neurons and ReLU activation function.

- Dense Layer with 32 Neurons and ReLU activation function.

- Output Dense Layer (1 Neuron) with sigmoid activation function.
```

Simple Model Accuracy: 71%



#### Optimized Model :scissors:
Layers:

```
- Input Dense Layer (500 Neurons). It has 500 neurons & applies a ReLU (Rectified Linear Unit) activation function.

- Input Dense Layer (128 Neurons) with ReLU activation function and L2 regularization 

- Dropout Layer with a dropout rate of 0.2.

- Dense Layer with 64 Neurons, ReLU activation function, and L2 regularization 

- Dense Layer with 32 Neurons, ReLU activation function, and L2 regularization 

- Output Dense Layer (1 Neuron) with sigmoid activation function.
```

Optimized Model Accuracy: 80% 

## Training and Evaluation :repeat:
The models were trained using the provided dataset and evaluated using accuracy, precision, recall. Confusion matrix was also used to evaluate the error analysis. Hyperparameters were tuned using GridSearchCV for the optimized model.

## Expected Results :white_check_mark:
Both models were trained and evaluated on the provided dataset, with the simple model achieving an accuracy of approximately 71%, while the optimized model demonstrated improved performance with an accuracy of 80%. 

The optimized model, which incorporated L2 regularization and hyperparameter tuning, outperformed the simple model, indicating the effectiveness of these optimization techniques in enhancing model performance.

## Conclusion :round_pushpin:

These results suggest that further optimization efforts, such as exploring additional regularization techniques, adjusting network architecture or better data preprocessing, may lead to even better performance. Nonetheless, both models exhibit promising capabilities for classifying breast cancer tumors as benign or malignant based on the provided features.

## Author
- Nino Chibuzor Nwachukwu (c.nwachukwu@alustudent.com)





