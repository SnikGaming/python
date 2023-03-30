import requests
from bs4 import BeautifulSoup
import json

urlmain='https://shop2banh.vn/'


url = 'https://shop2banh.vn/vo-xe-lop-xe.html'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Lấy thông tin về sản phẩm
products = []
for img in soup.find_all('img'):
    src = img.get('src')
    title_div = img.find_next('div', class_='title-prod')
    if title_div is not None:
        title = title_div.find('a').text
    else:
        title = None
    price_div = img.find_next('div', class_='price-prod')
    if price_div is not None:
        price_new_div = price_div.find_next('div', class_='price-new-prod')
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

# In thông tin sản phẩm
for product in products:
    print('Đường dẫn ảnh:', product['src'])
    print('Tiêu đề:', product['title'])
    print('Giá:', product['price'])
    print('---------------------------------------------')

# Chuyển danh sách sản phẩm thành chuỗi JSON
json_products = json.dumps(products, ensure_ascii=False)

# In chuỗi JSON
print('---------------------------------------------')

print(json_products)
print('---------------------------------------------')

