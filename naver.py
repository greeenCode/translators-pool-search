from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# ChromeDriver 경로 설정
chrome_driver_path = r'C:\Util\chromedriver-win64\chromedriver.exe'

# ChromeDriver 서비스 객체 생성
service = Service(chrome_driver_path)

# ChromeDriver 옵션 설정 (필요시)
options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # 브라우저 창을 띄우지 않으려면 주석 해제
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# WebDriver 객체 생성
driver = webdriver.Chrome(service=service, options=options)

# Naver 홈페이지 열기
driver.get('https://www.naver.com')

# 현재 페이지의 제목 출력 (제대로 작동하는지 확인)
print(driver.title)

# 사용자 입력을 기다리기 (엔터 키를 누르면 종료)
input("Press Enter to quit...")

# WebDriver 종료
driver.quit()
