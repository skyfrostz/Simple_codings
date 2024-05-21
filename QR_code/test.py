import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 读取图像
image = cv2.imread('qrcode.png')

# 创建二维码检测器
qrCodeDetector = cv2.QRCodeDetector()

# 检测并解码二维码
decodedText, points, _ = qrCodeDetector.detectAndDecode(image)

# 如果检测到二维码
if points is not None:
    points = points[0].astype(np.int32)
    # 画出二维码的位置
    for i in range(len(points)):
        pt1 = tuple(points[i])
        pt2 = tuple(points[(i + 1) % 4])
        cv2.line(image, pt1, pt2, color=(255, 0, 0), thickness=2)
    
    # 显示解码的文本
    print("Decoded Text: ", decodedText)

    # 创建掩膜
    mask = np.zeros(image.shape[:2], dtype=np.uint8)
    cv2.fillPoly(mask, [points], 255)

    # 提取框内的区域
    masked_image = cv2.bitwise_and(image, image, mask=mask)

    # 获取框内区域的像素
    masked_pixels = image[mask == 255]

    # 使用 K-Means 聚类算法识别主要颜色
    k = 1  # 选择 1 个聚类中心
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(masked_pixels)
    colors = kmeans.cluster_centers_.astype(int)

    # 打印主要颜色
    for i, color in enumerate(colors):
        print(f"Main Color {i + 1} (BGR): {color}")

    # 显示图像和掩膜图像
    cv2.imshow("Image", image)
    cv2.imshow("Masked Image", masked_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No QR Code detected")
