import json

params = {
    'symbol': '123456',
    'type': 'limit',
    'price': 123.4,
    'amount': 23
}
#dumps,将python的基本数据类型转化为字符串
params_str = json.dumps(params)
print(params_str)
print(json.dumps([1,2,3]))
#loads将字符串转化为json基本类型
original_params = json.loads(params_str)
print('original_params type {},original_params:{}'.format(type(original_params),original_params))
#读文件
try:
    with open('param.json', 'r') as jsonfile:
        jsonparam = json.load(jsonfile)
        print(jsonparam)
except Exception as ex:
    print("exception ex {}".format(ex))

#dump写入文件
with open('param.json','w') as jsonfile:
    jsonparam = json.dump(params,jsonfile)
print('end json test')
