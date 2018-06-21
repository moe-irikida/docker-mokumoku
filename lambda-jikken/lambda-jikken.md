# AWS lambda + API gateway

## lambda サンプルプログラムを動かしたい

### GUI(Web)から動かした

- 公式の Lambda サンプルのステップを動かしたい
- https://docs.aws.amazon.com/ja_jp/lambda/latest/dg/with-on-demand-custom-android-example.html
- ユーザを、グループに所属させる。グループは、権限がふたつ > AWSLambdaExecute, AWSLambdaBasicExecutionRole
- cli でうまく動かなかったので、Lambda Management Console にコードやテストJsonを書いた。
- python を書いて実行、うまくいった。


## API gateway を使う

```
リクエスト: /HoushinSeiyuWikipedia?param1="太公望"&param2="小野賢章"
ステータス: 502
レイテンシー: 67 ms
レスポンス本文
{
  "message": "Internal server error"
}
```
> Amazon API Gateway を使用して HTTP リクエストに応答してコードを実行します。
- lambda を HTTP から呼び出すのが、API gateway か。そんで、json を返すのか。

### API に json を食わせる @ GUI

- テストとして、json を食わせている
- 本当はテストではなく、ただ呼び出すと API が返るようにしたい
- 静的 API となるが、これ意味あるの？
- パラメタによってレスポンスを変えるようにした(なんとなくしか作れないなー、業務で使う勘所がつかめない)

### cui(cli) で動かしたい

```
$ aws lambda create-function \
...
```

- role などの設定が変わってしまったので、来週続きをする

### サーバレスアプリで db を使いたい

- dynamoDB を調べる
- 何が違う？DynamoDBとRDS > http://blog.serverworks.co.jp/tech/2017/04/12/what_is_different_dynamodb_and_rds/
- いまいち -> amazon RDS 使ってみる
