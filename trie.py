'''
    Trie Module
    Implementation of Trie Data Structure and Node of Trie.
'''
# Implementation of Trie Node
class Node:
    '''
        char  <char> : Character stored in Node
        child < List<Node> > : Childrens of the Node
        end   <bool> : True if last character of any word else False
    '''
    def __init__(self,char,end):
        self.char = char
        self.child = [None for _ in range(26)]
        self.end = end

# Implementation of Trie
class Trie:
    '''
        root <Node> : Root of Trie
    '''
    def __init__(self):
        self.root = Node('R', False)

    def charToInt(self,char):
        '''
            Convert char to integer (a : 0, b : 1, .... , z : 25)
            params:
                char <char>
            return:
                integer value corresponding to character.
        '''
        return ord(char) - 97

    def addWord(self,word):
        '''
            Add Word 'word' in the Trie.
            params:
                word <string>
            return:
                return True or False based upon successful completion of
                operation.
        '''
        lth = len(word)
        temp = self.root
        for i in range(lth):
            char = word[i]
            idx = self.charToInt(char)
            if idx < 0 or idx > 25:
                continue
            if temp.child[idx] == None:
                newNode = Node(char, True if i + 1 == lth else False)
                temp.child[idx] = newNode
            else:
                temp.end = True if i + 1 == lth else temp.end
            temp = temp.child[idx]
        return temp.end
            
    def search(self,word):
        '''
            Search Word 'word' in the Trie.
            params:
                word <string>
            return:
                return True or False based upon successful completion of
                operation.
        '''
        lth = len(word)
        temp = self.root
        for i in range(lth):
            char = word[i]
            idx = self.charToInt(char)
            if idx < 0 or idx > 25:
                continue
            if temp.child[idx] == None:
                return False
            else:
                temp = temp.child[idx]
        return temp.end

    def display(self,root, string):
        '''
            Print all words stored in Trie.
            params:
                root <Node>
                string <string>
            This method use for Tesing.
        '''
        if root.char != 'R':
            string += root.char
        if root.end:
            print(string)
        for elem in root.child:
            if elem == None:
                continue
            else:
                self.display(elem, string)


# Code for Running File and Testing
if __name__ == "__main__":
    trie = Trie() # creating trie object
    testLi = list() # test word list
    word = input()
    while len(word) != 0:
        testLi.append(word)
        trie.addWord(word)
        word = input()
    word = testLi.pop() if len(testLi) != 0 else ""
    while len(word) != 0:
        assert(trie.search(word)) # assertion error if failed to retrieve word
        word = testLi.pop() if len(testLi) != 0 else ""
