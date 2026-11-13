# AGENTS.md — 論文搜尋 LLM Wiki 的維護規則（schema）

依 Karpathy LLM Wiki 的三層架構 [S1]：
- `raw/`：原始資料。只讀不改。每篇登記在 `raw/sources.json`（id、標題、作者/單位、網址、存取日、限制）。
- `wiki/`：由 AI 撰寫、人審核的 Markdown 頁面。
- 本檔：規則。

## 先討論、後生成
1. Ingest 一篇資料前，先列出「這篇要補哪幾頁、要寫哪幾個重點、有什麼疑慮」，給人確認。
2. 人同意後才寫入 wiki 頁面，並在 `wiki/log.md` 追加一行紀錄。

## 寫作規則
- 每一條事實句尾必須有來源標記，例如 `[S3]`；沒有來源的句子只能是「本 Wiki 整理」並標 `[整理]`。
- 數字（筆數、年份、引用數）必須能在來源原文找到；來源過時要在頁面寫明，不可當成現況。
- **Ingest 先核對身分**：寫內容前先核對來源的標題、作者、日期與網址是否一致（本規則於第一次執行後加入，見 docs/run-log.md）。
- 不確定的內容標 `【待查證】`，不可寫成定論。
- 每頁 frontmatter：`id`、`title`、`sources`。

## 簡報規則
- 每張投影片 `data-wiki` 指向一個 wiki 頁 id，頁尾顯示來源 S 編號。
- 投影片不可出現 wiki 沒有的新事實。

## 檢查（scripts/check.py）
- 每頁每條事實句有 `[S#]` 或 `[整理]`；S 編號存在於 sources.json。
- 每張投影片的 `data-wiki` 存在；投影片的 S 編號是該 wiki 頁 sources 的子集合。
- index.md 列出所有頁面，沒有孤兒頁。
