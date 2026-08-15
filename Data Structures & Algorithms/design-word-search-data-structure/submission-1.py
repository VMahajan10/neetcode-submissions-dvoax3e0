class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for i in range(len(word)):
            c = word[i]
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True 
        
    def search(self, word: str) -> bool:
        def dfs(i, node):
            cur = node
            for j in range(i, len(word)):
                c = word[j]
                if c == '.':
                    return any(dfs(j + 1, child) for child in cur.children.values())
                if c not in cur.children:
                    return False
                cur = cur.children[c]
            return cur.isWord

        return dfs(0, self.root)
                


        
