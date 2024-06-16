# checkpoint에 저장된 처리된 파잂명, 시각, 저장정보 출력

import os
import pickle
from datetime import datetime

# Configurations
target_folder = r'D:\Users\ie-woo\Documents\Google 드라이브\docs\인터비즈시스템N\_작업\2022 0516a 다국어 번역사\@Translators-Pool-Search'
checkpoint_path = os.path.join(target_folder, 'checkpoint.pkl')

def load_checkpoint(checkpoint_path):
    if os.path.exists(checkpoint_path):
        with open(checkpoint_path, 'rb') as f:
            checkpoint_data = pickle.load(f)
            return checkpoint_data
    else:
        print("Checkpoint file does not exist.")
        return None

def display_checkpoint(checkpoint_data):
    if not checkpoint_data:
        print("No data to display.")
        return

    processed_files_data = checkpoint_data.get('processed_files', [])
    current_batch_data = checkpoint_data.get('current_batch', [])

    print("Processed Files:")
    for entry in processed_files_data:
        file_path = entry.get('file_path', 'Unknown')
        processed_time = entry.get('processed_time', 'Unknown')
        if isinstance(processed_time, datetime):
            processed_time = processed_time.strftime('%Y-%m-%d %H:%M:%S')
        print(f"File Path: {file_path}, Processed Time: {processed_time}")

    print("\nCurrent Batch Data:")
    for entry in current_batch_data:
        print("---- Individual Data ----")
        for key, value in entry.items():
            print(f"{key}: {value}")
        print("---------------------------")

if __name__ == "__main__":
    checkpoint_data = load_checkpoint(checkpoint_path)
    display_checkpoint(checkpoint_data)
