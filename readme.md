# Currency exchange service

To run:

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
