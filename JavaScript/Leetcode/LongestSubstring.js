
function lengthOfLongestSubstring(s) {
    let charSet = new Set(); // To store unique characters in the current window
    let left = 0;  // Left pointer of the window
    let maxLength = 0;  // To track the length of the longest valid substring

    for (let right = 0; right < s.length; right++) {
        // If we find a duplicate character in the current window
        while (charSet.has(s[right])) {
            // Remove the leftmost character from the set and move the left pointer
            charSet.delete(s[left]);
            left++;
        }

        // Add the current character to the set
        charSet.add(s[right]);

        // Update the maximum length if we find a larger valid substring
        maxLength = Math.max(maxLength, right - left + 1);
    }

    return maxLength;
}

