'''
    SWFilter Module
    SWFilter (Stop Word Filter) Module is for performing operations it
    includes
    1. Adding Stop Word
    2. Checking whether a word is stop word or not.
    3. Filtering list for stop word.
'''
import trie
class SWFilter:
    def __init__(self):
        self.swDS = trie.Trie()
        with open("swfile.txt","r") as swfile:
            word = swfile.read()
            while word:
                self.swDS.addWord(word)
                word = swfile.read()

    def isSW(self,word):
        return self.swDS.search(word)

    def filterList(self,List):
        return list(filter(lambda word: not self.isSW(word), List))
                
    def addSW(self,word):
        self.swDS.addWord(word)