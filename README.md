# Eventex

Sistema de eventos

[![Build Status](https://travis-ci.org/edersonramalho/wttd_eventex.svg?branch=master)](https://travis-ci.org/edersonramalho/wttd_eventex)

[![Code Health](https://landscape.io/github/edersonramalho/wttd_eventex/master/landscape.svg?style=flat)](https://landscape.io/github/edersonramalho/wttd_eventex/master)

## Como desenvolver?

1. Clonar o repositório.
2. Criar um virtualenv com python 3.5.
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure as instâncias com o .env
6. Execute os tests 

```console
git clone git@github.com:edersonsantos/wttd.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```


## Como fazer o deploy?

1. Criar instância no heroku
2. Envie as configurações para o heroku
3. Defina uma SECRET_KEY
4. Defina DEBUG=False
5. Configure o serviço de e-mail
6. Envie o código para heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
#Configurar e-mail
git push heroku master --force
``` 