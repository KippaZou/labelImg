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
    r = requests.get("http://10.10.20.45:12345", imgFileName)
    if r.status_code == 404:
        return None, r.status_code
    pic_json_string = r.text
    pic_json = json.loads(pic_json_string)
    Result = pic_json["Result"]
    regions = Result['regions']
    lines = []
    shapes = []

    for i in range(len(regions)):
        lines.append(regions[i]['lines'])



    for i in range(len(lines)):
        for j in range(len(lines[i])):
            words = lines[i][j]["words"]
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
    for i in range(len(regions)):
        depth = [i]
        points = []
        point = boundingBox2float(regions[i]["boundingBox"])
        if len(point) == 0:
            continue

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
            for n in range(int(len(point) / 2)):
                points.append([point[2 * n], point[2 * n + 1]])
            label = lines[i][j]['text']
            shapes.append((label, points, None, None, depth))

    return shapes, r.status_code
a = "725481380411241801"
b,c=readJsonFromMongo(a)
print(len(b))
for i in range(len(b)):
    print(b[i])

#
#
#
# # import numpy as np
# # v = [(1,2),(1,2),(2,3),(2,3)]
# # c = np.array(v)
# # print(np.unique(c))
# # v = {[1,2],[]}
# # v = set(['1,2','1,2'])
# # print(v)

# import pymongo
# import json
#
# conn = pymongo.MongoClient('127.0.0.1',27017)
# db=conn.image2mongo
# my_set=db.images
#
def float2boundingBox(points):
    a = ""
    for i in range(len(points)):
        if i < len(points)-1:
            a = a + (str(points[i][0])) + ","
            a = a + (str(points[i][1])) + ","
        else:
            a = a + (str(points[i][0])) + ","
            a = a + (str(points[i][1]))
    return a
