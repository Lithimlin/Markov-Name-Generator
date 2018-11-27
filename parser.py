import os

def read_corpus(filename):
    try:
        with open(os.path.join('corpora', filename + '.txt')) as file:
            corpus = file.read()
        return corpus
    except FileNotFoundError as fnf:
        raise fnf

def save_corpus(filename, corpus):
    if filename is "":
        raise ValueError("Invalid filename! Name is empty")
    if os.path.exists(os.path.join('corpora', filename + '.txt')):
        raise FileExistsError("This name already exists! Please enter a different name.")
    with open(os.path.join('corpora', filename + '.txt'), 'w') as file:
        file.write(corpus)
    return

def remove_corpus(filename):
    try:
        os.remove(os.path.join('corpora', filename + '.txt'))
    except FileNotFoundError as fnf:
        raise fnf

def list_corpora():
    return [f[:-4] for f in os.listdir('corpora') if os.path.isfile(os.path.join('corpora', f))]
