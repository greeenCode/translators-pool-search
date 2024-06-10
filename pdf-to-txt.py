import fitz  # PyMuPDF 라이브러리
import os

def extract_text_from_pdf(pdf_path):
    # PDF 문서 열기
    document = fitz.open(pdf_path)
    
    text = ""
    
    # 각 페이지에서 텍스트 추출
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()

    return text

def save_text_to_file(text, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(text)

def main(pdf_path):
    extracted_text = extract_text_from_pdf(pdf_path)
    
    # pdf_path와 같은 디렉토리 설정
    output_dir = os.path.dirname(pdf_path)
    
    # 디렉토리 생성 (이미 존재하는 경우에도 동작하게 설정)
    os.makedirs(output_dir, exist_ok=True)
    
    # 파일 이름에서 확장자 제거하고 .txt 확장자 추가
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    output_file_path = os.path.join(output_dir, f"{base_name}.txt")
    
    # 텍스트 저장
    save_text_to_file(extracted_text, output_file_path)
    print(f"Extracted text saved to {output_file_path}")

# 사용 예제
pdf_path = r'abba\장수진.pdf'
main(pdf_path)
