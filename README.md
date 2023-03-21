# precure-bot

## 概要

好きなプリキュアまたは妖精を選んでお話しできるSlack用Bot

## 環境

- AWS Lambda
  - Python3.8

## 利用手順

1. `docker-compose run installer` で必要なモジュールをインストールする。
2. `docker-compose run terraform sh -c "cd ./terraform && terraform apply"` でデプロイ
3. 発行されるURLを `manifest.yml` の `request_url` に設定し、中身をコピーする。
4. [slack api](https://api.slack.com/apps/)を開く。
5. `Create an App` をクリックする。
6. `From an app manifest` をクリックする。
7. workspaceを選択し、 `Next` をクリックする。

## ローカルで確認

※ngrokが使える状態になっていなければなりません。

1. `docker-compose up -d lambda` で起動する。
   1. 簡単に確認する時 `curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'`
2. `ngrok http 9000` でlocalhostを一時的に公開する。
3. [上記Slack Botの設定](#利用手順)を行う。
   1. `manifest.yml` の `request_url` に `http://{ngrokで出来たホスト名}/2015-03-31/functions/function/invocations` を設定する。