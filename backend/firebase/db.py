
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import sys

# 親階層のapiを読み込む
sys.path.append('../')
import api
import work

cred = credentials.Certificate("firebase.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

docs = db.collection('user').get()

user = api.get_user('ase19410008')
repos = api.get_repos_json(user['repos_url'])

w = work.work({'cout':1, 'creatorImg':user['avatar_url']}).set_def_val()
# c2 = C({'cout':0, 'creatorImg':'fuga', 'bad_num':10, 'like_num':200, 'creator':'me', 'explation':'piyo'})
# c2.f2()
# db.collection('users').add({user['name']: api.get_repo(repos[1]['url'])['name']})
# db.collection('works').add(w)