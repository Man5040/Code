
def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()  # To store the characters in the current window
    left = 0  # Left pointer of the window
    max_length = 0  # Store the length of the longest substring
    
    for right in range(len(s)):  # Right pointer moves from left to right
        while s[right] in char_set:  # If we encounter a duplicate character
            char_set.remove(s[left])  # Remove the leftmost character
            left += 1  # Shrink the window from the left
        
        char_set.add(s[right])  # Add the current character to the set
        max_length = max(max_length, right - left + 1)  # Update the maximum length
    
    return max_length








