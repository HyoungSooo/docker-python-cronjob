from bardapi import Bard
import os
import random
import requests
import time
import json
os.environ['_BARD_API_KEY']="XQh0SFsOPtPqYWB4NREzmqRUY2CdbLWvQ8zB64vAbPriV6vWUKAg1f4sL9PzBX3BiQU1nw."

keyward = ['django', 'docker','computer architecture', 'operation system', 'python', 'django-rest-framework', 'algorithm']

queue = requests.get("http://web:8000/api/dashboard/queue/")

if not json.loads(queue.content):
    pass
else:
    query = json.loads(queue.content).pop()

    title = query["query"]
    sub_query = query["sub_query"]

    res = ""

    res += title + ' : '
    res += Bard().get_answer(input_text = title)['content'] + " | "
    if sub_query:
      for i in sub_query.split(','):
          res += Bard().get_answer(input_text = i)['content'] + " | "


    payload = {
        "title" : title, 
        "slug" : 'query' + f"{query['id']}",
        "content" : res,
        "query_string" : sub_query
    }

    requests.post("http://web:8000/api/post/", json = payload, headers={'Content-type': 'application/json'})

    es_payload = {
        "posting" : res,
        "query" : title,
        "sub_query" : sub_query
    }

    requests.post("http://web:8000/api/dashboard/post/", json = es_payload, headers={"Content-type": "application/json"})

    requests.post(f'http://web:8000/api/dashboard/queue/flag?id={query["id"]}')
    


