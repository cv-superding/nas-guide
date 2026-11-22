#!/usr/bin/env bash
# 使用 restic 备份到外置盘/异地
# 参考文档：docs/05-存储与数据保护/5.4-备份3-2-1原则.md
#
# 首次使用请先初始化仓库：
#   export RESTIC_REPOSITORY=/mnt/usb/backup-repo
#   export RESTIC_PASSWORD='YOUR_STRONG_PASSWORD'
#   restic init

set -euo pipefail

RESTIC_REPOSITORY="${RESTIC_REPOSITORY:-/mnt/usb/backup-repo}"
export RESTIC_REPOSITORY
# 密码建议从环境变量或受保护的密钥文件读取，切勿硬编码
: "${RESTIC_PASSWORD:?请设置 RESTIC_PASSWORD 环境变量}"

BACKUP_PATHS=(
  "/volume1/photos"
  "/volume1/documents"
)

echo "[$(date)] 开始备份到 $RESTIC_REPOSITORY"

restic backup "${BACKUP_PATHS[@]}" --tag auto

echo "[$(date)] 清理旧快照（保留策略）"
restic forget --keep-daily 7 --keep-weekly 4 --keep-monthly 6 --prune

echo "[$(date)] 备份完成"
