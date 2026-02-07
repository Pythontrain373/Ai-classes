import cv2

# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize video capture from the default camera (use webcam)
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()
while True:
    #Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture image.")
        break

    #Convert to greyscale

    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Detect faces in the greyscale image
    faces= face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    #Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w,y+h), (255,0,0),2)

        #Diasple the count of faces

    font= cv2.FONT_HERSHEY_SIMPLEX

    cv2.putText(frame, f'People Count: {len(faces)}', (10,30), font,1, (255,0,0),2)

    #Display the resulting frame with detected faces

    cv2.imshow('Face Tracking and counting', frame)

    #Exit the loop if 'q' is pressed

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Release the webcam and close the window

cap.release()
cv2.destroyAllWindows()