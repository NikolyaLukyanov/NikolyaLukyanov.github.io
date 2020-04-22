import json
jsonstr = '{"bomonque":[{"iu": [{"iu-1": []},{"iu10":[{"cozers": ["Zversky", "GoldGem", "Cnya176"]}]}]},{"fn":[{"fn-12":[{"obercozers": [],"cozers": ["Ivanov", "Petrov"]}]}]}]}'

json = json.loads(jsonstr)
cozers1 = json["bomonque"][0]["iu"][1]["iu10"][0]["cozers"]
cozers2 = json["bomonque"][1]["fn"][0]["fn-12"][0]["cozers"]
print('cozers={}'.format(cozers1))
print('cozers={}'.format(cozers2))

