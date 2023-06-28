# oss-haidilao

创建环境
```sh
# linux
python3 -m venv .venv
. .venv/bin/activate

# windows
py -3 -m venv .venv
.venv\Scripts\activate

```
启动flask
```sh
pip install flask
flask --app main run
```


使用docker
```sh
docker compose up -d --no-deps --build
```