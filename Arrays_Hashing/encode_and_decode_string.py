# ["Hello", "World"] -> 5#Hello5#World
# 5#Hello5#World -> ["Hello", "World"]

'''
Both encode and decode run in O(N) time, where N is the total length of all characters combined,
because we process each character a constant number of times without back-tracking.
The space complexity is O(N) to store and return the generated output string and array.

Overall, both encode and decode run in linear $O(N)$ time, where $N$ is the total number of characters across all strings

For encoding, we iterate over each string and copy its characters to form the prefix token. Across all strings, every character is copied once, leading to $O(N)$ time.

For decoding, the index pointer i moves strictly left-to-right from 0 to N. We slice each segment directly, so each character in the string is processed exactly once, yielding $O(N)$ time.

Strings in Python are immutable. When you concatenate str(len(s)) + "#" + s, Python cannot modify the original string in place.
It must allocate a new memory buffer of size $\text{len}(str(\text{len}(s))) + 1 + \text{len}(s)$ and copy every character from s into that new buffer. Copying the characters of s requires iterating through all of them, which takes $O(\text{len}(s))$ time.
'''

class Solution:
    def encode(self, strs: List[str]) -> str:
        encodedStr = []
        for s in strs:
            encodedStr.append(str(len(s)) + "#" + s) # O(len(s)) time
        return "".join(encodedStr) # O(N) total time complexity

    def decode(self, s: str) -> List[str]:
        decodedStr = []
        i = 0
        while i < len(s):
            length = []

            #calculate the length of the upcoming sting
            while s[i] != "#":
                length.append(s[i])
                i += 1

            # convert length from list of str to int
            intLength = int("".join(length))

            start = i + 1
            end = start + intLength #(points to length of next str)
            decodedStr.append(s[start:end]) #only appends the string
            
            # move index i at the start of the next length prefix
            i = end
    
        return decodedStr

'''
# Alternative Pythonic implementation
class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        decodedStr = []
        i = 0
        while i < len(s):
            j = s.find('#', i) #find the #
            length = int(s[i:j]) # before the hash is the length
            decodedStr.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
            
        return decodedStr
'''

# we need this because encode is defined as an instance method
# With @staticmethod, your Solution.encode(myList) will work without needing to instantiate Solution().
sol = Solution()
originalListOfStrings = ["Hello", "World"]
print(f"original list of strings = {originalListOfStrings}")
encodedStr = sol.encode(originalListOfStrings)
print(f"encoded string = {encodedStr}") # 5#Hello5#World
decodedStr = sol.decode(encodedStr)
print(f"decoded string = {decodedStr}")

originalListOfStrings = ["", "", ""]
print(f"original list of strings = {originalListOfStrings}")
encodedStr = sol.encode(originalListOfStrings)
print(f"encoded string = {encodedStr}") # 0#0#0#
decodedStr = sol.decode(encodedStr)
print(f"decoded string = {decodedStr}")

originalListOfStrings = ["abc#123"]
print(f"original list of strings = {originalListOfStrings}")
encodedStr = sol.encode(originalListOfStrings)
print(f"encoded string = {encodedStr}") # 7#abc#123
decodedStr = sol.decode(encodedStr)
print(f"decoded string = {decodedStr}")

originalListOfStrings = ["123"]
print(f"original list of strings = {originalListOfStrings}")
encodedStr = sol.encode(originalListOfStrings)
print(f"encoded string = {encodedStr}") # 3#123
decodedStr = sol.decode(encodedStr)
print(f"decoded string = {decodedStr}")
