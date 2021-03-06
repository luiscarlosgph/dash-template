# Description
This repository contains a template for a basic Python 
web application based on Dash. 
If you want to change the name of the package ```wat``` 
needs to be changed in the setup.py. In addition, the
name of the folder inside ```src``` and also the package 
imports need to be changed.

# Installation
```
$ python setup.py install --user
```
Edit ```setup.py``` if you want to change the name of the package.
The folder inside ```src``` must be also renamed.

# Execution
```
$ python -m whatever.run --port 1234 --input-dir /tmp 
```
The --input-dir parameter is just an example,
this parameter can be removed and others may be added.

# Deployment
```http://localhost:1234```

# Demo
![alt text](https://github.com/luiscarlosgph/dash-template/blob/main/demo/demo.jpg?raw=true)

# License
See LICENSE file.
