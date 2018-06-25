# AWS lambda + API gateway

## lambda サンプルプログラムを動かしたい

> 基本的なサーバーレスアプリケーションのほとんどは単一の関数です。

### GUI(Web)から動かした

- 公式の Lambda サンプルのステップを動かしたい
- https://docs.aws.amazon.com/ja_jp/lambda/latest/dg/with-on-demand-custom-android-example.html
- ユーザを、グループに所属させる。グループは、権限がふたつ > AWSLambdaExecute, AWSLambdaBasicExecutionRole
- cli でうまく動かなかったので、Lambda Management Console(Webアプリケーション) にコードやテストJsonを書いて実行、うまくいった。


## API gateway を使う

> Amazon API Gateway を使用して HTTP リクエストに応答してコードを実行します。
- lambda を HTTP から呼び出すのが、API gateway か。そんで、json を返すのか。

```
リクエスト: /HoushinSeiyuWikipedia?param1="太公望"&param2="小野賢章"
ステータス: 502
レイテンシー: 67 ms
レスポンス本文
{
  "message": "Internal server error"
}
```
### API に json を食わせる @ GUI

- パラメタによってレスポンスを変えるようにしたい

### cui(cli) で動かしたい

```
$ aws lambda create-function \
--region us-east-1 \
--function-name HoushinSeiyuWikipedia  \
--zip-file fileb:///Users/moe_irikida/Workspace/gh-dwango/docker-mokumoku/test.zip \
--role arn:aws:iam::688289487826:role/lambda-android-execution-role  \
--handler lambda_function.lambda_handler \
--runtime python3.6
```
```
aws lambda \
    update-function-code \
    --function-name HoushinSeiyuWikipedia \
    --zip-file fileb:///Users/moe_irikida/Workspace/gh-dwango/docker-mokumoku/test.zip \
    --publish
```
```
aws lambda invoke \
--function-name HoushinSeiyuWikipedia \
--payload '{"title": "houshin"}' \
outputfile.txt
```
-> outputfile.txt には、error が出た旨が出る

### サーバレスアプリで db を使いたい

- dynamoDB を調べる
- 何が違う？DynamoDBとRDS > http://blog.serverworks.co.jp/tech/2017/04/12/what_is_different_dynamodb_and_rds/
- いまいち -> amazon RDS 使ってみる
