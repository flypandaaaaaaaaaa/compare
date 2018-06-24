An app for comparing 2 files or 2 texts directly and showing the differences in a html page.

Commponents:
Flask,flask_bootstrap,flask_wtf,wtforms,werkzeug

you can install these components via pip
or 
execute the setup.py to do an easy installation.

Configuration:

The default port in this app is 10012(Flask default port is 5000),you can modify to anyone you want.

The default listen on IP is 0.0.0.0 which means it works for all the interfaces on the host.You can modify to a certain IP if you want.

Here
--- compare.py

app.run(host='0.0.0.0',port=10112)

Important:

In order to avoid the CSRF attack,you need to modify the configuration:

app.config['SECRET_KEY']='DADSSADSA'

to a complex string that make nobody can guess.

WebPage:

compare 2 files: 127.0.0.1:10012/cmpfile  .
compare 2 texts: 127.0.0.1:10012/cmptext  .



