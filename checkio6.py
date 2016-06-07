#������Ϸ����ʱҲ����Ϊ�������ͷ��ء�����һ��������ң�X��O��
#������־��3��3������Ŀռ��������Ϸ������������һ��ֱ��
#��ˮƽ�ߣ���ֱ�߻�Խ��ߣ��ϳɹ�����������ǵ�һ����ʤ��
#�����ǲ�ȥ�������Ϸ���㽫�������Ϸ�Ĳ��С��㱻������Ϸ�Ľ����
#�Լ�������ж���Ϸ��ƽ�ֻ�������ʤ�����Լ�˭�����Ϊ����Ӯ�ҡ�
#���X��һ�ʤ�����ء�X�������O��һ�ʤ�����ء�O�������������ƽ��
#�����ء�D����
#x-o-referee
#��Ϸ�Ľ������Ϊ�ַ�����ʽ���б����С�X���͡�O������ҵı�־����.���ǿո�
#����: ��Ϸ�����Ϊ�ַ�����ʽ���б�(Unicode)��
#���: ��X������O����D����Ϊ�ַ�����ʽ��
#ǰ��:
#Ҫô��һ��Ӯ�ң�Ҫôƽ��
#len(game_result) == 3
#all(len(row) == 3 for row in game_result)


def checkio(game_result):
    rows = game_result
    cols = map(''.join, zip(*rows))
    diags = map(''.join, zip(*[(r[i], r[2 - i]) for i, r in enumerate(rows)]))
    lines = rows + list(cols) + list(diags)
    
    return 'X' if ('XXX' in lines) else 'O' if ('OOO' in lines) else 'D'

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        u"X.O",
        u"XX.",
        u"XOO"]) == "X", "Xs wins"
    assert checkio([
        u"OO.",
        u"XOX",
        u"XOX"]) == "O", "Os wins"
    assert checkio([
        u"OOX",
        u"XXO",
        u"OXX"]) == "D", "Draw"
    assert checkio([
        u"O.X",
        u"XX.",
        u"XOO"]) == "X", "Xs wins again"

