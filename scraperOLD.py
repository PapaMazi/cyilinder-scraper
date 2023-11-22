from PIL import Image
import cv2 
import pytesseract
import numpy as np
import pyautogui
import pyperclip, time

# pytesseract.pytesseract.tesseract_cmd = r"C:\Users\papam\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

## OCR method

# path = 'to_scrape.png'

# image = cv2.imread(path)
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# data = pytesseract.image_to_string(gray, lang='eng', config='--psm 6')

# print(data)

## pyautogui method
# find coords of "Cylinder_0001"
# mouse click with pyautogui
# copy text and paste to dict in python
# repeat until all cylinder done
# output .csv file

# text = 'Cylinder_0001'

# screenshot = pyautogui.screenshot()

# # Convert the screenshot to grayscale
# img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

# # Find the provided text (text) on the grayscale screenshot 
# # using the provided language (lang)
# data = pytesseract.image_to_data(img, lang='eng', output_type='data.frame')

# # Find the coordinates of the provided text (text)
# try:
#     x_coord, y_coord = data[data['text'] == text]['left'].iloc[0], data[data['text'] == text]['top'].iloc[0]
#     # print(x,y) # print check
    
#     pyautogui.click(x = x_coord, y = y_coord) # click on 'Cylinder_0001' to select it

#     for i in range(20):
#         pyautogui.hotkey('ctrl', 'c')
#         title = pyperclip.paste()

#         pyautogui.press('down') 
#         pyautogui.hotkey('ctrl', 'c')
#         value = pyperclip.paste()
#         print(title," ",value)

# except IndexError:
#     # The text was not found on the screen
#     print("text not found")

pyautogui.keyDown('alt')
time.sleep(.2)
pyautogui.press('tab')
time.sleep(.2)
pyautogui.keyUp('alt')

for i in range(20):
    pyautogui.hotkey('ctrl', 'c')
    title = pyperclip.paste()

    pyautogui.press('down') 
    pyautogui.hotkey('ctrl', 'c')
    value = pyperclip.paste()
    pyautogui.press('down') 
    print(title," ",value)
    