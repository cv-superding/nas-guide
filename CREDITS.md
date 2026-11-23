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
| [Linux zfs 精通篇：调优与最佳实践（mickeylan）](http://mp.weixin.qq.com/s?__biz=MzYyMzk5ODAwMQ==&mid=2247485198&idx=1&sn=f8473888f5498899a0e18b3a5a088731) | "每 1TB 配 1GB ARC"、recordsize、压缩与去重的取舍 | 13.1 ZFS 调优 |
| [ZFS on Linux: Six Months of Production Use（besterry.com）](https://besterry.com/posts/zfs-on-linux) | 半年生产使用经验：校验发现损坏文件、快照极快 | 13.1 的 ZFS 价值说明 |
| [ZFS on a dedicated server（novogara.com）](https://www.novogara.com/kb/zfs) | send/receive 作为块级增量复制的说明 | 13.2 zfs send/recv |
| [ZFS: CoW with Snapshots and RAID-Z（Hash Hackers）](https://blog.hashhackers.com/blog/zfs-guide) | zfs send/receive 全量与增量命令示例 | 13.2 的命令写法 |
| [How to Optimize ZFS on Linux（YouStable）](https://www.youstable.com/blog/optimize-zfs-on-linux/) | 按用途设置 recordsize、compression、primarycache | 13.1 的调优参数表 |
| [UPS Sizing Guide for Home Servers（selfhosting.sh）](https://selfhosting.sh/hardware/ups-sizing-calculator/) | 常见 UPS 机型在 85W/200W 下的续航参考 | 13.3 UPS 选型表 |
| [Sizing a UPS and Setting Up NUT（rhomelab.com）](https://rhomelab.com/hardware/ups-sizing-and-nut-setup) | NUT 配置思路（ups.conf、nut-scanner） | 13.3 NUT 配置 |
| [UPS Auto-Shutdown on Synology/QNAP（techfromalex.com）](https://techfromalex.com/ups-auto-shutdown-synology-qnap-nut) | 主/客户端 UPS 关系说明 | 13.3 多设备共用 UPS |
| [Paperless-ngx on Portainer（SelfHostHero）](https://selfhosthero.com/?p=3345/) | 必改的三个变量、分卷存储的部署要点 | 14.3 Paperless-ngx |
| [How to Install Paperless NGX on Synology（mariushosting.com）](https://mariushosting.com/how-to-install-paperless-ngx-on-your-synology-nas/) | NAS 上部署 Paperless-ngx 的实践 | 14.3 的 NAS 场景 |
| [Home Assistant Container（sequr.be）](https://sequr.be/blog/2022/09/home-assistant-container-part-2-home-assistant-container) | HA 容器的 Compose 配置思路 | 14.2 Home Assistant |

## 四、开源项目与教学项目

正是这些项目，让"自己搭一台 NAS"这件事变得可能。致谢它们，也鼓励读者去官方仓库点亮星标：

CasaOS、飞牛 fnOS、TrueNAS、Nextcloud、Immich、Jellyfin、qBittorrent、Transmission、Syncthing、Ollama、AnythingLLM、RAGFlow、Nginx Proxy Manager、Uptime Kuma、restic、borgbackup、fail2ban、Ansible、MkDocs Material。

在**如何组织一套教程**这件事上，我们参考了下面这些高星教学/文档/清单项目。它们各有所长——有的擅长分类索引，有的擅长概念拆解，有的用真实配置说话。本指南从它们身上学到了很多：

### 文档与指南类

| 项目 | 我们借鉴的组织方式 |
| --- | --- |
| [CasaOS](https://github.com/IceWhaleTech/CasaOS) / [OpenMediaVault](https://www.openmediavault.org/) | 面向新手的平实表达、功能分块说明（见 3.5、3.8） |
| [TrueNAS 文档](https://www.truenas.com/docs/) | 概念先行、术语对照、按主题拆分章节（见 3.4、5.1） |
| [Proxmox VE 中文手册](https://pve-doc-cn.readthedocs.io/) | 目录式结构、概念先行的技术文档写法（见第 11 章） |
| [Ansible-NAS](https://github.com/davestephens/ansible-nas) | "用代码定义配置"的自动化章节组织（见 8.2） |
| MoviePilot / getnas 等中文项目 | 中文场景化表达、本土应用说明 |
| openclaw-homelab-nas-guide 等 homelab 指南 | 从零到进阶的实战路径、多平台对比框架 |

### 精选清单类（Awesome List）

| 项目 | 我们借鉴的组织方式 |
| --- | --- |
| [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | 按场景分类、条目带技术栈/许可证标签的清单体系（见第 10 章） |
| [mikeroyal/Self-Hosting-Guide](https://github.com/mikeroyal/Self-Hosting-Guide) | 按场景组织 + 名词速查表 + "自托管地图"的定位（见第 10 章） |
| [AwesomeHomelab/awesome-homelab](https://github.com/AwesomeHomelab/awesome-homelab) | homelab 精选应用的分类方式 |
| [TWO-ICE/Awesome-NAS-Docker](https://github.com/TWO-ICE/Awesome-NAS-Docker) | 中文 NAS + Docker 项目按场景分类（见第 10 章） |

### 真实 Homelab 配置仓库

这些仓库公开了自己真在跑的配置，让我们学到"活文档"该怎么组织（见第 12 章）：

| 项目 | 我们借鉴的实践 |
| --- | --- |
| [TechHutTV/homelab](https://github.com/TechHutTV/homelab) | 云原生 homelab 的项目组织、媒体自动化栈 |
| [kimzam30/my-homelab-setup](https://github.com/kimzam30/my-homelab-setup) | Docker Compose + Tailscale + 监控的整体结构 |
| [jbaznik/homelab](https://github.com/jbaznik/homelab_codeasashu) | 双盘存储模型 + "verified nightly backups"（经验证的每夜备份） |
| [northcutted/homelab](https://github.com/northcutted/homelab) | 按功能分目录的配置组织 |
| [truethari/home-lab](https://github.com/truethari/home-lab) | 单一主 Compose 文件 + "Always Evolving" 的迭代理念 |
| [SinghChinmayy/homelab](https://github.com/SinghChinmayy/homelab) | 媒体自动化栈 + 可选 Tailscale 集成 |

这些项目的内容和文档各有千秋，本指南只是站在它们的思路之上做了自己的整理。若你尚未读过，强烈建议去看看原文、给它们点个星标。

## 五、图片与素材来源声明

这一节说明本指南里所有图片、图示的来源与版权立场。我们尽量做到"每一张图都能说清来历"。

### 5.1 配图（原创生成）

`docs/assets/images/` 下的 **14 张手绘水彩风格插画**，是为本指南专门生成的原创配图，覆盖 00～13 章。它们采用温暖的故事书风格（刻意避开生硬的技术示意图感），用于让阅读体验更柔和，也让零基础读者不至于被冷冰冰的内容劝退。

- 这些插画为本项目原创生成，**不含第三方素材**，右下角可能存在的生成工具标记已做技术处理去除
- 你可以随本仓库的 MIT 许可证自由使用、修改这些配图

| 配图 | 用于章节 |
| --- | --- |
| `cover-home-nas.png` | 封面、前言、附录 |
| `ch01-know-nas.png` ～ `ch09-cases.png` | 01～09 章 |
| `ch10-app-map.png` | 10 自托管应用图谱 |
| `ch11-pve.png` | 11 PVE 底层方案 |
| `ch12-homelab.png` | 12 Homelab 实战样板 |
| `ch13-data-advanced.png` | 13 数据保护进阶 |

### 5.2 图示（Mermaid 源码）

`docs/assets/diagrams/` 下的 `.mmd` 文件，以及正文中大量的 Mermaid 代码块，都是**纯文本绘制的流程图/架构图**，由本项目原创编写。它们可版本管理、可 diff、便于修改，遵循本仓库 MIT 许可证。

### 5.3 实操界面截图（来自社区教程）

这份指南是"汇总 + 改写"，所以**真实的软件界面截图，我们直接取自优质的开源教程**，而不是自己凭空画——毕竟教程的价值就在于"看到真实界面，跟着做"。

所有截图都存放在 `docs/assets/screenshots/`，并在正文对应位置标注了来源。版权归各自原作者/项目所有，本项目仅作**教学与非商业用途**引用，并尽可能指向原文。若某位作者不希望其图片被引用，请提 Issue，我们会立即移除。

| 截图 | 来源 | 版权/用途 |
| --- | --- | --- |
| `fnos-install-*.png`（4 张安装向导） | [飞牛官方帮助中心](https://help.fnnas.com/articles/v1/start/install-os) | © 飞牛 fnOS，官方安装文档截图 |
| `fnos-init-*.jpg`（3 张初始化向导） | [飞牛官方帮助中心](https://help.fnnas.com/articles/v1/start/install-os) | © 飞牛 fnOS，官方初始化文档截图 |
| `disk-benchmark.jpg`（SSD 基准测试） | [NEBULA（ooppll.icu）](https://ooppll.icu/) | © NEBULA 作者，教学引用 |
| `hardware-compare.webp`（硬件方案对比） | [fnnas.wiki](https://fnnas.wiki/) | © fnnas.wiki 作者，教学引用 |
| `fnos-desktop.png` / `fnos-appstore.webp` | [Lycoris 的小破站](https://lycoris.cloud/archives/019eda7f-15b1-743e-9aab-d0ee8999b0a5) | © Lycoris，教学引用 |
| `paperless-portainer-*.png`（3 张）/ `paperless-stack*.png`（2 张） | [Marius Hosting](https://mariushosting.com/how-to-install-paperless-ngx-on-your-synology-nas/) | © Marius Hosting，教学引用 |
| `tailscale-*.jpg`（6 张：官网/密钥/容器配置/管理后台/连接成功） | [太平洋知科技（pconline）](https://zhikeji.pconline.com.cn/article/497454)、[少数派](https://sspai.com/post/78811) | © 各作者，教学引用 |

> 💡 我们尽量减少重复截图，每张图只在最相关的位置用一次。宁可少而准，不要多而乱。

### 5.4 关于图片使用的原则

1. **装饰性配图**：自己生成（见 5.1），风格统一、无版权负担
2. **流程图/架构图**：用 Mermaid 重绘（见 5.2），纯文本可维护
3. **实操界面**：取自优质教程并标注来源（见 5.3），因为真实界面最有价值
4. **正文内容**：用自己的话重新组织，不整段照搬，并标注来源链接

如果你发现本仓库某张图来源标注有误或涉及授权问题，请提 Issue，我们会立即核实、替换或补充授权说明。

### 5.5 第三方品牌与商标

文中提及的群晖、威联通、TrueNAS、CasaOS、飞牛 fnOS 等产品名称与 Logo 归各自所有者所有。本指南仅为教学目的提及，不构成背书或商业使用。

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
