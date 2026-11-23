#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文档截图抓取工具 —— 从官方文档站批量提取真实界面截图。

用途：本指南坚持"用真实界面图"，这个工具帮你从文档站抓取图片，
人工挑选后放进 docs/assets/screenshots/ 并在正文引用、标注来源。

用法：
    # 飞牛官方帮助中心（图片在 help-static.fnnas.com CDN）
    python tools/fetch_doc_images.py --site fnnas

    # 从任意页面抓图（自动识别常见 CDN pattern）
    python tools/fetch_doc_images.py --url "https://example.com/tutorial"

    # 查看某站抓到多少图（不下载）
    python tools/fetch_doc_images.py --site fnnas --list-only

说明：
    - smzdm / 少数派 / 官方 GitHub README 等站点也适用 --url 模式
    - 抓到的图务必人工筛选（过滤 logo/二维码/广告），并确认版权与来源
    - 不要把整站图片无脑塞进仓库，精选与内容强相关的
"""
import argparse
import re
from pathlib import Path
from urllib.parse import urljoin

import requests

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}


def fetch_page_images(url, cdn_hint=None):
    """抓取单页的图片 URL。"""
    r = requests.get(url, timeout=20, headers=HEADERS)
    r.encoding = r.apparent_encoding
    imgs = re.findall(
        r'(?:src|data-src|data-original|href)=["\']([^"\']+)["\']', r.text, re.I
    )
    urls = []
    for u in imgs:
        if u.startswith("data:"):
            continue
        full = urljoin(url, u)
        if not any(x in full.lower() for x in (".png", ".jpg", ".jpeg", ".webp", ".gif")):
            continue
        if cdn_hint and cdn_hint not in full:
            continue
        # 过滤明显无关的
        if any(x in full.lower() for x in ("logo", "avatar", "qrcode", "icon", "emoji", "badge", "shield")):
            continue
        if full not in urls:
            urls.append(full)
    return urls


def crawl_fnnas():
    """爬飞牛官方帮助中心的所有页面。"""
    entry = "https://help.fnnas.com/"
    r = requests.get(entry, timeout=20, headers=HEADERS)
    links = re.findall(r'href=["\']([^"\']+)["\']', r.text)
    pages = set()
    for l in links:
        full = urljoin(entry, l)
        if ("help.fnnas.com" in full and "/articles/" in full
                and not any(x in full for x in (".png", ".jpg", ".css", ".js", ".svg", ".ico"))):
            pages.add(full)
    all_urls = []
    for page in sorted(pages):
        try:
            all_urls += fetch_page_images(page, cdn_hint="help-static.fnnas.com")
        except Exception:
            pass
    return list(dict.fromkeys(all_urls))


def main():
    ap = argparse.ArgumentParser(description="文档截图抓取工具")
    ap.add_argument("--site", choices=["fnnas"], help="预设站点")
    ap.add_argument("--url", help="任意页面 URL")
    ap.add_argument("--list-only", action="store_true", help="只列出 URL 不下载")
    ap.add_argument("--out", default="fetched_images", help="下载目录")
    args = ap.parse_args()

    if args.site == "fnnas":
        print("爬取飞牛官方帮助中心...")
        urls = crawl_fnnas()
    elif args.url:
        print(f"抓取页面: {args.url}")
        urls = fetch_page_images(args.url)
    else:
        ap.error("请指定 --site 或 --url")

    print(f"找到 {len(urls)} 张图片:")
    for u in urls[:40]:
        print("  ", u[:130])
    if len(urls) > 40:
        print(f"   ... 还有 {len(urls)-40} 张")

    if not args.list_only:
        out = Path(args.out)
        out.mkdir(exist_ok=True)
        ok = 0
        for i, u in enumerate(urls):
            try:
                r = requests.get(u, timeout=15, headers=HEADERS)
                if r.status_code == 200 and len(r.content) > 5000:
                    ext = ".jpg" if ".jpg" in u or ".jpeg" in u else ".png"
                    (out / f"img_{i:03d}{ext}").write_bytes(r.content)
                    ok += 1
            except Exception:
                pass
        print(f"下载 {ok} 张到 {out}/")
        print("下一步：人工筛选 → 重命名 → 放进 docs/assets/screenshots/ → 正文引用并标注来源")


if __name__ == "__main__":
    main()
