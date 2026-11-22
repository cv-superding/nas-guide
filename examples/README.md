# 配套示例 examples/

本目录收录可直接使用的配置示例、脚本与自动化 Playbook，配合正文使用。

> ⚠️ **所有示例中的路径、账号、密码均为占位符**，使用前请按你的环境修改。请勿提交真实凭据。

## 目录结构

```
examples/
├── docker-compose/
│   ├── jellyfin/            # 影音中心
│   ├── qbittorrent/         # 下载器
│   ├── nextcloud/           # 私有云
│   ├── immich/              # AI 相册
│   ├── ollama/              # 本地大模型
│   ├── nginx-proxy-manager/ # 反向代理
│   ├── cloudflared/         # 内网穿透
│   ├── uptime-kuma/         # 监控
│   └── vaultwarden/         # 密码管理
├── scripts/
│   ├── disk-health-check.sh # 硬盘健康检查
│   └── backup-restic.sh     # restic 备份
├── configs/
│   └── fail2ban/jail.local  # 防暴力破解
└── ansible/
    ├── inventory.ini
    ├── setup.yml
    └── deploy_containers.yml
```

## 使用原则

1. **先读懂再运行**：特别是涉及端口、权限、删除操作的配置。
2. **路径替换**：把 `/volume1/...` 等示例路径改成你 NAS 上的实际路径（群晖常为 `/volume1`，其他系统可能为 `/mnt/...`）。
3. **凭据管理**：密码用 `.env` 文件或 secrets，不要写死在文件里（`.env` 已在 `.gitignore` 中）。
4. **数据持久化**：确认 `volumes` 映射到了 NAS 的实际存储，见 [7.1 Docker 基础](../docs/07-应用服务/7.1-Docker基础.md)。

## 通用 .env 示例

```env
# 复制为 .env 并修改，切勿提交
PUID=1000
PGID=1000
TZ=Asia/Shanghai
NAS_DATA=/volume1/docker
```

## 平台路径差异

| 平台 | 常见数据路径 |
| --- | --- |
| 群晖 | `/volume1/docker`、`/volume1/media` |
| 威联通 | `/share/Container`、`/share/Media` |
| TrueNAS | `/mnt/tank/...` |
| 飞牛/CasaOS/通用 Linux | `/volume1/...` 或 `/mnt/...`（以实际为准） |
