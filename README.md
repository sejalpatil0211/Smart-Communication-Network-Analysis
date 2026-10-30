# Smart Communication Network Analysis and Prediction Using Machine Learning

## 📌 Project Overview

Smart Communication Network Analysis and Prediction is a Machine Learning-based web application developed to analyze network parameters and predict network conditions.

The system uses a Random Forest Classifier to identify different network conditions based on input parameters such as signal strength, latency, packet loss, channel utilization, DHCP failures, and DNS risk score.

The application is developed using Python and Streamlit.

## 🎯 Objectives

- Analyze important network parameters.
- Identify different network issues.
- Predict network conditions using Machine Learning.
- Provide an easy-to-use web interface for network analysis.
- Display prediction results and probability scores.

## 📊 Dataset

The dataset was obtained from Hugging Face.

**Dataset:** SmartNet Network Incidents

**Dataset link:** https://huggingface.co/datasets/codingkiddo/smartnet-network-incidents

- Total records: 4,200
- Total columns: 11
- Number of prediction classes: 6

**Note:** The dataset is synthetic and is used for academic and educational purposes. The results do not represent validated performance on real-world network traffic.

## ⚙️ Input Parameters

The model uses the following input features:

1. RSSI (Signal Strength)
2. Channel Utilization
3. Latency
4. Packet Loss
5. DHCP Failures
6. DNS Risk Score
7. Device Type

## 🔍 Predicted Network Conditions

The model classifies network conditions into six categories:

- Healthy
- Weak Signal
- High Latency
- Wi-Fi Congestion
- DHCP Failure
- DNS Security Risk

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib
- Jupyter Notebook

## 🤖 Machine Learning Algorithm

**Random Forest Classifier**

The model is trained using a train-test split of 80:20 with stratified sampling.

The trained model is saved using Joblib and integrated into a Streamlit web application for prediction.

## 📈 Model Performance

The model achieved **99.88% test accuracy** on the held-out test portion of the synthetic dataset.

This result is specific to the available synthetic dataset and does not establish real-world network detection accuracy.

## 💻 Application

The Streamlit application allows users to:

- Enter network parameters.
- Select the device type.
- Predict the network condition.
- View prediction probability scores.

## 🚀 Future Scope

- Integration with real-time network monitoring.
- Testing with real-world network datasets.
- Improving model generalization.
- Adding network performance visualization.
- Developing an automated network issue detection system.

## 👩‍💻 Author

**Sejal Patil**

Third Year Electronics and Telecommunication Engineering Student

**Project:** Smart Communication Network Analysis and Prediction Using Machine Learning
