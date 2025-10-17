import cv2
from fer import FER

def detect_mood():
    cap = cv2.VideoCapture(0)
    detector = FER(mtcnn=True)
    print("Press 'q' to capture mood from webcam.")

    mood = None
    while True:
        ret, frame = cap.read()
        if not ret:
            continue
        cv2.imshow("Mood Detection", frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            result = detector.top_emotion(frame)
            if result:
                mood = result[0]
            break

    cap.release()
    cv2.destroyAllWindows()
    return mood
