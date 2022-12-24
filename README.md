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
``` bash
python manage.py runserver
```

### Modular envionrment support
Each run-time enviornment settings file can be found in the `/number_to_langue/settings` folder. All settings derive from `base.py`

Set the enviornment variable `ENV` to respective settings name to run accordingly.

Example for local (default)
``` bash
ENV=[local] python manage.py runserver
```

Example for production
``` bash
ENV=[production] python manage.py runserver
```

### Testing the API

#### Endpoints
[GET|POST] /num_to_english
[GET|POST] /num_to_spanish

#### Using POST (english)
``` bash
curl --location --request POST 'localhost:8000/num_to_english' \
--header 'Content-Type: application/json' \
--data-raw '{
    "number": 123
}'
```

Response:
``` bash
{"status":"ok","num_in_english":"one hundred and twenty-three"}
```

#### Using GET (spanish)
``` bash
curl --location --request GET 'localhost:8000/num_to_spanish?number=123' \
--header 'Content-Type: application/json'
```

Response:
``` bash
{"status":"ok","num_in_spanish":"uno ciento veinte y tres"}
```
