def palindrome(lst):

    if lst == lst[::-1]:
        return True
    else:
        return False
