# PhishGuard — Phishing URL Detection using Machine Learning

## 1. Problem Statement

Phishing attacks are a major cybersecurity threat in which attackers create fake or malicious websites to steal sensitive information such as usernames, passwords, banking details, and personal data.

Manually identifying whether a URL is legitimate or phishing can be difficult. Therefore, this project aims to develop a machine learning-based system that automatically analyzes URL characteristics and predicts whether a URL is **SAFE** or **PHISHING**.

---

## 2. Objective

The main objectives of PhishGuard are:

* To analyze URLs and extract relevant characteristics.
* To use machine learning algorithms for phishing URL classification.
* To compare the performance of multiple machine learning models.
* To identify the best-performing model.
* To provide a live prediction for a new URL.
* To display the prediction in a simple and understandable manner.

---

## 3. Proposed Solution

The proposed system follows this workflow:

```text
Input URL
    ↓
Feature Extraction
    ↓
Machine Learning Model
    ↓
Model Prediction
    ↓
SAFE / PHISHING
```

The system extracts useful characteristics from a URL and provides them to a trained machine learning model. The model then classifies the URL as either legitimate or phishing.

---

## 4. System Workflow

1. Collect labelled URL data.
2. Preprocess the dataset.
3. Extract relevant URL features.
4. Split the dataset into training and testing data.
5. Train multiple machine learning models.
6. Evaluate the models using performance metrics.
7. Compare the model results.
8. Select the best-performing model.
9. Use the selected model for live URL prediction.
10. Display the final prediction to the user.

---

## 5. Feature Engineering

The system uses characteristics of URLs to help identify suspicious patterns.

The exact features used in the final implementation will be documented here after integration with the feature extraction code.

**Implemented Features:**

* [Feature from final implementation]
* [Feature from final implementation]
* [Feature from final implementation]

> Note: Only features actually implemented in the project should be listed here.

---

## 6. Machine Learning Models

Multiple machine learning models are trained and compared to determine which model performs best for phishing URL classification.

**Models used:**

* [Actual Model 1]
* [Actual Model 2]
* [Actual Model 3]

The final model names will be updated after receiving the confirmed implementation from the machine learning team.

---

## 7. Dataset

The project uses a labelled dataset containing legitimate and phishing URLs.

The dataset is used for:

* Training the machine learning models.
* Testing model performance.
* Comparing different classification algorithms.

**Dataset Source:** [Add actual dataset source]

**Dataset Size:** [Add actual number of records]

**Classes:**

* Legitimate / Safe
* Phishing

---

## 8. Technology Stack

### Programming Language

* Python

### Development Environment

* Google Colab
* Visual Studio Code

### Libraries and Frameworks

* pandas
* NumPy
* scikit-learn
* matplotlib
* seaborn
* Streamlit

> Only technologies actually used in the final implementation should remain in this list.

### Version Control

* Git
* GitHub

---

## 9. Model Results

The performance of the trained machine learning models will be compared using standard classification metrics.

| Model   |       Accuracy |      Precision |         Recall |       F1-Score |
| ------- | -------------: | -------------: | -------------: | -------------: |
| Model 1 | [ACTUAL VALUE] | [ACTUAL VALUE] | [ACTUAL VALUE] | [ACTUAL VALUE] |
| Model 2 | [ACTUAL VALUE] | [ACTUAL VALUE] | [ACTUAL VALUE] | [ACTUAL VALUE] |
| Model 3 | [ACTUAL VALUE] | [ACTUAL VALUE] | [ACTUAL VALUE] | [ACTUAL VALUE] |

### Best Performing Model

**Model:** [ACTUAL BEST MODEL]

**Accuracy:** [ACTUAL ACCURACY]

The final values will be added after model evaluation is completed.

---

## 10. Confusion Matrix

A confusion matrix is used to evaluate the classification performance of the selected machine learning model.

It shows:

* True Positives
* True Negatives
* False Positives
* False Negatives

The final confusion matrix will be added to the `results/` folder.

---

## 11. Live Prediction Demo

The project provides a live interface where the user can enter a URL and receive a prediction.

### Example

```text
Enter URL
    ↓
Feature Extraction
    ↓
Trained Model
    ↓
Prediction
    ↓
SAFE / PHISHING
```

The final screenshots of the live prediction interface will be stored in the `screenshots/` folder.

---

## 12. Testing

The system will be tested using sample URLs representing both legitimate and suspicious websites.

Testing will include:

* Legitimate URL prediction.
* Phishing URL prediction.
* Checking the prediction output.
* Verifying that the live interface works correctly.

Actual test examples and outputs will be documented after final integration.

---

## 13. Challenges Faced

Some challenges that may be encountered during development include:

* Preparing and cleaning the URL dataset.
* Selecting useful URL characteristics.
* Training and comparing different machine learning models.
* Integrating the trained model with the live prediction interface.
* Ensuring that the prediction system works correctly for new URLs.
* Organizing the project components for final deployment and demonstration.

The final documented challenges will be updated based on the actual development experience of the team.

---

## 14. Solutions to Challenges

The team addresses these challenges through:

* Dataset preprocessing and validation.
* Feature extraction from URL characteristics.
* Comparison of multiple machine learning algorithms.
* Testing the trained model with sample URLs.
* Integration testing between the model and prediction interface.
* Version control using Git and GitHub.

---

## 15. Limitations

The system has some limitations:

* Machine learning predictions depend on the quality and diversity of the training dataset.
* URL-based features alone may not identify every type of phishing website.
* New phishing techniques may not be represented in the training data.
* The current system may not include external real-time threat intelligence.

---

## 16. Future Scope

Possible future improvements include:

* Integration with real-time threat intelligence.
* Domain age analysis.
* DNS-based analysis.
* WHOIS information analysis.
* Browser extension support.
* Continuously updated phishing datasets.
* Improved prediction explainability.
* Real-time URL reputation checking.

---

## 17. How to Run

### Step 1 — Clone the Repository

```bash
git clone https://github.com/poornimaraju1278-stack/URL_detection.git
```

### Step 2 — Open the Project

```bash
cd URL_detection
```

### Step 3 — Install Dependencies

If a `requirements.txt` file is available:

```bash
pip install -r requirements.txt
```

### Step 4 — Run the Project

Use the final run command provided by the team after integration.

For a Streamlit application, the command may be:

```bash
streamlit run app.py
```

> The final command should be updated according to the actual application file created by the team.

---

## 18. Project Structure

```text
URL_detection/
│
├── README.md
├── requirements.txt
├── data/
├── notebooks/
├── src/
├── models/
├── results/
├── screenshots/
├── presentation/
└── team_details.md
```

The final structure may be updated during project integration.

---

## 19. Team Members

| Member   | Name         | Roll Number | Contribution                                                        |
| -------- | ------------ | ----------- | ------------------------------------------------------------------- |
| Member 1 | Poornima R   | R25EF181    | Machine Learning models, training and evaluation                    |
| Member 2 | Nikhi Rathod | R25EF167    | Dataset preparation and feature engineering                         |
| Member 3 | Rakshita H   | R25EF211    | Live prediction interface and testing                               |
| Member 4 | Pavana M     | R25EF179    | Documentation, presentation, research and final integration support |

---

## 20. Project Status

**Project:** PhishGuard — Phishing URL Detection using Machine Learning

**Status:** In Development / Hackathon Prototype

The documentation will be updated as the machine learning model, live prediction interface, test results, screenshots, and final presentation are integrated.
