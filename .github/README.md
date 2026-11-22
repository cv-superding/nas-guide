# .github 协作配置

本目录存放 GitHub 协作相关的模板与自动化配置。

## 内容

```
.github/
├── ISSUE_TEMPLATE/
│   ├── bug.yml            # 内容纠错
│   ├── topic.yml          # 选题建议
│   └── config.yml         # Issue 模板配置
├── PULL_REQUEST_TEMPLATE.md
├── workflows/
│   ├── mkdocs.yml         # 文档站点构建与部署
│   └── link-check.yml     # 链接检查
└── README.md
```

## 工作流说明

- **mkdocs.yml**：推送到 main 时自动构建并部署文档站点到 GitHub Pages。
- **link-check.yml**：定期检查文档中的链接是否有效，避免死链。

> 💡 首次使用 Pages：请在仓库 Settings → Pages 中将 Source 设为 GitHub Actions。
