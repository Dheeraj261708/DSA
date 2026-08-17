class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # stack=[]
        # water=0
        # for i in range(len(height)):
        #     while stack and height[i]>height[stack[-1]]:
        #         x=stack.pop()
        #         if not stack:
        #             break
        #         d=i-stack[-1]-1
        #         min_height=min(height[i],height[stack[-1]])
        #         water=water+d*(min_height-height[x])
        #     stack.append(i)
        # return water


        left = 0
        right = len(height) - 1
        leftmax = 0
        rightmax = 0
        water = 0
        
        while left <= right:
            if height[left] <= height[right]:
                if height[left] >= leftmax:
                    leftmax = height[left]
                else:
                    water += leftmax - height[left]
                left += 1
            else:
                if height[right] >= rightmax:
                    rightmax = height[right]
                else:
                    water += rightmax - height[right]
                right -= 1
                
        return water
        