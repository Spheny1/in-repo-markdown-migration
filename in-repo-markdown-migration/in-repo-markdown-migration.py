import os.path
from mkdocs.config import config_options as mkd
from .configitems import ConfigItems
from mkdocs.plugins import BasePlugin

def InRepoMarkdownMigration(BasePlugin):
    config_scheme = ()
    def on_config(config):
        print("helloworld")

    def on_files(files, config):
        print("On_files")
