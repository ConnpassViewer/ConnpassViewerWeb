# ConnpassApiServer

## 環境

- Ruby: 2.5.0
- Rails: 5.2.0

## Docker による環境構築

### セットアップ

```
docker-compose build
docker-compose up -d
```

### DB の設定

```bash
docker-compose run --rm app rails db:create #DBの作成
docker-compose run --rm app rails db:migrate #DBのMigration
docker-compose run --rm app rails db:seed #初期値の投入
```

### 起動方法

```
docker-compose up -d
```

### Scrapy の実行

```bash
docker-compose run --rm scrapy scrapy crawl connpass
```
