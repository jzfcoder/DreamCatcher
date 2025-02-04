import torch
from torch import nn

class Net(nn.Module):
    def __init__(self, start_dim, hidden_dim, out_dim, num_hidden_layers, dropout, actfunc):
        super(Net,self).__init__()
        self.start_dim = start_dim
        self.hidden_dim = hidden_dim
        self.out_dim = out_dim
        self.fc1 = nn.Linear(self.start_dim, self.hidden_dim)
        self.out = nn.Linear(self.hidden_dim, self.out_dim)

        self.layers = nn.ModuleList()
        self.layers.append(self.fc1)
        for n in np.arange(0, num_hidden_layers):
            self.layers.append(nn.Linear(self.hidden_dim, self.hidden_dim))
        self.layers.append(self.out)

        self.drop = nn.Dropout(p=dropout)
        self.actfunc = nn.ReLU()
        self.sig = nn.Sigmoid()

    def forward(self, x):
        for layer in self.layers[:-1]:
            x = self.drop(self.actfunc(layer(x)))
        x = self.layers[-1](x)
        x = self.sig(x)
        return x