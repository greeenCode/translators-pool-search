# 저장된 checkpoint 파일에서 파일명 - 처리 시각 - +d 형태로 출력

import os
import pickle
from datetime import datetime

checkpoint_path = r"D:\Users\ie-woo\Documents\Google 드라이브\docs\인터비즈시스템N\_작업\2022 0516a 다국어 번역사\@Translators-Pool-Search\checkpoint.pkl"

# Checkpoint loading
if os.path.exists(checkpoint_path):
    with open(checkpoint_path, 'rb') as f:
        checkpoint_data = pickle.load(f)
        processed_files = checkpoint_data.get('processed_files', [])
        
        # 처리된 파일 목록 화면에 출력
        print("처리된 파일 목록:")
        previous_time = None
        for idx, file_info in enumerate(processed_files, 1):
            file_name = os.path.basename(file_info['file_path'])
            processed_time = file_info['processed_time']
            processed_time_str = processed_time.strftime('%Y-%m-%d %H-%M-%S')
            if previous_time:
                time_diff = (processed_time - previous_time).total_seconds()
            else:
                time_diff = 0
            print(f"{idx}. {file_name} -- {processed_time_str} +{int(time_diff)}")
            previous_time = processed_time
else:
    processed_files = []
