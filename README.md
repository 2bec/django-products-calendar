# django-products-calendar
Retorna lista de preços por data e horário. Feito com Django e FullCalendar.

## Enviroments
First set a virtualenv ``` virtualenv env ``` and active than ``` source env/bin/active ```.

## Requirements
``` pip install -r requirements.txt ```

## Usage
Shell ``` python mange.py shell ```.

Get an product and get all prices for him and filter using date range
```
>>> from products.models import Product
>>> p = Product.objects.get(pk=1)
>>> prices = p.price_set.all()
>>> prices.filter(date_start__range=(date_start, date_end))
```

Get all prices with date_start and date_end. Can be one day or a real range.
```
>>> from products.models import Price
>>> import datetime
>>> date_start = datetime.datime.now()
>>> date_end = date_start + datetime.timedelta(7)
>>> prices = Price.objects.filter(date_start__range=(date_start, date_end))
```

Server, migrate ``` python manage.py migrate ``` and runserver ``` python manage.py runserver 9090 ```. Access:
* http://127.0.0.1:9090/products/calendario/2016/11/21/ - to see a price list for this product on the day (yyyy/mm/dd) - use: ?format=json [get] para receber a lista em json
* http://127.0.0.1:9090/products/calendario/2016/month/11/ - to see a price list for this product on the month (yyyy/month/mm) - use: ?format=json [get] para receber a lista em json
* http://127.0.0.1:9090/products/calendario/2016/week/47/ - to see a price list for this product on the week (yyyy/week/W) - use: ?format=json [get] para receber a lista em json
* http://127.0.0.1:9090/products/json/2016-11-11/2016-11-30/ - to see a json price list for this product on the range (date_start/date_enf)