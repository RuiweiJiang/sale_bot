from tools import *

def get_promotions(page, retailer='faceshop', merchandise='skincare'):
    url = read_config(merchandise, retailer, page)
    print url
    page_source = get_page_source(url)
    promotions = []
    for i in range(len(page_source)):
        line = page_source[i]
        if re.search('promotion', line) is not None:
            promotions.append(line)
    promotion_clean = {}
    for p in promotions:
        if re.search('href', p) is not None:
            href = re.split('"', re.split('href',p)[1])[1]
            if re.search('promotions$|promotions/$', href) is None:
                promotion = re.split('/', href)[-1]
                promotion = re.sub('-', ' ', promotion.lower())
                promotion_clean[promotion] = href
    return promotion_clean

def get_tag_associated_url(keywords):
    url = read_config('skincare', 'faceshop', 'home')
    search_results = access_page_search(url, keywords)
    for line in search_results:
        if find_tag_in_source(line, ['hyperlink', 'title']):
            return None
    return None