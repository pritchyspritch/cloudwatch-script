# cloudwatch-script

## Set up

```
pipenv --python 3.7
pipenv install
pipenv shell
```

OR 
```
python3 -m venv cloudwatch-venv
source cloudwatch-venv/bin/activate
pip install boto3
```

## Execution

You will need to assume the role of the account you would like to send logs to.

E.g. `aws-vault exec <account_name> -- python send_cloudwatch.py`
