info = {'name':'班长', 'id':100, 'sex':'f', 'address':'地球亚洲中国北京'}
# print(info['name'])
# print(info['address'])
age = info.get('age')
print(age)
print(type(age))
age = info.get('age', 18)
print(age)
