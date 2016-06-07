#斯蒂芬和索菲亚对于一切都使用简单的密码，忘记了安全性。请你帮助尼古拉开
#发一个密码安全检查模块。如果密码的长度大于或等于10个符号，至少有一个数
#字，一个大写字母和一个小写字母，该密码将被视为足够强大。密码只包含ASCII
#拉丁字母或数字。
#输入: 密码 (str, unicode)。
#输出: 密码的安全与否，作为布尔值(bool)，或者任何可以转换和处理为布尔值
#的数据类型。你会在结果看到转换后的结果(True 或 False)。

#前提::
#re.match("[a-zA-Z0-9]+", password)
#0 < len(password) ≤ 64


def checkio(data):

    #replace this for solution
    return ( (len(data) >= 10) and 
             (not data.islower()) and 
             (not data.isupper()) and 
             (not data.isalpha()) and
             (not data.isdigit()))

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u'A1213pokl') == False, "1st example"
    assert checkio(u'bAse730onE4') == True, "2nd example"
    assert checkio(u'asasasasasasasaas') == False, "3rd example"
    assert checkio(u'QWERTYqwerty') == False, "4th example"
    assert checkio(u'123456123456') == False, "5th example"
    assert checkio(u'QwErTy911poqqqq') == True, "6th example"