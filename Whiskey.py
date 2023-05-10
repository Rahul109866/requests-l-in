import requests
import lxml.html
from bs4 import BeautifulSoup


def get_page_links(url):
    base_url = 'https://snackstar.in'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    links = soup.select("h3 a")
    hrefs = []
    for link in links:
        hrefs.extend([base_url + link['href']])
    return hrefs


def product_data(url):
    response1 = requests.get(url)
    soup = BeautifulSoup(response1.text, 'lxml')
    product = {
        'name': soup.select_one('h1.product_title.entry-title').text.strip(),
        'price': soup.select_one('p.price_range ins').text.strip() if soup.select_one('p.price_range ins') else 'N/A',
        'stock': soup.select_one('span.js_in_stock ').text.strip()
    }
    print(product)


def main():
    urls = get_page_links('https://snackstar.in/collections/candies')

    results = [product_data(url) for url in urls]

    with open("candies.csv", 'w') as f:
        f.write(','.join(results[0].keys()))
        f.write('\n')
        for row in results:
            f.write(','.join(str(x) for x in row.values()))
            f.write('\n')
    return results


main()
