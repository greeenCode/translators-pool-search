# 이 스크립트를 실행하면 지정된 폴더와 그 하위 폴더 내의 모든 DOC 파일이 동일한 폴더 내에서 같은 파일명의 DOCX 파일로 변환됩니다.

import os
import win32com.client as win32

def convert_doc_to_docx(doc_path, word):
    # DOC 파일 열기
    doc = word.Documents.Open(doc_path)
    
    # DOCX 파일 경로 설정
    docx_path = os.path.splitext(doc_path)[0] + ".docx"
    
    # DOC 파일을 DOCX 파일로 저장
    doc.SaveAs(docx_path, FileFormat=16)  # 16 corresponds to wdFormatXMLDocument (.docx)
    
    # 문서 닫기
    doc.Close()

    return docx_path

def convert_docs_in_folder(source_folder):
    # Microsoft Word 애플리케이션 실행
    word = win32.Dispatch("Word.Application")
    word.Visible = False

    try:
        # 주어진 폴더와 하위 폴더를 재귀적으로 탐색
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                if file.lower().endswith(".doc") and not file.lower().endswith(".docx"):
                    doc_path = os.path.join(root, file)
                    try:
                        convert_doc_to_docx(doc_path, word)
                        print(f"Converted: {doc_path}")
                    except Exception as e:
                        print(f"Failed to convert: {doc_path} - {e}")
    finally:
        # Microsoft Word 애플리케이션 종료
        word.Quit()

# 사용 예시
source_folder = r"D:\Users\ie-woo\Documents\Google 드라이브\docs\인터비즈시스템N\_작업\2022 0516a 다국어 번역사\abba resource"
convert_docs_in_folder(source_folder)
