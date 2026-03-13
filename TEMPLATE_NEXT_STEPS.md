# Template Next Steps

这个目录现在是一个最小 Docker + GitHub Actions 样板。

## 已具备
- 最小 Python HTTP 服务
- Dockerfile / Dockerfile.local
- 本地运行说明
- GitHub Actions CI 样板
- 本机排障经验笔记

## 如何迁移到真实项目

### 1. 替换业务代码
- 用真实应用替换 `app.py`
- 确认应用监听端口与容器暴露端口一致

### 2. 调整 Dockerfile
- Python 项目：补 `requirements.txt` / `pip install`
- Node 项目：改用 `node:` 基础镜像与 `npm ci`
- Web 项目：可拆成 build 阶段 + runtime 阶段

### 3. 调整 CI 工作流
- 把 `python -m py_compile app.py` 改成真实测试命令
  - Python: `pytest`
  - Node: `npm test`
- 把 health check 路径改成真实健康接口，如 `/healthz`
- 如需提速，可补缓存与 matrix

### 4. 如需上线交付
可继续增加：
- 镜像推送到 registry
- tag/release 流程
- 自动部署到服务器或云平台
- secrets / environments 管理

## 当前建议
先保持这个模板尽量小，确认：
1. 本地可 build
2. 本地可 run
3. CI 结构清楚
4. README 能指导别人复用
