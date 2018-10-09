class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start_point = 0
        end_point = len(height) - 1
        max_box = 0

        start_num = height[start_point]
        end_num = height[end_point]

        while(start_point != end_point):
            start_num = height[start_point]
            end_num = height[end_point]
            box = min(start_num, end_num) * abs(start_point - end_point)
            max_box = max(box, max_box)

            if start_num < end_num:
                start_point += 1
            else:
                end_point -= 1

        return max_box
