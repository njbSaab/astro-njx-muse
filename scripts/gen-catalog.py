#!/usr/bin/env python3
"""Generate src/data/mock-catalog.json for Noble Muse (28 pieces, 10 categories)
plus scripts/photos.json (file -> candidate URLs) for fetch-photos.py."""
import json, os, re

def u(pid): return f'https://images.unsplash.com/{pid}?auto=format&fit=crop&w=1100&q=80'
def px(pid): return f'https://images.pexels.com/photos/{pid}/pexels-photo-{pid}.jpeg?auto=compress&cs=tinysrgb&w=1100'

def slug(s):
    s = re.sub(r'[^a-z0-9]+', '-', s.lower())
    return re.sub(r'-+', '-', s).strip('-')

COLORS = {
 'ink': ('Ink Navy', '#191936'), 'cream': ('Cream', '#efe9df'),
 'mulberry': ('Mulberry', '#6d3550'), 'sage': ('Sage', '#9aa48f'),
 'camel': ('Camel', '#b3906a'), 'black': ('Black', '#14141a'),
 'stone': ('Stone', '#c9c3b8'), 'indigo': ('Washed Indigo', '#4a5a78'),
}
STD = 'XS,S,M,L,XL'
DEN = '26,27,28,29,30,31'
ONE = 'ONE SIZE'

# (idx, name, category, price, sale, badge, colors, sizes, [main cands], [gallery cands])
PIECES = [
 ('nm01','Vesper Slip Dress','Dresses',149.95,0,'NEW IN','ink,cream',STD,[u('photo-1515372039744-b8f02a3ae446')],[px(985635)]),
 ('nm02','Aurelie Midi Dress','Dresses',169.95,0,'','mulberry,ink,sage',STD,[px(1055691)],[px(291762)]),
 ('nm03','Solene Knit Dress','Dresses',129.95,89.95,'LAST CHANCE','camel,black',STD,[px(972995)],[px(1926769)]),
 ('nm04','Marguerite Shirt Dress','Dresses',139.95,0,'','cream,indigo',STD,[px(1926769)],[u('photo-1515372039744-b8f02a3ae446')]),
 ('nm05','Odette Silk Blouse','Blouses',129.95,0,'','cream,mulberry',STD,[px(2065200)],[px(6764928)]),
 ('nm06','Lenna Balloon Blouse','Blouses',99.95,0,'NEW IN','ink,cream,sage',STD,[px(1381556)],[px(2065195)]),
 ('nm07','Ivo Bow Blouse','Blouses',109.95,69.95,'LAST CHANCE','black',STD,[u('photo-1583846717393-dc2412c95ed7')],[px(3965548)]),
 ('nm08','Cove Poplin Shirt','Shirts & Tops',79.95,0,'','cream,indigo',STD,[u('photo-1564257631407-4deb1f99d992')],[px(1036623)]),
 ('nm09','Nera Rib Top','Shirts & Tops',49.95,0,'','black,cream,mulberry',STD,[px(1036623)],[px(794064)]),
 ('nm10','Wren Cotton Tee','Shirts & Tops',39.95,0,'','cream,sage',STD,[px(2065195)],[px(1381556)]),
 ('nm11','Halden Cashmere Jumper','Sweaters & Hoodies',179.95,0,'NEW IN','camel,ink',STD,[px(45982)],[px(6764007)]),
 ('nm12','Rowan Cable Knit','Sweaters & Hoodies',139.95,0,'','cream,sage',STD,[u('photo-1434389677669-e08b4cac3105')],[px(45982)]),
 ('nm13','Elgin Hoodie','Sweaters & Hoodies',89.95,0,'','stone,black',STD,[px(1183266)],[px(794064)]),
 ('nm14','Mira Merino Cardigan','Sweaters & Hoodies',149.95,99.95,'','mulberry,cream',STD,[px(794064)],[u('photo-1434389677669-e08b4cac3105')]),
 ('nm15','Aldford Wool Coat','Jackets & Coats',299.95,0,'NEW IN','ink,camel',STD,[px(2887766)],[u('photo-1544923246-77307dd654cb')]),
 ('nm16','Bryn Quilted Jacket','Jackets & Coats',189.95,0,'','sage,black',STD,[u('photo-1591047139829-d91aecb6caea')],[px(1462637)]),
 ('nm17','Sable Trench','Jackets & Coats',249.95,0,'','stone',STD,[u('photo-1578102718171-ec1f91680562')],[px(2887766)]),
 ('nm18','Tessa Shearling Jacket','Jackets & Coats',279.95,199.95,'LAST CHANCE','cream,camel',STD,[px(1462637)],[u('photo-1591047139829-d91aecb6caea')]),
 ('nm19','Marlow Tweed Blazer','Blazers',199.95,0,'NEW IN','ink,stone',STD,[u('photo-1594938298603-c8148c4dae35')],[px(1036622)]),
 ('nm20','Juno Longline Blazer','Blazers',179.95,0,'','black,mulberry',STD,[px(1036622)],[u('photo-1594938298603-c8148c4dae35')]),
 ('nm21','Ida Wide Trouser','Trousers',119.95,0,'','ink,cream,camel',STD,[u('photo-1594633312681-425c7b97ccd1')],[u('photo-1509551388413-e18d0ac5d495')]),
 ('nm22','Lo Pleated Trouser','Trousers',129.95,0,'NEW IN','black,stone',STD,[u('photo-1509551388413-e18d0ac5d495')],[u('photo-1594633312681-425c7b97ccd1')]),
 ('nm23','Faye Straight Jean','Denim',99.95,0,'','indigo,black',DEN,[u('photo-1541099649105-f69ad21f3246')],[u('photo-1542272604-787c3835535d')]),
 ('nm24','Nine Barrel Jean','Denim',109.95,0,'NEW IN','indigo',DEN,[u('photo-1542272604-787c3835535d')],[u('photo-1541099649105-f69ad21f3246')]),
 ('nm25','Robin Wide Denim','Denim',89.95,59.95,'','indigo,stone',DEN,[u('photo-1584370848010-d7fe6bc767ec')],[u('photo-1541099649105-f69ad21f3246')]),
 ('nm26','Otta Leather Belt','Accessories',59.95,0,'','black,camel',ONE,[u('photo-1553062407-98eeb64c6a62')],[px(2079438)]),
 ('nm27','Suri Wool Scarf','Accessories',69.95,0,'LAST CHANCE','mulberry,cream',ONE,[u('photo-1520903920243-53111ea4f7ea')],[px(45982)]),
 ('nm28','Base Rib Bodysuit','Essentials',44.95,0,'','black,cream',STD,[px(3965548)],[px(6764928)]),
]

