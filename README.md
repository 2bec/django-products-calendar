# django-products-calendar
Retorna lista de preços por data e horário. Feito com Django e FullCalendar.

## Enviroments
First set a virtualenv ``` virtualenv env ``` and active than ``` source env/bin/active ```.

## Requirements
``` pip install -r requirements.txt ```

## Usage
Migrate ``` python manage.py migrate ``` and runserver ``` python manage.py runserver 9090 ```.
Access:
* http://127.0.0.1:9090/products/calendario/2016/11/21/ - to see a price list for this product on the day (yyyy/mm/dd) - use: ?format=json [get] para receber a lista em json
* http://127.0.0.1:9090/products/calendario/2016/month/11/ - to see a price list for this product on the month (yyyy/month/mm) - use: ?format=json [get] para receber a lista em json
* http://127.0.0.1:9090/products/calendario/2016/week/47/ - to see a price list for this product on the week (yyyy/week/W) - use: ?format=json [get] para receber a lista em json
* http://127.0.0.1:9090/products/json/2016-11-11/2016-11-30/ - to see a json price list for this product on the range (date_start/date_enf)