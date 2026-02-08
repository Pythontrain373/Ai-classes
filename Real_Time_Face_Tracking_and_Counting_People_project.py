import cv2

def rotate_image(image, angle):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, matrix, (w, h))
    return rotated

def adjust_brightness(image, value=30):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value
    final_hsv = cv2.merge((h, s, v))
    bright_img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return bright_img

def crop_to_face(image):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    if len(faces) == 0:
        return image  
    (x, y, w, h) = faces[0]
    margin = 20
    x_start = max(x - margin, 0)
    y_start = max(y - margin, 0)
    x_end = min(x + w + margin, image.shape[1])
    y_end = min(y + h + margin, image.shape[0])
    cropped = image[y_start:y_end, x_start:x_end]
    return cropped

def process_image(input_path, output_path, rotation_angle=0, brightness_value=30):
    image = cv2.imread(input_path)
    if image is None:
        raise FileNotFoundError(f"Image not found at {input_path}")
    rotated = rotate_image(image, rotation_angle)
    brightened = adjust_brightness(rotated, brightness_value)
    cropped = crop_to_face(brightened)
    cv2.imwrite(output_path, cropped)

process_image('small_image.jpg', 'small_image_processed.jpg', rotation_angle=5, brightness_value=40)
