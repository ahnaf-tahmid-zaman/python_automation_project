from bs4 import BeautifulSoup
import requests
import openpyxl

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = "price"
sheet.append(['Brand', 'Name', 'Price'])
try:
    url = requests.get(
        'https://www.techlandbd.com/pc-components/graphics-card?limit=100')
    url.raise_for_status()
    soup = BeautifulSoup(url.text, 'html.parser')
    cards = soup.find(
        'div', class_='main-products product-grid').find_all('div', class_='product-layout has-extra-button')
    for card in cards:
        name = card.find('div', class_='name').a.text
        title = name.split(' ', 1)[1]
        brand = name.split(' ', 1)[0]
        price = card.find('div', class_='price').span.text
        print(title, price)
        sheet.append([brand, title, price])
except Exception as e:
    print(e)
excel.save('Graphics Card.xlsx')
