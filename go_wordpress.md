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
* 次どうしたら？

## デザイン自動ビルド
