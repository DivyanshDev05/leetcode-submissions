def binarySearch(nums, target):
    n = list(int(x) for x in nums)
    t = int(target)
    l = 0
    r  = len(n) - 1

    while l <= r:
        m = l + ((r - l)//2)
        if n[m] < t:
            l = m + 1
        elif n[m] > t:
            r = m - 1
        else:
            return m
        
    return -1




if __name__ == '__main__':
    inpArr = input(f"Enter the arr elms only non floating integers and sorted: \n")
    t = input(f"Enter the target to find: \n")
    print(f"The index of {t} is {binarySearch(inpArr, t)}")

