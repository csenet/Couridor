# coding: utf-8
import urllib.request
import json
import base64

GITHUB_BASE_URL = 'https://api.github.com/'


def f(url):
    try:
        with urllib.request.urlopen(url) as res:
            return json.loads(res.read())
    except urllib.error.URLError as e:
        return e.reason


def get_user(user):
    return f(GITHUB_BASE_URL + 'users/' + user)


def get_repos_list(url):
    repos = []
    for i in get_repos_json(url):
        repos.append(i['name'])
    return repos

# 複数の公開リポジトリ


def get_repos_json(url):
    return f(url)


def get_repo(url):
    return f(url)

# ルートのファイル構成


def get_cont(url):
    return f(url + '/contents')


def get_file_cont(url):
    return base64.b64decode(f(url)['content'])


def getUserRepoList(username):
    u = get_user(username)
    repos_list = get_repos_list(u['repos_url'])
    return repos_list

# u = get_user('ase19410008')
# 複数のリポジトリを取得
# repos_json = get_repos_json(u['repos_url'])
# repos_list = get_repos_list(u['repos_url'])
# [x] 選択されたリポジトリ (0が先頭)
# repo = get_repo(repos_json[0]['url'])
# work = [u['name'], repo['name']]
# ルートのファイル構成
# c = get_cont(repo['url'])
# c[0]['url'] 選択されたソースコード
# f = get_file_cont(c[0]['url'])
