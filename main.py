from flask import Flask, request, jsonify
import torch
from PIL import Image
from functions import read_image, encode_image_to_base64

# YOLO 모델 로드
model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt', force_reload=True)

app = Flask(__name__)

# 해양 쓰레기 검출 및 분류 엔드포인트
@app.route("/detect", methods=["POST"])
def detect():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']

    try:
        img = read_image(file)
        results = model(img)
        df = results.pandas().xyxy[0]  # bounding box, confidence, class

        # 검출된 객체 정보 포맷
        detections = []
        for index, row in df.iterrows():
            if row['confidence'] >= 0.25:
                detection = {
                    "class": row['name'],
                    "confidence": row['confidence'],
                    "bounding_box": [row['xmin'], row['ymin'], row['xmax'], row['ymax']]
                }
                detections.append(detection)

        # 해양 쓰레기가 검출되지 않은 경우 처리
        if not detections:
            return jsonify({"message": "해양 쓰레기 인식 불가"}), 404

        # 이미지에 바운딩 박스 그리기
        img_with_boxes = results.render()[0]
        img_pil = Image.fromarray(img_with_boxes)

        # 이미지를 Base64로 인코딩
        img_base64 = encode_image_to_base64(img_pil)

        return jsonify({"detections": detections, "image": img_base64}), 200

    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": "처리 중 오류가 발생했습니다: " + str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)
