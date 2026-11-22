#!/usr/bin/env bash
# 硬盘健康检查脚本
# 参考文档：docs/05-存储与数据保护/5.5-硬盘健康监控.md
# 用法：sudo ./disk-health-check.sh /dev/sda [/dev/sdb ...]

set -euo pipefail

if [[ $# -eq 0 ]]; then
  echo "用法: $0 /dev/sda [/dev/sdb ...]"
  exit 1
fi

if ! command -v smartctl >/dev/null 2>&1; then
  echo "错误: 未安装 smartmontools，请先执行: sudo apt install smartmontools"
  exit 1
fi

for disk in "$@"; do
  echo "========== $disk =========="
  # 整体健康状态
  smartctl -H "$disk" | grep -E "SMART overall-health|SMART Health" || true
  # 温度
  smartctl -A "$disk" | grep -i -E "Temperature_Celsius|Airflow_Temperature" || true
  # 关键属性
  smartctl -A "$disk" | grep -i -E "Reallocated_Sector|Current_Pending|Offline_Uncorrectable|Reported_Uncorrect" || true
  echo
done

echo "提示: 关注指标趋势，若关键值持续增长请立即备份并更换硬盘。"
