"""
判断一个字符串是否是回文串
例如 level，noon
"""
word = input("请输⼊⼀个单词")
i, word_n = 0, len(word) - 1
j = word_n
pal_flag = True
while i <= word_n // 2:
    if word[i] != word[j]:
        pal_flag = False
        break
    i += 1
    j -= 1
if pal_flag:
    print(f'{word}是回⽂串')
else:
    print(f'{word}不是回⽂串')
