# Transfer Learning for Cardiomegaly Disease Prediction


## Description

### Problem Statement

Cardiomegaly, or an enlarged heart, is a critical medical condition that can be indicative of various underlying diseases. Early detection and accurate diagnosis are essential for effective treatment and management. This project leverages transfer learning techniques to develop a robust Convolutional Neural Network (CNN) model for predicting cardiomegaly from chest X-ray images.

### Dataset

The dataset used for this task is sourced from Kaggle and contains labeled chest X-ray images categorized into two classes: true (presence of cardiomegaly) and false (absence of cardiomegaly). The dataset is split into training and testing subsets, with an equal number of images in each class. The dataset can be found <a href="https://www.kaggle.com/datasets/rahimanshu/cardiomegaly-disease-prediction-using-cnn?resource=download" target="_blank">here</a>. 

## Experimental Findings

### Pre-trained models

These three pre-trained models were selected for fine-tuning:

- VGG16
- ResNet101
- DenseNet121


### Justification 

##### VGG16:

- **Performance:** VGG16 has been widely used in various image classification tasks and has demonstrated good performance. While it may not be the most computationally efficient model compared to newer architectures, it still achieves competitive accuracy.

- **Architecture:** It has a simple and uniform architecture consisting of 13 convolutional layers and 3 fully connected layers. This simplicity makes it easier to understand and modify for transfer learning purposes.

- **Suitability:** Given the relatively simple architecture of VGG16, it can be a good starting point for transfer learning, especially if computational resources are limited or if you want a model that is easier to modify and fine-tune.


##### ResNet101:

- **Performance:** ResNet101 is a deeper variant of the ResNet architecture, which has shown impressive performance in various image recognition tasks. Its skip connections help alleviate the vanishing gradient problem, allowing for effective training of very deep networks.

- **Architecture:** The model consists of 101 layers, making it deeper than VGG16. This depth allows the model to learn more complex features from the data, potentially leading to better performance.

- **Suitability:** It is suitable for transfer learning tasks where you require a deeper model to capture more intricate features in the data. Its architecture facilitates effective fine-tuning, especially when dealing with complex datasets like medical images.


##### DenseNet121:

- **Performance:** DenseNet121 has gained popularity due to its dense connectivity pattern, which encourages feature reuse and facilitates gradient flow through the network. This often leads to improved performance, especially when dealing with limited training data.

- **Architecture:** DenseNet121 consists of densely connected blocks where each layer receives direct input from all preceding layers within the same block. This architecture promotes feature reuse and enables effective information propagation through the network.

- **Suitability:** The model is suitable for transfer learning tasks where you want to leverage feature reuse to improve model performance, particularly when dealing with relatively small datasets like medical imaging. Its architecture encourages the effective transfer of learned features from the pre-trained model to your specific task.


## Fine-tuning process

After loading the models with weights trained from the ImageNet dataset, this is the process that the models went through:

**1.** **Freezing Layers:** This step involved setting the trainable attribute of each layer in the pre-trained models to `False`. I did this to retain the pre-trained features. By freezing these layers, my aim was to preserve these learned features, which are highly beneficial for the new task. But overall, training fewer layers reduced the computational requirements and sped up the training process.

**2. Adding custom Top Layers:** I flattened the layer and added a dense layer with 128 units and ReLU activation function. Then I added a final Dense layer with 1 unit and a sigmoid activation function. The aim of doing this was to tailor the model specifically for the new task of cardiomegaly detection, while still leveraging the feature extraction capabilities of the pre-trained convolutional base.

**3. Creating the fine-tuned models:** In this step, I applied the `add_top_layers` function to each of the base models to create the final fine-tuned models. Through this, I aimed to form a complete model for the training process. 

**4. Model Compilation:** I used the Adam optimizer with a learning rate of `0.0001` because Adam optimizer is well-suited for this task as it adapts the learning rate during training, making the training process efficient. In this step, I aimed to minimize the loss and improve the accuracy of the models.  


**But overall, this is the overview of the fine-tuning for each of the models.** 

##### VGG16

**Layer Modifications:**

- The top (fully connected) layers of the VGG16 model were removed.

- A Global Average Pooling (GAP) layer was added.
- Dense layers with Dropout for regularization were added to prevent overfitting.
- A final Dense layer with a sigmoid activation function was used for binary classification.

**Rationale:**
- The VGG16 architecture is known for its simplicity and effectiveness in image classification tasks. By replacing the fully connected layers with GAP and custom Dense layers, the model can better adapt to the specific task of detecting cardiomegaly while reducing the risk of overfitting.


