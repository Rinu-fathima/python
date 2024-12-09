from fnpalindrom import is_palindrome
def longest_palindromic_substring(s):
        n=len(s)
        longest_palindrome=""
        for i in range(n):
                for j in range(i+1,n+1):
                        substring=s[i:j]
                        if is_palindrome(substring) and len(substring)>len(longest_palindrome):
                                longest_palindrome=substring
        return longest_palindrome

text=input("Enter a string:")
print("Longest palindromic substring:",longest_palindromic_substring(text))

