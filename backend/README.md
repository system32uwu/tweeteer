# Setting things Up

## Create a virtual environment

Create a virtual environment by your preferred means.

Using [venv](https://docs.python.org/3/tutorial/venv.html):

```sh
python -m venv venv
```

Activate the virtual environment:

### On Windows

```sh
./venv/Scripts/activate
```

### On Linux

```sh
source venv/bin/activate
```

Then install the dependencies:

```sh
pip install -r requirements.txt
```

## Creating the database

On first run, or when making changes to database schema, run:

```sh
python tools/db.py
```
