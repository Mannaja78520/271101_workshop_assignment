import cv2
import mediapipe as mp

finger = 0
cap = cv2.VideoCapture(0)

#Call hand pipe line module
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    
    finger = ""
    cxSet = []
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                cxSet.append(cx)
                # print(id, cx, cy)
                if id % 4 == 0:
                    if cxSet[id] > cxSet[id-1]:
                        if id == 4:
                            finger = "Thumb"
                        if id == 8 :
                            finger = "Index"
                        if id == 12:
                            finger = "Middle"
                        if id == 16:
                            finger = "Ring"
                        if id == 20:
                            finger = "Pinky"

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    text_size = cv2.getTextSize(str(finger), cv2.FONT_HERSHEY_SIMPLEX, 3, 3)[0]
    # Calculate the position to center the text
    text_x = (img.shape[1] - text_size[0]) // 2

    cv2.putText(img, str(finger), (text_x + 30, 470), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)
    
    cv2.putText(img, str("Man"), (img.shape[1] - 100, 470), cv2.FONT_HERSHEY_PLAIN, 3,
                (0, 120, 255), 3)
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)
#Closeing all open windows
#cv2.destroyAllWindows()