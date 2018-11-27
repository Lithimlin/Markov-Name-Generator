import random

class Markov:
    def __init__(self, corpus="", n=2, maxLength=20, IGNORED_CHARS='.,:;_!?/#*"()'):
        self.n = n
        self.maxLength = maxLength
        for sym in IGNORED_CHARS:
            corpus = corpus.replace(sym, '')
        corpus = corpus.split()
        ngrams = self.make_ngrams(corpus, n+1)
        self.tree = self.make_tree(ngrams)

    def make_ngrams(self, sequence, n):
        def ngramsFromWord(word):
            if n < 1 or n > len(word):
                return []
            else:
                return [word[i:i+n] for i in range(len(word)-(n-1))]

        ngrams = []
        for word in sequence:
            ngrams += (ngramsFromWord(word))
        return ngrams

    def make_tree(self, ngrams):
        root = {'count': len(ngrams), 'frequency': 1.0, 'continuations': {}}

        for ngram in ngrams:
            node = root
            for letter in ngram:
                if letter not in node['continuations']:
                    node['continuations'][letter] = {'continuations': {}, 'count': 0}
                node = node['continuations'][letter]
                node['count'] += 1

        def normalize(node):
            for childName, child in node['continuations'].items():
                child['frequency'] = child['count']/node['count']
                normalize(child)

        normalize(root)
        return root

    def generate(self):
        result = ""
        def currentState():
            return result[max(0, len(result)-self.n):]
        def nextLetter():
            return self.getContinuation(currentState())
        next = nextLetter()
        while len(result) < self.maxLength and next != None:
            result += next
            next = nextLetter()
        return result

    def getContinuation(self, sequence):
        node = self.findNode(sequence)
        if node is not None:
            target = random.random()
            sum = 0
            for contName, contNode in node['continuations'].items():
                sum += contNode['frequency']
                if sum >= target:
                    return contName
        return None

    def findNode(self, sequence):
        node = self.tree
        for letter in sequence:
            if letter in node['continuations']:
                node = node['continuations'][letter]
            else:
                return None
        return node
