#encoding:UTF-8

#----------------------------------------------------------------------
def get_7_not_5():
    """"""
    l = []
    for i in range(2000, 3200):
        if i%7 == 0 and i%5 != 0:
            l.append(str(i))
    
    print ','.join(l)
    
if __name__ == '__main__':
    get_7_not_5()