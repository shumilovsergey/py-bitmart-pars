FOR DOCKER USERS:

1) env.env -> .env
2) docker build -t {{image name}} .
3) docker run {{image name}}

FOR CLI USERS:

1) env.env -> .env
2) pip install virtualenv
3) virtualenv env
4) source env/bin/activate
5) pip install -r requirements.txt
6) python main.py
