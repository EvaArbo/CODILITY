class WordLadder:
    def __init__(self, beginWord, endWord, wordList):
        self._beginWord = beginWord
        self._endWord = endWord
        self._wordSet = set(wordList)  # private variable

    # Getter for beginWord
    def get_beginWord(self):
        return self._beginWord

    # Setter for beginWord
    def set_beginWord(self, word):
        self._beginWord = word

    # Getter for endWord
    def get_endWord(self):
        return self._endWord

    # Setter for endWord
    def set_endWord(self, word):
        self._endWord = word

    # Method to check one-letter difference
    def one_letter_diff(self, word1, word2):
        count = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                count += 1
            if count > 1:
                return False
        return count == 1

    # Main method to find the ladder length
    def find_ladder_length(self):
        if self._endWord not in self._wordSet:
            return 0

        queue = [(self._beginWord, 1)]  # simple list for BFS

        for front in queue:
            word, steps = front
            if word == self._endWord:
                return steps

            # Create a copy of set to avoid modifying during loop
            for next_word in list(self._wordSet):
                if self.one_letter_diff(word, next_word):
                    queue.append((next_word, steps + 1))
                    self._wordSet.remove(next_word)

        return 0


# Example usage
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

ladder = WordLadder(beginWord, endWord, wordList)
print(ladder.find_ladder_length())  # Output: 5
#BFS IS used to find the shortest transformation sequence
# from beginWord to endWord
# where each transformed word must exist in the wordList.