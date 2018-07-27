# リハビリ出社 de mokumoku

## what is here

* いりきだが、リハビリ出社の間、よくわかっていない docker を業務で使えるくらいわかるようになる。
* [黙々]と docker に関して調べ、docker をさわる。
* つっこみあったらコメントいただけるとうれしい
* gist にあげないのは、ただのメモだから

## 進捗

### phase1: wordpress を動かす

* プライベートの積みタスク。

#### 2018/6/11-12
<!-- - 読んだ: https://thinkit.co.jp/story/2015/07/29/5382 -->
 - git の復習
 - キーバインドがおかしくなっていたのを修正。karabinder という怪しいアプリを入れていたのだった。
#### 2018/06/13
 - github 開通確認、動作確認
<!-- - 読んだ:  https://www.osscons.jp/cloud/%E3%83%80%E3%82%A6%E3%83%B3%E3%83%AD%E3%83%BC%E3%83%89/?action=common_download_main&upload_id=698
 - 読んだ: https://www.slideshare.net/zembutsu/docker-container-image-command-introduction-2017-03 -->
 - intellij, Sublime Text, Workbench を DL
<!-- - 読んだが古かった: https://tech.recruit-mp.co.jp/infrastructure/post-11266/ -->

#### 2018/06/14
<!-- - 読んだ: https://ginpen.com/2017/11/08/docker-official-wordpress/ -->
 - 読んだ(公式を始めに読まない癖を直そう・・・): https://hub.docker.com/_/wordpress/
#### 2018/06/15
<!--  - 読んだ(docker stack とは): https://qiita.com/takyam/items/058865f1e1fb185e9fc4
- 読んだ: http://naremo.jp/2016/11/docker-wordpress/, https://www.kimurak.net/wordpress/wordpress/2505/ -->
- docker stack を使って、簡易環境を用意する(stack は、ボリュームのマウントができない。マイクロサービス開発時、他サービスの簡易環境など)
- docker-compose を使って、環境を用意する。wordpress 動作確認。(ボリュームのマウントできた。)

