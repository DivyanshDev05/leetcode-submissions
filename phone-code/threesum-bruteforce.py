def threeSum(arr, tgt):
    res = None
    arr = [int(d) for d in arr]
    tgt = int(tgt)
    arrlen = len(arr)
    if arrlen in [None, 1, 2] or tgt is None:
        return res
    else:
        arr = sorted(arr)
        for i in range(2, arrlen):
            if(arr[i] >= tgt):
                break
            if((arr[i] + arr[i-1] + arr[i-2]) == tgt):
                return [arr[i-2], arr[i-1], arr[i]]


if __name__ == '__main__':
    inpArr = input(f"Enter the arr elms only non floating integers: \n")
    target = input(f"Enter the target sum: \n")

    print(f"ThreeSum is : \n {threeSum(inpArr, target)}")
