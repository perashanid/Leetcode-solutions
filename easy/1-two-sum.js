/**
 * Problem: Two Sum
 * Number: 1
 * Difficulty: Easy
 * Link: https://leetcode.com/problems/two-sum/
 * Date: 2025-10-09
 */

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 *
 * Time Complexity: O(n) - We iterate through the array once.
 * Space Complexity: O(n) - In the worst case, we might store all the numbers in the hash map.
 */
const twoSum = (nums, target) => {
  // Create a hash map to store the numbers and their indices.
  const numMap = new Map();

  // Iterate through the array.
  for (let i = 0; i < nums.length; i++) {
    // Calculate the complement needed to reach the target.
    const complement = target - nums[i];

    // Check if the complement exists in the hash map.
    if (numMap.has(complement)) {
      // If it exists, return the indices of the current number and its complement.
      return [numMap.get(complement), i];
    }

    // If the complement doesn't exist, add the current number and its index to the hash map.
    numMap.set(nums[i], i);
  }

  // If no solution is found, return an empty array. This should not happen given the problem constraints,
  // but it's good practice to include a default return.
  return [];
};