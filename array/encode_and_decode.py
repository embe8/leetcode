'''Problem name: Encode and decode Strings
Problem: Given a list of strings, encode into a single string and decode back to original list of strings
Approach: use 000n where n is the length of a string to mark each word
For example given hark, ham decoded form is 0004hark003ham'''

class Solution:
    def encode(self, strs: List[str]) -> str:
        encodedStr = [] # store encoded single string
        for i in range(0, len(strs)):
            # we use the format 000n where n is the length of string
            length = f"{len(strs[i]):4}" # pad the length of string so that its 4 chars long
            encodedStr.append(length+strs[i])
        return "".join(encodedStr)

    def decode(self, s: str) -> List[str]:

        decoded_strings = []
        index = 0
        total_length = len(s)

            # Process the encoded string by reading length prefixes and extracting strings
        while index < total_length:
            # Read the 4-character length prefix
            string_length = int(s[index:index + 4])
            index += 4
            # Extract the string of the specified length
            decoded_string = s[index:index + string_length]
            decoded_strings.append(decoded_string)
            index += string_length

        return decoded_strings



