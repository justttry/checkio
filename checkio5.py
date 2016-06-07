#encoding:UTF-8
#﻿
#给你一个其中包含不同的英文字母和标点符号的文本，
#你要找到其中出现最多的字母，返回的字母必须是小
#写形式，
#当检查最想要的字母时，不区分大小写，所以在你的
#搜索中 "A" == "a"。 请确保你不计算标点符号，
#数字和空格，只计算字母。
#母， 返回那个先出现在字母表中的字母。 例如 -- 
#“one”包含“o”，“n”，“e”每个字母一次，因此我们
#选择“e”。
#输入: 用于分析的文本 (str, unicode).
#输出: 最常见的字母的小写形式。
#前提::
#密码只包含ASCII码符号
#0 < len(text) ≤ 105

def checkio(text):
    newtext = text.lower()
    d = {i:newtext.count(i) for i in set(newtext) if i.isalpha()}
    letter = 'z'
    count = 0
    for key, value in d.items():
        if value > count:
            count = value
            letter = key
        elif value == count:
            count = value
            if letter > key:
                letter = key
    return letter
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"Hello World!") == "l", "Hello test"
    assert checkio(u"How do you do?") == "o", "O is most wanted"
    assert checkio(u"One") == "e", "All letter only once."
    assert checkio(u"Oops!") == "o", "Don't forget about lower case."
    assert checkio(u"AAaooo!!!!") == "a", "Only letters."
    assert checkio(u"abe") == "a", "The First."
    print("Start the long test")
    assert checkio(u"a" * 9000 + u"b" * 1000) == "a", "Long."
    print("The local tests are done.")
