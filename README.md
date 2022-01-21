# create-your-own-resolution

![https://img.shields.io/github/license/relarizky/create-your-own-resolution](https://img.shields.io/github/license/relarizky/create-your-own-resolution)

it started off with me realizing that i got so many resolution this year. <br>
so i feel like i need something that make me keep in touch with the progress that i make for achieving my resolution <br>
then i made this. Maybe you got the same need as mine, you can use this or make it better.

## Installation
```
$ git clone https://github.com/relarizky/create-your-own-resolution.git
$ cd create-your-own-resolution/
$ pip install -r requirements.txt
$ flask db init; flask db migrate; flask db upgrade
$ python run.py
```

make sure you use python 3.x.x <br>
mine runs on python 3.8.10 <br>

just to make sure that everything is ok, you can run the following command
```
$ pytest -v tests/unit tests/integration
```

## Preview

<img src="https://github.com/relarizky/create-your-own-resolution/blob/master/screenshot/resolution-home-1.png?raw=true" height=50% width=48%> <img src="https://github.com/relarizky/create-your-own-resolution/blob/master/screenshot/resolution-statistic-1.png?raw=true"
height=50% width=48%>

## Demo

https://create-resolution.herokuapp.com/home <br>
https://create-resolution.herokuapp.com/api/doc/
