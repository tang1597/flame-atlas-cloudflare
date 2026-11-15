# 液態燃燒證據包：閱讀入口

本輪將液滴資料、相關模型與原始文獻整理為可追溯的研究材料，支援載人環境的防火、偵測與抑制洞見。隔離液滴的結論不能直接轉成噴霧、油池、燃料管線或載人艙操作規範。正式habitat atlas沒有在本輪改動。

## 本輪四項交付

1. **盤點並逐子集提供Markdown**：保留來源燃料、配置、試次識別、變因、量測、單位與缺件。
2. **整理論文、報告、簡報及海報覆蓋**：追到作者結論、公式及原圖；缺全文、只讀摘要和版本不同都明記。
3. **比較共同與不同的消防意義**：區分共享資料、同類架構與不同實驗，連到預防／偵測／抑制及待驗證構想。
4. **提供物理式與實驗對照工具**：列明來源碼名稱、係數來源、模型及觀測目標，分開既有模型輸出重播與獨立預測。

這是本輪需求的交付結構，不是把NASA題目的選做事項改寫為強制條款。[共用題目依據](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/docs/challenge/SHARED_CHALLENGE_BRIEF.md>)另說明NASA核心、選做項與使用者加強方向。

## 先選閱讀路線

| 文件 | 回答什麼 |
|---|---|
| [01 文獻與原始結論](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/markdown/01_LITERATURE_AND_CONCLUSIONS.md>) | 哪份文件、讀到哪頁、與哪些資料相連 |
| [02 跨資料集消防洞見](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/markdown/02_CROSS_DATASET_FIRE_SAFETY.md>) | 哪些共通、哪些不能合併、構想還缺什麼驗證 |
| [03 公式與視覺化](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/markdown/03_EQUATIONS_AND_VISUALIZATION.md>) | 公式目標、係數來源、如何比較來源曲線 |
| [子集總盤點](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/data_inventory/liquid_subdatasets.json>) | stable IDs、來源位置、列號、SHA及52個navigation leaves |
| [因子字典](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/data_inventory/factor_dictionary.json>)／[Excel對照](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/data_inventory/factor_crosswalk.md>) | 操縱、設定、應變、來源分析與模型量的候選對應 |

## 不同分母不可相加

| 分母 | 數量 | 單位與限制 |
|---|---:|---|
| 來源standardized.csv全表 |2,225|207欄；不是2,225次液滴燃燒|
| 本輪液態摘要列 |564|FLEX274 Test摘要＋CFI226 Test摘要＋FLEX2 64 Fuel configuration|
| Test摘要列 |500|499個investigation/test-ID鍵；193F001兩列不同結果，仍未驗證獨立burn數|
| 核心燃料群／明列核心子集 |14／22|燃料依明示氣氛選項分支；不是新增試驗|
| PSI117來源表／linked branches |9／22|5份PROCI＋4份MST2024；按表×燃料×實驗/模型角色分支|
| PSI142相關葉節點 |8|地面counterflow/premixed data-ID工作表；不是8個液滴燃燒|
| navigation leaves |22＋22＋8=52|閱讀組織粒度，不是52個獨立campaign或burn|
| FLEX/FLEX2 metadata書目 |99條／61群組|51＋48原條目；exact DOI/title查找群組，不是61個實驗|
| FLEX/FLEX2審讀卡／非raw文件 |16／20|16卡＝15本機選頁＋1出版社索引；20文件含規格/圖紙/資料說明，兩者有重疊|
| CFI/相關文獻卡 |23|含同源版本、metadata、規劃、摘要及詳讀；不能與16卡相加成獨立文獻或試驗數|

FLEX2來源8燃料列展開為64氧/氣氛配置選項（4個O2值×2氣氛）。缺逐次run-ID與Y時，不能稱64筆可訓練配對。FLEX2015報告284 tests與現274摘要、CFI舊227與本輪226列、FLEX2舊DoD40群組屬不同來源母體，尚未完整調和。

## 原始資料與索引

原始payload使用active分享包；標準摘要和使用者Excel是明示參考輸入，不取代原始實驗來源。原始檔未修改、未重算。

- [standardized.csv](<C:/Users/User/Downloads/standardized.csv>)；SHA256 0f8a7644a9506305b050cb38a0c4868f33abf2fbb6d074721befbe508954fc6d。
- [檔案來源與分類索引.json](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/來源與缺件紀錄/檔案來源與分類索引.json>)；SHA256 a127404ccb0637b0e94114c341b44f54f110e2dea450040c9d8ebeef2fbc03ab。
- [architecture_inventory.json](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/flame_geometry_ml_20261114/inventory/architecture_inventory.json>)；SHA256 b33d8797da293b829907948a9c8dcae1ecb25a0e04c1f3fc45fab0c908405e78。
- [使用者Excel參照](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/data_inventory/workbook_reference.json>)：四工作表結構、127列液態/相關模型欄位對照；原Excel路徑及SHA在內。
- [離線來源曲線](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/data_inventory/visualization_data.json>) → [準備後視覺化資料](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/visualization_view.json>)；數值與原始路徑留離線，不上傳Git。

## 完成範圍

本次沒有新訓練、係數擬合、原作者CFD求解器執行或正式demo改版。物理式須來源條件/參數齊備才可正向求值；來源K重建屬同源診斷。**單位未核對的曲線不畫物理比較圖，原始數值仍可展開查閱。**

- [FLEX/FLEX2完整書目與卡](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/literature/flex_flex2_literature.json>)；[FLEX搜尋紀錄](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/literature/search_log.json>)。
- [CFI/PSI117文獻卡與公式](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/literature/cfi_literature.json>)；[CFI審讀摘要](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/literature/cfi_review.md>)；[CFI搜尋紀錄](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/literature/cfi_search_log.json>)。
- [67條PSI117 series單位審查](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/literature/unit_audit.json>)。
- [獨立物理與視覺化QA](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/qa/independent_physics_visualization_review.json>)：最終狀態以綁定SHA為準，測試通過不替代來源審核。

## 逐子資料集入口

[04_SUBDATASET_INDEX.md：52份來源葉節點](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/markdown/04_SUBDATASET_INDEX.md>)列出22個core、22個PSI117分支及8個related工作表的實際Markdown連結。
