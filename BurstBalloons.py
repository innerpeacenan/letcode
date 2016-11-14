class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(1)  
        nums.insert(0,1)  #让每次都是三个数的运算
        dp = [[0 for i in range(len(nums))] for i in range(len(nums))]  #构造一个[n][n]的二维数组
        n = len(nums)  
      
        for k in range(2,n): #扎破k个气球
            for l in range(0,n - k): #扎破的起始位置
                h = l + k  #扎破的最终位置
                for m in range(l + 1,h):  #最后扎破的那个气球
                    dp[l][h] = max(dp[l][h],nums[l] * nums[m] * nums[h] + dp[l][m] + dp[m][h])  
      
        return dp[0][len(nums) - 1]
    #这题主要用到了dp[][]、k策略，逐级实现获取最大