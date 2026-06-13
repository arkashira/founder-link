import json
import os
from dataclasses import dataclass
from urllib.parse import urlparse

@dataclass
class MVP:
    name: str
    url: str
    updated: bool

class FounderLink:
    def __init__(self, mvp_name):
        self.mvp_name = mvp_name
        self.mvps = {}

    def host_mvp(self, mvp):
        self.mvps[mvp.name] = mvp

    def deploy_mvp(self, mvp_name):
        if mvp_name in self.mvps:
            return self.mvps[mvp_name].url
        else:
            return None

    def update_mvp(self, mvp_name):
        if mvp_name in self.mvps:
            self.mvps[mvp_name].updated = True
            return self.mvps[mvp_name].url
        else:
            return None

    def get_mvp_url(self, mvp_name):
        if mvp_name in self.mvps:
            return self.mvps[mvp_name].url
        else:
            return None
