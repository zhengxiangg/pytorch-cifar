import torch.nn as nn

class testNet(nn.Module):
    def __init__(self):
        self.layer = nn.Linear(32*32, 10)
        self.m = nn.Softmax(dim=10)
    def forward(self,x):
        out = self.layer(x)
        out = self.m(out)
        retrun out