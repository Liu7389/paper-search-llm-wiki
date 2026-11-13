---
id: llm-wiki-method
title: LLM Wiki 方法
sources: [S1]
---
# 本 Wiki 怎麼建：LLM Wiki 方法

- LLM Wiki 讓 AI 在你和原始資料之間，持續維護一個互相連結的 Markdown Wiki，而不是每次提問都重新從原始文件找答案。[S1]
- 三層：原始資料（不可修改）、Wiki（AI 撰寫）、schema（規則檔，如 AGENTS.md）。[S1]
- 三個操作：Ingest（加入資料，可能更新多頁）、Query（對 Wiki 提問，好答案可存回成新頁）、Lint（檢查矛盾、過時說法、孤兒頁、缺少交叉連結）。[S1]
- index.md 是內容目錄，提問時先讀它；log.md 是只能追加的時間紀錄。[S1]
- 作者偏好一次 ingest 一篇並親自參與：讀摘要、檢查更新、決定重點。[S1]
