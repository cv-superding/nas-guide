# 配图与图示资源

<p align="center">
  <img src="images/cover-home-nas.png" alt="温暖的 NAS 首页插画" width="280">
</p>

这一页存放全书的手绘配图和图示源码。

## 关于这些配图

`images/` 下的 10 张插画是为本指南专门生成的原创配图，统一采用温暖的手绘水彩风格，刻意避开了冷冰冰的技术示意图感觉。我们想让读文档这件事，也带一点人情味。

配图清单：

| 图片 | 用在 |
| --- | --- |
| `cover-home-nas.png` | 封面、前言、附录 |
| `ch01-know-nas.png` | 01 认识 NAS |
| `ch02-hardware.png` | 02 硬件选型 |
| `ch03-platforms.png` | 03 平台横评 |
| `ch04-first-build.png` | 04 第一次搭建 |
| `ch05-data-safety.png` | 05 数据安全 |
| `ch06-network.png` | 06 网络访问 |
| `ch07-apps.png` | 07 应用服务 |
| `ch08-advanced.png` | 08 进阶主题 |
| `ch09-cases.png` | 09 实战案例 |

## 目录结构

```
docs/assets/
├── images/      # 手绘配图（png）
└── diagrams/    # Mermaid 图示源码（.mmd）
```

> 💡 配图放在 `docs/` 目录下，是为了让 MkDocs 能把它一起打包进文档站点——否则 GitHub 上能看到图，网页版却是坏图。

## 图示（Mermaid）

正文里的架构图、流程图优先用 Mermaid 源码，好处是：

- 纯文本，可版本管理、可 diff
- 修改方便，不用打开图片工具
- MkDocs Material 原生支持渲染

图示源码放 `diagrams/`，清单：

| 图示 | 文件 | 用于章节 |
| --- | --- | --- |
| 数据保护体系 | `diagrams/data-protection.mmd` | 05 |
| 远程访问决策 | `diagrams/remote-access.mmd` | 6.2 |

## 配图规范（想贡献的话）

- 文件名用英文小写 + 短横线：`nas-overview.png`
- 截图务必打码：IP、账号、序列号、家庭住址
- 风格尽量与现有配图协调：温暖、柔和、故事感
- 单图控制在合理大小（建议 < 500KB）

这份指南参考了很多前辈和同好的资料，完整清单见仓库根目录的 [CREDITS.md（致谢与来源）](https://github.com/cv-superding/nas-guide/blob/main/CREDITS.md)。

详见 [贡献指南](../../CONTRIBUTING.md)。
