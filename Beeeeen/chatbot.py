from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# ChatBot 객체 생성
chatbot = ChatBot("MyChatBot")

# 챗봇 훈련
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.korean")

# 채팅 시작
print("챗봇과 대화를 시작합니다. 종료하려면 '종료'를 입력하세요.")
while True:
    user_input = input("사용자: ")
    if user_input == "종료":
        print("챗봇과의 대화를 종료합니다.")
        break

    response = chatbot.get_response(user_input)
    print("챗봇:", response)
