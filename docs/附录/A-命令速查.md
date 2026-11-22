# A 命令速查

<p align="center">
  <img src="../assets/images/cover-home-nas.png" alt="随时回来翻查的工具箱" width="200">
</p>


> ⚠️ 执行前请将占位符替换为实际值；破坏性操作请谨慎。

## 磁盘与文件系统

```bash
lsblk                          # 列出块设备
df -h                          # 查看文件系统占用
sudo fdisk -l                  # 查看分区表
sudo smartctl -a /dev/sdX      # 查看硬盘 SMART 信息
sudo smartctl -t long /dev/sdX # 硬盘长测试
sudo badblocks -v /dev/sdX     # 坏道扫描（只读）
```

## ZFS

```bash
zpool status                   # 查看池状态
zpool list                     # 池容量概览
zfs list                       # 数据集列表
zfs list -t snapshot           # 快照列表
sudo zfs snapshot tank/data@名字      # 创建快照
sudo zfs rollback tank/data@名字      # 回滚（⚠️ 丢弃之后更改）
sudo zfs destroy tank/data@名字       # 删除快照
sudo zpool scrub tank                 # 启动数据校验
sudo zfs set recordsize=16K tank/data # 调整记录大小
```

## Btrfs

```bash
sudo btrfs subvolume snapshot -r /mnt/data /mnt/snapshots/data-日期
sudo btrfs subvolume list /mnt
sudo btrfs subvolume delete /mnt/snapshots/data-日期
sudo btrfs scrub start /mnt
sudo btrfs scrub status /mnt
```

## Docker

```bash
docker ps -a                   # 列出所有容器
docker logs -f <容器>           # 查看日志
docker exec -it <容器> sh       # 进入容器
docker compose up -d           # 启动编排
docker compose pull            # 拉取新镜像
docker compose down            # 停止并移除
docker image prune             # 清理无用镜像
docker system df               # 查看占用
```

## 网络

```bash
ip addr                        # 查看 IP
ethtool eth0                   # 查看网口协商速率
iperf3 -s                      # 启动测速服务端
iperf3 -c <IP>                 # 客户端测速
curl -I https://example.com    # 查看 HTTP 头
```

## 文件同步与校验

```bash
rsync -avP 源/ 目标/            # 断点续传复制
find /path -type f | wc -l     # 统计文件数
find /path -type f -exec sha256sum {} \; | sort > sum.txt  # 生成校验和
```

## 性能监测

```bash
top / htop                     # 系统资源
iostat -x 1                    # IO 状态
iotop                          # 磁盘 IO 进程
fio <配置文件>                 # 存储基准测试
```

## 备份（restic）

```bash
restic init --repo /path/repo         # 初始化仓库
restic -r /path/repo backup /data     # 备份
restic -r /path/repo snapshots        # 查看快照
restic -r /path/repo restore LATEST --target /restore  # 恢复
```

## 校验下载

```bash
sha256sum file.iso             # 计算校验和，与官方值比对
```
