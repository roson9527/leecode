class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0:
            return 0
        
        max_index = height.index(max(height))

        move_peak = 0
        trip_rain = 0

        for i in range(0, max_index):
            if move_peak < height[i]:
                move_peak = height[i]
            else:
                trip_rain += move_peak - height[i]

        move_peak = 0
        for j in range(len(height) - 1, max_index, -1):
            if move_peak < height[j]:
                move_peak = height[j]
            else:
                trip_rain += move_peak - height[j]
        
        return trip_rain