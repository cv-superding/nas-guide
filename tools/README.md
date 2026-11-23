# 工具目录

这里放本项目维护时用到的小工具。

## video_transcribe.py —— 视频转文字

NAS 领域很多优质教程是 B 站视频。这个工具把视频转成带时间戳的中文文字稿，方便我们**提炼知识点、整理改写进指南**（而不是凭空编造视频内容）。

### 原理

```
yt-dlp 下载音频 → ffmpeg 转 16k 单声道 wav → faster-whisper 本地转录
```

不需要视频自带字幕，中文语音直接转文字。

### 安装

```bash
pip install yt-dlp faster-whisper
```

- 需要系统装有 `ffmpeg`
- 首次运行会下载 Whisper 模型（small 约 500MB），国内建议设镜像：

```bash
# Linux/macOS
export HF_ENDPOINT=https://hf-mirror.com
# Windows PowerShell
$env:HF_ENDPOINT='https://hf-mirror.com'
```

### 用法

```bash
python tools/video_transcribe.py "https://www.bilibili.com/video/BVxxxxx" \
  --model small \
  --hint "这是一段关于飞牛 fnOS 安装的中文教程"
```

- `--model`：tiny/base/small/medium，越大越准但越慢（CPU 转录，small 约实时 0.5～1 倍速）
- `--hint`：主题提示，帮助模型识别专有名词
- 输出在 `transcripts/<视频ID>.txt`

### 校对

转录是机器识别，**专有名词常出错**（比如"U盘引导"可能识别成"右盘音脑"）。整理进指南前务必人工校对，并标注来源视频链接与 UP 主。见 [致谢](../CREDITS.md)。
