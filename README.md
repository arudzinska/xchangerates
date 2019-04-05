# Currency exchange rate viewer (RSS feed reader)

Django REST API with an endpoint that lists the currency exchange rates using the European Central Bank RSS feed reader.


## Deployment
Install modules from Pipfile and run its shell (`pipenv` required - alternatively, you can use the old venv 
creation and `requirements.txt`):
```bash
$ pipenv install
$ pipenv shell
```

Prepare the database and run the local server:

```
$ ./dev_server.sh
```
The above script will apply fixtures with a choice of 5 currencies into the database. Further currencies can be added 
manually.

## API endpoint

* **/exchangerate**

    **Method:** GET
    
    **Success Response:**
    
     Code: 200
     
     Content: JSON with the exchange rate for each currency
        
    **Sample Call:**
    
        $ curl http://localhost:8000/exchangerate
        
    Output (example): 
    ```json
    [  
      {  
        "currency":"USD",
        "rate":"1.123",
        "created":"2019-04-05T22:08:29.020752Z"
      },
       ...
    ]
    ```
    
## Description of functionality

The app contains two models: Currency and ExchangeRate. An already prepared fixtures file will
create entries for 5 currencies in the Currency table: USD, GBP, CHF, PLN, and JPY. 

Each time an API call is made the app will check if there are entries in the database (table: ExchangeRate) for the 
current day and for each currency - if not, it will read corresponding RSS feeds to retrieve the newest record and
save it into the ExchangeRate table. At the end, today's rates are fetched and sent in the response.

Although only today's rates are sent in the response, the database will keep the older records if the API calls
were made on previous days.

It is possible to add new valid currencies (that have an RSS feed) into the Currency table and they will be included in 
the subsequent API responses.
 
 
 ## My thoughts, possible next steps for the app
 
 * The GET call could include possiblity of filtering by currency - the queryset in the views would need to be filtered
 then.
 * When app compares datetime.date() objects it assumes the same time zone. The time zone support could be implemented.
 * Some tests should be created
