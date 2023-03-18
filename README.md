# precure-bot

## 概要

好きなプリキュアまたは妖精を選んでお話しできるSlack用Bot

## 環境

- AWS Lambda
  - Python3.8

## 利用手順

1. `docker-compose run terraform sh -c "cd ./terraform && terraform apply"` でデプロイ
2. 発行されるURLを `manifest.yml` の `request_url` に設定し、中身をコピーする。
3. [slack api](https://api.slack.com/apps/)を開く。
4. `Create an App` をクリックする。
5. `From an app manifest` をクリックする。
6. workspaceを選択し、 `Next` をクリックする。

## ローカルで実行

1. `docker-compose run -p 9000:8080 lambda` で起動する。
2. コンソールから `curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'` で確認する。
3. 上記Slack Botの設定を行う。
   1. `manifest.yml` の `request_url` には `http://localhost:9000/2015-03-31/functions/function/invocations` を設定する。
