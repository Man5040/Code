
#include <stdio.h>
#include <stdlib.h>

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    // Create a hash map to store number -> index
    // Assuming numsSize is small, we'll use a fixed-size hash table for simplicity.
    int* hashMap = (int*)calloc(10000, sizeof(int));  // Size of hashMap is large enough for typical cases
    int* result = (int*)malloc(2 * sizeof(int));  // To store the result indices

    // Initialize returnSize to 2 since we'll always return 2 indices
    *returnSize = 2;

    for (int i = 0; i < numsSize; i++) {
        // Calculate the complement
        int complement = target - nums[i];
        
        // If the complement is already in the hashMap, we've found the solution
        if (hashMap[complement] != 0) {
            result[0] = hashMap[complement] - 1;  // Retrieve the stored index (1-based index stored)
            result[1] = i;  // Current index is the second one
            free(hashMap);  // Clean up memory before returning
            return result;
        }
        
        // Store the index of the current number in the hashMap
        hashMap[nums[i]] = i + 1;  // Store indices 1-based to differentiate from default 0 value
    }

    free(hashMap);  // Clean up memory in case no solution was found
    return NULL;  // If no solution is found, return NULL
}










