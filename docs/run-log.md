# 實際執行與檢查紀錄（第 1 次完整執行，2026-11-13）

執行者：Claude（AI）＋ Michael（討論與確認）。工具：WebSearch / WebFetch、Python（scripts/build.py、scripts/check.py）。

## A. 討論（人）
| # | 內容 | 結果 |
|---|---|---|
| A1 | AI 提三個主題 | 使用者改選「找指定領域論文」 |
| A2 | AI 提示範領域「交通工程」 | 同意，另要求加本科系示範 |
| A3 | 本科系 = 人工智慧碩士班 | 第二個示範領域定為 AI（以 RAG 為例，銜接第七週作業） |
| A4 | 使用者看過第一版後要求：改抓頂會論文，每篇必須附網址 | 拿掉 NDLTD 人工查詢；交通改用 TRB 年會／TRR |
| A5 | 使用者補充：AI 包含影像辨識、IR、LLM、網路、資安、RAG、Agent、量子 | 新增「怎麼判斷頂會」頁，每個子領域各找頂會論文 |

## B. 取得 → Ingest（每篇資料各跑一次）
| # | 節點 | 發生什麼 | 處理 |
|---|---|---|---|
| B1 | 取得 | 國圖原始 PDF（ref.ncl.edu.tw）被 robots 擋下 | 改用華梵大學轉載的國圖簡報（S7） |
| B2 | 核對 | S7 是 2013 年資料，收錄筆數已過時 | Wiki 只寫收錄範圍，不寫筆數，並在頁面註明 |
| B3 | 取得/核對 | 檔名 `ESEM___Snowballing.pdf`，原以為是 Wohlin 的滾雪球指引，讀完發現是 Felizardo 等人的另一篇論文 | 用 OpenAlex 以 DOI 10.1145/2601248.2601268 核對 Wohlin 書目，拆成 S5（Wohlin）、S6（Felizardo） |
| B4 | 整理 | 想寫「Google Scholar 可用 allintitle: 搜標題」，但官方說明沒把它列為技巧 | 不寫進 Wiki |
| B5 | 整理 | TRID 收錄筆數：S3 沒寫，S4 寫逾 130 萬筆 | 該句改標 S4 |
| B6 | 取得 | curl 直連 OpenAlex 被代理擋；data.gov.tw（運研所資料集）被 robots 擋 | OpenAlex 改用 WebFetch；運研所資料放棄，不湊數 |
| B8 | 核對 | arXiv API 手冊（S10）沒有提到是否同儕審查，不能用它支撐「arXiv 不經同儕審查」 | 另外 ingest arXiv 審核政策頁（S11），原文明說審核不是同儕審查 |
| B9 | 整理 | OpenAlex 的 RAG 結果中，2020 原始論文出現兩筆（arXiv DOI 與無 DOI） | 寫進 Wiki 當教學重點：預印本與正式版要合併 |
| B10 | 取得 | dblp.org 被 Anubis 機器人防護擋下 | 放棄，不湊數 |
| B11 | 取得 | CORE 排名網站：ACL、EMNLP、CVPR、AAMAS、QCE 頁取得成功，SIGIR、SIGCOMM、IEEE S&P、NeurIPS、AAAI 頁被 robots 擋下 | 這幾個會議改用 CSRankings 與 WSU 清單佐證，沒取得的 CORE 等級一律不寫 |
| B12 | 核對網址 | NeurIPS 論文的 DOI（10.52202）導向 Curran 代售頁，不是官方論文頁 | 改用 proceedings.neurips.cc 官方網址 |
| B13 | 核對網址 | AAMAS 論文 DOI 前綴 10.65109 少見 | 用 doi.org handle API 確認導向 ACM Digital Library |
| B14 | 整理 | SIGCOMM 第一名在 OpenAlex 只有標題「Swift」，資料不完整 | 不採用，改用標題完整的第 2、3 名 |
| B15 | 整理 | 量子：CSRankings 與 WSU 清單都沒有量子領域，IEEE QCE 在 ICORE2026 只是 National/Regional | 明寫「量子沒有公認的資訊類頂會」，改用 NeurIPS 的量子機器學習論文示範 |
| B7 | 整理 | demo 頁寫「前 8 筆只有 1 筆標題直接相關」，自我審查時發現不精確（沒有一筆標題含該詞） | 改寫為「沒有一筆標題含 hard shoulder running，只有 1 篇主題相近」 |

## C. 自動檢查（scripts/check.py）
| 輪次 | 結果 | 問題 | 修正 |
|---|---|---|---|
| 1 | 3 ERROR、2 WARN | 練習題投影片掛在 six-steps 頁，但用了 S2、S3（該頁沒有）；投影片自己寫了「5,000 筆」，Wiki 沒有這個數字；demo 頁 frontmatter 列了沒用到的 S2 | 把練習題做成 Wiki 新頁 `practice`（Query 結果存回 Wiki），刪掉 5,000，清 frontmatter |
| 2 | 1 ERROR | practice 頁說明句沒有來源標記 | 標 `[整理]` |
| 3 | 通過，1 WARN | 人工發現投影片寫「Wiki 11 頁」，新增 practice 後實際 12 頁，但檢查程式沒抓到 | 改成 12，並在 check.py 新增「份數/頁數要等於實際數量」規則；用 11 頁測試確認會報錯 |
| 4 | 通過，1 WARN | NDLTD 中文查詢需人工操作（容器連不到） | 保留為待辦 |
| 5 | 2 ERROR | 加入 AI 領域（S10–S12、arxiv、demo-ai）後，第 3 輪新增的規則抓到投影片仍寫「9 份資料、12 頁」 | 改為 12 份、14 頁，並新增 2 張 AI 投影片 |
| 6 | 通過，1 WARN | 人工複查發現投影片寫了「Lewis 等人」，Wiki 沒有作者名；數字檢查抓不到人名 | 刪除人名；記入反思（人名、專有名詞仍靠人工檢查） |

| 7 | 1 ERROR、1 WARN | 新增「示範頁的論文必須有網址」規則後，抓到交通示範提到一篇無 DOI 的論文；S15 只用在表格裡，檢查程式沒算到 | 改寫該句不列論文名；check.py 改為表格中的來源也算使用 |
| 8 | 通過 | — | — |

## D. 預覽
- D1 用 Chromium 開啟簡報，桌機與手機寬度截圖檢查（見 docs/screenshots/）。
- D2 發布到 GitHub Pages 後逐頁打開，發現 Wiki 索引頁的表格沒有輸出（build.py 遇到頁面最後一行是表格時沒輸出）→ 修正並重新發布，確認 15 列都出現。

## 統計
- 原始資料 18 份（≥5）；Wiki 15 個內容頁＋index＋log；投影片 17 張，每張都對應 1 個 Wiki 頁與來源；示範論文 20 篇，每篇都有網址。
- 錯誤最多的節點：取得/Ingest 與核對（B1–B3、B6、B8、B10–B13 共 10 次），其次是產生投影片（C1 兩項、C3、C5、C6）。
