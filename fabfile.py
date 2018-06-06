import os
from fabric.api import local, lcd


def clean():
    with lcd(os.path.dirname(__file__)):
        # local("python3.6 setup.py clean --all")
        local("find . | grep -E \"(__pycache__|\.pyc$)\" | xargs rm -rf")
        local("rm -rf ./docs/build || true")
        local("rm -rf ./docs/source/reference/_autosummary || true")


def make():
    local("python3.6 setup.py bdist_wheel")


def update():
    with lcd("./aux/resources/vecto-resources"):
        local("git pull")


def deploy():
    # test()
    # make()
    local("nikola github_deploy")


def test():
    local("python3.6 -m unittest")
