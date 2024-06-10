import os
from collections import Counter

def count_files_and_extensions(source_folder):
    # 파일 개수와 확장자별 개수를 저장할 변수 초기화
    total_files = 0
    extension_counts = Counter()

    # 소스 폴더와 그 하위 폴더를 순회
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            # 파일 개수 증가
            total_files += 1

            # 파일 확장자 추출 및 개수 증가
            extension = os.path.splitext(file)[1]
            extension_counts[extension] += 1

    return total_files, extension_counts

# 소스 폴더 지정
source_folder = r"D:\Users\ie-woo\Documents\Google 드라이브\docs\인터비즈시스템N\_작업\2022 0516a 다국어 번역사"

# 함수 호출
total_files, extension_counts = count_files_and_extensions(source_folder)

# 결과 출력
print(f"총 파일 개수: {total_files}")
print("파일 확장자별 개수:")
for extension, count in extension_counts.items():
    print(f"{extension}: {count}")
