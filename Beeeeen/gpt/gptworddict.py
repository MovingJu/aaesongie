# 유의어와 반의어를 포함하는 딕셔너리
word_dict = {
    "happy": {"synonyms": ["joyful", "cheerful"], "antonyms": ["sad", "unhappy"]},
    "cold": {"synonyms": ["chilly", "frigid"], "antonyms": ["hot", "warm"]},
    "big": {"synonyms": ["large", "huge"], "antonyms": ["small", "tiny"]}
}

# 검색할 단어 입력 받기
search_word = input("검색할 단어를 입력하세요: ")

# 딕셔너리에서 검색한 단어의 유의어와 반의어 출력
if search_word in word_dict:
    synonyms = word_dict[search_word]["synonyms"]
    antonyms = word_dict[search_word]["antonyms"]
    print(f"{search_word}의 유의어: {', '.join(synonyms)}")
    print(f"{search_word}의 반의어: {', '.join(antonyms)}")
else:
    print(f"'{search_word}'에 대한 정보를 찾을 수 없습니다.")
