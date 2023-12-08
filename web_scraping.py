import requests
import bs4

result = requests.get('https://books.toscrape.com/')

two_star_titles = []

for page_num in range(1,51):
    
    page_url = "https://books.toscrape.com/catalogue/page-{}.html"
    pages = page_url.format(page_num)
    
    result = requests.get(pages)

    soup = bs4.BeautifulSoup(result.text,"lxml")
    books = soup.select(".product_pod")
    

    for book in books:
  
        if len(book.select('.star-rating.Two')) != 0:
            book_title = book.select('a')[1]['title']
            two_star_titles.append(book_title)
        else:
            pass

print(two_star_titles)


