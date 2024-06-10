from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def extract_text_from_html(file_path):
    text = ""
    try:
        # Selenium 옵션 설정
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # 브라우저 창을 띄우지 않음
        # chrome_options.add_argument("--disable-gpu")  # GPU 사용 안함
        chrome_options.add_argument("--no-sandbox")  # 샌드박스 모드 사용 안함

        # ChromeDriver 경로 설정
        chrome_driver_path = r'C:\Util\chromedriver-win64\chromedriver.exe'  # ChromeDriver 경로로 변경
        service = Service(chrome_driver_path)

        # 브라우저 열기
        driver = webdriver.Chrome(service=service, options=chrome_options)

        try:
            # HTML 파일 열기
            driver.get(f'file:///{os.path.abspath(file_path)}')
            
            # 잠시 대기하여 페이지가 완전히 로드되도록 함
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
            
            # 페이지의 전체 텍스트 추출
            text = driver.find_element(By.TAG_NAME, 'body').text
            
        except Exception as e:
            print(f"Error extracting text from HTML {file_path}: {e}")
            
        finally:
            # 드라이버 종료
            driver.close()
            driver.quit()
            
    except Exception as e:
        print(f"Error initializing WebDriver: {e}")
    
    return text

