# airG Test

## Test for software engineer

### Install requirements 

````shell
poetry install
````

or 

````shell
python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
````
### Usage

#### Exercise one:

````shell
python3 one/script.py 
````

#### Exercise two:

````shell
python3 two/script.py --num_rows=1000 --filename=data.csv --chunk_size=100
````

> Note: All optional parameters


#### Exercise three:

````shell
python3 three/script.py data.csv --delimiter="|" --quote_char='"'
````

### Run Tests



````shell
coverage run -m unittest discover

coverage report

coverage html (optional)

````

### My last open source project

[django outbox pattern](https://github.com/hugobrilhante/django-outbox-pattern)