# apache を立てて、wordpress 乗せてみる

## 事前準備

* docker 公式でアカウントを作って DL, install, デスクトップでログインして running させる。
* 今は version 18 くらいみたい

## ホストOS を立てる

* docker container run hello-world
```
% docker container run hello-world                               (git)-[master]
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
9bb5a5d4561a: Pull complete
Digest: sha256:f5233545e43561214ca4891fd1157e1c3c563316ed8e237750d59bde73361e77
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/engine/userguide/
```

* docker pull centos
```
% docker image list                                              (git)-[master]
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
centos              latest              49f7960eb7e4        8 days ago          200MB
```

* docker run -it centos bash
```
% docker run -it centos bash                                     (git)-[master]
[root@71bac331b0b2 /]# shutdown -h now
Failed to talk to init daemon.
[root@71bac331b0b2 /]# yum install httpd
....
Complete!
[root@71bac331b0b2 /]#

おおお
なるほど
```

* docker run docker/whalesay cowsay hello world
 * 実行するイメージ/イメージ内で実行するコマンド/任意の文字列

```
% docker run docker/whalesay cowsay hello world                  (git)-[master]
Unable to find image 'docker/whalesay:latest' locally
latest: Pulling from docker/whalesay
e190868d63f8: Pull complete
909cd34c6fd7: Pull complete
0b9bfabab7c1: Pull complete
a3ed95caeb02: Pull complete
00bf65475aba: Pull complete
c57b6bcc83e3: Pull complete
8978f6879e2f: Pull complete
8eed3712d2cf: Pull complete
Digest: sha256:178598e51a26abbc958b8a2e48825c90bc22e641de3d31e18aaf55f3258ba93b
Status: Downloaded newer image for docker/whalesay:latest
 _____________
< hello world >
 -------------
    \
     \
      \
                    ##        .
              ## ## ##       ==
           ## ## ## ##      ===
       /""""""""""""""""___/ ===
  ~~~ {~~ ~~~~ ~~~ ~~~~ ~~ ~ /  ===- ~~~
       \______ o          __/
        \    \        __/
          \____\______/
[moe_irikida@moirikida] ~/Workspace/gh-dwango/docker-mokumoku
%

ほう
多分中のOSのコンソールにはあまり入らないんだろうな
```

## wordpress を乗せる

* docker pull wordpress

```
...
Status: Downloaded newer image for wordpress:latest

```

