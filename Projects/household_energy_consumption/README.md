# 🔋 Energy Demand Forecasting Using LSTM

This project uses an LSTM (Long Short-Term Memory) neural network to forecast household electricity consumption based on historical time series data. The data is processed, resampled, and used to train a model that predicts future energy usage.

---

## 📊 Dataset

- **Source**: UCI Machine Learning Repository   
- **Name**: Individual Household Electric Power Consumption  
- **Description**: Minute-by-minute measurements of active power usage over 4 years.

---

## 🧰 Technologies Used

- Python
- Pandas, NumPy
- TensorFlow / Keras
- Scikit-learn
- Matplotlib
- Jupyter Notebook

---

## 🔄 Workflow

1. Load and clean the dataset
2. Resample to hourly energy consumption
3. Normalize values using MinMaxScaler
4. Create input/output sequences for supervised learning
5. Split data into training and testing sets
6. Train an LSTM model
7. Evaluate and visualize predictions
8. Tune model using Keras Tuner 

---

## 🔍 Results

- Predicts energy usage one hour ahead
- Can be adapted to forecast further into the future or to other resolutions (e.g., daily)


---

## 🚀 Future Improvements

- Add weather or appliance usage as additional features
- Deploy model via Gradio/Streamlit dashboard
