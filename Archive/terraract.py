# try:
#     from PIL import Image
# except ImportError:
#     import Image
# import pytesseract
#
# # If you don't have tesseract executable in your PATH, include the following:
# #pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
# # Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
#
# # Simple image to string
# #print(pytesseract.image_to_boxes(Image.open('/Users/ryan/Desktop/a.png')))
#
# # French text image to string
# #print(pytesseract.image_to_string(Image.open('/Users/ryan/Desktop/a.png'), lang='fra'))
#
# # In order to bypass the image conversions of pytesseract, just use relative or absolute image path
# # NOTE: In this case you should provide tesseract supported images or tesseract will return error
# print(pytesseract.image_to_string('/Users/ryan/Desktop/a.png'))
#
# # Batch processing with a single file containing the list of multiple image file paths
# # print(pytesseract.image_to_string('/Users/ryan/Desktop/a.png'))
# #
# # # Get bounding box estimates
# # print(pytesseract.image_to_boxes(Image.open('/Users/ryan/Desktop/a.png')))
# #
# # # Get verbose data including boxes, confidences, line and page numbers
# # print(pytesseract.image_to_data(Image.open('/Users/ryan/Desktop/a.png')))
# #
# # # Get information about orientation and script detection
# # print(pytesseract.image_to_osd(Image.open('/Users/ryan/Desktop/a.png')))
# #
# # # Get a searchable PDF
# # pdf = pytesseract.image_to_pdf_or_hocr('/Users/ryan/Desktop/a.png', extension='pdf')
# #
# # # Get HOCR output
# # hocr = pytesseract.image_to_pdf_or_hocr('test.png', extension='hocr')

import cv2
from PIL import Image
import pytesseract


def ocr_core(filename):
    temp=cv2.resize(cv2.imread(filename),(3000,1785))
    #temp=cv2.GaussianBlur(temp,(11,11),0)
    #temp=cv2.medianBlur(temp,9)
    cv2.imshow('image',temp)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    text = pytesseract.image_to_string(temp,lang='eng')  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

print(ocr_core('/users/ryan/desktop/a.png'))

# img = cv2.resize(img,(3000,1785))
# img = cv2.GaussianBlur(img,(11,11),0)
# img = cv2.medianBlur(img,9)
# cv2.imshow('asd',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# txt = pytesseract.image_to_string(img)
# print('recognition:', txt)
