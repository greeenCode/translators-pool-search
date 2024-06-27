# 이 스크립트를 실행하면 지정된 폴더 내 모든 .doc 파일이 filename@.doc 형식으로 이름이 변경됩니다. 이 스크립트는 동일한 폴더 구조를 유지하면서 파일 이름만 변경합니다.
# 실행 전 작업대상 파일 수 출력, 계속여부 확인

import os

source_folder = r"D:\Users\ie-woo\Documents\Google 드라이브\docs\인터비즈시스템N\_작업\2022 0516a 다국어 번역사\abba resource"

def count_doc_files(folder):
    count = 0
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.lower().endswith(".doc"):  # .doc 및 .DOC 파일 모두 포함
                count += 1
    return count

def rename_files_in_folder(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.lower().endswith(".doc"):  # .doc 및 .DOC 파일 모두 포함
                old_path = os.path.join(root, file)
                new_file_name = file.replace(".doc", "@.doc").replace(".DOC", "@.DOC")
                new_path = os.path.join(root, new_file_name)
                os.rename(old_path, new_path)
                print(f'Renamed: {old_path} to {new_path}')  # 변경 내용을 출력

doc_count = count_doc_files(source_folder)
print(f"Number of .doc/.DOC files to be renamed: {doc_count}")

if doc_count > 0:
    proceed = input("Do you want to continue with renaming? (y/n): ").strip().lower()
    if proceed == 'y':
        rename_files_in_folder(source_folder)
        print("Renaming completed.")
    else:
        print("Renaming aborted.")
else:
    print("No .doc/.DOC files found to rename.")
