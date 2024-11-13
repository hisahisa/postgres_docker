# Dockerfile
FROM postgres:14

ENV TZ=Asia/Tokyo

# procpsパッケージをインストール
RUN apt update && apt install -y procps

# ログディレクトリを作成し、オーナーをpostgresに設定
RUN mkdir -p /var/lib/postgresql/log && chown -R postgres:postgres /var/lib/postgresql/log
