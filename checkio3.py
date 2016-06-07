#˹�ٷҺ������Ƕ���һ�ж�ʹ�ü򵥵����룬�����˰�ȫ�ԡ���������������
#��һ�����밲ȫ���ģ�顣�������ĳ��ȴ��ڻ����10�����ţ�������һ����
#�֣�һ����д��ĸ��һ��Сд��ĸ�������뽫����Ϊ�㹻ǿ������ֻ����ASCII
#������ĸ�����֡�
#����: ���� (str, unicode)��
#���: ����İ�ȫ�����Ϊ����ֵ(bool)�������κο���ת���ʹ���Ϊ����ֵ
#���������͡�����ڽ������ת����Ľ��(True �� False)��

#ǰ��::
#re.match("[a-zA-Z0-9]+", password)
#0 < len(password) �� 64


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