def palindrome(lst):

    if lst == lst[::-1]:
        return True
    else:
        return False

print(palindrome([1,2,"Expresso","Madeline",2,1]))
print(palindrome(['a',True,False,False,True,'a']))
print(palindrome([3]))
