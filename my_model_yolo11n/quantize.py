# export_model.py
from ultralytics import YOLO

model = YOLO('my_model_yolo11n_quantize/train/weights/best.pt')  # load a custom model

model.export(format="onnx", int8=True, data="data.yaml")  # export the model to ONNX format with INT8 quantization
