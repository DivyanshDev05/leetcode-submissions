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


def printMatrix(r):
   print("The 2d arr output:")
   print(f" _ \t  _")
   print(f"| \t   |")
   for i in range(int(r)):
       print("|", end="")
       for j in l[i]:
           print(f" {j}", end = " ")
       print(f" |")
   print(f"| \t   |")
   print(f" _ \t  _")

def input2dMatrix():
   r = input(f"\nEnter the number of rows: \n\n\t")
   l = []
   for i in range(int(r)):
       t = input(f"\nEnter the {i+1} row: \n\n\t")
       m = [int(x) for x in t]
       l.append(m)
   return l



def unitTest1(l):
    t1 = [[0,1,0], [0,0,1], [1,1,1], [0,0,0]]
    res = [[0,0,],[],[],[]]

#TODO::2. add func for game of life problem

def climbStairs(n):
    n = int(n)
    s2 = 1 if n >= 2 else 0
    s1 = 1 if n >= 1 else 0
    if n < 3:
        return n
    else:
        for i in range(n-2, 0, -1):
            cs1 = s1
            s1 += s2
            s2 = cs1
            print(n, s1, s2, cs1)
        return s1




if __name__ == '__main__':
   #print(f"\nThe strings {t} and {s} are valid Anagram:  {validAnagram(s, t)}\n")
   n = input(f"\n Enter number of stairs: \n")
   print(f"\nThe ways in which stairs {n} can be climbed if it can takes 1 or 2 steps:  {climbStairs(n)}\n")

