import json
import numpy as np
import requests

def boundingBox2float(boundingBox):
    a = []
    b = set()
    temp = boundingBox.split(',')
    for i in range(int(len(temp)/2)):
        b.add(temp[i*2]+temp[i*2+1])
    if len(b) <= 2:
        return a
    for i in range(len(temp)):
        a.append(float(temp[i]))
    return a
#
#
# def distinct(point):
#     c = np.array(point)
#     return np.unique()
#
def readJsonFromMongo(imgFileName):
    r = requests.get("http://127.0.0.1:12345", imgFileName)
    if r.status_code == 404:
        return None, r.status_code
    pic_json_string = r.text
    pic_json = json.loads(pic_json_string)
    Result = pic_json["Result"]
    regions = Result['regions']
    lines = []
    shapes = []
    for i in range(len(regions)):
        depth = [i]
        points = []
        point = boundingBox2float(regions[i]["boundingBox"])
        if len(point) == 0:
            continue
        lines.append(regions[i]['lines'])
        for k in range(int(len(point)/2)):
            points.append([point[2*k], point[2*k+1]])
        label = ('大框' + str(i))
        shapes.append((label, points, None,  None, depth))

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            depth = [i,j]
            points = []
            point = boundingBox2float(lines[i][j]["boundingBox"])
            if len(point) == 0:
                continue
            words = lines[i][j]["words"]
            for n in range(int(len(point) / 2)):
                points.append([point[2 * n], point[2 * n + 1]])
            label = lines[i][j]['text']
            shapes.append((label, points, None, None, depth))
            for k in range(len(words)):
                poi = []
                dep = [i,j,k]
                poin = boundingBox2float(words[k]["boundingBox"])
                if len(poin) == 0:
                    continue
                for m in range(int(len(poin) / 2)):
                    poi.append([poin[2 * m], poin[2 * m + 1]])
                labe = words[k]["word"]
                shapes.append((labe, poi, None, None, dep))
    return shapes, r.status_code
a = "725481380411241801"
b,c=readJsonFromMongo(a)
print(len(b))




# import numpy as np
# v = [(1,2),(1,2),(2,3),(2,3)]
# c = np.array(v)
# print(np.unique(c))
# v = {[1,2],[]}
# v = set(['1,2','1,2'])
# print(v)