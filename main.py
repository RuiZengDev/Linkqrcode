import qrcode
from PIL import Image

# 定义二维码参数
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=20,
    border=4
)
# 添加数据到二维码
data = "https://www.isbe-online.org/"
qr.add_data(data)
qr.make(fit=True)

# 生成二维码图像
qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGBA')

# 加载中心图像并调整大小
center_img = Image.open('C:/Users/winnerzr/Downloads/icon.png').convert("RGBA")
center_size = (225, 225)
center_img = center_img.resize(center_size)

# 创建一个具有透明背景的图像容器
result_img = Image.new("RGBA", qr_img.size, (0, 0, 0, 0))

# 将二维码图像粘贴到结果图像中
result_img.paste(qr_img, (0, 0))

# 计算中心图像的位置
x = int((qr_img.width - center_size[0]) / 2)
y = int((qr_img.height - center_size[1]) / 2)

# 将中心图像粘贴到结果图像中心位置
result_img.paste(center_img, (x, y), mask=center_img)

# 保存带有中心图像的二维码图片为PNG格式
result_img.save('qrcode_with_center.png', 'png')
