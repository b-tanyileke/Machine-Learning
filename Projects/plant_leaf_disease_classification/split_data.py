import os, shutil
import random

def split_data(source_dir, train_dir, val_dir, test_dir, split=(0.7, 0.2, 0.1)):
    """ This function is used to split a dataset into training, validation and testing sets"""
    for class_name in os.listdir(source_dir):
        class_path = os.path.join(source_dir, class_name)
        if not os.path.isdir(class_path):
            continue
        images = os.listdir(class_path)
        random.shuffle(images)
        n = len(images)
        train_n = int(split[0] * n)
        val_n = int(split[1] * n)

        # Create subfolders
        for folder in [train_dir, val_dir, test_dir]:
            os.makedirs(os.path.join(folder, class_name), exist_ok=True)

        for i, img in enumerate(images):
            src = os.path.join(class_path, img)
            if i < train_n:
                dst = os.path.join(train_dir, class_name, img)
            elif i < train_n + val_n:
                dst = os.path.join(val_dir, class_name, img)
            else:
                dst = os.path.join(test_dir, class_name, img)
            shutil.copy2(src, dst)


def main():
    # call split_data function. 
    # modify fill path based on your dataset location
    split_data(
        source_dir='Plant_Leave_Diseases',
        train_dir='plant_leave_disease/train',
        val_dir='plant_leave_disease/val',
        test_dir='plant_leave_disease/test'
)
    
if __name__ == "__main__":
    main()

