import pytesseract
import cv2
import matplotlib.pyplot as plt
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'


if __name__ == '__main__':
    # coordinates to crop must be manually tuned
    c = [(760, 380), (1000, 420)]
    org_image = cv2.imread('example.jpg')
    cv2.rectangle(org_image, (c[0][0], c[0][1]), ((c[1][0], c[1][1])), color=(255, 0, 255), thickness=3)
    plt.figure(figsize=(10,10))
    plt.imshow(org_image)
    plt.show()

    # cropping image img = image[y0:y1, x0:x1]
    cropped_image = org_image[c[0][1]:c[1][1], c[0][0]:c[1][0]]
    plt.figure(figsize=(10,10))
    plt.imshow(cropped_image)
    plt.show()

    # convert the image to black and white for better OCR
    ret, thresh1 = cv2.threshold(cropped_image, 120, 255, cv2.THRESH_BINARY)
    plt.figure(figsize=(10,10))
    plt.imshow(thresh1)
    plt.show()
    # pytesseract image to string to get results
    text = str(pytesseract.image_to_string(thresh1, config='--psm 6', lang='fas'))
    with open('out.txt', 'w') as f:
        f.write(text)
