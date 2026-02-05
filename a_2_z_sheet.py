# Counting Frequencies of Array Elements
# Easy

# Hints
# Company
# Given an array nums of size n which may contain duplicate elements.



# Rreturn a list of pairs where each pair contains a unique element from the array and its frequency in the array.



# You may return the result in any order, but each element must appear exactly once in the output.


# Example 1

# Input: nums = [1, 2, 2, 1, 3]

# Output: [[1, 2], [2, 2], [3, 1]]

# Explanation:

# - 1 appears 2 times

# - 2 appears 2 times

# - 3 appears 1 time

# Order of output can vary.

# Example 2

# Input: nums = [5, 5, 5, 5]

# Output: [[5, 4]]

# Explanation:

# - 5 appears 4 times.


class Solution:
    def countFrequencies(self, nums):
        # Your code goes here
        mpp={}
        list=[]
        for i in range(len(nums)-1):
            mpp[nums[i]]=mpp.get(nums[i],0)+1
        result=[]
        for key,value in mpp.items():
            result.append([key,value])
        return result
        
a=Solution()
x=a.countFrequencies([1,2,3,4,1,2])
print(x)
        
        