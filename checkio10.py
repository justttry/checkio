def pegoens():
    n = 1
    num = 0
    while n:
        num = num + n
        yield num
        n = n + 1

def checkio(number):
    a = pegoens()
    n = 1
    b = a.next()
    while number >= 0:
        b = a.next()
        number = number - b
        if number >= 0:
            n = b
        
    return n
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"