import cv2
from PIL import Image
import pytesseract

def ocr_core(filename):
    #cv2.imshow('image',cv2.imread(filename))
    temp=cv2.resize(cv2.imread(filename),None,fx=3,fy=3)
    #temp=cv2.GaussianBlur(temp,(11,11),0)
    #temp=cv2.medianBlur(temp,9)
    cv2.imshow('image',temp)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    text = pytesseract.image_to_string(temp,lang='eng')  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

# img = Image.open("'/users/ryan/desktop/cropped.png")
# area = (400, 400, 800, 800)
# cropped_img = img.crop(area)
# cropped_img.show()
print(ocr_core('/users/ryan/desktop/cropped.png'))
