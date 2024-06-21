import cv2
import mediapipe as mp

# Mediapipe hands 모델 초기화
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# 웹캠 캡처 객체 초기화
cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        # 이미지를 RGB로 변환
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # 손 랜드마크 탐지
        results = hands.process(image)

        # 이미지를 다시 BGR로 변환
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # 손 랜드마크 그리기
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
                # 랜드마크 좌표 추출
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]

                # 집게손 모양 인식 (엄지와 집게가 가까이 있고 중지는 멀리 떨어져 있는지 확인)
                thumb_index_dist = ((thumb_tip.x - index_finger_tip.x) ** 2 + (thumb_tip.y - index_finger_tip.y) ** 2) ** 0.5
                index_middle_dist = ((index_finger_tip.x - middle_finger_tip.x) ** 2 + (index_finger_tip.y - middle_finger_tip.y) ** 2) ** 0.5

                if thumb_index_dist < 0.05 and index_middle_dist > 0.1:
                    cv2.putText(image, 'Warning: Pinch Gesture Detected!', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

        # 이미지 출력
        cv2.imshow('Hand Gesture Recognition', image)

        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
