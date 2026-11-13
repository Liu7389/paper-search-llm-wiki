---
id: keywords-boolean
title: 關鍵字、布林與萬用字元
sources: [S3, S4, S9]
---
# 關鍵字、布林與萬用字元

- 先列出同義詞、縮寫、拼法變化，以及詞庫（thesaurus）裡的標準用語。[S4]
- `AND` 縮小範圍、`OR` 擴大範圍、`NOT` 排除；括號可組合巢狀查詢。[S3]
- 用引號搜尋完整片語，例如 `"traffic signals"`。[S3]
- TRID 不會自動找單複數，要用 `*` 截字，例如 `sign*` 可找到 sign、signs、signals、signalization。[S3]
- 實測：在 OpenAlex 以全文搜尋 "hard shoulder running" 得 322 筆，前幾名多是離題的高引用論文；改成只搜標題後剩 63 筆，前 8 筆都切題。[S9]
- 結論：太寬時把詞限制在標題或摘要，太窄時加 OR 同義詞。[整理]

範例（路肩開放）：`("hard shoulder running" OR "temporary shoulder use" OR "part-time shoulder use") AND (capacity OR safety)`［整理，同義詞需在詞庫或結果中確認］
