# 变更日志

本项目所有重要变更都会记录在此文件中。格式参考 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)。

## [0.7.3] - 2026-11-26

### 修复（结构一致性）
- 补齐第 10～16 章共 7 个配套练习文件（此前只有 00～09 章有练习）
- 更新 exercises 索引表与进度表至 16 章
- 一致性审计：章节 / 练习 / 导航 / SUMMARY 现已完全对齐
- 882 个链接零失效

## [0.7.2] - 2026-11-24

### 新增（第 16 章：工具实战补充）
- 把第 10 章图谱里一笔带过的四个高频工具扩写成"安装+配置+实测"小节：AdGuard Home、filebrowser、Gitea、Uptime Kuma
- 新增 3 个可运行 Compose 示例（adguardhome/filebrowser/gitea），全部通过 config 校验
- 配 AdGuard 官方仪表盘截图，其余复用已有官方截图
- 更新导航/SUMMARY/README/examples 清单/CREDITS

## [0.7.1] - 2026-11-24

### 新增（图片覆盖继续补齐）
- 从群晖教程后半段与 GitHub 官方仓库精选 7 张（SSH 终端、内网测速、权限配置、控制面板、filebrowser、Nginx Proxy Manager 等）
- 嵌入 8.2/6.1/10.1/6.3/4.3/8.1 等小节
- 对 11 PVE/12 Homelab/13 数据保护/15 视频博客做合理交叉引用（同一界面从不同角度说明）
- 截图总数 70→77 张，全部被引用，838 个链接零失效
- 所有内容章节现均有真实截图（00 前言为纯指引章节，保留占位说明）

## [0.7.0] - 2026-11-24

### 新增（群晖截图 + 抓图工具化）
- 从什么值得买群晖 DS920+ 万字教程抓真实 DSM 界面截图，精选 12 张入库（桌面/安装/存储池/套件中心/FileStation/Container Manager/相册/影音等）
- 嵌入 3.2 群晖分论、2.4 硬件、5.2 存储、7.1/7.2/7.4 应用、4.2 安装、9.2 案例等图片偏少章节
- 新增 `tools/fetch_doc_images.py`：把抓图能力固化成可复用工具，贡献者可用来扩充图片
- 截图总数 58→70 张，70 张全部被引用
- 探测了群晖知识中心/威联通/TrueNAS 文档站（均 JS 动态加载，暂无法直接抓取）

## [0.6.8] - 2026-11-23

### 新增（飞牛官方文档图片第二批）
- 再挖飞牛文档 8 个页面（AI 相册/照片分享/WebDAV/NFS/WiFi/TV端/Infuse/文件夹创建），精选 13 张入库
- 嵌入 7.4（AI 人脸聚类/分享二维码）、6.3（WebDAV）、7.2（TV端/Infuse）、4.4（创建文件夹）、6.1（WiFi）、7.3（NFS）等小节
- 截图总数 45→58 张，58 张全部被引用，794 个链接零失效

## [0.6.7] - 2026-11-23

### 新增（飞牛官方文档图片大扩充）
- 系统爬取飞牛官方帮助中心 71 个文档页，发现 176 张官方截图，精选 17 张入库（用户权限、存储池、影音、GPU 直通、SSD 缓存、访问服务等）
- 这 17 张嵌入到最匹配的小节：4.3 用户管理、5.2 存储池、7.2 影音、8.3 SSD 缓存、11.2 GPU 直通、6.1 访问设置等
- 给图片偏少的章节概览补图（01/12/13/15），全部 16 章现均有真实截图
- 截图总数 28→45 张，45 张全部被文档引用
- CREDITS 补全飞牛官方文档页面来源

## [0.6.6] - 2026-11-23

### 新增（图片补全）
- 新增 6 张来自 GitHub 官方仓库的真实界面截图：CasaOS 桌面、Immich 相册、Nextcloud 文件、Gitea（2 张）、Uptime Kuma
- 10 个章节概览页补上最相关的真实截图并标注来源
- 3.5/7.4/8.5/10.3 核心小节嵌入匹配的真实界面图
- 6 个无合适真实截图的章节（前言/认识NAS/PVE/Homelab/数据保护进阶/视频博客）加"图片说明"，明确占位原因与替代方案
- CREDITS 补全官方截图来源

## [0.6.5] - 2026-11-23

### 新增（视频内容二次提炼 · 平台选型）
- 转录旅客君 LookUplus《从 TrueNAS 换到飞牛 OS》（BV1ncjJ6wE7C）
- 3.6 飞牛分论加入真实用户视角：素材管理、iCloud+NAS 分工、微信备份、家人零门槛使用
- 更新文字稿索引与 CREDITS（累计 4 篇视频文字稿）

## [0.6.4] - 2026-11-23

