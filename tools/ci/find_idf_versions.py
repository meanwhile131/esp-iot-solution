# SPDX-FileCopyrightText: 2026 Espressif Systems (Shanghai) CO LTD
# SPDX-License-Identifier: Apache-2.0
import json
import urllib.request
import sys

data = {'next': 'https://hub.docker.com/v2/repositories/espressif/idf/tags'}
versions = ['latest']
min_major = 5
min_minor = 3

while data['next']:
    req = urllib.request.urlopen(data['next'])
    data = json.loads(req.read().decode())
    for result in data['results']:
        name: str = result['name']
        if not name.startswith('release-'):
            continue
        ver = name.lstrip('release-v')
        major, minor = map(int, ver.split('.'))
        if major > min_major or (major == min_major and minor >= min_minor):
            versions.append(name)

json.dump(versions, sys.stdout)
