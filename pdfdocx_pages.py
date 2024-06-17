# 소스폴더 내 모든 pdf, docx, doc 파일, 페이지 수 출력

import os
import pandas as pd
from PyPDF2 import PdfReader
import docx

# 소스 및 타겟 폴더 경로
source_folder = r'D:\Users\ie-woo\Documents\Google 드라이브\docs\인터비즈시스템N\_작업\2022 0516a 다국어 번역사'
target_folder = r'D:\Users\ie-woo\Documents\Google 드라이브\docs\인터비즈시스템N\_작업\2022 0516a 다국어 번역사\@Translators-Pool-Search'

# 엑셀 저장 경로
excel_path = os.path.join(target_folder, 'filelist_withpage.xlsx')

# 모든 파일 경로를 리스트에 저장
pdf_files = []
docx_files = []
doc_files = []
for root, dirs, files in os.walk(source_folder):
    # '@'가 폴더명에 포함된 경우 건너뜀
    if '@' in root:
        continue
    for file in files:
        # '@'가 파일명에 포함되지 않으며, 확장자가 '.pdf', '.PDF', '.docx', '.DOCX', '.doc', '.DOC'인 경우
        if file.lower().endswith('.pdf') and '@' not in file:
            pdf_files.append(os.path.join(root, file))
        elif file.lower().endswith('.docx') and '@' not in file:
            docx_files.append(os.path.join(root, file))
        elif file.lower().endswith('.doc') and '@' not in file:
            doc_files.append(os.path.join(root, file))

# PDF 파일 정보 추출
file_info_list = []
processed_count_pdf = 0
error_files_pdf = []
for pdf_file in pdf_files:
    try:
        pdf = PdfReader(pdf_file)
        num_pages = len(pdf.pages)
        file_info_list.append({
            '파일명': os.path.basename(pdf_file),
            '링크': pdf_file,
            '페이지수': num_pages,
            '확장자': 'pdf'
        })
        processed_count_pdf += 1
    except Exception as e:
        error_files_pdf.append(pdf_file)
        print(f"Error processing {pdf_file}: {e}")

# DOCX 파일 정보 추출
processed_count_docx = 0
error_files_docx = []
for docx_file in docx_files:
    try:
        doc = docx.Document(docx_file)
        num_pages = len(doc.element.xpath('//w:sectPr'))
        file_info_list.append({
            '파일명': os.path.basename(docx_file),
            '링크': docx_file,
            '페이지수': num_pages,
            '확장자': 'docx'
        })
        processed_count_docx += 1
    except Exception as e:
        error_files_docx.append(docx_file)
        print(f"Error processing {docx_file}: {e}")

# DOC 파일 정보 추출 (단순히 확장자만 다르므로 같은 방식 사용)
processed_count_doc = 0
error_files_doc = []
for doc_file in doc_files:
    try:
        doc = docx.Document(doc_file)
        num_pages = len(doc.element.xpath('//w:sectPr'))
        file_info_list.append({
            '파일명': os.path.basename(doc_file),
            '링크': doc_file,
            '페이지수': num_pages,
            '확장자': 'doc'
        })
        processed_count_doc += 1
    except Exception as e:
        error_files_doc.append(doc_file)
        print(f"Error processing {doc_file}: {e}")

# 데이터프레임 생성
df = pd.DataFrame(file_info_list, columns=['파일명', '링크', '페이지수', '확장자'])

# 엑셀 파일로 저장
with pd.ExcelWriter(excel_path, engine='xlsxwriter') as writer:
    df.to_excel(writer, index=False, sheet_name='Files')
    
    # 워크북과 워크시트 객체 가져오기
    workbook  = writer.book
    worksheet = writer.sheets['Files']

    # 링크 컬럼에 하이퍼링크 추가
    for row_num, link in enumerate(df['링크'], start=1):
        worksheet.write_url(f'B{row_num + 1}', f'file:///{link}', string=link)

# 파일 수 출력
print(f"폴더 내 PDF 총 파일 수: {len(pdf_files)}")
print(f"엑셀에 저장된 PDF 파일 수: {processed_count_pdf}")

print(f"폴더 내 DOCX 총 파일 수: {len(docx_files)}")
print(f"엑셀에 저장된 DOCX 파일 수: {processed_count_docx}")

print(f"폴더 내 DOC 총 파일 수: {len(doc_files)}")
print(f"엑셀에 저장된 DOC 파일 수: {processed_count_doc}")

# 에러가 발생한 파일 경로 출력
if error_files_pdf or error_files_docx or error_files_doc:
    print("\n에러가 발생한 파일 경로:")
    for error_file in error_files_pdf:
        print(f"PDF 파일: {error_file}")
    for error_file in error_files_docx:
        print(f"DOCX 파일: {error_file}")
    for error_file in error_files_doc:
        print(f"DOC 파일: {error_file}")

print(f"엑셀 파일이 '{excel_path}'에 생성되었습니다.")
