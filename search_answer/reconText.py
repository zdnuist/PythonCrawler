from PIL import Image
import pytesseract
import webbrowser
import urllib

image = Image.open('imgs/WechatIMG3.png')
print(image.size)
region = (50,50,1000,1000)
image = image.convert("L")


image = image.crop(region)

image.save("imgs/result1.jpg")

text = pytesseract.image_to_string(Image.open('imgs/result1.jpg'),lang='chi_sim')
print(text)
text = ''.join(text.split())
new_text = text.encode('gbk')
new_text = urllib.parse.quote(new_text)
print(new_text)
url = 'http://www.baidu.com/s?wd=%s' % new_text
print(url)
webbrowser.open(url)