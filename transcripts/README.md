# 视频文字稿

这里存放从优质视频教程转录的中文文字稿。它们是本指南"整合网络内容"的一手素材——我们先用 [`tools/video_transcribe.py`](../tools/README.md) 把视频逐句转成文字，再人工校对、提炼知识点写进正文，并在正文标注来源视频与 UP 主。

> ⚠️ 这些文字稿是**机器转录的半成品**，仅供内部引用与校对，专有名词可能有误（比如"ARC 缓存"被识别成"Ark"、"TrueNAS"被识别成"Chunas/QNAS"）。请勿直接当作技术文档使用，正文里的内容均经过人工核对。

## 已转录的视频

| 文字稿 | 视频 | UP 主 | 主题 | 提炼到了哪里 |
| --- | --- | --- | --- | --- |
| [BV1VrTg66EUu.txt](BV1VrTg66EUu.txt) | [BV1VrTg66EUu](https://www.bilibili.com/video/BV1VrTg66EUu) | 正经de群晖 | 黑群晖 DSM7.4 安装（五步流程、U盘引导、BIOS、硬盘选择） | [15.1 B 站 UP 主](../docs/15-中文视频与博客/15.1-B站UP主.md) |
| [BV1gEfYBxE8V.txt](BV1gEfYBxE8V.txt) | [BV1gEfYBxE8V](https://www.bilibili.com/video/BV1gEfYBxE8V) | 司波图 | TrueNAS + 飞牛双系统架构（ZFS 兜底、KVM 虚拟机、GPU 直通、风险提醒） | [11.3 该不该 AIO](../docs/11-PVE底层方案/11.3-该不该AIO.md)、[15.1](../docs/15-中文视频与博客/15.1-B站UP主.md) |
| [BV1cUud6nEKm.txt](BV1cUud6nEKm.txt) | [BV1cUud6nEKm](https://www.bilibili.com/video/BV1cUud6nEKm) | 司波图 | 行业观察："为什么 NAS 越来越不好玩"（五盏灯熄灭、回归基础设施） | [1.3 谁需要 NAS](../docs/01-认识NAS/1.3-谁需要NAS.md) |
| [BV1ncjJ6wE7C.txt](BV1ncjJ6wE7C.txt) | [BV1ncjJ6wE7C](https://www.bilibili.com/video/BV1ncjJ6wE7C) | 旅客君LookUplus | 从 TrueNAS 换到飞牛的真实感受（素材管理、iCloud 分工、微信备份） | [3.6 飞牛 fnOS](../docs/03-平台横评与选型/3.6-飞牛fnOS.md) |

## 如何新增一篇

1. 找到优质视频的 BV 号
2. 用工具转录：`python tools/video_transcribe.py "https://www.bilibili.com/video/BVxxx" --hint "主题提示"`
3. 人工校对文字稿（重点看专有名词）
4. 提炼核心观点，用自己的话写进对应章节，标注视频链接与 UP 主
5. 更新上表与 [CREDITS](../CREDITS.md)

具体步骤见 [tools/README.md](../tools/README.md)。
