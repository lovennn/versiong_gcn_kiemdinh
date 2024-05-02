# Viết chương trình đọc lấy dữ liệu từ trang dantri.com

# Import thư viện

import requests
from bs4 import BeautifulSoup

# Lấy dữ liệu từ trang web

url = 'https://dantri.com.vn'

response = requests.get(url)

# Kiểm tra xem kết quả trả về có thành công không

if response.status_code == 200:
    print('Kết nối thành công')

    # Lấy dữ liệu từ trang web

    soup = BeautifulSoup(response.text, 'html.parser')

    # Tìm tất cả thẻ h3 có class = 'article-title'

    titles = soup.find_all('h3', class_='article-title')

    # In ra các tiêu đề

    for title in titles:
        print(title.text)
        
        # Lưu dữ liệu vào file text, tên file sẽ lấy theo ngày tháng năm, giờ phút giây

        with open('dantri.txt', 'a', encoding='utf-8') as f:
            f.write(title.text + '\n')

            

       
else:
    print('Kết nối thất bại')






