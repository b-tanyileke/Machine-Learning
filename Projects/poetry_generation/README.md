# 📝 Poetry Generation using LSTM & GRU (Keras)

This project demonstrates how to generate poetry using Recurrent Neural Networks (RNNs) with LSTM / GRU layers in Keras. It includes training on multiple poem datasets and generating new poetic lines based on a seed text.

---

## 📁 Project Structure

- `poem_generator.ipynb`  
  Trains word-level LSTM & GRU models using a plain text file (`poem.txt`) containing a collection of poems. 

- `poetry_generator.ipynb`  
  A secondary notebook that trains similar models on another dataset loaded from a CSV file (`kaggle_poem_dataset.csv`).

---

## 📦 Datasets

1. `poem.txt` — A custom plain text file containing poems, used for training models.
2. `kaggle_poem_dataset.csv` — A structured CSV file with individual poems.

---

## 🧠 Model Summary

- Framework: TensorFlow/Keras
- Tokenization: Word-level
- Architecture:
  - Embedding layer
  - One or more LSTM /GRU layers (optionally Bidirectional)
  - Dense softmax output layer
- Loss Function: Categorical crossentropy
- Output: Poetic text generated one word at a time
- Temperature Sampling: Used to adjust randomness of generation

---

## 🚀 Features

- Accepts user-defined seed text
- Adjustable output length and creativity (temperature)
- Simple and extensible design

---

## ✅ Future Work
 
- Experiment Transformer models  
- Create a Gradio interface for interactive use  
- Fine-tune on specific poets or styles

---

## 🛠️ Requirements

- Python 3.x  
- TensorFlow / Keras  
- NumPy, Pandas

---

## 📄 License

This project is for educational purposes.
