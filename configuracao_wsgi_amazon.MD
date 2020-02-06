
1- Atualizar pacotes 
` 

` 
 sudo apt-get update && sudo apt-get upgrad
`

2- Criar .venv
caso não esteja instalado o virtual env `sudo apt-get install python3-venv` 
 
```
python3 -m venv .venv
```

3- Ativar a venv

```
source .venv/bin/activate
```

4- Seria criar projeto, como já está criado,  fazer o clone do projeto git

```git
git clone https://github.com/gelhen/gestao_rh.git
```

5- Instalar dependencias

````
pip install -r requirements.txt
````

6- Liberar acesso na porta 8080 

7- Acessar 

````
54.196.4.161:8080
````

6-Instalar WSGI
  wsgi dentro da virtualenv não deu certo, foi instaldo no paython so systema
  [documentação WSGI](https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html)
  Caso tenha erro [instalação WSGI](https://uwsgi-docs.readthedocs.io/en/latest/Install.html)
  

````
sudo apt-get install build-essential python
sudo apt-get install python-dev
sudo apt-get install python3.6-dev
pip install wheel
pip install uwsgi
````

7- Criar um teste test.py

````python
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"] # python3
    #return ["Hello World"] # python2
````
8- Testar 

````
uwsgi --http :8000 --wsgi-file test.py
````
9- Testar o projeto

````
uwsgi --http :8000 --module gestao_rh.wsgi
````

# 10 Configurar Nginx

## 10.1 Instalar

    ````
    sudo apt-get install nginx
    ````
## 10.2 configurar
Criar arquivo uwsgi_params dentr da pasta do projeto
conteudo para o arquivo [uwsgi_params](https://github.com/nginx/nginx/blob/master/conf/uwsgi_params)
```
vim uwsgi_params

uwsgi_param  QUERY_STRING       $query_string;
uwsgi_param  REQUEST_METHOD     $request_method;
uwsgi_param  CONTENT_TYPE       $content_type;
uwsgi_param  CONTENT_LENGTH     $content_length;

uwsgi_param  REQUEST_URI        $request_uri;
uwsgi_param  PATH_INFO          $document_uri;
uwsgi_param  DOCUMENT_ROOT      $document_root;
uwsgi_param  SERVER_PROTOCOL    $server_protocol;
uwsgi_param  REQUEST_SCHEME     $scheme;
uwsgi_param  HTTPS              $https if_not_empty;

uwsgi_param  REMOTE_ADDR        $remote_addr;
uwsgi_param  REMOTE_PORT        $remote_port;
uwsgi_param  SERVER_PORT        $server_port;
uwsgi_param  SERVER_NAME        $server_name;
```

##10.3 Criar aquivo do site
 Nome do arquivo gestao_rh.conf no diretório /etc/nginx/sites-available/
 Substituir os caminhos pelo PATH do projeto

````
# the upstream component nginx needs to connect to
upstream django {
    # server unix:///path/to/your/mysite/mysite.sock; # for a file socket
    server 127.0.0.1:8001; # for a web port socket (we'll use this first)
}

# configuration of the server
server {
    # the port your site will be served on
    listen      8000;
    # the domain name it will serve for
    server_name example.com; # substitute your machine's IP address or FQDN
    charset     utf-8;

    # max upload size
    client_max_body_size 75M;   # adjust to taste

    # Django media
    location /media  {
        alias /path/to/your/mysite/media;  # your Django project's media files - amend as required
    }

    location /static {
        alias /path/to/your/mysite/static; # your Django project's static files - amend as required
    }

    # Finally, send all non-media requests to the Django server.
    location / {
        uwsgi_pass  django;
        include     /path/to/your/mysite/uwsgi_params; # the uwsgi_params file you installed
    }
}
````
 ## 10.4 Criar link simbólico do arquivo do site
 
 ```
 sudo ln -s /etc/nginx/sites-available/gestao_rh.conf /etc/nginx/sites-enabled/gestao_rh.con
 ```

## 10.4 Incluir o STATICROOT no settings do projeto

````
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
````
##### 10.4.1
````
python manage.py collectstatic
````

##10.5 Restart nginx:

```
sudo /etc/init.d/nginx restart
```
## 10.6 Testar com Unix sockets
No arquivo gestao_rh.conf, descomentar a linha server unix.....
e comentar a server 127.0.0.1....

````
server unix:///path/to/your/mysite/mysite.sock; # for a file socket
# server 127.0.0.1:8001; # for a web port socket (we'll use this first)
````
#### 10.6.1 Testar 

````
uwsgi --socket gestao_rh/mysite.sock --wsgi-file test.py

````
case apresente erro acrescentar a 
`--chmod-socket=666 # (very permissive)` ou `--chmod-socket=666 # (very permissive)` 
no fina do comendo

## 11 Roddar aplicação DJango

````
    uwsgi --socket mysite.sock --module gestao_rh.wsgi --chmod-socket=666
````
## 12 Criar arquivo de inicialização

Dentro da pasta do projeto, criar um arquivo com o nome uwsgi.ini

```
[uwsgi]

chdir           = /home/ubuntu/gestao_rh
module          = gestao_rh.wsgi
home            = /home/ubuntu/.venv
master          = true
processes       = 10
socket          = /home/ubuntu/gestao_rh/mysite.sock
vacuum          = true
chmod-socket    = 666
``` 

## 13 Teste para rodar o projeto

```
uwsgi --ini uwsgi.ini
```

## 14 Configurando o systemctl para start no boot

Na pasta raiz /home/ubuntu, criar um arquivo, uwsgi.sh

````
#!/bin/bash
/home/ubuntu/.venv/bin/uwsgi --emperor /etc/uwsgi/vassals --uid www-data --gid www-data
````
Dar permissão de execução para o arquivo

````
sudo chmod 744 uwsgi.sh
````

Criar um arquivo gestao_rh.service dentro do diretório /etc/systemd/system
com o conteúdo abaixo.
````
[Unit]
Description=uWSGI modo Emperor
After=network.target

[Service]
ExecStart=/home/ubuntu/uwsgi.sh
Type=forking
User=ubuntu
[Install]
WantedBy=default.target

````
````
sudo vim /etc/systemd/system/gestao_rh.service
sudo chmod 666 /etc/systemd/system/gestao_rh.service
````
Reload no processo
Vai pedir a senha do ubuntu, para teste cadastrei senha 123456

````
systemctl daemon-reload
systemctl enable gestao_rh.service
````
Por fim iniciar o serviço
````
systemctl start gestao_rh.service
````
