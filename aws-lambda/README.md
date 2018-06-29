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

#### グローバルで動かす

```
% aws s3 mb s3://hello-world-sam
% sam package \
     --template-file template.yaml \
     --output-template-file packaged.yaml \
     --s3-bucket hello-world-sam
```

#### ロールに苦戦 (!無駄)
* ※sam コマンドにしないと、aws コマンドは、古い `aws-cli` を使った動作になるため、この項目は無駄(だけど、ためになった)

- それで出てきたコマンド
```
% aws cloudformation deploy --template-file ~/Workspace/gh-dwango/docker-mokumoku/aws-lambda/sam-app/packaged.yaml --stack-name HelloWorldFunction
```

- AWSCloudFormationFullAccess がない？readonly というポリシーしかない。
- インラインポリシーにて、このプログラムのみ適用される、"cloudformation:* " というオリジナルポリシーを作成。
- 例:  https://docs.aws.amazon.com/ja_jp/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-cloudformation
- をもとにして、自分のID、stack、programID的なものをARNに入力
- (一度、例をコピペして、後で「ポリシーの編集」をして、自分のIDを入力するとやりやすい)
- もう一回、ポリシーを入れろと出るので、記述されてるポリシーを、インラインポリシーに入力。
- それで出たエラーにもとづいて、コマンドの最後に
```
--capabilities CAPABILITY_IAM
```
- を追記。つまり
```
% aws cloudformation deploy --template-file ~/Workspace/gh-dwango/docker-mokumoku/aws-lambda/sam-app/packaged.yaml --stack-name HelloWorldFunction --capabilities CAPABILITY_IAM
...
Failed to create/update the stack. Run the following command
to fetch the list of events leading up to the failure
aws cloudformation describe-stack-events --stack-name HelloWorldFunction
```
- 次に打つコマンドが載ってるけど、ここで README にもとづき、 sam コマンドでやる

#### 改めて、sam で続き
```
% sam deploy \
>     --template-file packaged.yaml \
>     --stack-name sam-app \
>     --capabilities CAPABILITY_IAM
```
- 2回、ポリシーの追加を要求されるので記載する
- 次に打つコマンドが出てくるので、打つ
```
$ aws cloudformation describe-stack-events --stack-name sam-app
```

### API に GET パラメタ渡したい

### サーバレスアプリで db を使いたい

- dynamoDB を調べる
- 何が違う？DynamoDBとRDS > http://blog.serverworks.co.jp/tech/2017/04/12/what_is_different_dynamodb_and_rds/
- いまいち -> amazon RDS 使ってみる
