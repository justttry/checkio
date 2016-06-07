#�����ϲ����һ�п����Ķ������з��ࡣ ��һ�Σ�˹�ٷ�������һ����ǩ����Ϊ����������� 
#�����˰��ڴ��ϵ�ÿ����ı�ǩ˺�˼������ڡ� ����ʱ��������������ʵ���ҵ������Լ��� 
#ͼ��ݵ�����������ϱʼǡ� ����������֪ python �ֵ䣬���������������ǵĻ����˵Ŀ���
#�����á� ���ڣ���Щ�ļ�����֯��һ�������Ƕ�׽ṹ�� �������ǲ���ϲ�������������ǰ���
#�����Ǳ�ƽ����Щ�ֵ䡣
#Python�ֵ���һ�ֿ�����������ش洢�ʹ������õ��������͡���������ͨ����������Ƕ�׽�
#�����洢���ݡ������õ�һ���ֵ䣬���еļ����ַ�����ֵ���ַ������ֵ䡣���ǵ�Ŀ����ʹ
#�ֵ��ƽ����������Ľṹ�еļ�������Ӧ����һ���ֵ�û��Ƕ�׵��ֵ䡣��Ӧ����ԭ����
#�ֵ��еĸ�����·������·���еļ������ԡ�/���ֿ������ֵ��һ���յ��ֵ䣬��ô��Ӧ����
#һ�����ַ�����""����ȡ��������������һ�����ӣ�
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
#��������:
#{"name/first": "One",           #one parent
 #"name/last": "Drone",
 #"job": "scout",                #root key
 #"recent": "",                  #empty dict
 #"additional/place/zone": "1",  #third level
 #"additional/place/cell": "2"}
#�������Ѿ�д���������Ĵ��룬������һ��©���� ����Ҫ�ҵ����޸����©����
#����: ��Ϊ�ֵ��һ��ԭʼ�ֵ䡣
#���: ��Ϊ�ֵ��һ����ƽ���ֵ䡣
#ǰ��:
#�ֵ��е�Keys�Ƿǿյ��ַ���
#�ֵ��е�Values���ֵ�����ַ���
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