##### ResNet101

**Layer Modifications:**

- The top layers of the ResNet101 model were removed.
- A Global Average Pooling (GAP) layer was added.
- Dense layers with Dropout for regularization were added.
- A final Dense layer with a sigmoid activation function was used.

**Rationale:**
- ResNet101, with its deep residual learning framework, helps in training very deep networks. By fine-tuning the top layers, the model leverages its pre-trained weights to extract relevant features while being customized for cardiomegaly detection.


##### DenseNet121

**Layer Modifications:**

- The top layers of the DenseNet121 model were removed.
- A Global Average Pooling (GAP) layer was added.
- Dense layers with Dropout were introduced for regularization.
- A final Dense layer with a sigmoid activation function was used.


**Rationale:**
- DenseNet121 connects each layer to every other layer in a feed-forward fashion, which strengthens feature propagation. Fine-tuning the top layers allows the model to use its dense connectivity to effectively learn from the cardiomegaly dataset.


## Overview of Evaluation Metrics
To assess the performance of the fine-tuned models, the following evaluation metrics were used:

- **Accuracy:** The proportion of correctly predicted instances out of the total instances.

- **Loss:** The value of the loss function, representing how well the model's predictions match the actual labels.

- **Precision:** The ratio of true positive predictions to the total predicted positives.

- **Recall:** The ratio of true positive predictions to the total actual positives.

- **F1 Score:** The harmonic mean of precision and recall, providing a balance between the two metrics.


## Results


![Transfer Learning Results Image](file:///C:/Users/Lenovo/Downloads/Transfer%20Learning%20Results%20Image.jpg)

+-------------+----------+----------+-----------+--------+----------+
| Model       | Accuracy | Loss     | Precision | Recall | F1 Score |
+-------------+----------+----------+-----------+--------+----------+
| VGG16       | 0.656    | 0.616238 | 0.625806  | 0.776  | 0.692857 |
+-------------+----------+----------+-----------+--------+----------+
| ResNet101   | 0.554    | 0.689052 | 0.532847  | 0.876  | 0.662632 |
+-------------+----------+----------+-----------+--------+----------+
| DenseNet121 | 0.662    | 0.779899 | 0.616046  | 0.860  | 0.717863 |
+-------------+----------+----------+-----------+--------+----------+


| Model      | Accuracy | Loss    | Precision | Recall | F1 Score |
|------------|----------|---------|-----------|--------|----------|
| VGG16      | 0.656    | 0.616238| 0.625806  | 0.776  | 0.692857 |
| ResNet101  | 0.554    | 0.689052| 0.532847  | 0.876  | 0.626232 |
| DenseNet121| 0.662    | 0.779899| 0.616046  | 0.860  | 0.717863 |



## Discussion of findings

1. **Models Comparison:** DenseNet121 achieved the highest accuracy (0.662),  followed by VGG16 (0.656), and ResNet101 (0.554). Although, VGG16 had the second-best accuracy, it had the least loss value (0.616), indicating better performance in terms of minimizing errors and also achieved the highest precision (0.625).

2. **Strengths and Limitations of Transfer Learning:** By leveraging pre-trained models, the training time was reduced. Also, the pre-trained models provided a good starting point, resulting in higher accuracy and better generalization compared to training a model from scratch. However, the pre-trained models were initially trained on the ImageNet dataset, which consists of natural images. Medical images differ significantly, which might limit the effectiveness of the features learned by the pre-trained models. Also, fine-tuning such deep models still requires significant computational resources, including GPUs and memory, which can be a limitation for some users, including myself. 

3. **Why the Models underperformed:** 

- Limited Dataset Size: Although I reduced number of training images (500 for training and 500 for testing) — as otherwise, each epoch was taking about an hour — it might not have been sufficient to capture all the variations and intricacies in the cardiomegaly images.

- Class Imbalance: There might have been an imbalance in the number of positive and negative samples, which can affect the model's ability to learn effectively. 

- Fine-Tuning Strategy: While I froze the convolutional base layers, experimenting with different fine-tuning strategies, such as unfreezing some layers and using different learning rates, might yield better results.


## Conclusion
Through this project, I aimed to demonstrate the efficacy of transfer learning in medical image classification, specifically for detecting cardiomegaly from chest X-rays. While the results might not be the best, further improvements could be made by acquiring more data and exploring additional fine-tuning techniques. Thank you!

