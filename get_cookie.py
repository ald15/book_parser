# Получение cookie с bookmate.com

from selenium import webdriver


def get_cookie():
   driver = webdriver.Chrome('chromedriver.exe')
   cookie_file = open('auth.txt', mode='w', encoding='utf8')
   print('Получение доступа (cookie) к аккаунту')
   link = input('Введите ссылку на страницу книги ')
   driver.get(link)
   print('-------------------------!!!!!!!!!!!-------------------------')
   print('\t 1. Долистайте книгу до просьбы войти в аккаунт, ввойдите в него.')
   print('\t 2. Выберите страницу для старта копирования и останьтесь на ней (управляйте стрелками на экране)')
   print('-------------------------!!!!!!!!!!!-------------------------')
   login = input('Для продолжения нажмите кнопку Enter...')
   cookie = driver.get_cookies()[0]
   print(cookie)
   cookie_file.write(str(cookie))
   print('\nДанные для входа были успешно получены!')
   cookie_file.close()
   e = input()


get_cookie()
   

   
