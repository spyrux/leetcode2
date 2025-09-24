class AutocompleteNode:
    def __init__(self):
        self.chars = {}
        #sentence end
        self.end = False
        self.times = 0

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = AutocompleteNode()
        self.currInput = ''
        self.currPointer = self.root
        for sentence, time in zip(sentences, times):
            self.insert(sentence, time)
        
    def insert(self, sentence: str, time: int):
        curr = self.root
        for char in sentence:
            if char not in curr.chars:
                curr.chars[char] = AutocompleteNode()
            curr = curr.chars[char]
        curr.end = True
        curr.times += time
    
    def get(self) -> List[str]:
        results = []
        self.dfs(self.currPointer, results, self.currInput)
        results.sort(key=lambda x: (-x[1], x[0]))
        return [sentence for sentence, _ in results[:3]]
    
    def dfs(self, node, results, currSentence):
        if node.end:
            results.append((currSentence, node.times))

        for char, n in node.chars.items():
            self.dfs(n, results, currSentence+char)


    def input(self, c: str) -> List[str]:
        if not (c == '#'):
            self.currInput += c
            if c not in self.currPointer.chars:
                self.currPointer.chars[c] = AutocompleteNode()
                self.currPointer = self.currPointer.chars[c]
                return []
            else:
                self.currPointer = self.currPointer.chars[c]
                return self.get()
        else:
            self.insert(self.currInput, 1)
            self.currInput = ''
            self.currPointer = self.root
            return []
        

        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)