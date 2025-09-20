import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #use bfs because were in a graph looking for shortest path to endword from beginword
        #each transformation can only be done with one character and the transformed word has to be in the list
        #for each char in current word run thru the alphabet 
        if endWord not in wordList:
            return 0

        seen = set()
        wordSet = set(wordList)
        queue = [(beginWord, 1)]
        seen.add(beginWord)

        char_list = string.ascii_lowercase

        while queue:
            curr_word, level = queue.pop(0)
            for i in range(0, len(curr_word)):
                for char in char_list:
                    new_word = curr_word[:i]+char+curr_word[i+1:]
                    if new_word not in seen and new_word in wordSet and new_word != curr_word:
                        if new_word == endWord:
                            return level+1
                        seen.add(new_word)
                        queue.append((new_word, level+1))

        return 0