import re #search default patterns in text (cleaning data)
import requests

#Books ids from Project Gutenberg
# book_ids = [
#     76046, 1342, 84, 15399, 3700, 58083, 2951, 2513, 28205, 2147,
#     11808, 20417, 15957,16328, 7370, 12296, 14591, 2701, 1232
# ] 

book_ids = [10001] #Training book



def download_book(book_ids) -> dict:
    '''
    Download books data from project gutenberg
    Parameters: Books ids
    Return : a dict with the books founded
    '''
    results = {}
   
    for book_id in book_ids:
        url =  f"https://www.gutenberg.org/cache/epub/{book_id}/pg{book_id}.txt"
        try :
            response = requests.get(url)
            text = response.text.lstrip('\ufeff')
            results[book_id] = text
            print(f"Downloaded book {book_id}")
        except requests.exceptions.RequestException as e:
               print(f"Failed to download book {book_ids}")
    return results
    
def clean_raw_text(text:dict) -> dict:
    '''
    Clean the data from project gutenberg'books
    Params: The downloaded books from Project Gutenberg
    Return : Cleaned text to be tokenize
    '''
    start_marker = r"\*\*\* START OF (THE|THIS) PROJECT GUTENBERG EBOOK .* \*\*\*"
    end_marker = r"\*\*\* END OF (THE|THIS) PROJECT GUTENBERG EBOOK .* \*\*\*"

    start_clean = re.search(start_marker,text)
    end_clean = re.search(end_marker,text)

    if start_clean and end_clean:
       text = text[start_clean.end():end_clean.start()] #end() => return the end of the index // and start the beggining of the index

    text = re.sub(r"\s+"," ",text) #removing white spaces

    return text.strip() #remove white spaces again (start and end)
   
