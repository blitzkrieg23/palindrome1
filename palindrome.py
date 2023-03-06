def isPalindrome(str):
    start = 0
    end = len(str)-1
    
    for x in str:
        if str[start]!=str[end]:
            return False
    return True

print(isPalindrome("kayak"))
print(isPalindrome("car"))