#尼古拉喜欢对一切看到的东西进行分类。 有一次，斯蒂芬送了他一个标签机作为他的生日礼物， 
#机器人把在船上的每个面的标签撕了几个星期。 从那时起，他归类在他的实验室的所有试剂， 
#图书馆的书和在桌子上笔记。 但后来他得知 python 字典，并分类所有索菲亚的机器人的可能
#的配置。 现在，这些文件被组织在一个很深的嵌套结构， 但索菲亚并不喜欢这样。让我们帮助
#索菲亚扁平化这些字典。
#Python字典是一种可以用来方便地存储和处理配置的数据类型。它允许你通过键来创建嵌套结
#构来存储数据。您将得到一个字典，其中的键是字符串，值是字符串或字典。我们的目标是使
#字典扁平化，但保存的结构中的键。其结果应该是一个字典没有嵌套的字典。键应包含原来的
#字典中的父键的路径。在路径中的键是由以“/”分开。如果值是一个空的字典，那么它应该由
#一个空字符串（""）所取代。让我们来看一个例子：
#{
    #"name": {
        #"first": "One",
        #"last": "Drone"
    #},
    #"job": "scout",
    #"recent": {},
    #"additional": {
        #"place": {
            #"zone": "1",
            #"cell": "2"}
    #}
#}
#其结果将是:
#{"name/first": "One",           #one parent
 #"name/last": "Drone",
 #"job": "scout",                #root key
 #"recent": "",                  #empty dict
 #"additional/place/zone": "1",  #third level
 #"additional/place/cell": "2"}
#索菲亚已经写了这个任务的代码，但它有一个漏洞。 你需要找到并修复这个漏洞。
#输入: 作为字典的一个原始字典。
#输出: 作为字典的一个扁平化字典。
#前提:
#字典中的Keys是非空的字符串
#字典中的Values是字典或者字符串
#root_dictionary != {}

def flatten(dictionary):
    stack = [((), dictionary)]
    result = {}
    while stack:
        path, current = stack.pop()
        if not current:
            result["/".join(path)] = ''
        for k, v in current.items():
            if isinstance(v, dict):
                stack.append((path + (k,), v))
            else:
                result["/".join((path + (k,)))] = v
    return result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({"name": {
                        "first": "One",
                        "last": "Drone"},
                    "job": "scout",
                    "recent": {},
                    "additional": {
                        "place": {
                            "zone": "1",
                            "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}
