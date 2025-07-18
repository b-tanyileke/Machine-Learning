# Plant Leaf Disease Classification using Transfer Learning

This project contains two Jupyter notebooks and a Python script aimed at detecting plant leaf diseases using Convolutional Neural Networks (CNNs) with transfer learning.

## Project Structure

```
Plant-Leaf-Disease-Classification/
├── tomato_disease_detection.ipynb
├── plant_disease_detection.ipynb
├── split_data.py
├── README.md
```

- **tomato\_diseasse\_detection.ipynb**:

  - Focused on classifying tomato leaf diseases.
  - Models tested: VGG16, MobileNetV2, InceptionV3.
  - For each model:
    - First attempt: Base layers frozen.
    - Second attempt: Fine-tuning a few base layers.

- **plant\_disease\_detection.ipynb**:

  - Focused on classifying all 39 plant leaf disease classes from the PlantVillage dataset.
  - Model used: VGG16.
  - Two experiments:
    - Base layers frozen.
    - Fine-tuning a few base layers.

- **split\_data.py**:

  - Script to split raw image dataset into training, validation, and test sets.
  - Supports reproducibility and clean data management.

---

## Dataset

- **PlantVillage Dataset**:
  - The dataset is not included in this repository due to size constraints.
  - You can download it from Kaggle: [https://data.mendeley.com/datasets/tywbtsjrjv/1](https://data.mendeley.com/datasets/tywbtsjrjv/1)
  - Organize the dataset according to your directory structure and run `split_data.py` to create train/val/test splits.

---

## How to Use

1. Clone the repository:

2. Install required packages:
  - Only requirement is tensorflow

3. Prepare your dataset:

   - Download PlantVillage data.
   - Use `split_data.py` to split the data.

4. Run the notebooks:

---

## Highlights

- **Transfer Learning:** Pretrained VGG16, MobileNetV2, InceptionV3 models.
- **Fine-Tuning:** Comparison between frozen and partially trainable base layers.
- **Multi-Class Classification:** Includes both binary/multi-class classification (Tomato leaves) and full 39-class experiments.
- **Data Management:** Custom script for reproducible dataset splitting.

---

## License

This project is open-source and available under the MIT License.

---

## Acknowledgements

- PlantVillage Dataset
- TensorFlow/Keras


