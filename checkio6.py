#井字游戏，有时也被称为“进攻和防守”，是一个两人玩家（X和O）
#轮流标志着3×3的网格的空间的连珠游戏。最先在任意一条直线
#（水平线，垂直线或对角线）上成功连接三个标记的一方获胜。
#但我们不去玩这个游戏。你将是这个游戏的裁判。你被赋予游戏的结果，
#以及你必须判断游戏是平局还是有人胜出，以及谁将会成为最后的赢家。
#如果X玩家获胜，返回“X”。如果O玩家获胜，返回“O”。如果比赛是平局
#，返回“D”。
#x-o-referee
#游戏的结果是作为字符串形式的列表，其中“X”和“O”是玩家的标志，“.”是空格。
#输入: 游戏结果作为字符串形式的列表(Unicode)。
#输出: “X”，“O”或“D”作为字符串形式。
#前提:
#要么有一个赢家，要么平局
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

