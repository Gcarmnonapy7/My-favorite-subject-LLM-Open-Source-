import torch
block_size = 8
batch_size = 4
eval_iters = 100
num_epochs = 1000
patience = 100
lr = 1e-3
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')