# Marine-Litter-Detection-Backend(해양 쓰레기 검출 백엔드)

이 프로젝트는 해양 쓰레기를 검출하기 위한 백엔드 시스템을 구현하며, YOLO(You Only Look Once) 객체 감지 및 분류를 사용합니다. Flask를 사용하여 API를 생성하고, PyTorch로 YOLO 모델을 로드하며, PIL을 사용하여 이미지 처리를 수행합니다. 감지된 객체 정보는 JSON 형태로 반환되며, 주석이 달린 이미지도 함께 제공합니다.

## 동작 과정

1. 사용자가 잠재적인 해양 쓰레기가 포함된 이미지 파일을 업로드합니다.
2. YOLO 모델이 이미지를 처리하고 객체를 감지합니다.
3. 감지된 객체는 JSON 응답 형식으로 포맷됩니다.
4. 감지 결과가 주석 처리된 이미지도 함께 제공합니다.

## 기능 개요

- 이미지에서 해양 쓰레기 감지
- JSON 형식으로 자세한 감지 정보 반환
- 감지 결과가 포함된 주석 처리된 이미지 제공

## Flask API

### `/detect` [POST]

- **이미지 파일을 받아 해양 쓰레기를 검출합니다.**
- **요청 바디**: 이미지 파일 (key: `file`)
- **응답**: 감지된 객체와 주석 처리된 이미지가 포함된 JSON 객체

### 예시 요청

```bash
curl -X POST -F 'file=@path/to/image.jpg' http://localhost:5001/detect
```

### 예시 응답
```json
{
  "detections": [
    {
      "class": "tire",
      "confidence": 0.85,
      "bounding_box": [100, 150, 200, 250]
    },
    {
      "class": "fish net",
      "confidence": 0.78,
      "bounding_box": [300, 400, 450, 500]
    }
  ],
  "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA..."
}
```

## 이미지 디코딩
- Base64 to Image: https://base64.guru/converter/decode/image

## 모델 학습
- 해양 쓰레기 검출 및 분류 프로젝트: https://github.com/moonwlsdnl/Marine_Litter_Detection

## 결과
- 짧은 학습 시간을 가진 모델이라 그런지 정확도가 그리 높지 않은 모습을 보였습니다.
