import os
import pandas as pd
from datetime import datetime

# 소스 폴더와 타겟 경로 설정
source_folder = r'D:\Users\ie-woo\Documents\Google 드라이브\docs\인터비즈시스템N\_작업\2022 0516a 다국어 번역사'
target_folder = r'D:\Users\ie-woo\Documents\GitHub\ABBA Communication\pdf-to-txt\abba\extracted'
target_path = os.path.join(target_folder, 'file_info.xlsx')

# 기본 파일 수정일 설정
default_file_date = datetime(2000, 1, 1)

# 파일 목록과 파일 수정일을 저장할 리스트
file_data = []

# 제외할 시스템 파일 및 폴더 목록
system_files = ['desktop.ini', 'Thumbs.db']
excluded_char = '#'

# 특정일 이후 파일로 진행할지 물어봄
use_default_date = input(f"Do you want to use the default file date {default_file_date.date()}? (yes/y to use default): ").strip().lower()

if use_default_date in ('yes', 'y', ''):
    modified_file_date = default_file_date
else:
    date_input = input("Enter the modified file date (YYYY-MM-DD): ").strip()
    try:
        modified_file_date = datetime.strptime(date_input, '%Y-%m-%d')
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        exit()

# 소스 폴더와 하위 폴더 내 모든 파일의 개수를 계산
file_count = 0
for root, dirs, files in os.walk(source_folder):
    # 폴더 이름에 제외할 문자가 포함된 경우 제외
    dirs[:] = [d for d in dirs if excluded_char not in d]
    # 파일 이름에 제외할 문자가 포함된 경우 및 시스템 파일 제외
    files = [file for file in files if file not in system_files and excluded_char not in file]
    for file in files:
        file_path = os.path.join(root, file)
        file_modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
        if file_modified_time > modified_file_date:
            file_count += 1

# 파일 개수를 출력하고 계속 진행할지 물어봄
print(f"Total number of files in '{source_folder}' modified after {modified_file_date.date()}: {file_count}")
proceed = input("Do you want to proceed? (yes/y to continue): ").strip().lower()

if proceed in ('yes', 'y', ''):
    for root, dirs, files in os.walk(source_folder):
        # 폴더 이름에 제외할 문자가 포함된 경우 제외
        dirs[:] = [d for d in dirs if excluded_char not in d]
        for file in files:
            if file not in system_files and excluded_char not in file:  # 시스템 파일 및 제외할 문자 포함 파일 제외
                file_path = os.path.join(root, file)
                file_modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                if file_modified_time > modified_file_date:
                    file_link = f'=HYPERLINK("{file_path}")'
                    file_data.append((file, file_modified_time, file_link))
    
    # 데이터프레임 생성
    df = pd.DataFrame(file_data, columns=['File Name', 'Last Modified', 'File Link'])
    
    # 타겟 폴더가 존재하지 않으면 생성
    os.makedirs(target_folder, exist_ok=True)
    
    # 기존 엑셀 파일이 존재하는 경우, 기존 데이터에 추가
    if os.path.exists(target_path):
        existing_df = pd.read_excel(target_path)
        df = pd.concat([existing_df, df], ignore_index=True)
    
    # 엑셀 파일로 저장
    df.to_excel(target_path, index=False)
    print(f"File information saved to '{target_path}'")
else:
    print("Process aborted by the user.")
