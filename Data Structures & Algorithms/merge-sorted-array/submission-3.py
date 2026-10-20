class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = j = 0
        temp = nums1[:m].copy()

        while i < m and j < n:
            if temp[i] <= nums2[j]:
                nums1[i + j] = temp[i]
                i += 1
            else:
                nums1[i + j] = nums2[j]
                j += 1

        if i < m:
            nums1[i+j:] = temp[i:]
        if j < n:
            nums1[i+j:] = nums2[j:]