サイトのコピペを実行したら、
```
# docker-compose.yml
version: "3"

services:

  wp:
    image: wordpress
    ports:
      - "8080:80"
    volumes:
      - ./wp:/var/www/html
      - ./my-great-theme:/var/www/html/wp-content/themes/my-great-theme
    depends_on:
      - db

  db:
    image: mysql
    volumes:
      - ./db:/var/lib/mysql
    environment:
      MYSQL_RANDOM_ROOT_PASSWORD: "yes"
      MYSQL_DATABASE: wordpress
      MYSQL_USER: moe
      MYSQL_PASSWORD: wppass
```
-> webフロントで、[Error establishing a database connection]
->
```
% docker-compose up                                              (git)-[master]
Creating network "wp_default" with the default driver
Creating wp_db_1 ... done
Creating wp_wp_1 ... done
Attaching to wp_db_1, wp_wp_1
db_1  | 2018-06-14T05:20:47.108029Z 0 [Warning] [MY-011070] [Server] 'Disabling symbolic links using --skip-symbolic-links (or equivalent) is the default. Consider not using this option as it' is deprecated and will be removed in a future release.
db_1  | 2018-06-14T05:20:47.109465Z 0 [System] [MY-010116] [Server] /usr/sbin/mysqld (mysqld 8.0.11) starting as process 1
wp_1  | AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 172.19.0.3. Set the 'ServerName' directive globally to suppress this message
wp_1  | AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 172.19.0.3. Set the 'ServerName' directive globally to suppress this message
db_1  | mbind: Operation not permitted
db_1  | mbind: Operation not permitted
wp_1  | [Thu Jun 14 05:20:47.546008 2018] [mpm_prefork:notice] [pid 1] AH00163: Apache/2.4.25 (Debian) PHP/7.2.6 configured -- resuming normal operations
wp_1  | [Thu Jun 14 05:20:47.546146 2018] [core:notice] [pid 1] AH00094: Command line: 'apache2 -D FOREGROUND'
db_1  | 2018-06-14T05:20:48.417382Z 0 [Warning] [MY-010068] [Server] CA certificate ca.pem is self signed.
db_1  | 2018-06-14T05:20:48.431510Z 0 [Warning] [MY-011810] [Server] Insecure configuration for --pid-file: Location '/var/run/mysqld' in the path is accessible to all OS users. Consider choosing a different directory.
db_1  | 2018-06-14T05:20:48.455274Z 0 [Warning] [MY-010315] [Server] 'user' entry 'mysql.infoschema@localhost' ignored in --skip-name-resolve mode.
db_1  | 2018-06-14T05:20:48.455774Z 0 [Warning] [MY-010315] [Server] 'user' entry 'mysql.session@localhost' ignored in --skip-name-resolve mode.
db_1  | 2018-06-14T05:20:48.455856Z 0 [Warning] [MY-010315] [Server] 'user' entry 'mysql.sys@localhost' ignored in --skip-name-resolve mode.
db_1  | 2018-06-14T05:20:48.455876Z 0 [Warning] [MY-010315] [Server] 'user' entry 'root@localhost' ignored in --skip-name-resolve mode.
db_1  | 2018-06-14T05:20:48.456697Z 0 [Warning] [MY-010323] [Server] 'db' entry 'performance_schema mysql.session@localhost' ignored in --skip-name-resolve mode.
db_1  | 2018-06-14T05:20:48.456941Z 0 [Warning] [MY-010323] [Server] 'db' entry 'sys mysql.sys@localhost' ignored in --skip-name-resolve mode.
db_1  | 2018-06-14T05:20:48.457040Z 0 [Warning] [MY-010311] [Server] 'proxies_priv' entry '@ root@localhost' ignored in --skip-name-resolve mode.
db_1  | 2018-06-14T05:20:48.464353Z 0 [Warning] [MY-010330] [Server] 'tables_priv' entry 'user mysql.session@localhost' ignored in --skip-name-resolve mode.
db_1  | 2018-06-14T05:20:48.464397Z 0 [Warning] [MY-010330] [Server] 'tables_priv' entry 'sys_config mysql.sys@localhost' ignored in --skip-name-resolve mode.
db_1  | 2018-06-14T05:20:48.475243Z 0 [System] [MY-010931] [Server] /usr/sbin/mysqld: ready for connections. Version: '8.0.11'  socket: '/var/run/mysqld/mysqld.sock'  port: 3306  MySQL Community Server - GPL.
wp_1  | 172.19.0.1 - - [14/Jun/2018:05:21:02 +0000] "GET / HTTP/1.1" 500 556 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:60.0) Gecko/20100101 Firefox/60.0"
wp_1  | 172.19.0.1 - - [14/Jun/2018:05:21:03 +0000] "GET /favicon.ico HTTP/1.1" 200 228 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:60.0) Gecko/20100101 Firefox/60.0"
```
```
 % docker exec wp_wp_1 cat /var/www/html/wp-config.php
```
ある。
マウントされているため、docker-mokumoku/wp/wp/wp-config.php をいじるとすぐに反映される！

で、WPALLOWREPAIR -> true
にしても、うまくいかない。

そこで、docker hub / wordpress イメージ公式(最初にみようよ私！)
を見て、docker-compose.yml を修正

で、mysql に

> MySQL Connection Error: (1045)

と出たため、

> https://qiita.com/banrui/items/5669427f61cafc39162d

を参考に修正。

```
Access denied for user 'root'@'172.19.0.2' (using password: YES)
```
と出てしまう。パスワードの設定がだめみたい。

* stack を使う

docker hub wordpress 公式の stack.yml をコピペして、docker stack コマンドを打つも、事前にやれっていうコマンドが出てきたため打つ。
```
$ docker swarm join-token manager
$ docker swarm join --token SWMTKN-1-0ccr13y4s24m1zw5x4kvwj5zji91tsjzktpgwkr80l29jkzc2c-4s1vdjtjdq26nj2wdc3gj8ub6 192.168.65.3:2377
$ docker stack deploy -c stack.yml wordpress
```

そうしたら、wordpress 初期設定画面が出たー！

* ボリュームのマウント
stack でできるの？？簡易ビルドみたいで、ないなあ
* docker-compose で作成
```
$ docker-compose -f stack.yml up
```
 * よく使うコマンド docker kill all
```
$ docker kill $(docker ps -q)
```
なんか変なプロセスを落とした。苦戦した
```
$ docker rmi $(docker images)
$ docker stack rm wordpress
% docker swarm leave --force
```
## デザイン自動ビルド
