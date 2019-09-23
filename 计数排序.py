class Solution:
    def CountSort(self, nums):
        MIN = min(nums)
        for k in range(len(nums)):
            nums[k] -= MIN
        tmp = [0] * (max(nums)+1)
        for num in nums:
            tmp[num] += 1
        ans = []
        for k in range(len(tmp)):
            for _ in range(tmp[k]):
                ans.append(k)
        for k in range(len(ans)):
            ans[k] += MIN
        return ans

# test
solu = Solution()
nums = [3,7,6,4,1,9]
print(solu.CountSort(nums))