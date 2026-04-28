#!/usr/bin/env python3
"""
竞品照片应用动态追踪 — 研究计划生成器

输出结构化 JSON，包含各竞品的信息源 URL 列表，供后续 web_fetch 抓取。

用法：
    python3 scripts/research_plan.py [--week YYYY-WW]

Agent 随后对每个 URL 执行 web_fetch 并综合发现。
"""

import json
import sys
from datetime import datetime

# 竞品及信息源
COMPETITORS = {
    "Apple 照片": [
        ("Apple 新闻室", "https://www.apple.com/newsroom/", "新版本/功能发布"),
        ("iOS/macOS 更新说明", "https://support.apple.com/en-us/HT201222", "照片APP相关更新"),
        ("9to5Mac Photos", "https://9to5mac.com/guides/photos/", "照片APP新闻"),
        ("MacRumors", "https://www.macrumors.com/", "Apple 综合动态"),
    ],
    "Google Photos": [
        ("Google Photos 博客", "https://blog.google/products/photos/", "官方功能更新"),
        ("9to5Google", "https://9to5google.com/guides/google-photos/", "Google Photos 报道"),
        ("Android Authority", "https://www.androidauthority.com/tag/google-photos/", "功能分析与泄露"),
        ("Reddit r/googlephotos", "https://www.reddit.com/r/googlephotos/", "用户反馈热点"),
    ],
    "华为 HarmonyOS 图库": [
        ("华为消费者官网", "https://consumer.huawei.com/cn/", "HarmonyOS/图库更新"),
        ("鸿蒙更新", "https://consumer.huawei.com/cn/support/harmonyos/", "系统版本更新"),
        ("花粉俱乐部", "https://club.huawei.com/", "用户反馈"),
        ("华为终端微博", "https://weibo.com/huaweimobile", "官方动态"),
    ],
    "小米相册": [
        ("小米社区", "https://www.xiaomi.cn/", "相册功能讨论"),
        ("HyperOS", "https://www.mi.com/hyperos", "系统更新"),
        ("小米全球博客", "https://www.mi.com/global/blogs", "官方发布"),
    ],
    "OPPO 相册": [
        ("OPPO 社区", "https://www.oppo.cn/community/", "相册功能反馈"),
        ("ColorOS", "https://www.coloros.com/", "系统更新"),
        ("OPPO 微博", "https://weibo.com/oppo", "官方动态"),
    ],
    "VIVO 相册": [
        ("VIVO 社区", "https://community.vivo.com.cn/", "相册讨论"),
        ("OriginOS", "https://www.vivo.com.cn/originos", "系统更新"),
        ("VIVO 微博", "https://weibo.com/vivo", "官方动态"),
    ],
    "荣耀相册": [
        ("荣耀俱乐部", "https://club.hihonor.com/cn/", "用户反馈"),
        ("MagicOS", "https://www.hihonor.com/cn/magic/", "系统更新"),
        ("荣耀微博", "https://weibo.com/honorglobal", "官方动态"),
        ("荣耀官网", "https://www.hihonor.com/cn/", "综合动态"),
    ],
    "三星相册": [
        ("Samsung Newsroom", "https://news.samsung.com/", "官方新闻"),
        ("Samsung Members", "https://r1.community.samsung.com/", "用户社区"),
        ("One UI 支持", "https://www.samsung.com/us/support/mobile-support/", "系统更新"),
        ("Reddit r/samsung", "https://www.reddit.com/r/samsung/", "用户反馈"),
    ],
}


def main():
    week = datetime.now().strftime("%Y-W%W")
    if "--week" in sys.argv:
        idx = sys.argv.index("--week")
        if idx + 1 < len(sys.argv):
            week = sys.argv[idx + 1]

    plan = {
        "week": week,
        "generated_at": datetime.now().isoformat(),
        "competitors": COMPETITORS,
    }

    print(json.dumps(plan, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
