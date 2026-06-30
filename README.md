# 🏠 House Price Prediction using Machine Learning

A Machine Learning web application that predicts house prices based on property features such as area, bedrooms, bathrooms, age, parking, and location. The project is built using **Python**, **Scikit-learn**, and **Streamlit**.

---

## 📌 Project Overview

This project demonstrates the complete Machine Learning workflow:

- Data Collection
- Data Preprocessing
- Exploratory Data Analysis (EDA)
- Model Training
- Model Evaluation
- Model Deployment using Streamlit

Users can enter house details and receive an estimated house price instantly.

---

## 🚀 Features

- 🏠 Predict house prices
- 📊 Interactive Streamlit web application
- 📈 Data visualization
- 🤖 Linear Regression Machine Learning model
- 📍 Location-based prediction
- 💾 Trained model saved using Joblib
- 🎨 Clean and responsive UI

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Libraries
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib

---

## 📂 Project Structure

```
House-Price-Prediction/
│
├── data/
│   └── house_data.csv
│
├── models/
│   └── house_price_model.pkl
│
├── notebooks/
│   └── EDA.ipynb
│
├── app.py
├── train.py
├── generate_dataset.py
├── requirements.txt
├── README.md
└── screenshots/
     |__ Dashboard1.png (Input)
         Dashboard2.png (Output)
```

---

## 📊 Dataset Features

| Feature | Description |
|----------|-------------|
| Area | Area of house in square feet |
| Bedrooms | Number of bedrooms |
| Bathrooms | Number of bathrooms |
| Age | Age of property |
| Parking | Parking availability |
| Location | House location |
| Price | Target variable |

---

## 🤖 Machine Learning Workflow

### 1. Data Collection

Generated a dataset containing house information and prices.

### 2. Data Preprocessing

- Checked missing values
- Converted categorical data using One-Hot Encoding
- Selected features and target variable

### 3. Exploratory Data Analysis

- Data summary
- Correlation Heatmap
- Scatter plots
- Statistical analysis

### 4. Model Training

Used **Linear Regression** to train the model.

### 5. Model Evaluation

Evaluated the model using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

### 6. Deployment

Developed an interactive web application using **Streamlit**.

---

## 📈 Model Performance

Evaluation Metrics:

- MAE
- MSE
- RMSE
- R² Score

*(Update these values after training your final model.)*

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/VedantaSakpal/House-Price-Prediction.git
```

Go to the project folder

```bash
cd House-Price-Prediction
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📸 Screenshots

### Home Page

(Add Screenshot Here)

### Prediction Result

(Add Screenshot Here)

---

## 📚 Future Improvements

- Random Forest Regression
- XGBoost Regression
- House Price Trend Charts
- Prediction Confidence Score
- Google Maps Integration
- Real Dataset Support
- Cloud Deployment
- User Authentication

---

## 🎯 Learning Outcomes

Through this project, I learned:

- Python Programming
- Data Analysis
- Data Visualization
- Machine Learning
- Linear Regression
- Model Evaluation
- Streamlit Deployment
- Git & GitHub

---

## 👨‍💻 Author

**Vedant Anil Sakpal**

LinkedIn: https://www.linkedin.com/in/vedant-sakpal-8a70833a3/

GitHub: https://github.com/VedantaSakpal/

---

## ⭐ If you found this project useful, don't forget to Star the repository!