#### 2018/06/18
<!-- - 読んだ: https://www.webprofessional.jp/wordpress-theme-automation-with-gulp/ -->
- wordpress@docker に、独自テーマを適用。wp-content/themes/*
- 「docker とはなんぞ」ががわかったため、docker いじりは終了

### phase2: AWS を使う

#### 2018/06/18
- AWS の個人アカウント開通
- チュートリアルを読んで、EC2 鯖作るも、怖くなって消す(グローバル怖い)
- 初期設定(課金アラート、google 認証システムなど)
- IAM アカウントを作成(用語よくわかってない)

#### 2018/06/19
- Amazon CLI インストール(pipも)
- api gateway & lambda ドキュメントを読む
- intelliJ IDEA をさわる(IDE なつかしい)

#### 2018/06/20
- aws lambda をいじる。テスト用jsonを渡して、js, python で作った function を動かす。
- でも、本質がよくわかってないかんじなので、明日ドキュメントを読んで理解を深める。

#### 2018/06/21
- lambda で目的の function を作ることができた。(Webでコードを作成)
- lambda で DB を使うとして、dynamoDB は write に向かないらしいので、使いどころとしては一時キャッシュだ
- filesystem より read が早いなら、けっこういいかも(どうだろ)
- lambda を cui(cli) で実行しようとしたが、role や設定がダメで、こけてしまった

#### 2018/06/25
- cli で実行したくて、ACCESS_KEY の設定をする。
- アップロードはされた旨がコンソールに出るが、関数の実行がうまくいかない。
- AWS SAM LOCAL をインストールしたいが、python の依存ライブラリの関係で？うまくいかない。node(npm)のドキュメントはたくさん出るが・・・

#### 2018/06/26
- AWS SAM LOCAL で lambda アプリを動かした
- バージョンアップして、aws-sam-cli になったみたいだが、うまくバージョンアップできなかった。一応、警告なしでインストールできたかな？動作確認は明日。

#### 2018/06/28
- lambda & API gateway on local
- 自動でできた hello world 的なアプリにて、web API として動くことを確認。(local)

#### 2018/06/29
- s3, cloudformation に UP。aws-cli を使って。
- ロールにてこずって、時間がかかった。
- s3 / lambda / cloudformation / global URL の関係性がつかめない
- s3 にあげてるのか、cloudformation にあげてるのか、や、
- AWS の web から確認した時、どこのサービスにあげたプロジェクトがあるのか、関係性がわからない
- web API として global URL を発行したいが、よくわからない

#### 2018/07/02
- web API(global)を発行した
- AWS の ブラウザサービスをいじって、サービスごとの関係性を理解した
- web API(local)に、GET パラメタ渡して内容を変えてみてる途中

#### 2018/07/03
- web API(local)(helloworld改造)に、GET パラメタ渡す
- 上記をweb API(global)で動かす
- アニメの API を乗せる

#### 2018/07/04
- アニメの API の function 名などに hello-world という名称が残っているので対応

### Phase3: docker ふたたび

### 2018/07/05-06
- 公式 document を読んだ。
- docker image と docker コンテナについてわかった
> docker image は Read-only のシステムイメージ。
> docker image にコンテナレイヤが重なって、コンテナとなる。
> コンテナレイヤは docker image (サーバ構成)から書き換わったファイルを持つ。

- docker のファイルシステムについての公式 document を読んだ
- mac は overlay2 という、本番環境非推奨のファイルシステムみたい
- linux @ VM でいろいろ変えて操作感、状態、エラーメッセージなど調査したい

### 2018/07/09-11
- コマンドを頭に叩き込んでいる
- Dockerfile をいじる まだ書けないかな
- LXC についての資料を読んでいるが実際叩かないとわからんな
- cgroup と namespaces という技術がコンテナ技術の礎になってるようだが、よくわかってないので Linux でいじらな

### 2018/07/12
- LXC についての資料を読みこんだ。一番 LXC に明るい ubuntu が mac の VM でうまく動かない。のと、LXC は今の本筋ではないので、終了
- docker のネットワークについて理解したいので、がんばりはじめる。ポートフォワードはわかった。

### 2018/07/13
- mac の VM に centos を入れて、docker も入れた。が、ホスト OS から ssh をするのにてこずっている。。
- 公式ドキュメントのネットワークについて読んでる。mac だと docker のメインのブリッジがセキュリティの関係でなかったり、ツールのコマンドが入らなかったりで、あんま理解できてない。
- attach ができなかったのは、attach すると PID1 のプロセスに乱入するんだけど、入ろうとしてたコンテナの PID1 が `python app.py` だったので、これ入っても応答ないなーと。

### 2018/07/17
- VM に centos7 を入れた。ssh で接続するために、なんどもインストールした。。
- なんでも、インストールする前に「ネットワーク」項に「アダプター1:NAT」「アダプター2:ホストオンリーアダプタ」とやってあげると、192.168.56.101 がふられる。
- 中に docker を入れて、公式 document の、ネットワーク項を進めた。bridge ネットワークを作って、ふたつの bridge ネットワーク間では通信できなかったり、ひとつのコンテナに2つのネットワークを属させたり、それぞれのネットワークインタフェースに別名をつけて、それぞれの名前で ping したり。
- ちなみに ifconfig や ping は、busybox イメージなら元々入ってる。ubuntu ネットワークは入れるの難しい、resolv.conf を軽くいじったけど諦めた。。
- docker-machine, docker-swarm を、AWS でポケットマネーを出しつついじってみるぞ、というか AWS へのデプロイをやってみたいぞ。めっちゃ請求来ないでしょうね。。

### 2018/07/18-24
- docker swarm を mac 上で動かす。
- AWS VPC を、チュートリアルみながら動かす
- ECS のウィザードで勝手に作ってくれるやつを流されるままにやるが、全然わからない


## TODO
- python の実行環境を作る
- DockerHub のきになるイメージを触る

## 案: ドキュメント作成ベストプラクティクスの調査
* ワークフローを text で表現する記法を調べる
* ラムダファイル
* draw.io
* matplotlib(グラフ描画)
* Cacoo
* Gliffy
* DOT言語でサーバ構成図
