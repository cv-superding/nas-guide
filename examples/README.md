<p align="center">
  <img src="../docs/assets/images/ch07-apps.png" alt="可直接抄的配置和脚本" width="200">
</p>

# 示例：能直接抄的配置和脚本

这里放的是"可以拿来就用"的东西——Docker Compose、脚本、安全配置、自动化剧本。

> ⚠️ **所有账号、密码、Token 都是占位符**，用之前一定换成你自己的。千万别把真实凭据提交进仓库。

## 目录里有什么

```
examples/
├── docker-compose/          # 一键部署各种服务
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
│   ├── disk-health-check.sh # 硬盘体检
│   └── backup-restic.sh     # 自动备份
├── configs/
│   └── fail2ban/jail.local  # 防暴力破解
└── ansible/
    ├── inventory.ini
    ├── setup.yml
    └── deploy_containers.yml
```

## 怎么用才不出事

1. **先读懂再运行**——尤其涉及端口、权限、删除操作的配置
2. **改路径**——示例里的 `/volume1/...` 要换成你 NAS 上的实际路径
3. **凭据放 .env**——别写死在文件里（`.env` 已在 `.gitignore` 中）
4. **确认数据持久化**——`volumes` 一定要映射到 NAS 的实际存储，见 [7.1](../../docs/07-应用服务/7.1-Docker基础.md)

## 通用 .env 模板

复制成 `.env` 再改，别提交：

```env
PUID=1000
PGID=1000
TZ=Asia/Shanghai
NAS_DATA=/volume1/docker
```

## 各平台路径不一样

| 平台 | 常见数据路径 |
| --- | --- |
| 群晖 | `/volume1/docker`、`/volume1/media` |
| 威联通 | `/share/Container`、`/share/Media` |
| TrueNAS | `/mnt/tank/...` |
| 飞牛 / CasaOS / 通用 Linux | `/volume1/...` 或 `/mnt/...`（以实际为准） |

> 💡 不确定路径？先在系统里建一个共享文件夹，看看它实际的挂载路径是什么，再照着改配置。

## 脚本怎么用

```bash
# 硬盘体检：把 /dev/sda 换成你的硬盘
sudo bash disk-health-check.sh /dev/sda

# restic 备份：先设好环境变量
export RESTIC_REPOSITORY=/mnt/usb/backup-repo
export RESTIC_PASSWORD='你的强密码'
bash backup-restic.sh
```

更多说明在对应的正文小节：[5.5 硬盘健康](../../docs/05-存储与数据保护/5.5-硬盘健康监控.md)、[5.4 备份](../../docs/05-存储与数据保护/5.4-备份3-2-1原则.md)。
