# Q:给定一个整数数组，找到具有最大乘积的相邻元素对并返回该乘积。
# 找出列表中相邻的乘积最大的两个数的乘积
# 使用循环遍历列表中的所有数 将相邻的两个数相乘取得乘积然后进行比较
# 2 ≤ inputArray.length ≤ 10,
# -1000 ≤ inputArray[i] ≤ 1000.

# inputArray = [3, 6, -2, -5, 7, 3]
inputArray = [-23, 4, -3, 8, -12]


# 这个是我做出来的方法
def adjacentElementsProduct(inputArray):
    temp = 0
    for item1, item2 in zip(inputArray, inputArray[1:]):
        if temp == 0 and item1 * item2 < 0:
            temp = item1 * item2
        elif temp < item1 * item2:
            temp = item1 * item2

    return temp


# 下面这个是从网上找到的解决办法

def adjacentElementsProductTest(inputArray):
    return max([inputArray[i] * inputArray[i + 1] for i in range(len(inputArray) - 1)])

# print(adjacentElementsProduct(inputArray))
print(adjacentElementsProductTest(inputArray))
