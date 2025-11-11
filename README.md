# hoge-sh

リモートからシェルスクリプトを実行するデモ

## 概要

GitHubにホストされたシェルスクリプトを、curlで取得して直接実行できます。

## 使い方

ターミナルで以下のコマンドを実行すると、"hoge"と表示されます:

```bash
curl -fsSL https://raw.githubusercontent.com/s4na/hoge-sh/main/hoge.sh | bash
```

または、wgetを使う場合:

```bash
wget -qO- https://raw.githubusercontent.com/s4na/hoge-sh/main/hoge.sh | bash
```

## ファイル構成

- `hoge.sh` - "hoge"と表示するシンプルなシェルスクリプト

## 仕組み

1. `curl -fsSL` で GitHub の raw コンテンツを取得
2. パイプ (`|`) で bash に渡して実行

## オプション説明

- `-f`: 失敗時にエラーを返す
- `-s`: サイレントモード（進捗を表示しない）
- `-S`: エラーは表示する
- `-L`: リダイレクトに従う
