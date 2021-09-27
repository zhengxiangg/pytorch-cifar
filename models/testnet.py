import torch.nn as nn

class testNet(nn.Module):
    def __init__(self):
        self.layer = nn.Sequential(
            nn.Linear(32 * 32, 1000),
            nn.Sigmoid(),
            nn.Linear(1000,1000),
            nn.Sigmoid(),
            nn.Linear(1000,10),
            nn.Softmax(dim=10)
        )


    def forward(self,x):
        out = self.layer(x)
        return out