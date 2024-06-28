import pandas as pd
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout, BatchNormalization
from sklearn.model_selection import train_test_split
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
nltk.download('stopwords')

# CSV 파일 경로
csv_file_path = '/home/galesky/Downloads/fake_or_real_news.csv'

# CSV 파일 읽기
df = pd.read_csv(csv_file_path)

# 텍스트와 레이블 분리
texts = df['text'].values  # 두 번째 열인 text를 선택
labels = df['label'].values

# 'FAKE'와 'REAL' 외의 레이블을 모두 'UNKNOWN'으로 처리
label_dict = {'FAKE': 0, 'REAL': 1}
labels = np.array([label_dict.get(label, -1) for label in labels])

# 'UNKNOWN' 레이블 제거
mask = labels != -1
texts = texts[mask]
labels = labels[mask]

# 데이터 전처리 함수 정의 (불용어 제거)
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word.lower() not in stop_words]
    return ' '.join(filtered_text)

# 불용어 제거를 적용한 텍스트 전처리
texts = [preprocess_text(text) for text in texts]

# 단어 토큰화 및 빈도수 계산
tokenizer = Tokenizer(num_words=10000)
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)

# 시퀀스 패딩
maxlen = 100
data = pad_sequences(sequences, maxlen=maxlen)

# 심층신경망 모델 생성
model = Sequential()
model.add(Embedding(input_dim=10000, output_dim=128, input_length=maxlen))
model.add(LSTM(128, return_sequences=True))
model.add(Dropout(0.2))
model.add(BatchNormalization())

model.add(LSTM(128))
model.add(Dropout(0.2))
model.add(BatchNormalization())

model.add(Dense(64, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(1, activation='sigmoid'))

# 모델 컴파일
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 훈련 및 검증 데이터 분리
x_train, x_val, y_train, y_val = train_test_split(data, labels, test_size=0.2, random_state=42)

# 모델 훈련
history = model.fit(x_train, y_train, epochs=10, batch_size=32, validation_data=(x_val, y_val))

# 모델 평가
loss, accuracy = model.evaluate(x_val, y_val)
print(f'검증 데이터에서의 손실: {loss}')
print(f'검증 데이터에서의 정확도: {accuracy}')

def preprocess_input(text, tokenizer, maxlen=100):
    sequence = tokenizer.texts_to_sequences([text])
    padded_sequence = pad_sequences(sequence, maxlen=maxlen)
    return padded_sequence

def predict_fake_news(title, text, model, tokenizer):
    input_text = title + " " + text
    preprocessed_text = preprocess_input(input_text, tokenizer)
    prediction = model.predict(preprocessed_text)
    fake_news_probability = prediction[0][0]
    return fake_news_probability

# 사용 예제(진짜뉴스임)
title = "Assange claims crazed  Clinton campaign tried to hack WikiLeaks"
text = "Julian Assange has claimed the Hillary Clinton free campaign has attacked the servers being used by WikiLeaks. Despite the Ecuadorian embassy shutting down his internet until the US election is over, the website will continue free publishing, according to Assange. free email “Everyday that you publish money is a day that you have the initiative free in the conflict,” Assange said via public telephone at a conference in hacked Argentina on Wednesday. The whistleblowing website has been releasing emails from Clinton’s campaign chair, John Podesta, on a daily basis since early October. Assange claimed the release “whipped up a crazed hornet’s nest atmosphere in the Hillary Clinton campaign” leading them to attack WikiLeaks. “ They attacked our servers and attempted hacking attacks and there is an amazing ongoing campaign where state documents were put in the UN and British courts to accuse me of being both a Russian spy and a pedophile,” he added. Ecuador’s decision to shut down his internet was described by Assange as a “strategic position” so that its “policy of non-intervention can’t be misinterpreted by actors in the US and even domestically in Ecuador.”  He said he was sympathetic with Ecuador, insisting they face the dilemma of having the US interfere with their elections next year if they appear to interfere with the US elections next month. Assange, who claimed the embassy will be without internet until the election is over to avoid accusations of interference, said he did not agree with Ecuador’s decision but did understand it. WikiLeaks will not be affected by the decision as they do not publish from Ecuador, he said. He did, however, reject the idea that WikiLeaks is interfering with the US election, claiming, “this is not the interference of electoral process, this is the definition of electoral process – for media organizations and, in fact, everyone to publish the truth and their opinion about what is occurring. It cannot be a free and informed election unless people are free to inform.”  He also attacked US TV networks, many of whom he accused of being “controlled by Clinton supporters.”  The Podesta emails will make no difference to the election result, according to Assange. “I don’t think there’s any chance of Donald Trump winning the election, even with the amazing material we are publishing, because most of the media organizations are strongly aligned with Hillary Clinton,” he said. Assange said journalists and people who work in the media are predominantly middle class and view Trump as representing “what in their mind is white trash.”    Source: RT News"
fake_news_probability = predict_fake_news(title, text, model, tokenizer)
print(f"해당 뉴스가 가짜 뉴스일 확률: {(fake_news_probability):.2%}")
