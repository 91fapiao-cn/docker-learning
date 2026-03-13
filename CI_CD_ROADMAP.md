# CI/CD Roadmap

## 当前已完成
- 最小 Python 服务
- Docker 本地 build / run / HTTP 验证
- GitHub Actions CI：语法校验 + Docker build + smoke test
- Buildx 缓存配置
- 失败时日志 artifact 保留
- Release 模板：tag 触发时推送到 GHCR

## 下一阶段

### 1. 让测试更像真实项目
- 增加 `tests/`
- 用 `pytest` 替代 `py_compile`
- 增加 `/healthz` 健康检查接口

### 2. 让镜像更像生产镜像
- 使用非 root 用户
- 明确 `HEALTHCHECK`
- 控制镜像体积
- 固定基础镜像 tag 或 digest

### 3. 让交付更完整
- 配置 GHCR 发布
- 增加语义化版本 tag
- 增加 CHANGELOG / release notes
- 视情况接部署工作流

## 现在这个模板适合什么
- 学习 Docker + GitHub Actions
- 作为最小 Python 容器化模板
- 作为后续接真实仓库的骨架
