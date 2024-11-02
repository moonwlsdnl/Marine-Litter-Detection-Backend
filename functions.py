import numpy as np
import io
import base64
from PIL import Image

# 이미지 처리 함수
def read_image(file):
    try:
        img = Image.open(file.stream).convert("RGB")
        return np.array(img)
    except Exception as e:
        raise ValueError("이미지 처리 중 오류 발생: " + str(e))

# 이미지를 Base64로 인코딩하는 함수
def encode_image_to_base64(image):
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str