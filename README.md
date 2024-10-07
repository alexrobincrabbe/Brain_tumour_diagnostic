


# Brain Tumour Diagnostic Tool

An image classifier machine learning project for classifying MRI scans of braintumours/healthy barins, utilizing convolutional neural networks (CNN).

The link to the streamlit app can be found [here](https://brain-tumour-diagnostic-d316f77538fb.herokuapp.com/)

# Table of Contents

1. <a href="#project-dataset">Project Dataset</a>

2. <a href="#business-requirements">Business Requirements</a>

3. <details open>
    <summary><a href="#hypothesis-and-how-to-validate">Hypothesis and How to Validate</a></summary>

    - [Hypothesis](#hypothesis)

    - [Validation](#validation)

</details>

4. <details open>
    <summary><a href="the-rationale-to-map-the-business-requirements-to-the-data-visualizations-and-ml-tasks">The rationale to map the business requirements to the Data Visualizations and ML tasks</a></summary>


    -  [User Stories](#user-stories)
        <ul>

        - [Data collection and Preparation](#data-collection-and-preparation)

        - [Data visualisation](#data-visualisation)

        - [Modelling and Evaluation](#modelling-and-evaluation)

        - [Dashboard Development and Deployment](#dashboard-development-and-deployment)
        </ul>
    </details>

5. <a heref="ml-business-case">ML Business Case</a>


6. <a href="#modelling">Modelling</a>


7. <a href="#libraries">Libraries</a>

8. <details open>
    <summary><a href="#deployment">Deployment</a></summary>

    - [local deployment](#local-deployment)
    - [deployment to heroku](#deploy-to-heroku)

9. <a href="credits">credits</a>

## Project Dataset

The dataset consists of 7023 MRI scans. The scans are split into four classes: glioma, healthy, meningioma, pituitary. 

The data can be found at https://www.kaggle.com/datasets/rm1000/brain-tumor-mri-scans

## Business Requirements

The demand for MRI-based diagnostics is increasing, with over a million MRI brain scans conducted annually in hospitals and clinics worldwide. Radiologists often face the challenge of reviewing large volumes of images under pressure, which can lead to delays and diagnostic inconsistencies. Early and accurate diagnosis is critical for treatment planning and improving patient outcomes, particularly for conditions like glioma and meningioma that require timely intervention. There is a need for an automated solution to assist radiologists in identifying and classifying brain abnormalities swiftly and accurately.

The institution requires an automated solution to:

- 1 Provide visual insights into the nature of different categories through image analysis
- 2 Reduce diagnostic time by quickly categorizing brain scans into four key categories: glioma, meningioma, pituitary tumor, and healthy cases.

## Hypothesis and How to Validate

- Hypothesis: A machine learning model, using convolutional neural networks (CNNs), can accurately classify MRI brain scans into four categories—glioma, meningioma, pituitary tumor, and healthy and assit radialogists by providing quick reliable predictions.

- How to validate: Measure key metrics such as accuracy, precision, recall for each of the four categories.

## The rationale to map the business requirements to the Data Visualizations and ML tasks

### User Stories

#### Data collection and Preparation

- Data collection
    * Download Dataset from Kaggle
    * Unzip data

- Data cleaning
    * Remove non images from the dataset

- Split datasets
    * Split the dataset into train, validate and test sets

#### Data visualisation

- Calculate average image sizes
    * Display plot of image size distribution
    * Calculate average image size
    * Save image size embeddings

- Show average and variability of images (addresses business requirement 1)
    * Show plots of average images for each label
    * Show plots of average variability for each label
    * Save images

- Show average differences between images of different labels
    * Calculate and plot the average difference between images for each label with respect to every other label
    * Save images

#### Modelling and Evaluation

- Create model
    * Load dataset
    * Augment the data
    * Create model
    * Train model
    * Evaluate on test set
    * Save model and history plots

- Fine tune model (addresses business requirement 2)
    * Tune paremeters to maximise the model performance
    * Train model
    * Evaluate on test set

#### Dashboard Development and Deployment

- Set up Streamlit app
    * Create streamlit app.py
    * Create Multipage class

- Create project summary page
    * Create function to generate content for the summary page
    * Import and add the page to the streamlit app

- Create Machine Learning performance page
    * Create function to generate content for the ML performance page
    * Import and add the page to the streamlit app
    * Show loss and accuracy curves for training and validation sets
    * Show metrics on test set
    * Show precision and recall curves for training and validation sets, for each label

- Create brain tumour diagnostics page (addresses business requirement 2)
    * Create function to generate content for the brain tumour diagnostic page
    * Import and add the page to the streamlit app
    * create functions to load images and make predictions using the model
    * Plot the probailities of each label

- Create project hypothesis page
    * Create function to generate content for the project hypothesis page
    * Import and add the page to the streamlit app

- Create MRI scan visualiser page  (addresses business requirement 1)
    * Create function to generate content for the MRI scan visualiser page
    * Import and add the page to the streamlit app
    * Create function to load and display montage of images
    * Create functions to load and display average image and variablity for each label
    * Create function to load and display difference between average image for each pair of labels

## ML Business Case

- We aim to develop a machine learning model to predict whether a brain MRI scan falls into one of four categories: glioma, meningioma, pituitary tumor, or healthy. The model is a supervised, multi-class, single-label classification model based on historical MRI scan image data.
- Our ideal outcome is to provide radiologists with a faster and more reliable diagnostic tool to classify MRI brain scans, assisting them in identifying brain abnormalities or confirming healthy cases more accurately and efficiently.
- The model success metrics are:
    * Recall and precision of at least 0.7 accross all labels

- The model output is defined as a label for the MRI scan, indicating the predicted category (glioma, meningioma, pituitary tumor, or healthy) along with the associated probability score for each category. The medical team will upload MRI scans to the App, and predictions will be made on the fly, not in batches. These predictions can be used by radiologists as a support tool during their diagnostic process.
Heuristics:
- The current diagnostic process for detecting brain abnormalities in MRI scans requires experienced radiologists to carefully analyze images, often involving manual inspection. The process is time-consuming and subject to human variability, which can lead to errors or inconsistencies in diagnosis. This is especially problematic in under-resourced hospitals or diagnostic centers that are experiencing high demand and understaffing.
By introducing an AI-powered diagnostic tool, radiologists will be able to make faster, more consistent decisions, improving the quality of patient care. Furthermore, the tool will assist in areas where there is a shortage of radiologists, helping to alleviate diagnostic bottlenecks.

## Dashboard Design

### Page 1: Project Summary

- General info: background and context for the study

- Project dataset: link and basic info about the dataset
 
- Business requirements

### Page 2: Data Visualisation

Addresses business requirement 1

- Show a montage of images from each category in the dataset

- Show average image and variation for each label

- Show different between average image between each pair of labels

### Page 3: Brain Tumour Diagnostic

Addresses business requirement 2

- Allows images of MRI scans to be uploaded, and predicts which category (most likely) the image belongs to

- Shows probabilities for all categories

### Page 4: Hypothesis and Validation

- 

### Page 5: ML Metrics

- Shows balance of dataset labels

- Shows training loss and accuracy history

- Shows performance metrics on test set

- Shows training precision and recall training history by label

## Modelling

- The model contains 3 2d-convolution layers

- The 3 max pooling layers are needed to reduce the size of the image

- The flatten layer converts the pixel values to a 1-D array

- At least one dense layer is required for the parameter fitting

- The output activation function is softmax, as there are 4 categorical lables to be predicted

- The loss function is categorical cross entropy

### Model Tuning

- Batch size was increased from 20 to 40 to increase performance. As the set contains 4 labels, rather than a binary classifiction, it was supposed that a larger batch size would be necessary to fit each iteration of the model. Increasing above 40 didn't show any benefit.

- The total number of epochs were increased from 15 to 50, as the model appeared to still be improving up to 30 epochs and beyond

- The early stopping toleranz was increased from 3 to 6, as the validation loss showed large variability between epochs, and this caused training to sometimes be stoppped earlier than is should

- As meningioma showed the worst performance of all of the labels, a higher weight was given to this label to improve performance. However improving performance with the meningioma category appears to come at a cost of the performance in the glioma category. Increasing weights in both glioma and meningioma were also tried.

- Note: only the final model is stored in the github repository, in order to keep the repository size within the limits for deployment on Heroku

## Deployment

### Local Deployment

1. Clone the repository
2. Install dependencies:
    ``` 
    pip3 install -r "requirements.txt"
    ```
3. You will need an account with [kaggle](https://www.kaggle.com/) to download an API token. The kaggle.json file should be place in the route directory
4. To run the app:
    ``` 
    streamlit run app.py
    ```

### Deploy to Heroku

1. You will need an account at Heroku and be logged into your account
2. Click 'New' then 'Create new app'
3. Choose region
4. Click 'create app'
5. In the deploy tab under deployment method, choose GitHub
6. Under connect to Github, choose the repository to connect
7. Under Manual deploy, click 'Deploy Branch'

## Libraries

- Tensorflow
    * Image augmentation
    * Machine learning model and training

- Keras_tuner
    * Hyperparameter optimization

- Pandas
    * Dataframes

- Matplotlib/Seaborn
    * Plotting data

- Streamlit
    * Front end Deployment


## Credits

Project was adapted from this [Code Institute walkthrough project](https://github.com/Code-Institute-Solutions/WalkthroughProject01). The model hyper-parameters used were used as the starting point, and the notebook structure is based around the project.
