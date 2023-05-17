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

# 生成图片
img = qr.make_image(fill_color="black", back_color="white").convert('RGBA')

# 加载中心图案并调整大小
center_img = Image.open('C:/Users/winnerzr/Downloads/icon.png').convert("RGBA")
center_size = (225, 225)
center_img = center_img.resize(center_size)

# 添加中心图案到二维码
w, h = img.size
x = int((w - center_size[0]) / 2)
y = int((h - center_size[1]) / 2)
img.paste(center_img, (x, y))

# 保存二维码图片为PNG格式
img.save('qrcode_with_center2.png', 'png')
