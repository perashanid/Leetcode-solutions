/*
 * Problem: Longest Substring Without Repeating Characters
 * Number: 3
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
 * Date: 2025-10-10
 */

import java.util.HashSet;
import java.util.Set;

/*
 * Time Complexity: O(n), where n is the length of the input string s.
 * We iterate through the string at most twice (once with the left pointer and once with the right pointer).
 * Space Complexity: O(min(n, m)), where n is the length of the string s and m is the size of the character set.
 * In the worst case, the space complexity is O(n) if all characters in the string are unique.
 * However, if the character set is smaller than n (e.g., ASCII characters), the space complexity is O(m).
 */
class Solution {
    /**
     * Finds the length of the longest substring without repeating characters.
     *
     * @param s The input string.
     * @return The length of the longest substring without repeating characters.
     */
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        int maxLength = 0; // Initialize the maximum length of the substring
        int left = 0; // Left pointer of the sliding window
        int right = 0; // Right pointer of the sliding window
        Set<Character> charSet = new HashSet<>(); // Set to store the characters in the current window

        while (right < n) {
            // If the current character is not in the set, add it and expand the window
            if (!charSet.contains(s.charAt(right))) {
                charSet.add(s.charAt(right));
                maxLength = Math.max(maxLength, right - left + 1); // Update the maximum length
                right++; // Move the right pointer to expand the window
            } else {
                // If the current character is already in the set, shrink the window from the left
                charSet.remove(s.charAt(left));
                left++; // Move the left pointer to shrink the window
            }
        }

        return maxLength; // Return the maximum length found
    }
}