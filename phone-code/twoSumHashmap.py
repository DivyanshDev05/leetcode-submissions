def twoSum(nums, target):
    n = list(int(x) for x in nums)
    t = int(target)
    prevMap = {}

    for i, j in enumerate(n):
        f = t - j
        if f in prevMap:
            return [f, j]
        prevMap[i] = j
        


if __name__ == '__main__':
    inpArr = input(f"Enter the arr elms only non floating integers and sorted: \n")
    t = input(f"Enter the target sum to find: \n")
    print(f"The list of elements with sum {t} is {twoSum(inpArr, t)}")

