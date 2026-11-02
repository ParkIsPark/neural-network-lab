import torch.nn as nn


class EncoderLayer(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return x


class Encoder(nn.Module):
    def __init__(self):
        super().__init__()

        self.layers = nn.ModuleList([
            EncoderLayer() for _ in range(6)
        ])

    def forward(self, x):
        for layer in self.layers:
            x = layer(x)

        return x


class DecoderLayer(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, encoder_output):
        return x


def main():
    encoder = Encoder()
    decoder = DecoderLayer()


if __name__ == "__main__":
    main()