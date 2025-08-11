'''3. Longest Substring Without Repeating Characters
Attempted
Medium
Topics
premium lock icon
Companies
Hint
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.


Solution:'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()  # Track characters in current window
        left = 0          # Left boundary of sliding window
        max_length = 0    # Track the longest substring found
        
        for right in range(len(s)):  # Right boundary moves forward
            # If duplicate found, shrink window from left until duplicate is removed
            while s[right] in char_set:
                char_set.remove(s[left])  # Remove leftmost character
                left += 1                 # Move left boundary forward
            
            # Add current character to window
            char_set.add(s[right])
            
            # Update max length if current window is longer
            max_length = max(max_length, right - left + 1)
        
        return max_length

