# AWS lambda + API gateway

## lambda サンプルプログラムを動かしたい

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

- lambda に param を渡すのが、API gateway か。そんで、json を返すのか。で、合ってるかな？
