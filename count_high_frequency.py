"""169. Majority Element
Solved
Easy
Topics
premium lock icon
Companies
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 """



from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mpp={}
        
        for i in range(len(nums)):
            mpp[nums[i]]=mpp.get(nums[i],0)+1
        a=max(mpp.values())
        for key,values in mpp.items():
            if values==a:
                return key
a=Solution()
x=a.majorityElement([3,3,4])
print(x)
        