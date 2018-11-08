import os

def read_corpus(filename):
    try:
        with open(os.path.join('corpora', filename + '.txt')) as file:
            corpus = file.read()
        return corpus
    except FileNotFoundError as fnf:
        raise fnf

def save_corpus(filename, corpus):
    if os.path.exists(os.path.join('corpora', filename + '.txt')):
        raise FileExistsError
    with open(os.path.join('corpora', filename + '.txt')) as file:
        file.write(corpus)
    return
