import torch

import torch.optim as optim
import torch.nn as nn
from torch.nn import functional as F #loss_function and other things... like Softmax for self-attetion algorithm ;)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
torch.manual_seed(42) 

class BiagramLanguageModel(nn.Module):
    '''
     Super simple Bigram Language Model.
     Predicts the next token based only on the current one.
    '''
    def __init__(self):
        super().__init__()
        
        self.token_embedding = nn.Embedding()
        
    def forward(self,x,targets=None):
        logits = self.token_embedding(x)
        
        if targets == None:
            return logits,None
        
        #Cross Entropy NEEDS to be in 2D
        
        B,T,C = logits.shape
        logits = logits.view(B*T,C) # Flattens the logits from (B, T, C) to (B*T, C) for loss computation
        targets = targets.view(B*T)
        loss = F.cross_entropy(logits,targets)
        return loss
    def generation(self,x,max_new_tokens):
        '''
        Will generate new tokens
        '''
        
        for _ in range(max_new_tokens):
            logits,loss = self(x)
            logits = logits[:,-1,:]
            #SOFTMAX => probability
            
            prob = F.softmax(logits,dim=-1)
            
            next_x = torch.multinomial(prob,num_samples=1)
            x = torch.cat([x,next_x],dim=1)
            
            return x
        