# 성북구 철거업체 | 점포리턴 홈페이지

실제 서비스 제공 브랜드 **점포리턴**의 성북구 폐업철거·상가 원상복구 상담 안내용 정적 홈페이지입니다.

## 프로젝트 기본 정보

- 공식 사이트명: `성북구 철거업체`
- SEO Title: `성북구 철거업체 점포리턴 | 폐업철거·상가 원상복구 견적 상담`
- H1: `성북구 철거업체 점포리턴, 폐업철거부터 상가 원상복구까지`
- GitHub Organization으로 선택된 이름: `seongbuk-demolition-guide`
- GitHub Repository로 선택된 이름: `seongbuk-demolition-guide.github.io`
- 사용자가 선택한 **기술적 URL**: `https://seongbuk-demolition-guide.github.io/`
- 제작 기준: 2026-10-23. **실제 배포·도메인 소유확인·색인 및 검색 노출은 수행하지 않았습니다.** 제작 시점 위 URL은 404로 확인되었습니다.

## 배포 전에 꼭 확인할 사항 (중요)

**GitHub Pages는 상업적 거래를 주로 유도하는 영업 사이트를 무료 호스팅하는 용도가 허용되지 않습니다.** 본 사이트는 Google Forms 상담 전환이 주목적이므로 GitHub Repository에서 소스만 관리하고, 실제 홈페이지는 Netlify 같은 상업용 이용 정책에 맞는 무료 정적 호스팅 서비스로 공개하는 것을 권장합니다. 호스팅별 현재 약관을 직접 확인해 주세요.

- GitHub Pages 정책: https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits
- ZIP 최상위에 `index.html`이 있습니다. Netlify에 ZIP을 배포하거나 압축을 해제한 폴더를 업로드할 수 있습니다.
- 공개 도메인이 GitHub에서 선택했던 주소와 달라진 경우 **배포 전에** `python configure-site-url.py https://실제공개주소/` 명령을 실행하세요. 아래 위치를 한꺼번에 수정합니다.
  - HTML canonical 및 og:url, og:image
  - WebSite/WebPage/Organization/Service JSON-LD의 `@id`, URL과 이미지 URL
  - robots.txt의 Sitemap URL
  - sitemap.xml의 `<loc>`
- Python 사용이 어렵다면 `index.html`, `robots.txt`, `sitemap.xml` 세 파일에서 `https://seongbuk-demolition-guide.github.io/`을 **실제 공개 루트 URL**로 모두 찾기/바꾸기 하세요.
- 검색엔진에 등록하기 전 `https://공개주소/robots.txt`, `https://공개주소/sitemap.xml`, 파비콘과 OG 이미지가 모두 수집되는지 확인하세요.

## 구성

```
index.html
style.css
script.js
configure-site-url.py
assets/
  brand-mark.svg
  logo.svg
  commercial-demolition-illustration.webp
  restaurant-interior-illustration.webp
  office-interior-illustration.webp
  empty-store-illustration.webp
  construction-waste-illustration.webp
  consultation-banner.webp
  seongbuk-demolition-og.webp
  before_01.webp
  after_01.webp
  before_02.webp
  after_02.webp
  favicon-32.png
  favicon-48.png
  favicon-512.png
favicon.png
favicon.ico
robots.txt
sitemap.xml
.nojekyll
README.md
```

## 시공 사진과 생성 이미지

- **실제 촬영한 시공 사진 4장**은 사용자가 제공한 원본 WebP 파일을 재압축하지 않고 그대로 복사했습니다.
- 첫 번째 동일 현장: `before_01.webp` ↔ `after_01.webp`.
- 두 번째 동일 현장: `before_02.webp` ↔ `after_02.webp`.
- 서비스·히어로 이미지는 AI 생성 자료의 텍스트 없는 실제 공간 부분을 잘라낸 **일반 설명용 이미지**입니다. 생성한 디자인 자료에 들어 있던 임의 실적·고객만족도 문구는 홈페이지에 사용하지 않았습니다.
- 생성 이미지의 작업자·장비·공간은 점포리턴의 실제 소유 장비·직원·시공현장이라는 증거로 제시하면 안 됩니다.
- 실제 현장 사진에 임의의 공사 금액·공사기간·지역을 부여하지 않았습니다.

