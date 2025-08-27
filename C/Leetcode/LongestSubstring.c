
#include <stdio.h>
#include <string.h>

int lengthOfLongestSubstring(char *s) {
    int charMap[128] = {0};  // To track characters (ASCII values)
    int left = 0;  // Left pointer of the window
    int maxLength = 0;  // To store the length of the longest valid substring

    for (int right = 0; s[right] != '\0'; right++) {
        // If we find a duplicate character, move the left pointer to the right of the duplicate
        while (charMap[s[right]] > 0) {
            charMap[s[left]]--;  // Remove the leftmost character from the window
            left++;  // Move the left pointer
        }

        // Add the current character to the map (mark it as seen)
        charMap[s[right]]++;

        // Update the maximum length if the current window is longer
        maxLength = (right - left + 1 > maxLength) ? (right - left + 1) : maxLength;
    }

    return maxLength;
}

int main() {
    char s[] = "abcb";
    int result = lengthOfLongestSubstring(s);
    printf("The length of the longest substring without repeating characters is: %d\n", result);
    return 0;
}
