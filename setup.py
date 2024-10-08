import csv
import os
import requests


def download(url, path):
    print(f'Downloading {url} to {path}...', end=' ')
    r = requests.get(url)
    if r.status_code != 200:
        print(f'Failed: {r.status_code}.')
        return
    with open(path, 'wb') as f:
        f.write(r.content)
    print('Done.')


def read_tsv(path):
    with open(path, encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        header = next(reader)
        data = list(reader)
    return header, data


def generate_wang3_js():
    print(f'Generating wang3.js...', end=' ')
    js = 'const wang3 = {\n'
    for k in ['corresponding', 'unique']:
        header, data = read_tsv(f'wang3_{k}.tsv')
        header = ','.join(header)
        data = '|'.join([','.join(line) for line in data])
        js += f'  {k}Header: `{header}`,\n'
        js += f'  {k}: `{data}`,\n'
    js += '};'
    with open(f'wang3.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print('Done.')


download('https://cdn.jsdelivr.net/npm/tshet-uinh@0.15.1', 'tshet-uinh.js')
os.makedirs('schemas', exist_ok=True)
for schema_name in ['tupa', 'unt', 'panwuyun']:
    download(f'https://nk2028-1305783649.file.myqcloud.com/tshet-uinh-examples/{schema_name}.js',
             f'schemas/{schema_name}.js')
generate_wang3_js()
