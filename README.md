# python-number-to-language
A python API for converting integer numbers to English or Spanish text.

### Install using Python virtual environment

```bash
git clone https://github.com/edster9/python-number-to-language.git
cd python-number-to-language
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### Run with local server settings
python manage.py runserver

### Run with custom environment server settings 
ENV=[enviornment] python manage.py runserver --insecure

### Test the API

#### Using POST
``` bash
curl --location --request POST 'localhost:8000/num_to_english' --header 'Content-Type: application/json' \
--data-raw '{
    "number": 123
}'
```

Response:
``` bash
{"status":"ok","num_in_english":"one hundred and twenty-three"}
```

#### Using GET
``` bash
curl --location --request GET 'localhost:8000/num_to_english?number=123' --header 'Content-Type: application/json'
{"status":"ok","num_in_english":"one hundred and twenty-three"}
```

Response:
``` bash
{"status":"ok","num_in_english":"one hundred and twenty-three"}
```
