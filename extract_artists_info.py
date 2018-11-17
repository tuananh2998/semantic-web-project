from utils import *
import pickle
import traceback

sep = '##### NEW FILE #####\n'
error = []
site = 'nct'

if site == 'zing':
    files = ['zing/tieu_su_' + str(i) + '.txt' for i in range(3)]
elif site == 'nct':
    files = ['nct/tieu_su_' + str(i) + '.txt' for i in range(1)]

with open(site + '_artists.kb', 'rb') as f:
# with open('tmp.kb', 'rb') as f:
    kb = pickle.load(f)
error = []

for file in files:
    print('>>>', file)
    with open(file, 'r', encoding='utf8') as f:
        list_tieu_su = f.read().split(sep)[1:]

    for tieu_su in list_tieu_su:
        url, html = tieu_su.split('\n', 1)

        if url not in kb or error_404 in html:
            continue

        try:
            name = kb[url]['name']
            # professions = kb[url]['professions']
            # instruments = kb[url]['instruments']
            # name = extract_artist_name(html, site)
            # text = extract_biography(html, site)
            # professions = extract_professions(text)
            # instruments = extract_instruments(text)

            info = extract_artist_info(html, site)
            kb[url]['dob'] = info['dob']
            if ' == ' in name:
                kb[url]['birth_name'] = name.split(' == ')[1]
            else:
                kb[url]['birth_name'] = info['birth_name']
            if 'dob' not in kb[url]:
                kb[url]['dob'] = info['dob']
            if ' >> ' in name:
                kb[url]['country'] = name.split(' >> ')[1]
            else:
                kb[url]['country'] = info['country']

            # kb[url]['name'] = name
            # kb[url]['professions'].update(professions)
            # kb[url]['instruments'].update(instruments)

            print('*' * 80)
            print('url:', url)
            print('name:', name)
            # print('professions:', professions)
            # print('instruments:', instruments)
            print(kb[url])
            print()
        except:
            error.append(url)

# with open(site + '_artists.kb', 'wb') as f:
#     pickle.dump(kb, f)
#
# with open('error.pickle', 'wb') as f:
#     pickle.dump(error, f)