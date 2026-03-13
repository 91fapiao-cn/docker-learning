# Docker Learning Notes

## 本次验证结果

- Docker Desktop 已恢复可用。
- `docker pull alpine` 成功。
- `docker pull python:3.12-alpine` 成功。
- 本地镜像 `docker-learning:local` 已成功构建。
- 容器 `docker-learning-test` 已成功运行，HTTP `GET /` 返回 200。

## 关键经验

### 1. Docker Desktop 启动链路
排查顺序：
1. `docker --version`
2. `docker compose version`
3. `docker info`
4. `Get-Service com.docker.service`
5. `wsl -l -v`
6. `docker desktop status`

### 2. settings-store.json 不能带 BOM
路径：`C:\Users\Administrator\AppData\Roaming\Docker\settings-store.json`

如果以带 BOM 的 UTF-8 重写，Docker Desktop backend 会崩溃，日志会报：
`invalid character 'ï' looking for beginning of value`

安全写法：使用无 BOM UTF-8。

### 3. 当前网络环境下的稳定构建方案
当前环境里，BuildKit 访问 `auth.docker.io` 仍可能不稳定。

稳定方案：
1. 先单独拉基础镜像
   - `docker pull python:3.12-alpine`
2. 构建时关闭 BuildKit，避免重新走远端 token 链路
   - PowerShell: `$env:DOCKER_BUILDKIT='0'`
   - `docker build --pull=false -t docker-learning:local .`

### 4. 当前 Docker Desktop 代理状态
- HTTP Proxy: `http.docker.internal:3128`
- HTTPS Proxy: `http.docker.internal:3128`
- No Proxy: `hubproxy.docker.internal`
- `settings-store.json` 当前已写入：
  - `dNSInhibition = "ipv4"`
  - `proxyHTTPMode = "system"`

## 已验证命令

```powershell
# 构建
$env:DOCKER_BUILDKIT='0'
docker build --pull=false -f Dockerfile.local -t docker-learning:local .

# 运行
docker run -d --name docker-learning-test -p 18081:8000 docker-learning:local

# 验证
Invoke-WebRequest -UseBasicParsing http://127.0.0.1:18081/

# 查看状态
docker ps --filter name=docker-learning-test
docker logs --tail 50 docker-learning-test
```
