import torch
import cv2
import numpy
import time
from picamera2 import Picamera2

# init model by hub load
model = torch.hub.load('yolov5', 'custom', path='best.pt', source='local', device='cpu')

# Model config
# model.conf = 0.25  # NMS confidence threshold
# model.iou = 0.45  # NMS IoU threshold
# model.agnostic = False  # NMS class-agnostic
# model.multi_label = True  # NMS multiple labels per box
# model.max_det = 1000  # maximum number of detections per image
# model.amp = False  # Automatic Mixed Precision (AMP) inference

# save model class information
cls_dict = model.names