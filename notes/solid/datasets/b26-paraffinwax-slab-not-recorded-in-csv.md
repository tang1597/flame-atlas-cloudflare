# paraffinwax / slab / not_recorded_in_CSV

小資料集 ID：`b26-paraffinwax-slab-not-recorded-in-csv`

## 資料身份與範圍

| 項目 | 內容 |
| --- | --- |
| NASA investigation | [PSI-26](https://psi.nasa.gov/physci/repo/data/investigations/PSI-26) |
| 材料／配方 | paraffinwax |
| 幾何 | slab |
| 實驗模式 | not_recorded_in_CSV |
| 證據角色 | 固體火焰核心資料 |
| 環境 | ISS 微重力／來源指定的地面比較；逐次氣氛與流況不由材料名補值 |
| 資料粒度／共享試片 | 3 筆來源紀錄；獨立燃燒次數未自動確認；a/b、重複sample與階段保持原身份。 |
| 可用數值 | index_and_related_source_cases_exact_trial_join_pending |

## 1. 文獻結果與視覺化程式

### B26-WAX　B26-WAX

**Burning and Suppression of Solids (BASS): An Overview of Recent ISS Results**

Japanwax/candle圖例17%O2、低於1cm/s仍可見火焰；末流量關閉後熄滅。相鄰頁屬各自sourcecase，不將幾何/化學不明的candle欄自動補Japanwax。

- 證據身份：source_slide_observation。
- 文獻定位：bass-6e654a346857: physicalpp59-61。
- 使用數據部分：literature_locator: physicalpp59-61；trial_binding: Literaturecase/familyrelationonly; exactrawtrialtopanelbindingnotestablished；scope: 逐次索引為可用候選紀錄，不代表文獻使用其全部列。。
- 本組適用層級：本材料／幾何系列文獻結論；只有原文明寫Trial／圖板條件才直接適用。Literaturecase/familyrelationonly; exactrawtrialtopanelbindingnotestablished。
- 使用／控制因子：source_O2_percent: 17；source_low_flow_cm_s: <1；p59_image_interval_approx_s: 9。
- 來源限制：缺逐試次rawjoin及熔蠟成分/溫度；不推所有蠟/飛滴抑制效果。。
- 搜尋句（改寫）：Japanwax/candle圖例17%O2、低於1cm/s仍可見火焰；末流量關閉後熄滅。相鄰頁屬各自sourcecase，不將幾何/化學不明的candle欄自動補Japanwax。。
- 來源：https://psi.ndc.nasa.gov/mpglobal/api/athena/file/70383/?inline=1&log=1
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/簡報與海報/第一批下載/PSI-26_BASS/Presentations/PSI-26_Presentations_BASS_Overview of Recent ISS Results.pdf>)

尚未取得可逐項對照的紀錄。

## 2. 使用資料與參數總表的因子對照

| 總表原分類 | 來源身份 | 原欄名單位 | 原欄名例 | 總表定位 |
| --- | --- | --- | --- | --- |
| 尺寸／幾何 | 裝置或樣本條件 | 未由欄名確認 | MM)；ImageWidth | '物理參數'!A146:K146 |
| 影像／光譜設定 | 儀器設定或影像座標 | 未由欄名確認 | AF-S DX Zoom-Nikkor 12-24mm f/4G IF-ED or Tokina AT-X 124 AF PRO DX II (AF 12-24mm f/4)；ColorSpace；HistorySoftwareAgent : Adobe Photoshop Camera Raw 8.1；Adobe Photoshop Camera Raw 8.1 (Windows)；ColorComponents | '物理參數'!A147:K147 |

以上是該 investigation 的欄位盤點；個別結論實際使用的因子以第1節與下列補充為準。

