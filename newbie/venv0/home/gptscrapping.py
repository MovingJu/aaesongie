import requests
from bs4 import BeautifulSoup

# 웹페이지의 HTML 가져오기
url = "https://namu.wiki/w/%EB%82%98%EB%AC%B4%EC%9C%84%ED%82%A4:%EB%8C%80%EB%AC%B8"
response = requests.get(url)
html_content = response.text

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(html_content, "html.parser")

# 클래스 번호가 "example-class"인 요소 찾기
elements = soup.find_all(class_="D8mMMoro")

# 요소 출력
for element in elements:
    print(element.text)
