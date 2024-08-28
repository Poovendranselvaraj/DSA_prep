
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
 
# sol
# print(nums[k+1:]+nums[:k+1])

# class Solution(object):
#     def rotate(self, nums, k):
#         n = len(nums)
#         k = k % n 
        
#         def reverse(start, end):
#             while start < end:
#                 nums[start], nums[end] = nums[end], nums[start]
#                 start += 1
#                 end -= 1
        
#         # Step 1: Reverse the entire array
#         reverse(0, n - 1)
        
#         # Step 2: Reverse the first k elements
#         reverse(0, k - 1)
        
#         # Step 3: Reverse the remaining n-k elements
#         reverse(k, n - 1)

# solution = Solution()
# nums = [1, 2, 3, 4, 5, 6, 7]
# k = 3
# solution.rotate(nums, k)
# print(nums) 

# Example 2:

# Input: 
# nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

# sol
nums = [-1,-100,3,99]
k = 2
print(nums[k:]+nums[:k])