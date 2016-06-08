def longest_palindromic(text):
    length = len(text)
    palinds = []
    palind = ''
    for i in range(1, length-1):
        for j in range(1, min(i+1, length - i)):
            if text[i+j] == text[i-j]:
                palind = text[i-j:i+j+1]
            else:
                break
        palinds.append(palind)
    maxp = 0
    palind = ''
    for pal in palinds:
        if len(pal) > maxp:
            maxp = len(pal)
            palind = pal
    return palind
                
            

if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
