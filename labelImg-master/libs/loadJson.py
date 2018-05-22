import json
import requests

def boundingBox2float(boundingBox):
    a = []
    temp = boundingBox.split(',')
    for i in range(len(temp)):
        a.append(float(temp[i]))
    return a

def readJsonFromMongo(imgFileName):
    r = requests.get("http://127.0.0.1:12345", imgFileName)
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
        lines.append(regions[i]['lines'])
        for k in range(int(len(point)/2)):
            points.append([point[2*k], point[2*k+1]])
        label = ('大框' + str(i))
        shapes.append(
            {"depth":depth,
             "file_color": None,
             "label": label,
             "line_color": None,
             "points": points}
        )

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            depth = [i,j]
            points = []
            point = boundingBox2float(lines[i][j]["boundingBox"])
            words = lines[i][j]["words"]
            for n in range(int(len(point) / 2)):
                points.append([point[2 * n], point[2 * n + 1]])
            label = lines[i][j]['text']
            shapes.append(
                {"depth": depth,
                 "file_color": None,
                 "label": label,
                 "line_color": None,
                 "points": points}
            )
            for k in range(len(words)):
                poi = []
                dep = [i,j,k]
                poin = boundingBox2float(words[k]["boundingBox"])
                for m in range(int(len(poin) / 2)):
                    poi.append([poin[2 * m], poin[2 * m + 1]])
                labe = words[k]["word"]
                shapes.append(
                    {"depth": dep,
                     "file_color": None,
                     "label": labe,
                     "line_color": None,
                     "points": poi}
                )
    return shapes, r.status_code


