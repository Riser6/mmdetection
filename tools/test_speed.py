import mmcv
import sys
import os
sys.path.insert(0, '/data2/zwt/wd/mmdetection')
from mmdet.apis import init_detector, inference_detector
from mmdet.core import get_classes

config_file = 'configs/coat_yolo/yolox_m_mobilevit_s.py'
checkpoint_file = 'checkpoints/coatl_yolox.pth'
img_folder = "VOCdevkit/VOC2012/JPEGImages"
img_names = os.listdir(img_folder)[:100]
imgs = [os.path.join(img_folder, filename) for filename in img_names]


model = init_detector(config_file, checkpoint_file, device='cuda:0')
model.CLASSES = get_classes('voc')

for i, img in enumerate(imgs):
    print(i)
    result = inference_detector(model, img)

print("finish!")