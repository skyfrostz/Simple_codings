import cv2
import numpy as np
# from pyzbar.pyzbar import decode
from collections import Counter
import zxing

# 读取图像
image = cv2.imread('image.png')

# 解码所有二维码
reader = zxing.BarCodeReader()
decoded_objects = reader.decode('image.png')

# 检查解码结果是否为空
if decoded_objects is None:
    print("未能解码任何二维码")
    exit()

# 获取二维码信息
def get_dominant_color(image, rect):
    x, y, w, h = rect
    qr_region = image[y:y+h, x:x+w]
    qr_region = cv2.cvtColor(qr_region, cv2.COLOR_BGR2RGB)
    pixels = np.float32(qr_region.reshape(-1, 3))
    n_colors = 5
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, 0.1)
    flags = cv2.KMEANS_RANDOM_CENTERS
    _, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)
    _, counts = np.unique(labels, return_counts=True)
    dominant_color = palette[np.argmax(counts)]
    return dominant_color

def classify_color(rgb_color):
    colors = {
        "black": [0, 0, 0],
        "white": [255, 255, 255],
        "red": [255, 0, 0],
        "green": [0, 255, 0],
        "blue": [0, 0, 255]
    }
    color_name = min(colors.keys(), key=lambda color: np.linalg.norm(np.array(colors[color]) - rgb_color))
    return color_name

# 遍历解码的二维码并识别颜色
for obj in decoded_objects:
    rect = obj.rect
    dominant_color = get_dominant_color(image, (rect.left, rect.top, rect.width, rect.height))
    color_name = classify_color(dominant_color)
    content = obj.data.decode('utf-8')
    print(f"QR内容: {content}, 颜色: {color_name}")
