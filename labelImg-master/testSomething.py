import json
import requests
# pic_json={}
r=requests.get("http://127.0.0.1:12345","725481380411241801")
pic_json_string=r.text
pic_json=json.loads(pic_json_string)
# print(pic_json['errorCode'])
Result = pic_json["Result"]
regions = Result['regions']
lines = []
    # print(len(lines))
words = []
boundingbox=[]
text=[]
results={}
for i in range(len(regions)):
    boundingbox.append(regions[i]['boundingBox'])
    lines.append(regions[i]['lines'])
    text.append('大框')
    results['大框'+str(i)]=regions[i]['boundingBox']
for j in range(len(lines)):
    for k in range(len(lines[j])):
        boundingbox.append(lines[j][k]['boundingBox'])
        words.append(lines[j][k]['words'])
        text.append(lines[j][k]['text'])
for m in range(len(words)):
    for n in range(len(words[m])):
        boundingbox.append(words[m][n]['boundingBox'])
        text.append(words[m][n]['word'])

print(boundingbox)
print(text)
print(results)
def boundingbox_to_float(boundingbox):
    a = []
    for i in range(len(boundingbox)):
        temp = boundingbox[i].split(',')
        # print(temp)
        a.append([])
        for j in range(8):
            a[i].append(float(temp[j]))
    return a

a=boundingbox_to_float(boundingbox)
print(a)

