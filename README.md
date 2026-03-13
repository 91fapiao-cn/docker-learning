# docker-learning

[![CI](https://github.com/91fapiao-cn/docker-learning/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/91fapiao-cn/docker-learning/actions/workflows/ci.yml)
[![Release Docker Template](https://github.com/91fapiao-cn/docker-learning/actions/workflows/release-docker-template.yml/badge.svg)](https://github.com/91fapiao-cn/docker-learning/actions/workflows/release-docker-template.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

一个最小但尽量像真实工程的 Docker + GitHub Actions 样板。

## 当前能力

- Python 内置 HTTP 服务
- `/` 与 `/healthz` 两个接口
- 本地 Docker 镜像构建
- 容器运行与 HTTP 验证
- `pytest` 最小测试
- GitHub Actions CI 样板
- GHCR release workflow 模板

## 本地运行

### 1. 安装测试依赖

```powershell
python -m pip install -r requirements-dev.txt
```

### 2. 运行测试

> 本机若存在全局 pytest 插件污染，可临时禁用自动加载。

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'
python -m pytest -q tests/test_app.py
```

### 3. 构建（当前网络环境稳定方案）

```powershell
$env:DOCKER_BUILDKIT='0'
docker build --pull=false -f Dockerfile.local -t docker-learning:local .
```

### 4. 运行容器

```powershell
docker rm -f docker-learning-test 2>$null
docker run -d --name docker-learning-test -p 18081:8000 docker-learning:local
```

### 5. 验证服务

```powershell
Invoke-WebRequest -UseBasicParsing http://127.0.0.1:18081/
Invoke-WebRequest -UseBasicParsing http://127.0.0.1:18081/healthz
```

预期：
- `/` 返回 hello JSON
- `/healthz` 返回健康状态 JSON

## 环境变量

复制 `.env.example`，当前仅使用：

- `PORT`：服务监听端口，默认 `8000`

## 项目文件

- `app.py` - 最小 HTTP 服务
- `tests/test_app.py` - 最小测试
- `requirements-dev.txt` - 开发/测试依赖
- `Dockerfile` - 更接近 CI/发布的标准构建文件
- `Dockerfile.local` - 当前环境更稳的本地构建版本
- `.dockerignore` - Docker 构建忽略
- `.gitignore` - Git 忽略
- `.gitattributes` - 跨平台换行策略
- `LICENSE` - MIT 许可
- `CHANGELOG.md` - 版本变更记录
- `DOCKER_LEARNING_NOTES.md` - 本机实战笔记
- `TEMPLATE_NEXT_STEPS.md` - 如何迁移到真实项目
- `CI_CD_ROADMAP.md` - 后续 CI/CD 演进路线
- `.github/workflows/ci.yml` - GitHub Actions CI
- `.github/workflows/release-docker-template.yml` - GHCR 发布模板

## GitHub Actions 说明

### CI
当前 CI 做这些事：
1. 安装测试依赖
2. 运行 `pytest`
3. Docker build
4. 启动容器
5. 对 `/` 与 `/healthz` 做 smoke test
6. 失败时上传日志 artifact

### Release 模板
`release-docker-template.yml` 预留了：
- tag 触发
- 登录 GHCR
- 自动生成镜像 metadata
- build 并 push 镜像

当仓库真实接入 GitHub 后，可继续补：
- 语义化版本标签
- CHANGELOG
- 发布说明
- 自动部署
