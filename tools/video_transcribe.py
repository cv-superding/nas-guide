#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
视频转文字工具 —— 让文档贡献者能把优质视频教程转成文字稿，用于整理改写。

原理：yt-dlp 下载音频 → ffmpeg 转 16k 单声道 wav → faster-whisper 本地转录。
无需视频字幕，中文语音直接转文字。

用法：
    # 1. 安装依赖（在虚拟环境中）
    pip install yt-dlp faster-whisper

    # 2. 设置模型镜像（国内网络）——下载一次后缓存
    export HF_ENDPOINT=https://hf-mirror.com   # Windows PowerShell: $env:HF_ENDPOINT='https://hf-mirror.com'

    # 3. 转录
    python tools/video_transcribe.py "https://www.bilibili.com/video/BVxxxxx" --model small

输出：transcripts/<视频ID>.txt，带时间戳的中文文字稿。

说明：
- 模型可选 tiny/base/small/medium，越大越准但越慢
- 首次运行会下载模型（small 约 500MB），之后走缓存
- 转录结果请人工校对后使用，专有名词可能误识别
"""
import argparse
import subprocess
import sys
import wave
from pathlib import Path

import numpy as np


def find_ffmpeg():
    """查找 ffmpeg 可执行文件。"""
    import shutil
    p = shutil.which("ffmpeg")
    if p:
        return p
    for candidate in [
        r"D:\Tool\ffmpeg\ffmpeg-8.0-full_build\bin\ffmpeg.exe",
        r"C:\Users\29436\ffmpeg\bin\ffmpeg.exe",
    ]:
        if Path(candidate).exists():
            return candidate
    return None


def download_audio(url, workdir):
    """用 yt-dlp 下载纯音频。"""
    import yt_dlp
    outtmpl = str(workdir / "audio.%(ext)s")
    opts = {
        "format": "bestaudio/best",
        "outtmpl": outtmpl,
        "quiet": True,
        "no_warnings": True,
    }
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=True)
    audio = list(workdir.glob("audio.*"))
    if not audio:
        raise RuntimeError("音频下载失败")
    return audio[0], info


def to_wav(ffmpeg, src, dst):
    """ffmpeg 转 16k 单声道 wav。"""
    subprocess.run(
        [ffmpeg, "-y", "-i", str(src), "-ar", "16000", "-ac", "1",
         "-c:a", "pcm_s16le", str(dst)],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )


def read_wav(path):
    """标准库读 wav -> float32 numpy，绕过 av 解码兼容问题。"""
    with wave.open(str(path), "rb") as w:
        raw = w.readframes(w.getnframes())
    return np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0


def transcribe(audio, model_size, hint):
    """faster-whisper 转录。"""
    from faster_whisper import WhisperModel
    model = WhisperModel(model_size, device="cpu", compute_type="int8")
    segments, info = model.transcribe(
        audio,
        language="zh",
        initial_prompt=hint or "这是一段中文技术教程视频，关于 NAS 网络存储与服务器搭建。",
        vad_filter=True,
    )
    return segments, info


def main():
    ap = argparse.ArgumentParser(description="视频转文字工具")
    ap.add_argument("url", help="视频 URL（B站/YouTube 等 yt-dlp 支持的站点）")
    ap.add_argument("--model", default="small", help="whisper 模型：tiny/base/small/medium")
    ap.add_argument("--hint", default="", help="提示词，帮助模型理解主题（专有名词等）")
    ap.add_argument("--out", default="transcripts", help="输出目录")
    args = ap.parse_args()

    ffmpeg = find_ffmpeg()
    if not ffmpeg:
        sys.exit("未找到 ffmpeg，请先安装")

    root = Path(__file__).resolve().parent.parent
    out_dir = root / args.out
    out_dir.mkdir(exist_ok=True)
    work = out_dir / "_work"
    work.mkdir(exist_ok=True)

    vid = args.url.rstrip("/").split("/")[-1].split("?")[0] or "video"
    print(f"[1/4] 下载音频: {args.url}")
    audio, info = download_audio(args.url, work)
    print(f"      标题: {info.get('title', '')}")

    print("[2/4] 转换为 wav")
    wav = work / "audio.wav"
    to_wav(ffmpeg, audio, wav)

    print("[3/4] 读取音频并转录（这步最慢，请耐心）")
    samples = read_wav(wav)
    segments, meta = transcribe(samples, args.model, args.hint)

    print("[4/4] 写出文字稿")
    out_file = out_dir / f"{vid}.txt"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(f"# {info.get('title', '')}\n")
        f.write(f"# 来源: {args.url}\n")
        f.write(f"# UP主: {info.get('uploader', '')}\n\n")
        n = 0
        for seg in segments:
            f.write(f"[{seg.start:6.1f}s] {seg.text.strip()}\n")
            n += 1
    print(f"完成: {out_file}（{n} 段）")
    print("提示：转录结果请人工校对后使用，专有名词可能误识别。")

    # 清理临时音频
    for p in work.glob("audio.*"):
        p.unlink()
    work.rmdir()


if __name__ == "__main__":
    main()
