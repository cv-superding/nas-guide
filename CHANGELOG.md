# 变更日志

本项目所有重要变更都会记录在此文件中。格式参考 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)。

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

[Unreleased]: https://github.com/cv-superding/nas-guide/compare/v0.3.0...HEAD
[0.3.0]: https://github.com/cv-superding/nas-guide/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/cv-superding/nas-guide/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/cv-superding/nas-guide/releases/tag/v0.1.0
