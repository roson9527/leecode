class Solution:
    def split(self, string, width):
        result = []
        i = 0
        length = len(string)

        while i <= length-width:
            result.append(string[i:i+width])
            i = i+width

        return result

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        result = []
        words_count = len(words)

        if words_count > 0:
            length_word = len(words[0])
        else:
            length_word = 0

        i = 0
        length_s = len(s)

        if length_s == 0 or words_count == 0:
            return []

        while i <= length_s-length_word*words_count:
            string_list = self.split(
                s[i:i+length_word*words_count], length_word)

            string_list.sort()
            words.sort()
            print(string_list, words)
            if string_list == words:
                result.append(i)

            i = i + 1

        return result
