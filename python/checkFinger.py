# This code demonstrates how to show the location of hand landmarks and detect all fingers
import cv2
import mediapipe as mp

Nfing = 0  # Initialize the finger count to 0
cap = cv2.VideoCapture(0)

# Call hand pipeline module
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    fingerstring = ""
    finger = ["", "Thumb", "Index", "Middle", "Ring", "Pinky"]
    lastNfinger = 0
    Nfing = 0
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            Nfing = 0  # Reset finger count for each hand
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

                img.shape[1]
                
                if id == 3 and cx > handLms.landmark[4].y*h:
                    Nfing += 1
                    fingerstring += "Thumb "
                
                if id in [8, 12, 16, 20] and cy < handLms.landmark[id - 2].y * h:
                    Nfing += 1  # Thumb, Index, Middle, Ring, Pinky

                if id%4 == 0 and id != 0 and Nfing != lastNfinger:
                    fingerstring += finger[int(id/4)] + " "
                

                

                lastNfinger = Nfing
              



            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.putText(img, f"Finger Count: {Nfing}", (10, 70), cv2.FONT_HERSHEY_PLAIN, 1.5,
                (255, 0, 255), 2)
    text_size = cv2.getTextSize(fingerstring, cv2.FONT_HERSHEY_PLAIN, 1.5, 2)[0]

    text_x = (img.shape[1] - text_size[0]) // 2

    cv2.putText(img, fingerstring, (text_x, 400), cv2.FONT_HERSHEY_PLAIN, 1.5,
                (255, 0, 255), 2)
    cv2.imshow("Image", img)
    cv2.waitKey(1)

# Close all open windows
# cv2.destroyAllWindows()