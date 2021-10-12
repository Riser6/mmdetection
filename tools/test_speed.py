import mmcv
import sys
import os
sys.path.insert(0, '/data2/zwt/wd/mmdetection')
from mmdet.apis import init_detector, inference_detector
from mmdet.core import get_classes

config_file = 'configs/coat_yolo/yolox_m_coatl_s_1x_voc.py'
checkpoint_file = 'checkpoints/coatl_yolox.pth'
img_folder = "VOCdevkit/VOC2012/JPEGImages"
img_names = os.listdir(img_folder)[:1000]
imgs = [os.path.join(img_folder, filename) for filename in img_names]


model = init_detector(config_file, checkpoint_file, device='cuda:0')
model.CLASSES = get_classes('voc')

for img in imgs:
    result = inference_detector(model, img)

print("finish!")