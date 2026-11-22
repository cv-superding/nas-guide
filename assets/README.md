# 图片与图示资源 assets/

本目录存放正文的配图资源与图示源码。

## 目录结构

```
assets/
├── images/      # 最终图片（png/jpg/webp）
└── diagrams/    # Mermaid 图示源码（.mmd）
```

## 配图规范

### 图片

- 文件名用英文小写 + 短横线：`nas-overview.png`
- 截图务必打码：IP、账号、序列号、家庭住址等个人信息
- 优先使用浅色背景，保证深色模式下也可读
- 单图控制在合理大小（建议 < 500KB）

### 图示（Mermaid）

正文中的架构图、流程图优先用 Mermaid 源码，好处是：

- 纯文本，可版本管理、可 diff
- 修改方便，无需图片工具
- MkDocs Material 原生支持渲染

图示源码放 `assets/diagrams/`，并在正文中用 Mermaid 代码块引用（便于直接渲染）。

## 图示清单

| 图示 | 文件 | 用于章节 |
| --- | --- | --- |
| 三条阅读路径 | `diagrams/reading-path.mmd` | 00、首页 |
| NAS 与传统存储对比 | `diagrams/nas-vs-traditional.mmd` | 1.1 |
| 数据保护体系 | `diagrams/data-protection.mmd` | 05 |
| 远程访问决策 | `diagrams/remote-access.mmd` | 6.2 |

## 贡献配图

欢迎补充配图。请参考 [CONTRIBUTING.md](../CONTRIBUTING.md) 的写作规范，并将图片放到对应子目录、更新本清单。
