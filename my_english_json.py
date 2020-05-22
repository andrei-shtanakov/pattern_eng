import json

#me = {"man": "мужчина", "boy": "мальчик", "bank": "банк"}

#with open('data.json', 'w', encoding='utf-8') as fh: #открываем файл на запись
#    fh.write(json.dumps(me, ensure_ascii=False)) #преобразовываем словарь data в unicode-строку и записываем в файл


devices=[]
me = {}
file=open("test.txt", "r")
for item in file:
    item=item.split()
    print(item)
    devices.append(item)
    me[item[0]] = item[1]
file.close()
#print(devices)
print(me)



