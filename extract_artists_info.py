from utils import *
import pickle
import traceback

sep = '##### NEW FILE #####\n'
error = []
site = 'zing'

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

        if kb[url]['country']:
            continue

        # if kb[url]['country'] != 'Việt Nam':
        #     continue

        try:
            name = kb[url]['name']
            # professions = kb[url]['professions']
            # instruments = kb[url]['instruments']
            # name = extract_artist_name(html, site)
            text = extract_biography(html, site)
            # professions = extract_professions(text)
            # instruments = extract_instruments(text)

            # kb[url]['name'] = name
            # kb[url]['professions'].update(professions)
            # kb[url]['instruments'].update(instruments)

            # info = extract_artist_info(html, site)
            # kb[url]['dob'] = info['dob']
            # if ' == ' in name:
            #     kb[url]['birth_name'] = name.split(' == ')[1]
            # else:
            #     kb[url]['birth_name'] = info['birth_name']
            #     if 'dob' not in kb[url]:
            #         kb[url]['dob'] = info['dob']
            #         if ' >> ' in name:
            #             kb[url]['country'] = name.split(' >> ')[1]
            #         else:
            #             kb[url]['country'] = info['country']

            # img = extract_img(html, site)
            # kb[url]['img'] = img

            # city = extract_city(text)
            # height = extract_height(text)
            # kb[url]['city'] = city
            # kb[url]['height'] = height

            print('*' * 80)
            print('url:', url)
            print('name:', name)
            # print('professions:', professions)
            # print('instruments:', instruments)
            # print(kb[url]['img'])
            # print(kb[url]['city'])
            # print()
        except:
            error.append(url)

if site == 'zing':
    urls = ['https://mp3.zing.vn/nghe-si/Son-Tung-M-TP/tieu-su',
            'https://mp3.zing.vn/nghe-si/Soobin-Hoang-Son/tieu-su',
            'https://mp3.zing.vn/nghe-si/Dong-Nhi/tieu-su',
            'https://mp3.zing.vn/nghe-si/Phan-Manh-Quynh/tieu-su',
            'https://mp3.zing.vn/nghe-si/Thuy-Chi/tieu-su',
            'https://mp3.zing.vn/nghe-si/Noo-Phuoc-Thinh/tieu-su']
elif site == 'nct':
    urls = ['https://www.nhaccuatui.com/nghe-si-son-tung-mtp.html',
            'https://www.nhaccuatui.com/nghe-si-soobin-hoang-son.html',
            'https://www.nhaccuatui.com/nghe-si-dong-nhi.html',
            'https://www.nhaccuatui.com/nghe-si-phan-manh-quynh.html',
            'https://www.nhaccuatui.com/nghe-si-thuy-chi.html',
            'https://www.nhaccuatui.com/nghe-si-noo-phuoc-thinh.html']
urls = ['https://mp3.zing.vn/nghe-si/Anh-Linh/tieu-su',
        'https://mp3.zing.vn/nghe-si/Ngoc-Anh/tieu-su',
        'https://mp3.zing.vn/nghe-si/Truong-Tam/tieu-su',
        'https://mp3.zing.vn/nghe-si/Duc-Truong/tieu-su',
        'https://mp3.zing.vn/nghe-si/Thanh-Hung-TDSC/tieu-su',
        'https://mp3.zing.vn/nghe-si/Thuy-Huong/tieu-su',
        'https://mp3.zing.vn/nghe-si/Chi-Dung/tieu-su',
        'https://mp3.zing.vn/nghe-si/Thien-Kieu/tieu-su',
        'https://mp3.zing.vn/nghe-si/Chau-Giang/tieu-su',
        'https://mp3.zing.vn/nghe-si/Bich-Huong/tieu-su',
        'https://mp3.zing.vn/nghe-si/Nguyen-Phuong-Uyen-Tru-Tinh/tieu-su',
        'https://mp3.zing.vn/nghe-si/Giang-Tam-Tru-Tinh/tieu-su',
        'https://mp3.zing.vn/nghe-si/VRT/tieu-su',
        'https://mp3.zing.vn/nghe-si/Zero9/tieu-su',
        'https://mp3.zing.vn/nghe-si/DJ-Minh-Tri/tieu-su',
        'https://mp3.zing.vn/nghe-si/My-Van/tieu-su',
        'https://mp3.zing.vn/nghe-si/Machiot/tieu-su',
        'https://mp3.zing.vn/nghe-si/Dinh-Long/tieu-su',
        'https://mp3.zing.vn/nghe-si/Thai-Anthony/tieu-su',
        'https://mp3.zing.vn/nghe-si/Murda-Beatz/tieu-su']
for url in urls:
    print(kb[url])

# with open(site + '_artists.kb', 'wb') as f:
#     pickle.dump(kb, f)

# with open('error.pickle', 'wb') as f:
#     pickle.dump(error, f)
