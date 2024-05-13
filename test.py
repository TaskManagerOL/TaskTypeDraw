from art import *
from PIL import Image, ImageDraw, ImageFont
import sys
import cv2

ASCII_CHARS = '@%#*+=-|_\/ '

def get_ascii_char(pixel_value):
    return ' ' if (pixel_value == 2 or pixel_value == 5) else ASCII_CHARS[pixel_value // 32] # 映射灰度值为字符

def image_to_ascii(image_path,output_path):
    image = Image.open(image_path)
    image = image.convert('L')  # 转换为灰度图像

    ascii_image = ''
    for y in range(image.size[1]):
        for x in range(image.size[0]):
            pixel = image.getpixel((x, y))
            ascii_character = get_ascii_char(pixel)
            ascii_image += ascii_character
        ascii_image += '\n'  # 换行

    with open(output_path, 'w') as f:
        f.write(ascii_image)

def cv_art():
    image = cv2.imread("text_image.png")
    cv2.imshow('Text Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def pillow_art(input_text):
    image = Image.new('RGB', (1000, 50), color = (255, 255, 255))
    font = ImageFont.truetype("fusion-pixel-12px-monospaced-zh_hans.ttf", 20) #emoji无法读取是这个字体的原因
    d = ImageDraw.Draw(image)
    d.text((10,10), input_text, font=font, fill=(0,0,0))
    image.save("text_image.png")

if __name__ == "__main__":
    # 从用户输入中获取中文字符
    with open('inputThere.txt', 'r', encoding='utf-8') as file:
        # 读取文件内容
        chinese_text = file.read()
        # 输出文件内容
        print(chinese_text)

    # 将中文字符转化为字符画
    pillow_art(chinese_text)
    cv_art()

    image_to_ascii('text_image.png', 'output.txt')

