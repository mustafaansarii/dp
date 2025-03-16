def check_palindrom(strs):
    left=0
    right=len(strs)-1
    def palindrom(left,right,strs):
        if left>=right:
            return True
        if strs[left]==strs[right]:
            return palindrom(left+1, right-1, strs)
        if strs[left]!=strs[right]:
            return False
    return  palindrom(left,right,strs)


if  __name__ == "__main__":
    strs1 = "madam"
    strs2 =  "madan"
    print(check_palindrom(strs1))
    print(check_palindrom(strs2))
