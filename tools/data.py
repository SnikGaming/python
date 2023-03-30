import requests
from bs4 import BeautifulSoup

urlmain = 'https://shop2banh.vn/'

url = 'https://shop2banh.vn/vo-xe-lop-xe.html'
response = requests.get(url)

# <div class="col-lg-4 col-md-6 col-sm-4 col-xs-6 items ripple">
#         <div class="img-prod" style="min-height: 123px;">
#             <a href="https://shop2banh.vn/lop-aspira-sportivo-11080-14-14070-14-2054.html" title="Lốp Aspira Sportivo (110/80-14 - 140/70-14)">
#                                 <img src="https://shop2banh.vn/images/thumbs/2023/03/lop-aspira-sportivo-11080-14-14070-14-products-2054.jpg" alt="Lốp Aspira Sportivo (110/80-14 - 140/70-14)">
#                             </a>
#         </div>
#         <div class="title-prod aaccc"><a href="https://shop2banh.vn/lop-aspira-sportivo-11080-14-14070-14-2054.html" title="Lốp Aspira Sportivo (110/80-14 - 140/70-14)">Lốp Aspira Sportivo (110/80-14 - 140/70-14)</a></div>
#         <div class="price-prod">
#         					<div class="ct-child-pro-price-wrp"><div class="ct-sp-child-price ">Vỏ trước: <span>910.000 đ</span></div><div class="ct-sp-child-price ">Vỏ sau: <span>1.240.000 đ</span></div></div>                        <div class="clearFix"></div>
#         </div>
#     </div>

soup = BeautifulSoup(response.text, 'html.parser')

# Lấy thông tin về sản phẩm
products = []
div_items = soup.find_all('div', class_='col-lg-4 col-md-6 col-sm-4 col-xs-6 items ripple')
for div_item in div_items:
    img = div_item.find('img')
    src = img.get('src')
    title_div = div_item.find('div', class_='title-prod')
    if title_div is not None:
        title = title_div.find('a').text
    else:
        title = None
    price_div = div_item.find('div', class_='price-prod')
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

# In thông tin sản phẩm
for product in products:
    print('Đường dẫn ảnh:', product['src'])
    print('Tiêu đề:', product['title'])
    print('Giá:', product['price'])
    print('---------------------------------------------')
