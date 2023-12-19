# yolo_web_app

### アプリケーションの起動方法

- アプリケーションルートディレクトリに移動する。

```bash
cd [アプリのルートディレクトリ]
```

- イメージの作成

```bash
docker build . -t yolo_web_app_env
```

- コンテナの起動

```bash
docker run -p 8501:8501 -v $(pwd)/src:/opt/app/src --rm  --name yolo_web_app -it yolo_web_app_env
```

- コンテナの停止

```
ctr(コントロール) + c
```
