from tools import *


def get_sale_items(category, retailer='aritzia', merchandise='clothing'):
    url = read_config(merchandise, retailer, category)
    page_source = get_page_source(url)
    sale = []
    for i in range(len(page_source)):
        line = page_source[i]
        if re.search('product-standard-price', line) is not None:
            neighbor = page_source[(i-15):i]
            for row in neighbor:
                if re.search('http://www.aritzia', row) is not None:
                    sale.append(row)
    sale_items = {}
    for item in sale:
        name = re.split('"', re.split('title', item)[1])[1]
        name = name.upper()
        url = re.split('"', re.split('href', item)[1])[1]
        sale_items[name] = url
    return sale_items