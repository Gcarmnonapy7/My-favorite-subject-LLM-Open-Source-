import torch

def create_vocab(cleaned_texts:dict):
    all_text = ''.join(cleaned_texts.values())
    unique_chars = sorted(set(all_text))
    char_integer = {char:integer for integer,char in enumerate(unique_chars)}
    integer_char = {integer:char for integer,char in enumerate(unique_chars)}
    return char_integer,integer_char

def encode(cleaned_texts:dict, char_integer:dict):
    all_text = ''.join(cleaned_texts.values())
    return [char_integer[ch] for ch in all_text]

def decode(cleaned_texts:dict,integer_char:dict):
    all_text = ''.join(cleaned_texts.values()) 
    return [cleaned_texts[i] for i in all_text]
            
def get_batches(data:torch.Tensor,split:str,batch_size:int = 4,times:int = 8) -> list:
    """
     Splitting the data that we have into batches to be process
     Params: The way that we are going to split it
     Return : x and y already into batches
    """
    train_size = int(len(data) * 0.8)
    data = data[:train_size] if split == 'train' else data[train_size:]
    rand_index = torch.rand(len(data) - times,(batch_size,))
    x = torch.stack([data[i:i+times] for i in rand_index])
    y = torch.stack([data[i+1:i+times+1] for i in rand_index])
    
    return x,y