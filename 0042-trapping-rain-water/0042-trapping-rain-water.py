class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack=[]
        water=0
        for i in range(len(height)):
            while stack and height[i]>height[stack[-1]]:
                x=stack.pop()
                if not stack:
                    break
                d=i-stack[-1]-1
                min_height=min(height[i],height[stack[-1]])
                water=water+d*(min_height-height[x])
            stack.append(i)
        return water
        