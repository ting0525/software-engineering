# software-engineering

## install virtualenv
```shell
pip install virtualenv
``` 

## create virtual environment
```shell
virtualenv env
```
### windows
```shell
env\Scripts\activate
```
### linux
```shell
source env/activate
```
## leave virtual environment
```shell
deactivate
```

## export environment
```shell
pip freeze > module.txt
```

## check export
```shell
type module.txt
```
## download requirement
```shell
pip install -r module.txt
```

## start game
```shell
cd Codes
python Main.py
```

## turn on web
```shell
cd Codes
python exserver.py
```

## MySQL
```shell
CREATE TABLE game2(
		`id` varchar(20) primary key,      
		`score` INT
);
```
![網頁介面](/path/to/img.jpg)
