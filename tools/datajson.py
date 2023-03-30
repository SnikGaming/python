import requests
from bs4 import BeautifulSoup
import json

url = 'https://shop2banh.vn/vo-xe-lop-xe.html'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Lấy thông tin về sản phẩm
products = []
for item in soup.find_all('div', class_='col-lg-4 col-md-6 col-sm-4 col-xs-6 items ripple'):
    img = item.find('img')
    src = img.get('src')
    title_div = item.find('div', class_='title-prod')
    if title_div is not None:
        title = title_div.find('a').text
    else:
        title = None
    price_div = item.find('div', class_='price-prod')
    if price_div is not None:
        price_new_div = price_div.find('div', class_='price-new-prod')
        if price_new_div is not None:
            price = price_new_div.contents[0].strip()
            # Xóa ký tự đơn vị tiền tệ 'đ'
            price = price.replace(' đ', '')
        else:
            price_divs = price_div.find_all('div', class_='ct-sp-child-price')
            price = ''
            for price_div in price_divs:
                price += price_div.text.strip() + ' '
    else:
        price_new_div = None
        price = None
    products.append({
        'src': src,
        'title': title,
        'price': price
    })

# Chuyển đổi danh sách sản phẩm thành chuỗi JSON
products_json = json.dumps(products)

# In chuỗi JSON
print(products_json)


# Ghi nội dung vào file JSON
# with open('data.json', 'w', encoding='utf-8') as f:
#     json.dump(products_json, f, ensure_ascii=False, indent=4)
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, ensure_ascii=False, indent=4)
