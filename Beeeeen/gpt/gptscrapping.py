import requests
from bs4 import BeautifulSoup

# 웹페이지의 HTML 가져오기
url = "https://www.signal.bz/"
response = requests.get(url)
html_content = response.text

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(html_content, "html.parser")

# 클래스 번호가 "example-class"인 요소 찾기
elements = soup.find_all(class_="web tch-has")

# 요소 출력
for element in elements:
    print(element.text)
