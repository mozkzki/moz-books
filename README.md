# moz-books

[![CircleCI](https://circleci.com/gh/mozkzki/moz-books/tree/master.svg?style=svg)](https://circleci.com/gh/mozkzki/moz-books/tree/master)
[![codecov](https://codecov.io/gh/mozkzki/moz-books/branch/master/graph/badge.svg?token=BRB5vsPkO2)](https://codecov.io/gh/mozkzki/moz-books)
[![Maintainability](https://api.codeclimate.com/v1/badges/df50bbce59225073a577/maintainability)](https://codeclimate.com/github/mozkzki/moz-books/maintainability)

書籍関連APIの呼び出しを行う自前ライブラリ。

## Function

- `service.search_books()`

```python
    params = SearchParams(isbn="9784052046209")
    books = service.search_books(params)
```

- 対応サービス
  - Google Books API
  - Rakuten Books API
  - OpenDB
  - Calil

## Usage

Environmental variables

`.env`ファイルに書いてproject rootに配置。`.env_sample`をコピーすると楽。

```txt
calil_app_key=12345...
rakuten_app_id=12345...
```

Install

```sh
pip install git+https://github.com/mozkzki/moz-books
# upgrade
pip install --upgrade git+https://github.com/mozkzki/moz-books
# uninstall
pip uninstall moz-books
```

Coding

**ISBNで検索**

```python
import os
from moz_books import Calil, Google, OpenDB, Rakuten, SearchParams

params = SearchParams(isbn="9784052046209")
services  = [Rakuten(), Google(), OpenDB(), Calil()]
for service in services:
    books = service.search_books(params)
    for book in books:
        print(book)
```

**タイトル・著者で検索**

※ OpenDBとCalilはISBN検索のみ対応なので注意

```python
import os
from moz_books import Calil, Google, OpenDB, Rakuten, SearchParams

params = SearchParams(title="5秒後に意外な", author="桃戸ハル")
services  = [Rakuten(), Google()]
for service in services:
    books = service.search_books(params)
    for book in books:
        print(book)
```

## Develop

base project: [mozkzki/moz-sample](https://github.com/mozkzki/moz-sample)

### Prepare

```sh
poetry install
poetry shell
```

### Run (Example)

```sh
python ./examples/all.py
# or
make start

# 各サービスを個別実行
make google
make rakuten
make opendb
make calil
```

### Unit Test

test all.

```sh
pytest
pytest -v # verbose
pytest -s # show standard output (same --capture=no)
pytest -ra # show summary (exclude passed test)
pytest -rA # show summary (include passed test)
```

with filter.

```sh
pytest -k app
pytest -k test_app.py
pytest -k my
```

specified marker.

```sh
pytest -m 'slow'
pytest -m 'not slow'
```

make coverage report.

```sh
pytest -v --capture=no --cov-config .coveragerc --cov=src --cov-report=xml --cov-report=term-missing .
# or
make ut
```

### Lint

```sh
flake8 --max-line-length=100 --ignore=E203,W503 ./src ./tests
# or
make lint
```

### Create API Document (Sphinx)

```sh
make doc
```

### Update dependency modules

dependabot (GitHub公式) がプルリクを挙げてくるので確認してマージする。

- 最低でもCircleCIが通っているかは確認
- CircleCIでは、最新の依存モジュールでtestするため`poetry update`してからtestしている
- dependabotは`pyproject.toml`と`poetry.lock`を更新してくれる
