# 竞品系统应用 — 信息源参考

> 配合 `web_fetch` 和 `web_search` 抓取各厂商系统应用动态。
> 本文件列出各厂商通用信息源（适用于各类系统应用分析）。
> 如需分析特定应用（如备忘录、设置），先用 `web_search` 搜索补充该应用的专属信息源。

## Apple

| 来源 | URL | 适用性 |
|------|-----|--------|
| Apple 新闻室 | https://www.apple.com/newsroom/ | 通用功能发布 |
| iOS/macOS 更新说明 | https://support.apple.com/en-us/HT201222 | 系统级应用更新 |
| MacRumors | https://www.macrumors.com/ | Apple 综合动态 |
| 9to5Mac | https://9to5mac.com/ | Apple 产品报道 |

> 💡 搜索示例：`"Apple {app_name}" site:macrumors.com` 或 `"Apple {app_name}" update site:9to5mac.com`

## Google

| 来源 | URL | 适用性 |
|------|-----|--------|
| Google Blog | https://blog.google/ | 官方产品动态 |
| Google Play | https://play.google.com/store/apps | 应用更新日志 |
| Android Authority | https://www.androidauthority.com/ | Android 生态报道 |
| 9to5Google | https://9to5google.com/ | Google 产品报道 |
| Reddit r/android | https://www.reddit.com/r/android/ | 用户反馈 |

> 💡 搜索示例：`"Google {app_name}" update site:9to5google.com`

## 华为 HarmonyOS

| 来源 | URL | 适用性 |
|------|-----|--------|
| 华为消费者官网 | https://consumer.huawei.com/cn/ | 产品动态 |
| HarmonyOS 更新 | https://consumer.huawei.com/cn/support/harmonyos/ | 系统版本更新 |
| 花粉俱乐部 | https://club.huawei.com/ | 用户反馈 |
| 华为终端微博 | https://weibo.com/huaweimobile | 官方动态 |

## 小米 HyperOS

| 来源 | URL | 适用性 |
|------|-----|--------|
| 小米社区 | https://www.xiaomi.cn/ | 用户反馈 |
| HyperOS | https://www.mi.com/hyperos | 系统更新 |
| 小米微博 | https://weibo.com/xiaomishub | 官方动态 |

## OPPO ColorOS

| 来源 | URL | 适用性 |
|------|-----|--------|
| OPPO 社区 | https://www.oppo.cn/community/ | 用户反馈 |
| ColorOS | https://www.coloros.com/ | 系统更新 |
| OPPO 微博 | https://weibo.com/oppo | 官方动态 |

## VIVO OriginOS

| 来源 | URL | 适用性 |
|------|-----|--------|
| VIVO 社区 | https://community.vivo.com.cn/ | 用户反馈 |
| OriginOS | https://www.vivo.com.cn/originos | 系统更新 |
| VIVO 微博 | https://weibo.com/vivo | 官方动态 |

## 荣耀 MagicOS

| 来源 | URL | 适用性 |
|------|-----|--------|
| 荣耀俱乐部 | https://club.hihonor.com/cn/ | 用户反馈 |
| MagicOS | https://www.hihonor.com/cn/magic/ | 系统更新 |
| 荣耀微博 | https://weibo.com/honorglobal | 官方动态 |
| 荣耀官网 | https://www.hihonor.com/cn/ | 综合动态 |

## 三星 One UI

| 来源 | URL | 适用性 |
|------|-----|--------|
| Samsung Newsroom | https://news.samsung.com/ | 官方新闻 |
| Samsung Members | https://r1.community.samsung.com/ | 用户社区 |
| One UI 支持 | https://www.samsung.com/us/support/mobile-support/ | 系统更新 |
| Reddit r/samsung | https://www.reddit.com/r/samsung/ | 用户反馈 |

---

## 补充搜索策略

如果 `references/competitor-sources.md` 未收录目标应用的具体信息源，执行以下搜索补充：

```
web_search: "{厂商名} {app_name} 更新 2026"
web_search: "{厂商名} {app_name} new feature"
web_search: "{厂商名} {app_name} 用户反馈"
```

每个厂商补充搜索 1–2 条，选取最相关的 URL 用于后续抓取。
