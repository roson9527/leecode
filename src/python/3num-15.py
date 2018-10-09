class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        set_nums = [i for i in set(nums)]
        dict_nums = {set_nums[i]: 0 for i in range(len(set_nums))}

        for i in nums:
            dict_nums[i] += 1

        mix_list = []
        for n in set_nums:
            cnt = dict_nums.get(n)
            if cnt > 0:
                mix_list.append(n)
                if cnt >= 2:
                    mix_list.append(n)
                    if n == 0 and cnt > 2:
                        mix_list.append(n)

        mix_list.sort()
        # print(mix_list)
        output = []
        for i in range(len(mix_list)):
            if mix_list[i] > 0:
                break
            if i > 0 and mix_list[i] == mix_list[i - 1]:
                continue

            j = i + 1
            k = len(mix_list) - 1
            while j < k:
                # print(i, j ,k , mix_list[i], mix_list[j] , mix_list[k])
                if mix_list[j] + mix_list[k] + mix_list[i] == 0:
                    output.append([mix_list[i], mix_list[j], mix_list[k]])
                    while j < k and mix_list[j] == mix_list[j + 1]:
                        j += 1
                    while j < k and mix_list[k] == mix_list[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif mix_list[i] + mix_list[j] + mix_list[k] < 0:
                    j += 1
                else:
                    k -= 1

        return output