### 新增
- transcripts/README.md：文字稿索引表，列出每篇视频的来源、UP主、主题与提炼去向
- CREDITS 新增"视频内容的引用方式"章节，说明转录→校对→提炼→署名的流程

## [0.6.3] - 2026-11-23

### 新增（视频内容二次提炼 · 行业观察）
- 转录司波图《为什么 NAS 越来越不好玩了》（BV1cUud6nEKm）
- 1.3 新增"反向视角：为什么很多人最后不爱玩了"——从视频提炼的"五盏灯熄灭"与"回归基础设施"结论
- 引导读者区分"折腾的快乐"与"数据安稳的踏实"，呼应数据保护优先的理念

## [0.6.2] - 2026-11-23

### 新增（视频内容二次提炼）
- 转录司波图"TrueNAS + 飞牛双系统"视频（BV1gEfYBxE8V），文字稿存入 transcripts/
- 11.3 新增"真实案例：TrueNAS 打底 + 飞牛做体验层"——从视频逐句提炼的架构、实操细节与风险提醒
- 15.1 补充视频链接与文字稿/提炼内容的交叉引用

## [0.6.1] - 2026-11-23

### 新增（视频转文字能力）
- 新增 `tools/video_transcribe.py`：yt-dlp 下载音频 → ffmpeg 转 wav → faster-whisper 本地转录，把无字幕视频转成带时间戳的中文文字稿
- 实测转录了正经de群晖的黑群晖安装视频（BV1VrTg66EUu），文字稿存入 `transcripts/`
- 15.1 新增"从视频转录提炼的实操要点"——逐句看完视频后改写，而非泛泛索引
- 15.3 新增"把视频转成文字"一节，教读者使用工具

### 安装的工具
- yt-dlp、faster-whisper（项目 .venv），Whisper small 模型（HF 镜像下载并缓存）

## [0.6.0] - 2026-11-23

### 新增（整合 B 站与 CSDN 资源）
- 第 15 章「中文视频与博客」：B 站 UP 主地图（司波图、爱折腾的老高、正经de群晖等）、CSDN 博客精选、视频+文字配合学习法
- 把 UP 主/博主的核心观点用自己的话提炼成索引（如"TrueNAS 骨架+飞牛灵魂"、Docker"公寓/集装箱房"比喻、"小白先买成品"建议）
- 致谢页新增 B 站 UP 主与 CSDN 博客分类，全部标注来源与署名

## [0.5.1] - 2026-11-23

### 新增
- 引入 6 张 Tailscale 真实组网截图（官网、生成 auth key、容器配置、管理后台、连接成功），接入 6.2 远程访问章节
- 来源：太平洋知科技全平台 NAS 组网教程、少数派远程控制教程，已在 CREDITS 标注

## [0.5.0] - 2026-11-23

### 变更（图片体系重构）
- 引入 15 张来自优质教程的**真实实操截图**（飞牛官方安装/初始化向导、硬盘基准测试、飞牛桌面与应用中心、Paperless/Portainer 部署界面、硬件对比）
- 移除 63 个小节顶部雷同的手绘图，手绘图只在章节概览保留；每张截图只用在最相关的一处
- 首页 README 改为展示真实截图
- 图片来源声明如实标注每张截图出处、版权归原作者、仅作教学引用

### 为什么要改
- 之前全是自己生成的示意插画，缺少真实操作界面，且重复引用严重
- 本项目定位是"汇总 + 改写"，应当善用社区优秀教程的截图并注明来源

## [0.4.1] - 2026-11-23

### 新增
- 第 14 章「热门应用实战」：Portainer（容器图形化管理）、Home Assistant（智能家居）、Paperless-ngx（文档 OCR 归档）三个高频工具的"安装+配置+实测"小节
- 新增 3 个可运行的 Compose 示例（portainer / home-assistant / paperless-ngx），全部通过 `docker compose config` 校验
- 致谢页新增 3 篇部署教程来源

## [0.4.0] - 2026-11-23

### 新增（进阶教程整合）
- 第 13 章「数据保护进阶」：ZFS 调优（ARC/recordsize/压缩）、zfs send/recv 异地复制、UPS+NUT 断电保护
- 正文标注来源链接，致谢页新增 8 篇进阶教程（ZFS 调优/USP 选型/NUT 配置等）

### 图片与声明
- 新增第 13 章原创配图，配图总数 14 张，全部去除生成工具水印
- 致谢页新增「图片与素材来源声明」：配图原创、图示 Mermaid 原创、外部教程用链接引用而非搬运图片、第三方商标说明

### 修复
- 全部 14 张配图水印去除（纹理平移 + 精确 inpaint，因人而异选择方案）

## [0.3.0] - 2026-11-23

