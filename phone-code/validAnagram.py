def validAnagram(s, t):
    if len(s) != len(t):
        return False
    countS = {}
    countT = {}
    
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    for c in countS.keys():
        if (c not in countT.keys()):
            return False
        elif (countS[c] != countT[c]):
            return False

    return True




if __name__ == '__main__':
   t = input(f"\nEnter the 1st string: \n\n\t")
   s = input(f"\nEnter the 2st string: \n\n\t")
   print(f"\nThe strings {t} and {s} are valid Anagram:  {validAnagram(s, t)}\n")

