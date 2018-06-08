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
    rootDir = './vecto-resources/resources'
    for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
        for fname in fileList:
            yield(os.path.join(dirName, fname))


def filter_entry(metadata):
    if "description" not in metadata:
        metadata["description"] = "__temp"
    for key in ["url", "project_page"]:
        if key not in metadata:
            metadata[key] = ""
    keys = ["class", "description", "url", "project_page"]
    filtered = {key: metadata[key] for key in keys}
    return filtered


def main():
    rows = []
    for f in get_entries():
        # print(f)
        data = load_json(f)
        filtered = filter_entry(data)
        rows.append(filtered)
    mytemplate = Template(filename='./data.tmpl')
    result = mytemplate.render(rows=rows)
    with open("index.html", "w") as f:
        f.write(result)


if __name__ == '__main__':
    main()
