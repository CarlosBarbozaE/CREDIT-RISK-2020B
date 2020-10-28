# Borrowers

This is a simple application that allows you to register candidate borrowers into a json file.

## Instructions

1. [Sync your repository](https://www.youtube.com/watch?v=59PaqRdbCx8&list=PLIbTa97DHk7jHdOW7Jb2dozV59bOWc58O&index=7)!
2. Create a branch called: `HW-BORROWERS`
3. Complete the `show` method on the `Main` class located on `main.py`.
4. Complete the `Borrower` class located on `models.py`.
    * `to_json`: 
    * `save`: save the borrower into the candidates list on the json file.
    * `update`: update the borrower on the json file that matches the email.
    * NOTE: the `file` argument represents the "filename" (e.g., `borrowers/candidates.json`)
5. Add your implementation, run the examples on the `execution` section, and push to github.
    * Files: `main.py`, `models.py`, and `candidates.json`
6. Create a PR from `HW-BORROWERS` into `solutions`.

Consider that there are two relevant `updated_at` fields:
* Top level `updated_at`: this represents when the file has been updated, and should be modified anytime there's an
insert or update.
* Borrower `updated_at`: this represents updates on the borrower and should be modified ONLY when
calling the `update` command.

Hints:
* You can open a python file as "read" with:

```python
with open("path/to/file.json", "r") as f:
    content = f.read()
```

* You can open a python file as "write" with:

```python
content = "some content"
with open("path/to/file.json", "w") as f:
    f.write(content)
```

* You can create a dictionary from a string with:

```python
import json

string = '{"hello": "world"}'
dictionary = json.loads(string)
```

* You can create a string from a dictionary with:

```python
import json

dictionary = {"hello": "world"}

# Create a string
string_1 = json.dumps(dictionary)
print(string_1)

# Create a string but with indentation
string_2 = json.dumps(dictionary, indent=4)
print(string_2)
```

## Execution!

### (1 pts) Show Command

```commandline
$ python -m borrowers show
{
    "updated_at": "2020-01-01 00:00:00",
    "candidates": [

    ]
}

```

* The output should contain an empty list.
* The output should be formatted.

### (2 pts) Insert Command

Insert Alice with the following characteristics: 
* email: `alice@example.com`
* age: `23`
* income: `25000`

```commandline
$ python -m borrowers insert --email alice@example.com --age 23 --income 25000
```

```commandline
$ $ python -m borrowers show
{
    "updated_at": "2020-10-07 00:01:07",
    "candidates": [
        {
            "email": "alice@example.com",
            "age": 23,
            "income": 25000,
            "created_at": "2020-10-07 00:01:07",
            "updated_at": "2020-10-07 00:01:07"
        }
    ]
}
```

* The `updated_at` should be updated.
* The candidates list should contain `Alice` info.

Insert Bob with the following characteristics:
* email: `bob@example.com`
* age: `27`
* income: `15000`


```commandline
$ python -m borrowers insert --email bob@example.com --age 27 --income 15000
```

```commandline
$ python -m borrowers show
{
    "updated_at": "2020-10-07 00:02:23",
    "candidates": [
        {
            "email": "alice@example.com",
            "age": 23,
            "income": 25000,
            "created_at": "2020-10-07 00:01:07",
            "updated_at": "2020-10-07 00:01:07"
        },
        {
            "email": "bob@example.com",
            "age": 27,
            "income": 15000,
            "created_at": "2020-10-07 00:02:23",
            "updated_at": "2020-10-07 00:02:23"
        }
    ]
}

```
* The `updated_at` should be updated.
* The candidates list should contain `Alice` & `Bob` info.

Insert Carol with the following characteristics:
* email: `carol@example.com`
* age: `32`
* income: `35000`

```commandline
$ python -m borrowers insert --email carol@example.com --age 32 --income 35000
```

```commandline
$ python -m borrowers show
{
    "updated_at": "2020-10-07 00:03:28",
    "candidates": [
        {
            "email": "alice@example.com",
            "age": 23,
            "income": 25000,
            "created_at": "2020-10-07 00:01:07",
            "updated_at": "2020-10-07 00:01:07"
        },
        {
            "email": "bob@example.com",
            "age": 27,
            "income": 15000,
            "created_at": "2020-10-07 00:02:23",
            "updated_at": "2020-10-07 00:02:23"
        },
        {
            "email": "carol@example.com",
            "age": 32,
            "income": 35000,
            "created_at": "2020-10-07 00:03:28",
            "updated_at": "2020-10-07 00:03:28"
        }
    ]
}
```
* The `updated_at` should be updated.
* The candidates list should contain `Alice`, `Bob`, and `Carol` info.

### (2 pts) Update Command

Update Bob's income to `18000`

```commandline
$ python -m borrowers update --email bob@example.com --age 27 --income 18000
```

```commandline
$ python -m borrowers show
{
    "updated_at": "2020-10-07 00:04:27",
    "candidates": [
        {
            "email": "alice@example.com",
            "age": 23,
            "income": 25000,
            "created_at": "2020-10-07 00:01:07",
            "updated_at": "2020-10-07 00:01:07"
        },
        {
            "email": "bob@example.com",
            "age": 27,
            "income": 18000,
            "created_at": "2020-10-07 00:02:23",
            "updated_at": "2020-10-07 00:04:27"
        },
        {
            "email": "carol@example.com",
            "age": 32,
            "income": 35000,
            "created_at": "2020-10-07 00:03:28",
            "updated_at": "2020-10-07 00:03:28"
        }
    ]
}
```
* The `updated_at` should be updated.
* The candidates list should contain `Alice`, `Bob`, and `Carol` info.
* `Bob`'s income should be updated.
* `Bob`'s updated_at should be updated.
* `Bob`'s created_at should remain the same.
