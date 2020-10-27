# solution by Python3

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findKthLowNum(k): # 寻找第k小的数
            index1, index2 = 0, 0
            while(1):
                # 特殊情况，返回判断
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1: 
                    return min(nums1[index1], nums2[index2])
                    
                # 迭代寻找
                newIndex1 = min(index1 + k//2 - 1, m-1)
                newIndex2 = min(index2 + k//2 - 1, n-1)
                # 更新k，缩小k，每次迭代可以缩写k//2个数
                if nums1[newIndex1] <= nums2[newIndex2]:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1

        m, n = len(nums1), len(nums2)
        if (m+n) % 2 == 1: # 判定奇偶，对应不同的中位数计算方法
            return findKthLowNum((m+n)//2+1)
        else:
            return (findKthLowNum((m+n)//2)+findKthLowNum((m+n)//2+1))/2