CHROME_PHOTOS = {
 # hero campaign slides — moody editorial, text sits on top
 'hero-1.jpg': [u('photo-1469334031218-e382a71b716b'), px(2065195)],
 'hero-2.jpg': [u('photo-1483985988355-763728e1935b'), px(1755428)],
 'hero-3.jpg': [u('photo-1566174053879-31528523f8ae'), px(1926769)],
 # category tiles (3/4.2 portrait)
 'cat-coats.jpg': [px(2887766)],
 'cat-knitwear.jpg': [u('photo-1434389677669-e08b4cac3105')],
 'cat-dresses.jpg': [px(1055691)],
 'cat-blouses.jpg': [px(1381556)],
 # banners
 'banner-tweed.jpg': [u('photo-1594938298603-c8148c4dae35')],
 'banner-denim.jpg': [u('photo-1542272604-787c3835535d')],
 'banner-wide.jpg': [px(2955375), u('photo-1507679799987-c73779587ccf')],
 # shop the look tiles
 'look-1.jpg': [px(2065195)],
 'look-2.jpg': [px(45982)],
 'look-3.jpg': [px(2065200)],
 'look-4.jpg': [px(1462637)],
 'look-5.jpg': [u('photo-1541099649105-f69ad21f3246')],
 'look-6.jpg': [px(1036622)],
 'look-7.jpg': [px(794064)],
 'look-8.jpg': [px(1055691)],
 # newsletter + popup
 'newsletter.jpg': [px(1755428)],
 'popup.jpg': [px(2065195), px(972995)],
}

products, photos = [], dict(CHROME_PHOTOS)
for row in PIECES:
    (pid, name, category, price, sale, badge, colors, sizes, main_c, gal_c) = row
    handle = f'{pid}-{slug(name)}'
    photos[f'{pid}.jpg'] = main_c
    photos[f'{pid}b.jpg'] = gal_c
    products.append({
        'id': pid, 'handle': handle, 'title': name,
        'description': f'{name} in the Noble Muse autumn edit.',
        'vendor': 'Noble Muse',
        'images': [{'src': f'/products/{pid}.jpg', 'alt': name},
                   {'src': f'/products/{pid}b.jpg', 'alt': f'{name} — full look'}],
        'price': {'amount': sale if sale else price, 'currency': 'EUR'},
        **({'compareAtPrice': {'amount': price, 'currency': 'EUR'}} if sale else {}),
        'variants': [{'id': pid + 'v1', 'title': 'Standard', 'price': {'amount': sale if sale else price, 'currency': 'EUR'}, 'available': True}],
        'tags': [badge] if badge else [],
        'collectionHandles': ['noble-muse', slug(category)],
        'meta': {
            'cat': category, 'badge': badge,
            'colors': [{'name': COLORS[c][0], 'hex': COLORS[c][1]} for c in colors.split(',')],
            'sizes': sizes.split(','),
        },
    })

CATS = ['Dresses', 'Blouses', 'Shirts & Tops', 'Sweaters & Hoodies', 'Jackets & Coats', 'Blazers', 'Trousers', 'Denim', 'Accessories', 'Essentials']
collections = [{
    'handle': 'noble-muse', 'name': 'NOBLE MUSE', 'tagline': 'DRESSING MODERN MUSES',
    'categories': [{'name': c, 'count': len([p for p in products if p['meta']['cat'] == c])} for c in CATS],
    'count': len(products),
}]

out = {'collections': collections, 'products': products}
root = os.path.join(os.path.dirname(__file__), '..')
json.dump(out, open(os.path.join(root, 'src/data/mock-catalog.json'), 'w'), indent=1, ensure_ascii=False)
json.dump(photos, open(os.path.join(root, 'scripts/photos.json'), 'w'), indent=1)
print(len(products), 'pieces,', len(photos), 'photo files')
