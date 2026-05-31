class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        t = set()
        nums.sort()
        for i in range (0,len(nums)-2):
            j=i+1
            k=len(nums)-1
            while(j<k):
                if (nums[i]+nums[j]+nums[k]==0):
                    t.add((nums[i], nums[j], nums[k]))
                    j+=1
                    k-=1

                elif(nums[i]+nums[j]+nums[k]>0):
                    k-=1

                else:
                    j+=1
        print (t)
        return [list(x) for x in t]