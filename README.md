# DWH Challenge

## Items inside the `solution` directory
1. `solution.py`: A Python file where main program executed (the solution)

## Pre-requisites
### Python 3.9
As stated on Pipfile, I'm using Python 3.9.

### Pipenv
I'm using pipenv to list all packages required by this program. If you haven't had any of this installation, please install it by using `pip`
```
pip install pipenv
```

### Installing dependencies
Before you run the main script (`solution.py`), please install the following dependencies by using Pipenv
```
pipenv install
```

## Docker
If you want to use docker instead, please use 
```
docker-compose up
```
> Hint: do not forget to adjust your `DATA_PATH` in `docker-compose.yaml`

### Args
This program has three arguments 
```
python solution/solution.py <args>
<args>:
    --tabulate: to show all table in tabulation form
    --join: to join all related tables
```

### Environment
Do not forget to set your environment variable of `DATA_PATH` to your `data` path by using:
```
    export DATA_PATH=<your data dir>
```
or by simply exporting from `config.env` by using:
```
    source config.env
```

## Discussion
There are 4 transactions of id `c1globalid` -> from he activated his account until he requested to deactivated it:
`transaction 1` 
```
{
  "id": "c1globalid",
  "op": "u",
  "ts": 1578313800000,
  "set": {
    "credit_used": 12000
  }
}
```

`transaction 2` 
```
{
  "id": "c1globalid",
  "op": "u",
  "ts": 1578420000000,
  "set": {
    "credit_used": 19000
  }
}
```

`transaction 3` 
```
{
  "id": "c1globalid",
  "op": "u",
  "ts": 1578420000000,
  "set": {
    "credit_used": 19000
  }
}
```

`transaction 4` 
```
{
  "id": "c1globalid",
  "op": "u",
  "ts": 1578654000000,
  "set": {
    "credit_used": 0
  }
}
```

And there is one transaction of `c2globalid` indicated by this record:
```
{
  "id": "c2globalid",
  "op": "u",
  "ts": 1579361400000,
  "set": {
    "credit_used": 37000
  }
}
```