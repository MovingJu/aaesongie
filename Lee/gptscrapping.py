import requests
from bs4 import BeautifulSoup

# 웹페이지의 HTML 가져오기
url = "https://namu.wiki/w/%EB%8D%94%EC%8A%A4%ED%8B%B4%20%EB%8B%88%ED%8D%BC%ED%8A%B8?from=%EB%8B%88%ED%8D%BC%ED%8A%B8"
response = requests.get(url)
html_content = response.text

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(html_content, "html.parser")

# 클래스 번호가 "example-class"인 요소 찾기
elements = soup.find_all(class_="BXgio0S3")

print(type(elements))
# 요소 출력
for element in elements:
    print(element.text)
