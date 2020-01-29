# mmbooks

## 必要な環境変数

```(sh)
calil_app_key=<please specify calil application key>
rakuten_app_id=<please specify rakuten application id>
```

## インストール

```(sh)
pip install git+https://github.com/yukkun007/mmbooks
```

## アップグレード

```(sh)
pip install --upgrade git+https://github.com/yukkun007/mmbooks
```

## 使い方 (モジュールを利用)

```(sh)
python
>>> import mmbooks
>>> books = mmbooks.search(title="test")
>>> print(books)
```

## 使い方 (コマンドラインアプリを実行)

```(sh)
mmbooks
```

## アンインストール

```(sh)
pip uninstall mmbooks
```

## 開発フロー

### 環境構築

1. 環境変数追加 (project ディレクトリに仮想環境作成)

   - Linux

     ```(sh)
     export PIPENV_VENV_IN_PROJECT=true
     ```

   - Windows

     ```(sh)
     set PIPENV_VENV_IN_PROJECT=true
     ```

1. `pip install pipenv`
1. `git clone git@github.com:yukkun007/mmbooks.git`
1. `pipenv install --dev`

### install package

```(sh)
pip install .
```

### upgrade package

```(sh)
pip install --upgrade . (もしくは-U)
```

### install package (編集可能モード)

ソース編集の都度 upgrade が不要になる。

```(sh)
pip install -e .
```

### モジュールを利用

```(sh)
python
>>> import mmbooks
>>> books = mmbooks.search(title="test")
>>> print(books)
```

### コマンドラインアプリを実行

```(sh)
pipenv run start (もしくはmmbooks)
```

### unit test

```(sh)
pipenv run ut
```

### lint

```(sh)
pipenv run lint
```

### create api document (sphinx)

```(sh)
pipenv run doc
```

### ソースコード配布物の作成

dist/ 以下に mmbooks-0.0.1.tar.gz が生成される。

```(sh)
python setup.py sdist
```

### ソースコード配布物から pip でインストール

```(sh)
pip install mmbooks-0.0.1-tar.gz
```

### ビルド済み配布物(wheel 形式)の作成

dist/ 以下に mmbooks-0.0.1-py3-none-any.whl が生成される。

```(sh)
python setup.py bdist_wheel (wheelパッケージが必要)
```

### ビルド済み配布物(wheel 形式)から pip でインストール

```(sh)
pip install mmbooks-0.0.1-py3-none-any.whl
```

## 参考

### パッケージング/開発環境

- <https://techblog.asahi-net.co.jp/entry/2018/06/15/162951>
- <https://techblog.asahi-net.co.jp/entry/2018/11/19/103455>

### コマンドライン引数のパース

- <https://qiita.com/kzkadc/items/e4fc7bc9c003de1eb6d0>

### 環境変数の定義

- <https://pod.hatenablog.com/entry/2019/04/29/164109>
