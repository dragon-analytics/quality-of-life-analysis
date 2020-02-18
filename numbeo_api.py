import os
import requests
import json
from api_resources import RESOURCES
from functools import partial

API_FILE = 'api_key'
BASE_URL = 'http://www.numbeo.com:8008/api/'

class Numbeo:
    
    def __init__(self):
        #load api api
        self.api_key = self._load_api_key()
        
        # All of the api calls use the same pattern: 
        # /api/RESOURCE_NAME?api_key=YOUR_KEY&PARAMS 
        # Create methods programatically so one can call
        # Numbeo.RESOURCE_NAME(PARAM1=VALUE1,...)
        #set also docstrings for all the methods
        list(map(lambda method,doc: 
                [setattr(self, method, partial(self._collection_resource, method)),
                 setattr(getattr(self,method),'__doc__',doc)],
                 RESOURCES.keys(),RESOURCES.values()))
        
    def _make_request(self, url, payload):
        """
        wrapper around get requests
        """
        response = requests.get(url, params = payload)
        if response.status_code != 200:
            raise Exception(response)
            
        json_response = json.loads(response.content.decode('utf8'))
        if json_response.get('error'):
            raise Exception(json_response.get('error'))
        return json_response


    def _collection_resource(self, resource, **params):
        """
        This implements the methods in Numbeo.RESOURCE_LIST
        """
        url = BASE_URL + resource
        payload = {'api_key': self.api_key, **params} \
            if params else {'api_key': self.api_key}
        return self._make_request(url,payload)
    
    def _load_api_key(self):
        """
        Loads api key from file.
        If file doesn't exit, creates empty one and ask for key.
        """
        if os.path.isfile(API_FILE):
            #read file. If empty, ask for key
            with open(API_FILE, 'r', errors='ignore') as fdesc:
                api_key = fdesc.read()
            if api_key == '':
                raise Exception("Please paste the api key in file {}".format(API_FILE))
        else:
            open(API_FILE, 'w').close()
            raise Exception("Please paste the api key in file {}".format(API_FILE))


        return api_key