#
#
shape = [{'label': '大框0', 'points': [(777.0, 8.0), (791.0, 6.0), (793.0, 23.0), (779.0, 25.0)], 'depth': [0]}, {'label': '大框1', 'points': [(189.0, 149.0), (203.0, 147.0), (205.0, 175.0), (191.0, 176.0)], 'depth': [1]}, {'label': '大框2', 'points': [(91.0, 198.0), (145.0, 194.0), (153.0, 284.0), (99.0, 289.0)], 'depth': [2]}, {'label': '大框3', 'points': [(1385.0, 54.0), (1399.0, 52.0), (1406.0, 128.0), (1392.0, 129.0)], 'depth': [3]}, {'label': '大框4', 'points': [(101.0, 350.0), (220.0, 340.0), (227.0, 424.0), (108.0, 435.0)], 'depth': [4]}, {'label': '大框5', 'points': [(108.0, 594.0), (151.0, 590.0), (153.0, 620.0), (111.0, 624.0)], 'depth': [5]}, {'label': '大框6', 'points': [(129.0, 695.0), (143.0, 694.0), (145.0, 723.0), (131.0, 725.0)], 'depth': [6]}, {'label': '大框7', 'points': [(216.0, 639.0), (230.0, 638.0), (237.0, 718.0), (223.0, 719.0)], 'depth': [7]}, {'label': '大框8', 'points': [(199.0, 788.0), (228.0, 786.0), (230.0, 815.0), (201.0, 818.0)], 'depth': [8]}, {'label': '5', 'points': [(777.0, 8.0), (791.0, 6.0), (793.0, 23.0), (779.0, 25.0)], 'depth': [0, 0]}, {'label': '5', 'points': [(775.0, 7.0), (790.0, 5.0), (792.0, 24.0), (777.0, 26.0)], 'depth': [0, 0, 0]}, {'label': '+', 'points': [(189.0, 149.0), (203.0, 147.0), (205.0, 175.0), (191.0, 176.0)], 'depth': [1, 0]}, {'label': '+', 'points': [(189.0, 148.0), (202.0, 146.0), (204.0, 176.0), (192.0, 177.0)], 'depth': [1, 0, 0]}, {'label': '—', 'points': [(118.0, 196.0), (132.0, 195.0), (135.0, 229.0), (121.0, 231.0)], 'depth': [2, 0]}, {'label': '—', 'points': [(118.0, 194.0), (131.0, 193.0), (134.0, 232.0), (121.0, 233.0)], 'depth': [2, 0, 0]}, {'label': '', 'points': [(96.0, 254.0), (150.0, 249.0), (153.0, 284.0), (99.0, 289.0)], 'depth': [2, 1]}, {'label': '.', 'points': [(1385.0, 54.0), (1399.0, 52.0), (1406.0, 128.0), (1392.0, 129.0)], 'depth': [3, 0]}, {'label': '.', 'points': [(1385.0, 52.0), (1398.0, 51.0), (1405.0, 129.0), (1392.0, 130.0)], 'depth': [3, 0, 0]}, {'label': '', 'points': [(102.0, 350.0), (218.0, 340.0), (221.0, 383.0), (106.0, 393.0)], 'depth': [4, 0]}, {'label': '飞', 'points': [(105.0, 399.0), (224.0, 388.0), (227.0, 424.0), (108.0, 435.0)], 'depth': [4, 1]}, {'label': '飞', 'points': [(161.0, 438.0), (270.0, 429.0), (273.0, 466.0), (164.0, 476.0)], 'depth': [4, 1, 0]}, {'label': '涉', 'points': [(108.0, 594.0), (151.0, 590.0), (153.0, 620.0), (111.0, 624.0)], 'depth': [5, 0]}, {'label': '涉', 'points': [(121.0, 593.0), (150.0, 591.0), (152.0, 620.0), (123.0, 623.0)], 'depth': [5, 0, 0]}, {'label': '.', 'points': [(129.0, 695.0), (143.0, 694.0), (145.0, 723.0), (131.0, 725.0)], 'depth': [6, 0]}, {'label': '，', 'points': [(216.0, 639.0), (230.0, 638.0), (233.0, 673.0), (219.0, 674.0)], 'depth': [7, 0]}, {'label': '，', 'points': [(216.0, 637.0), (229.0, 636.0), (232.0, 675.0), (219.0, 676.0)], 'depth': [7, 0, 0]}, {'label': '', 'points': [(220.0, 684.0), (234.0, 683.0), (237.0, 718.0), (223.0, 719.0)], 'depth': [7, 1]}, {'label': '到', 'points': [(199.0, 788.0), (228.0, 786.0), (230.0, 815.0), (201.0, 818.0)], 'depth': [8, 0]}, {'label': '到', 'points': [(199.0, 787.0), (227.0, 785.0), (229.0, 817.0), (202.0, 819.0)], 'depth': [8, 0, 0]}]


def shape2json(shape):

    dict = {}
    firstLayer = 0
    secondLayer = 0
    thirdLayer = 0
    dict['errorCode'] = "0"
    dict['Result'] = {}
    dict['Result']['orientation'] = "UP"
    dict['Result']['regions'] = []
    for i in range(len(shape)):
        if len(shape[i]['depth']) == 1:
            firstLayer += 1
            dict['Result']['regions'].append({
                "boundingBox": float2boundingBox(shape[i]['points']),
                "lines": []
            })
    regions = dict['Result']['regions']
    for i in range(len(shape)):

        if len(shape[i]['depth']) == 2 or len(shape[i]['depth']) == 0:
            secondLayer += 1
            j = shape[i]['depth'][0]
            regions[j]['lines'].append({
                "boundingBox": float2boundingBox(shape[i]['points']),
                "words": [],
                "text": shape[i]['label'],
                "lang": "zh"
            })

    for i in range(len(shape)):
        if len(shape[i]['depth']) == 3:
            thirdLayer += 1
            j = shape[i]['depth'][0]
            k = shape[i]['depth'][1]
            regions[j]['lines'][k]['words'].append({
                "boundingBox": float2boundingBox(shape[i]['points']),
                "word": shape[i]['label']
            })
    return dict


d = shape2json(shape)
print(d)

# print(dict)
# my_set.insert(dict)
    # if len(shape[i]['depth']) == 2:
    #     secondLayer += 1
    # if len(shape[i]['depth']) == 3:
    #     thirdLayer += 1