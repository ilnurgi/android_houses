# arduino

репозитории проекта умного дома на базе ардуино

# как это все развернуть на ubuntu

* обновить пакетный менеджер ubuntu

  ```
  $ sudo apt-get update
  $ sudo apt-get upgrade
  ```
  
* установить Arduino IDE (A_IDE)

  ```
  $ sudo apt-get install arduino arduino-core git
  ```
  
  после чего у нас появится ссылка на A_IDE в меню Убунту
  
* определяем наш подключенный девайс

  ```
  $ ls -l /dev/ | grep ACM
  ```
  
  не вернет нам ничего
  подключаем девайс к компьютеру

  ```
  $ ls -l /dev/ | grep ACM
  crw-rw----  1 root dialout   166,   0 янв.  18 13:52 ttyACM0
  ```
  
  видим что девайс подключен как ttyACM0 устройство (/dev/ttyACM0)
  
* даем доступ к устройству всем пользователям

  ```
  $ sudo chmod a+rw /dev/ttyACM0
  ```
  
* запускаем A_IDE, в панели меню СЕРВИС->Последовательный порт->/dev/ttyACM0, если это есть, то все норм. 
  Если такого нет, значит наше устройство не может определить A_IDE

* клонируем этот репозитории

  ```
  $ git clone https://github.com/ilnurgi/arduino_houses.git
  ```

  
# Полезные ссылки

http://arduino.ru/
  
  
