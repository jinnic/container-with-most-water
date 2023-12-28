def container_with_most_water(height):
# Replace this placeholder return statement with your code
  left = 0
  right = len(height) -1 
  max = 0
  
  while left < right:
    area = min(height[left], height[right])*(right - left)
    print(height[left], height[right], area)
    if area > max:
      max = area 
    if height[left] < height[right]:
      left += 1 
    else:
      right -= 1
  return max

height = [7,7,2]

print(container_with_most_water(height))
