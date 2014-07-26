# In this script, I'm going to use the OpenCalais API to send 
# a chunk of text, and get back named entities in return. 

import requests
from calais import Calais


API_KEY = "c7pg9t7qj6wtrs3a7fjnm99s"
calais = Calais(API_KEY, submitter="s_carothers")

result = calais.analyze_url("http://www.bestofsicily.com/mafia.htm")

result.print_summary()