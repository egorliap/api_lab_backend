# Currency exchange service

## To run:

1. Clone this repo
2. Create a file `.env`, containing
```
ER_API_KEY = <Your ExchangeRate API KEY>
```
3. Run the following (Windows):
```
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app
``` 
4. Go to http://localhost:8000/docs to see the Swagger docs

## What does this service do?

With this service you can:

+ Get conversion rates of chosen currency
+ Get pair conversion (maybe amount chosen) for 2 chosen currencies
+ Save favorite pair conversion
+ Watch all your favorite pairs 

Code starts a local web service, which has 4 endpoints shown in http://localhost:8000/docs and [here](https://www.postman.com/egorliap/my-workspace/) on Postman

