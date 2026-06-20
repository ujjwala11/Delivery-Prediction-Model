# 🍔 Zomato Delivery Analytics & ETA Prediction

An end-to-end Data Analytics and Machine Learning project built using Python, Pandas, Scikit-Learn, and Streamlit.

The project analyzes food delivery operations data, identifies factors affecting delivery times, and predicts estimated delivery time using a Random Forest Regressor.

---

## 📌 Project Overview

Food delivery platforms face challenges in accurately estimating delivery times due to factors such as:

- Traffic conditions
- Weather conditions
- Delivery distance
- Rider performance
- Multiple deliveries
- Festivals

This project performs:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Machine Learning Modeling
- Business Insights Generation
- Interactive Streamlit Dashboard

---

## 🎯 Objectives

- Analyze operational delivery data
- Discover key factors causing delivery delays
- Build a delivery time prediction model
- Generate actionable business recommendations
- Create an interactive dashboard for predictions and insights

---

## 📊 Dataset

Dataset: Zomato Delivery Operations Analytics Dataset

Key Features:

- Delivery Person Age
- Delivery Person Ratings
- Vehicle Condition
- Multiple Deliveries
- Weather Conditions
- Traffic Density
- Festival Status
- City Type
- Restaurant Coordinates
- Delivery Coordinates

Target Variable:

```text
Time_taken (min)
```

---

## 🛠 Technologies Used

### Data Analysis

- Python
- Pandas
- NumPy

### Visualization

- Matplotlib
- Seaborn

### Machine Learning

- Scikit-Learn
- Linear Regression
- Random Forest Regressor

### Deployment

- Streamlit
- Joblib

---

## 🔍 Data Cleaning

Performed:

- Missing value handling
- Data type correction
- Invalid value detection
- Outlier treatment
- Feature validation

### Data Quality Issue Found

Some records contained:

```text
Delivery_person_Ratings = 6.0
```

Although ratings should be between 1 and 5.

These records were identified and removed before model training.

---

## ⚙️ Feature Engineering

### Distance Calculation

Calculated delivery distance using the Haversine Formula:

```text
Restaurant Latitude/Longitude
+
Delivery Latitude/Longitude
↓
Distance_km
```

### Rating Categories

Created rider performance groups:

- Low
- Average
- Good
- Excellent

---

## 📈 Exploratory Data Analysis

Analyzed:

### Traffic Density Impact

| Traffic | Avg Delivery Time |
|----------|------------------|
| Low | 21.27 min |
| Medium | 26.71 min |
| High | 27.23 min |
| Jam | 31.18 min |

### Weather Impact

| Weather | Avg Delivery Time |
|----------|------------------|
| Sunny | 21.85 min |
| Fog | 28.93 min |
| Cloudy | 28.92 min |

### Festival Impact

| Festival | Avg Delivery Time |
|----------|------------------|
| No | 25.99 min |
| Yes | 45.51 min |

### Multiple Deliveries Impact

| Deliveries | Avg Time |
|------------|----------|
| 0 | 22.87 min |
| 1 | 26.86 min |
| 2 | 40.44 min |
| 3 | 47.81 min |

---

## 🤖 Machine Learning

### Models Trained

#### Linear Regression

Results:

```text
MAE  = 4.78
RMSE = 5.99
R²   = 0.589
```

---

#### Random Forest Regressor

Results:

```text
MAE  = 3.18
RMSE = 4.03
R²   = 0.814
```

The Random Forest model significantly outperformed Linear Regression and was selected as the final model.

---

## 🚨 Data Leakage Detection

Initially, a feature called:

```text
Speed_kmph
```

was engineered using:

```text
Distance / Delivery Time
```

This caused data leakage because the target variable was used to create a predictor.

The issue was identified through unrealistically high model performance:

```text
R² ≈ 0.995
```

The leaked feature was removed and the model was retrained.

Final model performance:

```text
R² = 0.814
```

---

## 🏆 Feature Importance

Top factors affecting delivery time:

| Rank | Feature |
|--------|----------|
| 1 | Delivery Person Ratings |
| 2 | Distance (km) |
| 3 | Multiple Deliveries |
| 4 | Delivery Person Age |
| 5 | Traffic Density |

---

## 💡 Key Business Insights

### Rider Ratings Matter

Average delivery time by rider rating category:

| Category | Avg Delivery Time |
|-----------|------------------|
| Low | 36.23 min |
| Average | 35.90 min |
| Good | 30.57 min |
| Excellent | 24.48 min |

Higher-rated riders complete deliveries significantly faster.

---

### Festivals Cause Major Delays

Average delivery time increased from:

```text
25.99 min → 45.51 min
```

during festivals.

---

### Multiple Deliveries Increase Delivery Time

Average delivery time nearly doubled when riders handled multiple orders simultaneously.

---

## 📊 Streamlit Dashboard

The dashboard contains:

### ETA Prediction

Predict delivery time using:

- Distance
- Rider Rating
- Traffic
- Weather
- Festival Status
- City

### Business Insights

- Traffic Analysis
- Weather Analysis
- Festival Impact
- Feature Importance

### Delivery Optimizer

Business simulator for evaluating operational improvements.

### Model Performance

Displays:

- R² Score
- MAE
- RMSE
- Prediction Performance

---

## 📂 Project Structure

```text
Zomato-Delivery-Analytics/

│
├── app.py
│
├── models/
│   ├── delivery_time_model.pkl
│   └── model_columns.pkl
│
├── visualizations/
│   ├── traffic_analysis.png
│   ├── weather_analysis.png
│   ├── festival_analysis.png
│   ├── feature_importance.png
│   └── actual_vs_predicted.png
│
├── notebooks/
│   └── zomato_delivery_analysis.ipynb
│
├── requirements.txt
│
└── README.md
```

---

## 🚀 Future Improvements

- XGBoost Model
- Hyperparameter Tuning
- Live Deployment
- Geospatial Heatmaps
- Route Optimization
- Real-Time ETA Updates

---

