# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 11:46:29 2019

@author: hfuji
"""

import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
print(client)
print(client.database_names())

db = client.get_database('twitter')
result = db.tweets.insert_one({
    'created_at': 'Mon Jan 22 06:42:41 +0000 2018',
    'id': 955329854605537281,
    'lang': 'ja',
    'text': 'python使えるとWEBからデータ解析まで幅広いところで重宝されるから今のうち基礎固めとくといいことある'
})
print(result.acknowledged, result.inserted_id)

all([client.foo.bar == client['foo']['bar'],
     client.foo.bar == client.get_database('foo').get_collection('bar'),
     client['foo']['bar'] == client.get_database('foo').get_collection('bar')])

print(db.tweets.find_one())
print(list(db.tweets.find()))

db.tweets.insert_one({
    'created_at': 'Mon Jan 22 09:11:33 +0000 2018',
    'id': 955367321220067333,
    'lang': 'ja',
    'text': '@petrol0110 @setuko1234 ワタシはプログラミング言語としてのPythonをちょっとかじった程度なので、統計ツールとしてのPythonは良く知らないんで何とも言えないんだけど。どんなもんかかじってみるのは損には… https://t.co/vFAbolzrrk',
    'entities': {
        'hashtags': [],
        'symbols': [],
        'user_mentions': [
            {'screen_name': 'petrol0110',
             'name': '石油王',
             'id': 838950516742770689, 
             'id_str': '838950516742770689',
             'indices': [0, 11]},
            {'screen_name': 'setuko1234',
             'name': 'せつこ山(のりこ山)後で一緒に風呂行く？',
             'id': 420145642,
             'id_str': '420145642',
             'indices': [12, 23]}],
        'urls': [
            {'url': 'https://t.co/vFAbolzrrk',
             'expanded_url': 'https://twitter.com/i/web/status/955367321220067333',
             'display_url': 'twitter.com/i/web/status/9…',
             'indices': [117, 140]}
        ]
    }
})
print(list(db.tweets.find()))

db.tweets.insert_many([
    {'created_at': 'Mon Jan 22 09:24:34 +0000 2018',
     'id': 955370596229148673, 
     'lang': 'en',
     'text': 'RT @mikedailly: Who knew there were two different single markets? Labour’s position on #Brexit is the dead parrot in Monty Python’s sketch.…'
    },
    {'created_at': 'Mon Jan 22 08:39:56 +0000 2018',
     'id': 955359364310646784,
     'lang': 'ja',
     'text': '@sylvan5 データの読み込みは TensorFlow のモジュールを使って、モデルの部分は tf.keras を使うという手が。。。https://t.co/hueLxCqEF3',
    },
])

db.tweets.drop()
