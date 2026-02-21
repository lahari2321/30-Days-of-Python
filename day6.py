
def count_words(s):
    s=s.lower()
    s=s.split(" ")
    ans={}
    for word in s:
        if word in ans:
            ans[word]=ans[word]+1
        else:
            ans[word]=1

    return ans
if __name__=="__main__":
    s=input("Enter a string:--")
    s1=count_words(s)
    print(s1)
    