#Your optional code here
#You can import some modules or create additional functions
#�㽫�õ�һ������������X���ķǿ��б�������������Ӧ�÷����ڴ��б��еķ�ΨһԪ�ص��б�
#Ҫ������һ�㣬����Ҫɾ�����ж��ص�Ԫ�أ����ǰ�����һ���������б�ֻ��һ�ε�Ԫ�أ���
#����������ʱ�����ܸı��б��˳�����磺[1��2��3��1��3] 1��3�Ƿ�ΨһԪ�أ�������� [1, 3, 1, 3]��


def checkio(data):
    #Your code here
    #It's main function. Don't remove this function
    #It's used for auto-testing and must return a result for check.  
    import copy
    newdata = copy.copy(data)
    setdata = set(newdata)
    for i in setdata:
        newdata.remove(i)
    setdata1 = set(newdata)
    for i in copy.copy(data):
        if i not in setdata1:
            data.remove(i)
            
    #replace this for solution
    return data

#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#Loop over original list


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(checkio([1]), list), "The result must be a list"
    assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert checkio([1, 2, 3, 4, 5]) == [], "2nd example"
    assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"