import requests
from bs4 import BeautifulSoup

# 웹 페이지 URL
url = "https://namu.wiki/w/%EC%8B%A4%EC%8B%9C%EA%B0%84%20%EA%B2%80%EC%83%89%EC%96%B4"

# requests를 사용하여 HTML 가져오기
response = requests.get(url)
html_content = response.text

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(html_content, 'html.parser')

# div 태그 찾기
div_tag = soup.find('div', class_='viIaFwOi khkcFwKY')

# div 태그 안에 있는 a 태그 찾기
a_tags = div_tag.find_all('a')

# a 태그의 내용물 출력
for a_tag in a_tags:
    print(a_tag.text)
