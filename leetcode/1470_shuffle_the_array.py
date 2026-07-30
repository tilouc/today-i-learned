class Solution(object):
    def shuffle(self, nums, n):
        nums_len = len(nums)

        middle = nums_len // 2

        insert = 1

        temp = 0

        index = middle

        for num in range(middle):
            if (index != 0 and index != (nums_len - 1)):
                temp = nums[index]
                nums.pop(index)
                nums.insert(insert, temp)
                index += 1
                insert += 2

        return nums