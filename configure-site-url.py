#!/usr/bin/env python3
"""Update absolute SEO URLs when the actual public HTTPS root domain is fixed.
Usage: python configure-site-url.py https://your-public-domain.example/
"""
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

if len(sys.argv) != 2:
    raise SystemExit('사용법: python configure-site-url.py https://your-public-domain.example/')
new = sys.argv[1].strip().rstrip('/') + '/'
u = urlparse(new)
if u.scheme != 'https' or not u.netloc or u.path != '/' or u.query or u.fragment:
    raise SystemExit('루트에 공개한 HTTPS 주소만 입력해 주세요. 예: https://sample.netlify.app/')
root = Path(__file__).resolve().parent
html = (root / 'index.html').read_text(encoding='utf-8')
m = re.search(r'<link rel="canonical" href="(https://[^\"]+/)"', html)
if not m:
    raise SystemExit('index.html의 기존 canonical URL을 찾지 못했습니다.')
old = m.group(1)
for name in ('index.html', 'robots.txt', 'sitemap.xml'):
    f = root / name
    raw = f.read_text(encoding='utf-8')
    f.write_text(raw.replace(old, new), encoding='utf-8')
print(f'SEO 주소 변경 완료: {old} → {new}')
print('canonical, OG URL, JSON-LD URL, robots.txt, sitemap.xml 동기화')
