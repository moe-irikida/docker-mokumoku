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
--region ap-northeast-1 \
--function-name HoushinSeiyuWikipedia  \
--zip-file fileb:///Users/moe_irikida/Workspace/gh-dwango/docker-mokumoku/lambda-jikken/test.zip \
--role arn:aws:iam::688289487826:role/lambda-android-execution-role  \
--handler lambda_function.lambda_handler \
--runtime python3.6
```
```
$ aws lambda \
    update-function-code \
    --function-name HoushinSeiyuWikipedia \
    --zip-file fileb:///Users/moe_irikida/Workspace/gh-dwango/docker-mokumoku/lambda-jikken/test.zip \
    --publish
```
```
$ aws lambda invoke \
--function-name HoushinSeiyuWikipedia \
--payload '{"title": "houshin"}' \
outputfile.txt
```
- うまくいかない...zipファイル内にディレクトリができていた。その下にコードがある状態。本当は、ディレクトリではなく直にプログラムを置かなければいけなかった。
```
cd ~/Workspace/gh-dwango/docker-mokumoku/lambda-jikken/codes/
zip ./../test.zip ./*
```
- invoke できた〜動いた

#### sam cli version(aws-sam-cli)

```
docker run --rm -v "$PWD":/var/task lambci/lambda:python3.6 lambda_function.lambda_handler '{"title": "houshin"}'
```
- 一応動いた。
- でも、ちょっとaws-sam-cli の version が古いっぽい
- ので、pip で upgrade つまづいたのよ、
- pip3 で入れないと、こけるんですよ
- mac って標準でpython2系が指定されている
- pip は 2系が紐づけられている、変えられない。

```
pip3 install --user aws-sam-cli
pip3 install --upgrade pip
```

### AWS lambda w/ API gateway

```
$ sam init
```
- [sam-app] dir が作られた。中には、js が...
```
sam init --runtime python3.6
```
- おお、python project が作られたー
```
sam local invoke "HelloWorldFunction" --event "event.json"
```
> Event body: `--event {PATH}` or stdin
> Lambda function result: stdout


#### Setup process がこける
- http://yuzu441.hateblo.jp/entry/2015/10/15/212314
```
$ touch ~/.pydistutils.cf
$ echo "[install]\nprefix=" >> ~/.pydistutils.cfg
```
こうすると
```
pip3 install -r requirements.txt -t hello_world/build/
```
が通る

#### local で API のテスト
```
$ sam local start-api
```
- http://127.0.0.1:3000/hello
- すごい！出た！感動

* GET パラメタ渡したい
- 明日ね

### サーバレスアプリで db を使いたい

- dynamoDB を調べる
- 何が違う？DynamoDBとRDS > http://blog.serverworks.co.jp/tech/2017/04/12/what_is_different_dynamodb_and_rds/
- いまいち -> amazon RDS 使ってみる
