import requests
from urllib.request import urlopen
import time #импортируем модуль
f=open(r'ARCHIVE.zip',"wb") #открываем файл для записи, в режиме wb
login_url = "https://cp.beget.com/login?"
login = "$login=p91750xs"
password = "$password=rTTjKoZi"
auth = requests.get(str(login_url)+login+password)
print(auth)
ufr = requests.get("http://mosmimoza.ru/sa.rar") #делаем запрос
print(ufr)
f.write(ufr.content) #записываем содержимое в файл; как видите - content запроса
f.close()



URL="http://mosmimoza.ru/sa.rar"
while True:
    try:
        with urlopen(URL) as f:
            print(f.read())
  
        # Прошло без ошибок, выходим
        break
  
    except Exception as e:
        print(e)
  
        # Ждем 30 секунд перед повтором запроса
        time.sleep(30)