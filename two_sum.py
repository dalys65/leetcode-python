class Solution(object):
    def twoSum(self, nums, target):
        
        for i in range(len(nums)): #the nested loops run through each value individually comparing it to the other values in the set
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target: #the if statement adds the two numbers together and if they equal a target value their indices are printed and the loop stops
                    return [i, j]