## SEO와 콘텐츠

- `lang=ko`, UTF-8, viewport, 단일 H1, 원고 그대로의 메타설명 적용
- 공식 사이트명 `성북구 철거업체`: 화면 헤더, `application-name`, `og:site_name`, WebSite.name에 일치
- 실제 제공 브랜드 `점포리턴` 별도 명시
- robots.txt, sitemap.xml, canonical, OG 메타, WebSite·WebPage·Organization·Service JSON-LD
- 32px 이상 파비콘 및 192px PNG 적용
- 이미지 width/height, alt, Lazy Loading(히어로 제외), WebP, 반응형 시공 전후 비교
- 상담 링크는 모두 아래 지정 URL로 연결하며 새 창의 `noopener noreferrer`를 적용:
  `https://docs.google.com/forms/d/e/1FAIpQLSfdzNitwdwclnvlcy6wj8D73z8kBuRSHsiyCp-L3XB9agx9bQ/viewform?usp=header`
- 점포리턴 성북구 상세페이지 URL은 홈페이지 최종 섹션에 **한 번**만 사용

## 운영 전 추가 확인

1. 실제 배포 URL 확정 후 위 명령어로 SEO 주소를 교체하고, 공식 사이트명 노출·파비콘·검색엔진 수집을 확인하세요. 검색엔진 색인·순위·사이트명 표시는 보장되지 않습니다.
2. **희망리턴패키지 안내는 시점 민감 정보:** 제공된 원고에 따라 2026년 신규 접수 10월 21일 18시 마감으로 표시했습니다. 새 공고가 발표되면 공식 페이지 https://www.sbiz.or.kr/nhrp/main.do 를 확인해 문구를 갱신하세요.
3. 누적 지표 5,540건 이상·2,190건·1,850건은 원고를 보존했으나 집계 기준일과 중복 관계는 추가 확인이 필요합니다. 합산·지역별 전용 실적으로 가공하지 않았습니다.
4. 구글 폼이 실제로 접수 가능한지, 폼 운영 주체가 점포리턴 상담 담당인지 확인하세요.
5. 조직·저장소 개설과 실제 호스팅 업로드는 사용자가 수행해야 합니다.
6. 공사 범위·가용 일정·지원금 수급은 별도 확인 전 확정적으로 안내하지 마세요.

## 수동 확인 체크리스트

홈페이지 PC/태블릿/모바일 화면, 메뉴 버튼, 시공 사진 전후 대응, 4개 주요 상담 CTA, 점포리턴 상세페이지 1회, 이미지·파비콘 경로, 공식 지원사업 안내 갱신, robots/sitemap 도메인 일치를 최종 점검하세요.

## 화면 잘림 수정 내역 (2026-10-23)

- 데스크톱과 모바일에서 히어로 아래의 남색 3단계 안내 카드가 잘리지 않도록 부모 영역의 `overflow:hidden`을 제거했습니다.
- 히어로 사진과 참고 이미지 안내 문구를 같은 세로 흐름으로 배치해 사진 바로 아래에 문구가 표시되도록 했습니다.
- 히어로 사진에 `height:auto`와 `object-fit:contain`을 적용하여 파일의 전체 비율을 유지하도록 했습니다.
- Windows에서 `index.html`을 직접 열어 확인할 때도 파비콘 경로를 찾을 수 있도록 상대 경로를 사용했습니다.
- 390px/768px/1218px/1440px 화면 폭의 Chromium 기반 레이아웃에서 가로 스크롤 여부·안내 카드 노출 상태·히어로 원본 비율을 검사했습니다. 실제 배포 후 각 브라우저 최종 확인이 필요합니다.
