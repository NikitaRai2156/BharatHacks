# bharathacks

Created using Django.



### Setup

Make sure that you have mysql (5.6) installed on your system.

```
virtualenv --no-site-packages pyenv
source pyenv/bin/activate
pip install -r requirements/base.txt

# assuming pip install runs successfully

python src/manage.py migrate

# create super

python src/manage.py createsuperuser

# assuming you have bower install
bower install

```

### Run server

```
python src/manage.py runserver
```

Head over to [localhost:8000](http://localhost:8000)