### 新增（参考 20+ 开源项目）
- 第 10 章「自托管应用图谱」：按场景分类的应用地图，参考 awesome-selfhosted、Self-Hosting-Guide、AwesomeHomelab、Awesome-NAS-Docker
- 第 11 章「PVE 底层方案」：把 NAS 装进虚拟机与 AIO 的利弊，参考 Proxmox VE 中文手册、TechHutTV/homelab
- 第 12 章「Homelab 实战样板」：从真实开源仓库学组织思路，参考 kimzam30、jbaznik、northcutted、truethari、SinghChinmayy 等项目
- CREDITS.md 系统致谢全部参考项目（文档指南 / 精选清单 / 真实配置仓库三类）

### 修复
- 链接审计：修复 12 个失效内部链接 + 1 个失效锚点，全仓链接与 Mermaid 图健康度检查通过

## [0.2.0] - 2026-11-22

### 变更（内容重构）
- 全文从"模板化 AI 腔"重构为自然、叙事、有生活气息的表达：00～09 章所有概览页 + 40+ 个核心小节重写
- 模板标题统一自然化：`本章目标`→`这一节能帮你`、`小结`→`写在最后`、`前置`→`先读` 等
- 新增 10 张统一风格的手绘水彩配图，覆盖全部内容页；图文结合，避免纯文字堆砌
- 修复文档站点配图失效问题：配图移入 `docs/assets/images/`，批量修正 65 个文件的引用路径

### 新增
- [致谢与来源 CREDITS.md](CREDITS.md)：分类致谢官方文档、中文社区（fnnas.wiki、NEBULA、数巢笔记、飞牛论坛等）、英文理念文章（Big Iron、safeguard.sh 等）与高星教学项目的组织思路
- [新人避坑指南](docs/00-前言/新人避坑指南.md)：硬件/安装/数据/安全/Docker/心态六类共 12 个高频坑
- [一周上手计划](docs/00-前言/一周上手计划.md)：把章节串成七天可执行路线
- 正文中就地标注引用来源，读者可追溯

### 技术
- 分 30+ 次独立提交迭代，每次提交主题明确、可追溯
- MkDocs 严格模式构建持续通过
- 示例代码验证：9 个 Docker Compose 通过 `docker compose config`、2 个 Shell 脚本通过 `bash -n`、2 个 Ansible Playbook 结构校验通过

## [0.1.0] - 2026-11-22

### 新增
- 项目初始化，确立三条阅读路径（新手线 / 进阶线 / 场景线）
- 完成 00～09 章及附录的整体大纲与核心内容
- 建立多平台横向对比框架，覆盖群晖、威联通、TrueNAS、CasaOS、飞牛 fnOS、树莓派
- 建立 `examples/`、`exercises/`、`assets/`、`templates/` 配套资源目录
- 建立 Issue / PR 模板与文档站点配置
- 发布贡献指南、行为准则、安全政策与免责声明

[Unreleased]: https://github.com/cv-superding/nas-guide/compare/v0.7.3...HEAD
[0.7.3]: https://github.com/cv-superding/nas-guide/compare/v0.7.2...v0.7.3
[0.7.2]: https://github.com/cv-superding/nas-guide/compare/v0.7.1...v0.7.2
[0.7.1]: https://github.com/cv-superding/nas-guide/compare/v0.7.0...v0.7.1
[0.7.0]: https://github.com/cv-superding/nas-guide/compare/v0.6.8...v0.7.0
[0.6.8]: https://github.com/cv-superding/nas-guide/compare/v0.6.7...v0.6.8
[0.6.7]: https://github.com/cv-superding/nas-guide/compare/v0.6.6...v0.6.7
[0.6.6]: https://github.com/cv-superding/nas-guide/compare/v0.6.5...v0.6.6
[0.6.5]: https://github.com/cv-superding/nas-guide/compare/v0.6.4...v0.6.5
[0.6.4]: https://github.com/cv-superding/nas-guide/compare/v0.6.3...v0.6.4
[0.6.3]: https://github.com/cv-superding/nas-guide/compare/v0.6.2...v0.6.3
[0.6.2]: https://github.com/cv-superding/nas-guide/compare/v0.6.1...v0.6.2
[0.6.1]: https://github.com/cv-superding/nas-guide/compare/v0.6.0...v0.6.1
[0.6.0]: https://github.com/cv-superding/nas-guide/compare/v0.5.1...v0.6.0
[0.5.1]: https://github.com/cv-superding/nas-guide/compare/v0.5.0...v0.5.1
[0.5.0]: https://github.com/cv-superding/nas-guide/compare/v0.4.1...v0.5.0
[0.4.1]: https://github.com/cv-superding/nas-guide/compare/v0.4.0...v0.4.1
[0.4.0]: https://github.com/cv-superding/nas-guide/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/cv-superding/nas-guide/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/cv-superding/nas-guide/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/cv-superding/nas-guide/releases/tag/v0.1.0
