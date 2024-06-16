from docx import Document

def extract_text_from_docx(file_path):
    doc = Document(file_path)
    full_text = []
    
    # 문서의 모든 문단을 순회하며 텍스트를 추출
    for para in doc.paragraphs:
        full_text.append(para.text)
    
    # 문서의 모든 표를 순회하며 텍스트를 추출
    for table in doc.tables:
        for row in table.rows:
            row_text = []
            for cell in row.cells:
                row_text.append(cell.text)
            full_text.append('\t'.join(row_text))
    
    return '\n'.join(full_text)

# 사용 예시
file_path = r'D:\Users\ie-woo\Documents\Google 드라이브\docs\인터비즈시스템N\_작업\2022 0516a 다국어 번역사\영어\위미정_2023SEP.docx'  # 여기에 .docx 파일 경로를 입력하세요.
extracted_text = extract_text_from_docx(file_path)
print(extracted_text)
