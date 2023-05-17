# 二维码生成器与中心图案添加

这个项目是一个简单的二维码生成器，它可以生成带有自定义中心图案的二维码图像。该项目使用Python编程语言和一些常见的库来实现功能。

## 功能特点

- 生成二维码：根据输入的数据生成二维码图像。
- 中心图案添加：可以将自定义的图像添加到二维码的中心位置。
- 透明背景支持：中心图案可以具有透明背景，使其能够与二维码图像融合得更加自然。

## 使用方法

1. 安装依赖库：在运行代码之前，请确保已经安装了以下库：
   - qrcode：用于生成二维码图像。
   - PIL：用于图像处理和合成。

2. 配置参数：您可以根据需要自定义二维码的参数，例如错误纠正等级、尺寸等。

3. 添加数据：将您想要编码的数据添加到二维码。

4. 添加中心图案：提供您自己的图像，并将其添加到二维码的中心位置。

5. 生成二维码：运行代码，生成带有中心图案的二维码图像。

6. 保存图像：将生成的二维码图像保存为PNG格式，以便在其他地方使用。

## 示例代码

以下是使用示例代码生成带有中心图案的二维码的基本步骤：

```python
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

# 保存
