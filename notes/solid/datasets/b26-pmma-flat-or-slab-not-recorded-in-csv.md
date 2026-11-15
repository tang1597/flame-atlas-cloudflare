# PMMA / flat_or_slab / not_recorded_in_CSV

小資料集 ID：`b26-pmma-flat-or-slab-not-recorded-in-csv`

## 資料身份與範圍

| 項目 | 內容 |
| --- | --- |
| NASA investigation | [PSI-26](https://psi.nasa.gov/physci/repo/data/investigations/PSI-26) |
| 材料／配方 | PMMA |
| 幾何 | flat_or_slab |
| 實驗模式 | not_recorded_in_CSV |
| 證據角色 | 固體火焰核心資料 |
| 環境 | ISS 微重力／來源指定的地面比較；逐次氣氛與流況不由材料名補值 |
| 資料粒度／共享試片 | 26 筆來源紀錄；獨立燃燒次數未自動確認；a/b、重複sample與階段保持原身份。 |
| 可用數值 | index_and_related_source_cases_exact_trial_join_pending |

## 1. 文獻結果與視覺化程式

### B26-SLAB　B26-SLAB

**Burning and Suppression of Solids (BASS): An Overview of Recent ISS Results**

1cm寬flat acrylic例在約9cm/s可維持小火焰，最後風流關閉才在末影格熄滅；本例不能給無時延通用關風閥值。

- 證據身份：source_slide_observation。
- 文獻定位：bass-6e654a346857: physicalp54 +2014preheatingdeck。
- 使用數據部分：literature_locator: physicalp54 +2014preheatingdeck；trial_binding: Literaturecase/familyrelationonly; exactrawtrialtopanelbindingnotestablished；scope: 逐次索引為可用候選紀錄，不代表文獻使用其全部列。。
- 本組適用層級：本材料／幾何系列文獻結論；只有原文明寫Trial／圖板條件才直接適用。Literaturecase/familyrelationonly; exactrawtrialtopanelbindingnotestablished。
- 使用／控制因子：width_cm: 1；flow_approx_cm_s: 9；image_interval_s: 1.3。
- 來源限制：原文未給此圖rawtestID/厚度；不套到所有PMMAslab。。
- 搜尋句（改寫）：1cm寬flat acrylic例在約9cm/s可維持小火焰，最後風流關閉才在末影格熄滅；本例不能給無時延通用關風閥值。。
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
| B26-SLAB | 原表索引或相近來源案例；精確試次連結未決 | 可確認的材料與原紀錄身份列在逐次索引。 | 尚未取得多項可直接套用的結論；不製造第二個結論或衝突。 |

## 4. 消防洞見

| 類別 | 對應證據 | 數據支持的判斷 | 策略／產品構想 | 待驗證 |
| --- | --- | --- | --- | --- |
| 撲滅／抑制 | B26-SLAB | 指定案例降流後熄滅，但另有低流仍燃至燃料耗盡的來源；介入成效具材料與狀態依賴。 | 以火焰／熱反應回饋檢驗降流，而非採跨材料固定流速作停止條件。 | 同幾何、氧與熱歷史的流速介入試驗，區分耗盡與全局熄滅。 |
| 預防 | 尚未取得／不適用 | 尚未建立本組可直接支持此用途的數據結論。 | 先補對應資料與試次匹配，再決定可測試策略；此處是研究缺口。 | 需本組材料、幾何、操作歷史與對應端點的量測；相近系列不能代替。 |
| 偵測 | 尚未取得／不適用 | 尚未建立本組可直接支持此用途的數據結論。 | 先補對應資料與試次匹配，再決定可測試策略；此處是研究缺口。 | 需本組材料、幾何、操作歷史與對應端點的量測；相近系列不能代替。 |

## 逐次索引

| 原始檔／資料位置 | Trial／Run／列 | 共享身份與保留事項 |
| --- | --- | --- |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-26_BASS\Experimental table\PSI-26_Experimental table_BASS.csv | csv_row: 16；date: 5/11/2012；GMT: 132；test_number: 54；as_run: 15；sample: 21 | identity_notes: source_record_id: PSI-26-CSV-r16；raw_material: PMMA 2 cm；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: Date: 5/11/2012；GMT: 132；As Run Test #: 15；Test #: 54；Sample #: 21；Fuel Sample Material: PMMA 2 cm |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-26_BASS\Experimental table\PSI-26_Experimental table_BASS.csv | csv_row: 17；date: 5/11/2012；GMT: 132；test_number: 55；as_run: 16；sample: 21 | identity_notes: source_record_id: PSI-26-CSV-r17；raw_material: PMMA 2 cm；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: Date: 5/11/2012；GMT: 132；As Run Test #: 16；Test #: 55；Sample #: 21；Fuel Sample Material: PMMA 2 cm |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-26_BASS\Experimental table\PSI-26_Experimental table_BASS.csv | csv_row: 18；date: 5/11/2012；GMT: 132；test_number: 56；as_run: 17；sample: 21 | identity_notes: source_record_id: PSI-26-CSV-r18；raw_material: PMMA 2 cm；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: Date: 5/11/2012；GMT: 132；As Run Test #: 17；Test #: 56；Sample #: 21；Fuel Sample Material: PMMA 2 cm |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-26_BASS\Experimental table\PSI-26_Experimental table_BASS.csv | csv_row: 19；date: 5/11/2012；GMT: 132；test_number: 57；as_run: 18；sample: 21 | identity_notes: source_record_id: PSI-26-CSV-r19；raw_material: PMMA 2 cm；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: Date: 5/11/2012；GMT: 132；As Run Test #: 18；Test #: 57；Sample #: 21；Fuel Sample Material: PMMA 2 cm |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-26_BASS\Experimental table\PSI-26_Experimental table_BASS.csv | csv_row: 20；date: 5/11/2012；GMT: 132；test_number: 110；as_run: 19；sample: 21 | identity_notes: source_record_id: PSI-26-CSV-r20；raw_material: PMMA 2 cm；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: Date: 5/11/2012；GMT: 132；As Run Test #: 19；Test #: 110；Sample #: 21；Fuel Sample Material: PMMA 2 cm |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-26_BASS\Experimental table\PSI-26_Experimental table_BASS.csv | csv_row: 21；date: 6/5/2012；GMT: 157；test_number: 30；as_run: 20；sample: 15 | identity_notes: source_record_id: PSI-26-CSV-r21；raw_material: PMMA 1 cm；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: Date: 6/5/2012；GMT: 157；As Run Test #: 20；Test #: 30；Sample #: 15；Fuel Sample Material: PMMA 1 cm |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-26_BASS\Experimental table\PSI-26_Experimental table_BASS.csv | csv_row: 22；date: 6/5/2012；GMT: 157；test_number: 31；as_run: 21；sample: 15 | identity_notes: source_record_id: PSI-26-CSV-r22；raw_material: PMMA 1 cm；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: Date: 6/5/2012；GMT: 157；As Run Test #: 21；Test #: 31；Sample #: 15；Fuel Sample Material: PMMA 1 cm |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-26_BASS\Experimental table\PSI-26_Experimental table_BASS.csv | csv_row: 23；date: 6/5/2012；GMT: 157；test_number: 32；as_run: 22；sample: 15 | identity_notes: source_record_id: PSI-26-CSV-r23；raw_material: PMMA 1 cm；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: Date: 6/5/2012；GMT: 157；As Run Test #: 22；Test #: 32；Sample #: 15；Fuel Sample Material: PMMA 1 cm |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-26_BASS\Experimental table\PSI-26_Experimental table_BASS.csv | csv_row: 24；date: 6/5/2012；GMT: 157；test_number: 33；as_run: 23；sample: 15 | identity_notes: source_record_id: PSI-26-CSV-r24；raw_material: PMMA 1 cm；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: Date: 6/5/2012；GMT: 157；As Run Test #: 23；Test #: 33；Sample #: 15；Fuel Sample Material: PMMA 1 cm |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-26_BASS\Experimental table\PSI-26_Experimental table_BASS.csv | csv_row: 41；date: 6/28/2012；GMT: 180；test_number: 66；as_run: 39；sample: 33 | identity_notes: source_record_id: PSI-26-CSV-r41；raw_material: PMMA slab；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: Date: 6/28/2012；GMT: 180；As Run Test #: 39；Test #: 66；Sample #: 33；Fuel Sample Material: PMMA slab |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-26_BASS\Experimental table\PSI-26_Experimental table_BASS.csv | csv_row: 42；date: 6/28/2012；GMT: 180；test_number: 67；as_run: 40；sample: 33 | identity_notes: source_record_id: PSI-26-CSV-r42；raw_material: PMMA slab；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: Date: 6/28/2012；GMT: 180；As Run Test #: 40；Test #: 67；Sample #: 33；Fuel Sample Material: PMMA slab |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-26_BASS\Experimental table\PSI-26_Experimental table_BASS.csv | csv_row: 51；date: 7/3/2012；GMT: 185；test_number: 68；as_run: 49；sample: 33 | identity_notes: source_record_id: PSI-26-CSV-r51；raw_material: pmma slab；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: Date: 7/3/2012；GMT: 185；As Run Test #: 49；Test #: 68；Sample #: 33；Fuel Sample Material: pmma slab |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-26_BASS\Experimental table\PSI-26_Experimental table_BASS.csv | csv_row: 52；date: 7/12/2012；GMT: 194；test_number: 69；as_run: 50；sample: 33 | identity_notes: source_record_id: PSI-26-CSV-r52；raw_material: pmma slab；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: Date: 7/12/2012；GMT: 194；As Run Test #: 50；Test #: 69；Sample #: 33；Fuel Sample Material: pmma slab |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-26_BASS\Experimental table\PSI-26_Experimental table_BASS.csv | csv_row: 79；date: 8/21/2012；GMT: 234；test_number: 70；as_run: 76；sample: 34 | identity_notes: source_record_id: PSI-26-CSV-r79；raw_material: PMMA slab；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: Date: 8/21/2012；GMT: 234；As Run Test #: 76；Test #: 70；Sample #: 34；Fuel Sample Material: PMMA slab |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-26_BASS\Experimental table\PSI-26_Experimental table_BASS.csv | csv_row: 80；date: 8/21/2012；GMT: 234；test_number: 71；as_run: 77；sample: 34 | identity_notes: source_record_id: PSI-26-CSV-r80；raw_material: PMMA slab；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: Date: 8/21/2012；GMT: 234；As Run Test #: 77；Test #: 71；Sample #: 34；Fuel Sample Material: PMMA slab |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-26_BASS\Experimental table\PSI-26_Experimental table_BASS.csv | csv_row: 83；date: 4/5/2013；GMT: 95；test_number: 98；as_run: 80；sample: 24 | identity_notes: source_record_id: PSI-26-CSV-r83；raw_material: PMMA 2 cm；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: Date: 4/5/2013；GMT: 95；As Run Test #: 80；Test #: 98；Sample #: 24；Fuel Sample Material: PMMA 2 cm |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-26_BASS\Experimental table\PSI-26_Experimental table_BASS.csv | csv_row: 84；date: 4/5/2013；GMT: 95；test_number: 99；as_run: 81；sample: 24 | identity_notes: source_record_id: PSI-26-CSV-r84；raw_material: PMMA 2 cm；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: Date: 4/5/2013；GMT: 95；As Run Test #: 81；Test #: 99；Sample #: 24；Fuel Sample Material: PMMA 2 cm |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-26_BASS\Experimental table\PSI-26_Experimental table_BASS.csv | csv_row: 85；date: 4/9/2013；GMT: 99；test_number: 114；as_run: 82；sample: 25 | identity_notes: source_record_id: PSI-26-CSV-r85；raw_material: PMMA 2 cm；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: Date: 4/9/2013；GMT: 99；As Run Test #: 82；Test #: 114；Sample #: 25；Fuel Sample Material: PMMA 2 cm |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-26_BASS\Experimental table\PSI-26_Experimental table_BASS.csv | csv_row: 86；date: 4/9/2013；GMT: 99；test_number: 115；as_run: 83；sample: 25 | identity_notes: source_record_id: PSI-26-CSV-r86；raw_material: pmma 2 cm；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: Date: 4/9/2013；GMT: 99；As Run Test #: 83；Test #: 115；Sample #: 25；Fuel Sample Material: pmma 2 cm |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-26_BASS\Experimental table\PSI-26_Experimental table_BASS.csv | csv_row: 87；date: 4/9/2013；GMT: 99；test_number: 116；as_run: 84；sample: 25 | identity_notes: source_record_id: PSI-26-CSV-r87；raw_material: pmma 2 cm；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: Date: 4/9/2013；GMT: 99；As Run Test #: 84；Test #: 116；Sample #: 25；Fuel Sample Material: pmma 2 cm |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-26_BASS\Experimental table\PSI-26_Experimental table_BASS.csv | csv_row: 88；date: 4/9/2013；GMT: 99；test_number: 117；as_run: 85；sample: 25 | identity_notes: source_record_id: PSI-26-CSV-r88；raw_material: pmma 2 cm；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: Date: 4/9/2013；GMT: 99；As Run Test #: 85；Test #: 117；Sample #: 25；Fuel Sample Material: pmma 2 cm |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-26_BASS\Experimental table\PSI-26_Experimental table_BASS.csv | csv_row: 89；date: 4/9/2013；GMT: 99；test_number: 117a；as_run: 85；sample: 25 | identity_notes: source_record_id: PSI-26-CSV-r89；raw_material: pmma 2 cm；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: Date: 4/9/2013；GMT: 99；As Run Test #: 85；Test #: 117a；Sample #: 25；Fuel Sample Material: pmma 2 cm |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-26_BASS\Experimental table\PSI-26_Experimental table_BASS.csv | csv_row: 90；date: 4/12/2013；GMT: 102；test_number: 100；as_run: 86；sample: 24 | identity_notes: source_record_id: PSI-26-CSV-r90；raw_material: pmma 2 cm；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: Date: 4/12/2013；GMT: 102；As Run Test #: 86；Test #: 100；Sample #: 24；Fuel Sample Material: pmma 2 cm |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-26_BASS\Experimental table\PSI-26_Experimental table_BASS.csv | csv_row: 93；date: 4/16/2013；GMT: 106；test_number: 26；as_run: 89；sample: 17 | identity_notes: source_record_id: PSI-26-CSV-r93；raw_material: pmma 1 cm；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: Date: 4/16/2013；GMT: 106；As Run Test #: 89；Test #: 26；Sample #: 17；Fuel Sample Material: pmma 1 cm |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-26_BASS\Experimental table\PSI-26_Experimental table_BASS.csv | csv_row: 94；date: 4/16/2013；GMT: 106；test_number: 27；as_run: 90；sample: 17 | identity_notes: source_record_id: PSI-26-CSV-r94；raw_material: pmma 1 cm；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: Date: 4/16/2013；GMT: 106；As Run Test #: 90；Test #: 27；Sample #: 17；Fuel Sample Material: pmma 1 cm |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-26_BASS\Experimental table\PSI-26_Experimental table_BASS.csv | csv_row: 95；date: 4/16/2013；GMT: 106；test_number: 28；as_run: 91；sample: 17 | identity_notes: source_record_id: PSI-26-CSV-r95；raw_material: pmma 1 cm；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: Date: 4/16/2013；GMT: 106；As Run Test #: 91；Test #: 28；Sample #: 17；Fuel Sample Material: pmma 1 cm |

## 缺件與適用範圍

- 不足兩項有來源結論；多結論比較尚未完成，不以目的或推測湊數。
- 來源圖例有同族材料結果，但未找到逐圖/逐試次join；不把圖上O2/流速貼到所有索引record。
- 未支援的第二條結論明列缺口；rawCSV只有date/GMT/Test/AsRun/Sample/material。
