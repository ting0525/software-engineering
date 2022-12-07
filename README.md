# software-engineering

## install virtualenv
```shell
pip install virtualenv
``` 

## create virtual environment
```shell
virtualenv "name"
```
### windows
```shell
"name"\Script\activate
```
### linux
```shell
source "name"/activate
```
## leave virtual environment
```shell
deactivate
```

## export environment
```shell
pip freeze > "name".txt
```

## check export
```shell
type "name".txt
```
## download requirement
```shell
pip install -r "name".txt
```