class PrefixTree:

    def __init__(self):
        self.root = {} 

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node["$"] = True 

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and "$" in node
        

    def startsWith(self, prefix: str) -> bool:
        return self._walk(prefix) is not None
    
    def _walk(self, word: str) -> dict:
        node = self.root
        for char in word:
            if not (char in node):
                return None
            node = node[char]

        return node
    
        
        