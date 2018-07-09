# -*- coding: utf-8 -*-

import json
import os
import sys
from nikola.plugin_categories import RestExtension
from nikola.utils import LOGGER

from docutils import nodes
from docutils.parsers.rst import Directive, directives

from mako.template import Template
from pylatexenc.latexencode import utf8tolatex

plugin_path = os.path.dirname(os.path.realpath(__file__))
base_path = plugin_path.split("plugins")[0]


def load_json(path):
    f = open(path)
    s_data = f.read()
    data = json.loads(s_data)
    f.close()
    return data


def bibjson_to_bibtex(entry):
    result = f"@{entry['type']}{{{entry['id']},"
    entry.pop("type", None)
    entry.pop("id", None)
    if isinstance(entry["author"], str):
        result += f"\n   author = {entry['author']}"
    else:
        result += "\n   author = \""
        for name in entry["author"]:
            result += f"{utf8tolatex(name['name'])} and "
        result = result[:-5]
        result += "\""
    entry.pop("author", None)

    for key in entry:
        result += f"\n   {key} = \"{entry[key]}\""
    result += "\n}"
    #@inproceedings{karpinska2018RelNLP,
    #author = "Karpinska, Marzena and Li, Bofang and Rogers, Anna and Drozd, Aleksandr",
    #title = "Subcharacter Information in Japanese Embeddings: When Is It Worth It?",
    #booktitle = "In Proceedings of the Workshop on Relevance of Linguistic Structure in Neural Architectures for NLP (RELNLP) 2018",
    #pages = "to appear",
    #year = "2018",
    #organization = "ACL"
    #}
    return result

def filter_entry(metadata):
    if "description" not in metadata:
        metadata["description"] = ""
    filtered = {}
    for key in ["url", "project_page"]:
        if key in metadata:
            filtered[key] = metadata[key]
        else:
            filtered[key] = ""
    filtered["meta"] = metadata
    if "cite" in metadata:
        filtered["bibtex"] = bibjson_to_bibtex(metadata["cite"])
    else:
        filtered["bibtex"] = ""
    return filtered


def get_entries(path):
    for dirName, subdirList, fileList in os.walk(path, topdown=False):
        for fname in fileList:
            yield(os.path.join(dirName, fname))


class MetadataProcessor():
    def read_files(self):
        self.rows = []
        cnt = 0
        for fname in get_entries(os.path.join(base_path, "aux/resources/vecto-resources/resources")):
            data = load_json(fname)
            data = filter_entry(data)
            data["id"] = cnt
            cnt += 1
            self.rows.append(data)

    def render(self):
        self.read_files()
        mytemplate = Template(filename=os.path.join(plugin_path,'data.tmpl'))
        result = mytemplate.render(rows=self.rows)
        return result


class Plugin(RestExtension):

    name = "vecto_metadata"

    def set_site(self, site):
        self.site = site
        directives.register_directive('vecto_metadata', VectoMetadata)
        VectoMetadata.site = self.site
        # PublicationList.output_folder = self.site.config['OUTPUT_FOLDER']
        return super(Plugin, self).set_site(site)


class VectoMetadata(Directive):
    has_content = False
    # required_arguments = 1
    optional_arguments = sys.maxsize
    option_spec = {
    }

    def run(self):
        mp = MetadataProcessor()
        html =  mp.render()
        return [nodes.raw('', html, format='html'), ]

#class Plugin(Task):
#    name = "vecto_metadata"
#    def gen_tasks(self):

        # This function will be called when the task is executed

        # clone repo
#        def clone_repo():

#            cache_dir = base_path+"cache/git-resources"
#            if not os.path.exists(cache_dir):
#                os.mkdir(cache_dir)
#                Repo.clone_from("https://github.com/vecto-ai/vecto-resources.git", cache_dir)

        # generate corpora page

        # generate embeddings page

        # generate datasets page
#        def get_datasets():
#            dir = base_path+"cache/git-resources/resources.datasets"
#            dlist = os.listdir(dir)
#            for f in dlist:
#                fpath = dir+"/"+f+"/metadata.json"
        # to be continued


        # generate models page

        # generate tasks page

        # remove git cache

        # Yield a task for Doit
        # yield {
        #    'basename': 'vecto_metadata',
#       #     'actions': [(make_file, [base_path+"pages/data/test/test.rst"])],
        #    'actions': [(clone_repo, [])],
        #    'uptodate': [False],
        #}


def main(): # for developing 
    print("hi")


if __name__ == "__main__":
    main()
    mp = MetadataProcessor()
    mp.render()