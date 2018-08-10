from PIL import Image
import pytesseract
import webbrowser
import urllib
import os
import PIL.ImageOps
import time
import platform

start = time.time()
os.system("adb shell /system/bin/screencap -p /sdcard/screenshot.png")
if platform.system() == 'Windows':
    os.system("adb pull /sdcard/screenshot.png G:/workspace/py_ws/search_answer/imgs/")

if platform.system() == 'Windows':
    tessdata_dir_config = '--tessdata-dir "C:/Program Files/Tesseract-OCR/"'
else:
    tessdata_dir_config = None


image = Image.open('imgs/screenshot.png')
print(image.size)
region = (50,150,1000,1000)
image = image.convert("L")


image = image.crop(region)

# image = PIL.ImageOps.invert(image)

image.save("imgs/result1.jpg")

text = pytesseract.image_to_string(Image.open('imgs/result1.jpg'),lang='chi_sim' , config=tessdata_dir_config)
print(text)
text = ''.join(text.split())
new_text = text.encode('gbk')
new_text = urllib.parse.quote(new_text)
print(new_text)
if new_text:
    print("not empty")
    url = 'http://www.baidu.com/s?wd=%s' % new_text
    print(url)
    webbrowser.open(url)

end = time.time()

print(end - start)