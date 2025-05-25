from data.gutenberg import download_book, clean_raw_text
from model.blm import BiagramLanguageModel
from utils.helpers import create_vocab, encode, decode, get_batches
from config import *
import torch

#Most of the parameters are in the config.py

book_id = [10001]
results = download_book(book_ids=book_id)

cleaned = {}
for book_id,text in results.items():
  cleaned[book_id] = clean_raw_text(text)
  print(f"Clean book {book_id}")

stoi, itos = create_vocab(cleaned) #string to index and index to string ==> encode and decode
vocab_size = len(stoi)
encoded = encode(cleaned,stoi)
data = torch.tensor(encoded, dtype=torch.long)

model = BiagramLanguageModel(vocab_size).to(device)
optimizer = torch.optim.AdamW(model.parameters(), lr=lr)

best_loss = float('inf')
wait = 0
for epoch in range(num_epochs):
  x_batch,y_batch = get_batches('train',batch_size=batch_size,times=block_size)
  x_batch,y_batch = x_batch.to(device),y_batch.to(device)
  logits,loss = model(x_batch,y_batch)
  optimizer.zero_grad(set_to_none=True)
  loss.backward()
  optimizer.step()
  if loss.item() < best_loss:
    best_loss = loss.item()
  else :
    wait +=1 
    if wait >= patience:
      print(f"Best loss: {best_loss:.4f}")
    
  if epoch % 100 == 0:
    print(f"Epoch: {epoch} | Loss: {loss.item()}")
  
context = torch.zeros((1, 1), dtype=torch.long).to(device)
generated = model.generate(context, 200)[0].tolist()
print(decode(generated, itos))