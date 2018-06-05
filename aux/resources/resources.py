import os
import json
from mako.template import Template


def load_json(path):
    f = open(path)
    s_data = f.read()
    data = json.loads(s_data)
    f.close()
    return data


def get_entries():
    rootDir = './resources/resources'
    for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
        for fname in fileList:
            yield(os.path.join(dirName, fname))


def main():
    rows = []
    for f in get_entries():
        # print(f)
        data = load_json(f)
        if "description" not in data:
            data["description"] = "__temp"
        keys = ["class", "description", "url"]
        filtered = {key: data[key] for key in keys}
        # print(filtered)
        rows.append(filtered)
    mytemplate = Template(filename='./data.tmpl')
    result = mytemplate.render(rows=rows)
    with open("index.html", "w") as f:
        f.write(result)


if __name__ == '__main__':
    main()
