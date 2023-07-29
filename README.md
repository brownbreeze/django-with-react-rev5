# 도커
docker run -itd -p 0.0.0.0:28085:8080 -v {local path}:/home/node --name nodejs_dev_5 {node-alpine image name}:latest


# 프로젝트 시작
## backend
which python
which pip
pip freeze
pip install "django~=3.0.0"
pip freeze

python -m django startproject backend

## frontend
npm install --global yarn
npm install -g n
n 18.0.0
yarn create react-app frontend
