def is_palindrome(s):
    ans=""
    for char in s:
        if char.isalnum():
            ans += char.lower()
    ans=" ".join(ans)
            
    return ans == ans[::-1]

if __name__ == "__main__":

    input_string=input("enter a string:--")
    print(is_palindrome(input_string))