| 本組實際因子 | 總表定位／未列欄位 | 文獻中的用途 |
| --- | --- | --- |
| 材料／配方／幾何 | '實驗總覽'!E13 | 文獻選樣身份；逐次厚度、支撐與歷史另由原文補齊 |
| 環境／流向／重力 | '實驗總覽'!F13 | 環境摘要，非本組全部逐次聯合條件 |
| 尺寸／幾何 / MM)；ImageWidth | '物理參數'!G146 | 是否為模型輸入、控制條件或量測輸出，依第1節文獻定位逐項核對 |
| 厚度、支撐、前緣位置／延燒速度與熱物性 | 需文獻／原始影像補欄位；本總表未提供全部閉合數值 | 選擇薄片／厚板／棒模型並核對同一observable |

| 文獻因子／疑點 | 正確讀法或需補資料 |
| --- | --- |
| 需補因子 | 燃料厚度/寬度/直徑、燒面/backing、模式、點火/預熱歷史需由原文/原始表逐項補；workbook不是完整聯合試驗條件。 |

## 3. 共用資料的多項結論比較

| 結論／文獻 | 資料重疊身份 | 共同處 | 不同處／不能合併之處 |
| --- | --- | --- | --- |
| B26-WAX | 原表索引或相近來源案例；精確試次連結未決 | 可確認的材料與原紀錄身份列在逐次索引。 | 尚未取得多項可直接套用的結論；不製造第二個結論或衝突。 |

## 4. 消防洞見

| 類別 | 對應證據 | 數據支持的判斷 | 策略／產品構想 | 待驗證 |
| --- | --- | --- | --- | --- |
| 撲滅／抑制 | B26-WAX | 指定案例降流後熄滅，但另有低流仍燃至燃料耗盡的來源；介入成效具材料與狀態依賴。 | 以火焰／熱反應回饋檢驗降流，而非採跨材料固定流速作停止條件。 | 同幾何、氧與熱歷史的流速介入試驗，區分耗盡與全局熄滅。 |
| 預防 | 尚未取得／不適用 | 尚未建立本組可直接支持此用途的數據結論。 | 先補對應資料與試次匹配，再決定可測試策略；此處是研究缺口。 | 需本組材料、幾何、操作歷史與對應端點的量測；相近系列不能代替。 |
| 偵測 | 尚未取得／不適用 | 尚未建立本組可直接支持此用途的數據結論。 | 先補對應資料與試次匹配，再決定可測試策略；此處是研究缺口。 | 需本組材料、幾何、操作歷史與對應端點的量測；相近系列不能代替。 |

## 逐次索引

| 原始檔／資料位置 | Trial／Run／列 | 共享身份與保留事項 |
| --- | --- | --- |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-26_BASS\Experimental table\PSI-26_Experimental table_BASS.csv | csv_row: 81；date: 8/21/2012；GMT: 234；test_number: 74；as_run: 78；sample: 41 | identity_notes: source_record_id: PSI-26-CSV-r81；raw_material: paraffin wax slab；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: Date: 8/21/2012；GMT: 234；As Run Test #: 78；Test #: 74；Sample #: 41；Fuel Sample Material: paraffin wax slab |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-26_BASS\Experimental table\PSI-26_Experimental table_BASS.csv | csv_row: 82；date: 8/21/2012；GMT: 234；test_number: 75；as_run: 79；sample: 41 | identity_notes: source_record_id: PSI-26-CSV-r82；raw_material: parrafin wax slab；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: Date: 8/21/2012；GMT: 234；As Run Test #: 79；Test #: 75；Sample #: 41；Fuel Sample Material: parrafin wax slab |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-26_BASS\Experimental table\PSI-26_Experimental table_BASS.csv | csv_row: 110；date: 5/2/2013；GMT: 122；test_number: 78；as_run: 103；sample: 42 | identity_notes: source_record_id: PSI-26-CSV-r110；raw_material: paraffin wax slab；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: Date: 5/2/2013；GMT: 122；As Run Test #: 103；Test #: 78；Sample #: 42；Fuel Sample Material: paraffin wax slab |

## 缺件與適用範圍

- 不足兩項有來源結論；多結論比較尚未完成，不以目的或推測湊數。
- 來源圖例有同族材料結果，但未找到逐圖/逐試次join；不把圖上O2/流速貼到所有索引record。
- 未支援的第二條結論明列缺口；rawCSV只有date/GMT/Test/AsRun/Sample/material。
