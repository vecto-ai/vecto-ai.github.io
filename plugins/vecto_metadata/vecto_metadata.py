# -*- coding: utf-8 -*-

import json
import os
import sys
from nikola.plugin_categories import Task, RestExtension

from docutils import nodes
from docutils.parsers.rst import Directive, directives

from nikola.utils import LOGGER
from git import Repo
from mako.template import Template


plugin_path = os.path.dirname(os.path.realpath(__file__))
base_path = plugin_path.split("plugins")[0]


def load_json(path):
    f = open(path)
    s_data = f.read()
    data = json.loads(s_data)
    f.close()
    return data

def filter_entry(metadata):
    if "description" not in metadata:
        metadata["description"] = "__temp"
    for key in ["url", "project_page"]:
        if key not in metadata:
            metadata[key] = ""
    keys = ["class", "description", "url", "project_page"]
    filtered = {key: metadata[key] for key in keys}
    return filtered


def get_entries(path):
    for dirName, subdirList, fileList in os.walk(path, topdown=False):
        for fname in fileList:
            yield(os.path.join(dirName, fname))


class MetadataProcessor():
    def read_files(self):
        self.rows = []
        for fname in get_entries(os.path.join(base_path, "aux/resources/vecto-resources/resources")):
            data = load_json(fname)
            self.rows.append(filter_entry(data))
    
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