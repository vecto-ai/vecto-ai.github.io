# -*- coding: utf-8 -*-

# Copyright © 2012-2013 Roberto Alsina

# Permission is hereby granted, free of charge, to any
# person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the
# Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the
# Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice
# shall be included in all copies or substantial portions of
# the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import json
import os

plugin_path = os.path.dirname(os.path.realpath(__file__))
base_path = plugin_path.split("plugins")[0]


from nikola.plugin_categories import Task
from nikola.utils import LOGGER
from git import Repo




class Plugin(Task):

    name = "vecto_metadata"

    def gen_tasks(self):

        # This function will be called when the task is executed

        # clone repo
        def clone_repo():

            cache_dir = base_path+"cache/git-resources"
            if not os.path.exists(cache_dir):
                os.mkdir(cache_dir)
                Repo.clone_from("https://github.com/vecto-ai/vecto-resources.git", cache_dir)

        # generate corpora page

        # generate embeddings page

        # generate datasets page
        def get_datasets():
            dir = base_path+"cache/git-resources/resources.datasets"
            dlist = os.listdir(dir)
            for f in dlist:
                fpath = dir+"/"+f+"/metadata.json"
        # to be continued


        # generate models page

        # generate tasks page

        # remove git cache

        # Yield a task for Doit
        yield {
            'basename': 'vecto_metadata',
#            'actions': [(make_file, [base_path+"pages/data/test/test.rst"])],
            'actions': [(clone_repo, [])],
            'uptodate': [False],
        }
