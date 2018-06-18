# docker mokumoku

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
- api gateway & lambda
- Amazon CLI

### phase3: ドキュメント作成ベストプラクティクスの調査
* ワークフローを text で表現する記法を調べる
* ラムダファイル
* ? draw.io
* ? matplotlib(グラフ描画)
* ? CacooやGliffy

### そのほか やるネタ

* python の web アプリを作る - django
* Node.js をさわる
