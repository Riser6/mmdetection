import torch.nn as nn
from mmcv.runner import BaseModule

from ..builder import NECKS


@NECKS.register_module()
class PPN(BaseModule):
    def __init__(self, in_channels, out_channels):
        super(PPN, self).__init__()
        self.projs = nn.ModuleList([
            nn.Conv2d(ci, co, 1) for ci, co in zip(in_channels, out_channels)
        ])
    
    def forward(self, xs):
        return tuple([p(x) for p, x in zip(self.projs, xs)])
