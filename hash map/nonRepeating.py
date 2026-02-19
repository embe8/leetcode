'''Problem not from Neetcode, it's from self study with AI
Problem: Return the first non repeating character given a string
'''

class Solution:
    def firstNonOccuring(self, s: str) -> int:
        # initialize a dictionary
        map = {}
        
        for char in s:  # Fixed: was 's' which shadows parameter
            if char in map:
                map[char] += 1
            else:  # Fixed: need else here
                map[char] = 1
        
        min_value = min(map.values())  # Fixed: values() not itervalues() (Python 3)
        min_keys = [k for k in map if map[k] == min_value]
        
        print(min_keys)
        return min_keys[0] if min_keys else -1  # Fixed: actually return something


# Main function
def main():
    solution = Solution()
    
    # Test case 1
    test1 = "leetcode"
    print(f"Input: '{test1}'")
    result1 = solution.firstNonOccuring(test1)
    print(f"Result: {result1}\n")
    
    # Test case 2
    test2 = "loveleetcode"
    print(f"Input: '{test2}'")
    result2 = solution.firstNonOccuring(test2)
    print(f"Result: {result2}\n")
    
    # Test case 3
    test3 = "aabb"
    print(f"Input: '{test3}'")
    result3 = solution.firstNonOccuring(test3)
    print(f"Result: {result3}\n")


if __name__ == "__main__":
    main()
