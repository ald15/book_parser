import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

book_page = 'https://' # Ссылка на сайт
reader_page = book_page[0:8] + 'reader.' + book_page[8:20] + book_page[26:]

driver = webdriver.Chrome('chromedriver.exe')
driver.get(book_page)

# Получаем cookie
cookie = open('auth.txt', encoding='utf8')
c = cookie.readlines()[0].replace(',', '').split()
print(c)
driver.add_cookie({}) # вставить cookie

cookie.close()


driver.get(book_page)

pages_value = driver.find_elements_by_class_name('paper-pages__text')
pages_value = str(pages_value[0].get_attribute('innerHTML')).split()
print(pages_value)
pages_value = int(pages_value[0])
print(pages_value)

driver.get(reader_page)
time.sleep(10) # Сон 3 секунды

book = open('book.html', mode='w', encoding='utf8')
book.write('<div style="padding: 5em 20vw;display:flex;flex-direction: column;justify-content: center;align-items: center;">' + '\n')
book.close()
r1 = []
text = ''
for i in range(0, 20):
   print(i, end=' ')
   
   
   #results = driver.find_elements_by_class_name('paginated-content')[0].find_elements_by_tag_name('section')
   #r = str(results[0].get_attribute('innerHTML')).replace('src="/', 'src="./')
   results = driver.find_elements_by_class_name('paginated-content')[0]
   r = str(results.get_attribute('innerHTML')).replace('src="/', 'src="./')

   if text.count(r) == 0:
      text += r + '\n'
   # for img in results[0].find_elements_by_tag_name('img'):
   for img in results.find_elements_by_tag_name('img'):
      if r1.count(img.get_attribute('src')) == 0:
         r1.append(img.get_attribute('src'))

   btn = driver.find_element_by_class_name("pagination_forward")
   btn.click()
   time.sleep(1) # Сон 3 секунды
book = open('book.html', mode='w', encoding='utf8')           
book.write(text + '\n')
book.close()
book = open('book.html', mode='a+', encoding='utf8')
book.write('</div>' + '\n')
book.close()

images = open('images.txt', mode='w', encoding='utf8')
images.write(str(r1).replace('[', ''))
images.close()

