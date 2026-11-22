# 致谢与来源

<p align="center">
  <img src="docs/assets/images/cover-home-nas.png" alt="温暖的 NAS 首页插画" width="360">
</p>

> 这份指南不是凭空长出来的。它站在很多人的肩膀上——有人写了详尽的安装教程，有人把踩过的坑一条条记下来，有人耐心解释 ZFS 是什么。这里向他们致谢。

## 为什么要写这一页

网上关于 NAS 的好内容其实很多，散落在官方文档、论坛帖子、个人博客和各种视频里。我们在编写过程中参考、整理、重新组织了其中不少内容，用自己的话讲给零基础的读者听。

按照惯例，也出于尊重，我们把主要来源列在这里。如果你恰好是某篇文章的作者——谢谢你，也欢迎来 Issue 里打个招呼。

## 一、官方文档与手册（最主要的基础）

我们始终建议：**具体操作以官方最新文档为准**。以下官方文档是我们核对概念、流程和参数时最常翻的：

| 项目 | 来源 | 我们用它做了什么 |
| --- | --- | --- |
| 飞牛 fnOS | [飞牛帮助中心](https://help.fnnas.com/) | 安装流程、初始化步骤、系统盘建议 |
| 群晖 | Synology Knowledge Center（官方知识中心） | DSM 的存储、快照、Hyper Backup、QuickConnect 概念 |
| 威联通 | QNAP Documentation / User Manual | QTS 与 QuTS hero 的差异、HBS3、Container Station |
| TrueNAS | TrueNAS Documentation Hub | ZFS 池/数据集、RAIDZ、快照、scrub 的概念框架 |
| CasaOS | CasaOS 官方文档（IceWhale） | 安装方式、App Store、定位说明 |
| Docker | [Docker Docs](https://docs.docker.com/) | 镜像/容器/卷/Compose 的核心概念 |
| OpenZFS | OpenZFS Documentation | CoW、校验和、ARC、scrub 的解释 |
| Ansible | Ansible Documentation | Playbook、inventory、幂等性说明 |
| OpenMediaVault | [OpenMediaVault 官网](https://www.openmediavault.org/) | OMV 的定位、模块化设计、服务列表，见 3.8 |
| Redis/Nextcloud/Jellyfin 等 | 各项目官方文档 | 应用部署要点与端口说明 |

## 二、中文社区与教程站点

这些中文资料帮我们把"国外文档里的概念"变成了"中文用户能看懂的话"，也提供了大量真实场景：

| 来源 | 内容 | 我们参考的部分 |
| --- | --- | --- |
| [飞牛 OS 非官方教程站（fnnas.wiki）](https://fnnas.wiki/) | 从硬件选购到 Docker、Tailscale 的系统化中文教程 | 内容分层方式、硬件选择思路、远程访问章节的组织 |
| [飞牛私有云论坛（club.fnnas.com）](https://club.fnnas.com/) | 真实用户的装机记录（如旧 ThinkPad 装 fnOS） | 旧机改造的坑、安装实操细节 |
| [飞牛帮助中心](https://help.fnnas.com/articles/v1/start/install-os) | 安装与初始化官方指引 | 系统盘选择、BIOS/启动、初始化步骤 |
| [数巢笔记（shunot.com）](https://www.shunot.com/nas/1000.html) | 旧笔记本改 NAS 的三个月实测 | "合盖休眠"等真实踩坑经验，见 3.7、2.4 |
| [Lycoris 的小破站](https://lycoris.cloud/archives/019eda7f-15b1-743e-9aab-d0ee8999b0a5) | 从黑群晖到飞牛的折腾日记 | 装机过程的真实口吻、场景化表达 |
| [小众软件论坛 OMV 7 入门指北](https://meta.appinn.net/t/topic/73193/4) | 中文 OMV 7 图文教程 | OMV 章节的安装、配置、问题解决组织方式，见 3.8 |
| [悠哉网 OMV 指南](https://www.yoozai.com/21111.html) | OMV 设计哲学与插件/Docker 玩法 | "轻量、简洁、自由"的定位描述，见 3.8 |
| [NEBULA（ooppll.icu）](https://ooppll.icu/) | 飞牛实践、SSD 基准测试、自托管 AI 生态的中文经验分享 | 新盘检测的"跑一遍基准"习惯、在 NAS 上跑本地模型的思路，见 2.2、5.5、7.5 |
| [简米科技（idctop.com）](https://idctop.com/article/610259.html) | 旧电脑改 NAS 的硬件与安装说明 | 电源功率、启动盘、BIOS 设置的细节 |

## 三、英文社区与理念文章

这些文章把一些容易被说错的道理讲清楚了，我们据此重写了相关章节：

| 来源 | 内容 | 我们参考的部分 |
| --- | --- | --- |
| [RAID is not backup（Big Iron）](http://www.bigiron.cc/guides/raid-is-not-backup-what-backup-actually-means) | 什么才算真正的备份，镜像/快照为什么不算 | 5.3、5.4 关于"快照不是备份"的论述 |
| [The 3-2-1 Backup Rule, Actually Implemented（asidehouse.com）](https://asidehouse.com/story/the-3-2-1-backup-rule-actually-implemented) | 用清单检视常见"伪备份"配置 | 5.4 的常见配置评分思路 |
| [Homelab Backups Explained（safeguard.sh）](https://www.safeguard.sh/resources/blog/homelab-backups-explained-3-2-1-restic-borg-offsite-copies-and-restore-tests) | 3-2-1、restic/borg、恢复演练、离线备份 | 5.4 的恢复演练与离线加密备份建议 |
| [RAID Is Not a Backup（nasdecoded.com）](https://nasdecoded.com/raid-is-not-backup) | 大容量阵列重建期间的读取风险 | 2.3、5.2 关于大盘建议 RAID6 的解释 |
| [RAID is not a backup: the 3-2-1 rule, honestly（chartmann1590）](https://chartmann1590.github.io/homelab-the-right-way/posts/raid-is-not-a-backup-3-2-1) | 一份找出备份缺口的自查清单 | 5.4 的"什么算一份拷贝"讨论 |
| [Tailscale / WireGuard 官方文档](https://tailscale.com/kb/) | 组网 VPN 的原理与配置 | 6.2 远程访问方案对比 |

## 四、开源项目与教学项目

正是这些项目，让"自己搭一台 NAS"这件事变得可能。致谢它们，也鼓励读者去官方仓库点亮星标：

CasaOS、飞牛 fnOS、TrueNAS、Nextcloud、Immich、Jellyfin、qBittorrent、Transmission、Syncthing、Ollama、AnythingLLM、RAGFlow、Nginx Proxy Manager、Uptime Kuma、restic、borgbackup、fail2ban、Ansible、MkDocs Material。

在**如何组织一套教程**这件事上，我们还参考了这些高星教学/文档项目的思路——按章节递进、读路径分层、图文结合、示例与练习配套：

| 项目 | 我们借鉴的组织方式 |
| --- | --- |
| CasaOS / OpenMediaVault | 面向新手的平实表达、功能分块说明 |
| TrueNAS 文档 | 概念先行、术语对照、按主题拆分章节 |
| MoviePilot / getnas 等中文项目 | 中文场景化表达、本土应用说明 |
| Ansible-NAS | "用代码定义配置"的自动化章节组织（见 8.2） |
| openclaw-homelab-nas-guide 等 homelab 指南 | 从零到进阶的实战路径、多平台对比框架 |

这些项目的内容和文档各有千秋，本指南只是站在它们的思路之上做了自己的整理。若你尚未读过，强烈建议去看看原文。

## 五、配图说明

本仓库 `docs/assets/images/` 下的 10 张手绘水彩风格插画，是为本指南专门生成的原创配图（温暖故事书风格，刻意避开生硬的技术示意图感），用于让阅读体验更柔和。

`docs/assets/diagrams/` 下的 `.mmd` 文件是 Mermaid 图示源码，为正文中流程图、架构图的文本版本，便于修改与版本管理。

## 六、如果漏了谁

我们尽量标注每一处参考，但整理过程中难免有疏漏。如果你发现：

- 某段内容明显来自某篇文章却没署名
- 某个链接失效了
- 某处数据与最新官方文档不符

欢迎提 [Issue](https://github.com/cv-superding/nas-guide/issues) 或直接 PR，我们会尽快核实、补上或修正。

## 最后

写文档这件事，本质上是把别人赠予的知识，再整理好递给下一个人。谢谢上面所有作者，也谢谢正在读这份指南的你。

---

<p align="center">
  <img src="docs/assets/images/ch09-cases.png" alt="四个温暖的家庭与办公场景" width="240">
</p>
