def count_words(s):
    s = s.lower().split()
    ans = {}
    for char in s:
        if char in ans:
            ans[char] += 1
        else:
            ans[char] = 1
    return ans

sentence = input("Enter a sentence: ")
print(count_words(sentence))

