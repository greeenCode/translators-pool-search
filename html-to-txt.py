from bs4 import BeautifulSoup
import os

def extract_text_from_html(html_file):
    # HTML 파일 열기
    with open(html_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        
        # 텍스트 추출
        text = soup.get_text()
    
    return text

def save_text_to_file(text, output_file):
    # 텍스트를 파일에 쓰기
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(text)

def main():
    # 변환할 HTML 파일 경로
    html_file = "abba\Domullodzhon_202206210200021.html"  # 여기서 변환할 HTML 파일 경로를 지정하세요.
    
    # 텍스트 추출
    text = extract_text_from_html(html_file)
    
    # 저장할 파일명 설정
    output_file = os.path.splitext(html_file)[0] + ".txt"
    
    # 텍스트를 파일로 저장
    save_text_to_file(text, output_file)
    
    print(f"텍스트가 {output_file}로 성공적으로 추출되었습니다.")

if __name__ == "__main__":
    main()
