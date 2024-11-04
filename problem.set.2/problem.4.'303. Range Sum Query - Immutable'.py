class NumArray:

    def __init__(self, nums: List[int]):
        # initialize a prefix sum array
        self.psa = [0]
        running_sum = 0
        for i in nums:
            running_sum += i
            self.psa.append(running_sum)
        # now it's O(1) to find a sum from left to right, not O(n)

    def sumRange(self, left: int, right: int) -> int:
        return self.psa[right+1] - self.psa[left]
        # psa --> sum of left to right