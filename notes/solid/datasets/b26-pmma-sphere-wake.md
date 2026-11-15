# PMMA / sphere / wake

小資料集 ID：`b26-pmma-sphere-wake`

## 資料身份與範圍

| 項目 | 內容 |
| --- | --- |
| NASA investigation | [PSI-26](https://psi.nasa.gov/physci/repo/data/investigations/PSI-26) |
| 材料／配方 | PMMA |
| 幾何 | sphere |
| 實驗模式 | wake |
| 證據角色 | 固體火焰核心資料 |
| 環境 | ISS 微重力／來源指定的地面比較；逐次氣氛與流況不由材料名補值 |
| 資料粒度／共享試片 | 6 筆來源紀錄；獨立燃燒次數未自動確認；a/b、重複sample與階段保持原身份。 |
| 可用數值 | index_and_related_source_cases_exact_trial_join_pending |

## 1. 文獻結果與視覺化程式

### B26-PMMA-SPHERE-N2　B26-PMMA-SPHERE-N2

**Burning and Suppression of Solids (BASS): An Overview of Recent ISS Results**

PMMA球尾流例供入500cc/minN2只變弱未熄，停止N2後頁面標示熄滅；不得把p56的15mm/17%O2/1atm條件移到p57。

- 證據身份：source_slide_observation。
- 文獻定位：bass-6e654a346857: physicalp57; distinctadjacentp56。
- 使用數據部分：literature_locator: physicalp57; distinctadjacentp56；trial_binding: Literaturecase/familyrelationonly; exactrawtrialtopanelbindingnotestablished；scope: 逐次索引為可用候選紀錄，不代表文獻使用其全部列。。
- 本組適用層級：本材料／幾何系列文獻結論；只有原文明寫Trial／圖板條件才直接適用。Literaturecase/familyrelationonly; exactrawtrialtopanelbindingnotestablished。
- 使用／控制因子：p57_N2_flow_cc_min: 500。
- 來源限制：p57確切trialID、噴嘴位置、局部O2及流量參考狀態未閉合。。
- 搜尋句（改寫）：PMMA球尾流例供入500cc/minN2只變弱未熄，停止N2後頁面標示熄滅；不得把p56的15mm/17%O2/1atm條件移到p57。。
- 來源：https://psi.ndc.nasa.gov/mpglobal/api/athena/file/70383/?inline=1&log=1
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/簡報與海報/第一批下載/PSI-26_BASS/Presentations/PSI-26_Presentations_BASS_Overview of Recent ISS Results.pdf>)

### B26-JET-INTERPRETATION　B26-JET-INTERPRETATION

**Combustion, Complex Fluids, and Fluid Physics Experiments on the ISS**

作者報告局部N2jet可吹離stagnation區而wake仍燃，並將維持火焰解釋為捲入周圍空氣；屬早期overview與作者解釋，不是已量得localO2場。

- 證據身份：source_author_interpretation。
- 文獻定位：bass-3a6b661af9a9: physicalp13BASSpanel。
- 使用數據部分：literature_locator: physicalp13BASSpanel；trial_binding: Literaturecase/familyrelationonly; exactrawtrialtopanelbindingnotestablished；scope: 逐次索引為可用候選紀錄，不代表文獻使用其全部列。。
- 本組適用層級：本材料／幾何系列文獻結論；只有原文明寫Trial／圖板條件才直接適用。Literaturecase/familyrelationonly; exactrawtrialtopanelbindingnotestablished。
- 使用／控制因子：。
- 來源限制：不可直接與FLEX45%預混條件比較藥效或有人艙用量。。
- 搜尋句（改寫）：作者報告局部N2jet可吹離stagnation區而wake仍燃，並將維持火焰解釋為捲入周圍空氣；屬早期overview與作者解釋，不是已量得localO2場。。
- 來源：https://ntrs.nasa.gov/citations/20130000582
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/solid_combustion_evidence_20261115/bass_sources/downloads/20130000582.pdf>)

### B26-SPHERE-GEOMETRY　B26-SPHERE-GEOMETRY

**Burning and Suppression of Solids (BASS): An Overview of Recent ISS Results**

圖例分別有2cm球17%O2/12cm/s、1cm球17%O2/<1cm/s，另p56為15mm initialdiameter例；條件分屬各panel。

- 證據身份：source_case_conditions。
- 文獻定位：bass-6e654a346857: physicalpp34/36 and56。
- 使用數據部分：literature_locator: physicalpp34/36 and56；trial_binding: Literaturecase/familyrelationonly; exactrawtrialtopanelbindingnotestablished；scope: 逐次索引為可用候選紀錄，不代表文獻使用其全部列。。
- 本組適用層級：本材料／幾何系列文獻結論；只有原文明寫Trial／圖板條件才直接適用。Literaturecase/familyrelationonly; exactrawtrialtopanelbindingnotestablished。
- 使用／控制因子：p34_diameter_cm: 2；p34_O2_percent: 17；p34_flow_cm_s: 12；p36_diameter_cm: 1；p36_flow_cm_s: <1。
- 來源限制：未取得這些panel與CSV逐試次原始join。；sourcecomputedtemperaturefieldspp37-50不是量測物性。。
- 搜尋句（改寫）：圖例分別有2cm球17%O2/12cm/s、1cm球17%O2/<1cm/s，另p56為15mm initialdiameter例；條件分屬各panel。。
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
| B26-PMMA-SPHERE-N2；B26-JET-INTERPRETATION；B26-SPHERE-GEOMETRY | Literaturecase/familyrelationonly; exactrawtrialtopanelbindingnotestablished | 上述結論保留同材料系列各自觀察。 | 未確認完全同試次的第二篇獨立分析時不聲稱跨文獻一致；實驗觀察與作者解釋亦不互換。 |

## 4. 消防洞見

| 類別 | 對應證據 | 數據支持的判斷 | 策略／產品構想 | 待驗證 |
| --- | --- | --- | --- | --- |
| 撲滅／抑制 | B26-PMMA-SPHERE-N2；B26-JET-INTERPRETATION | 來源局部N2供給案例火焰減弱卻未全熄；捲吸是作者解釋，尚無局部氧場量測。 | 研究較低捲吸或包覆式送劑，將送劑流動與惰化能力各自量測。 | 同火源比較動量、局部氧、熱回授與再燃，不混用相鄰panel條件。 |
| 預防 | 尚未取得／不適用 | 尚未建立本組可直接支持此用途的數據結論。 | 先補對應資料與試次匹配，再決定可測試策略；此處是研究缺口。 | 需本組材料、幾何、操作歷史與對應端點的量測；相近系列不能代替。 |
| 偵測 | 尚未取得／不適用 | 尚未建立本組可直接支持此用途的數據結論。 | 先補對應資料與試次匹配，再決定可測試策略；此處是研究缺口。 | 需本組材料、幾何、操作歷史與對應端點的量測；相近系列不能代替。 |

## 逐次索引

| 原始檔／資料位置 | Trial／Run／列 | 共享身份與保留事項 |
| --- | --- | --- |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-26_BASS\Experimental table\PSI-26_Experimental table_BASS.csv | csv_row: 53；date: 7/12/2012；GMT: 194；test_number: 111；as_run: 51；sample: 21 | identity_notes: source_record_id: PSI-26-CSV-r53；raw_material: 2 cm sphere   wake ign；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: Date: 7/12/2012；GMT: 194；As Run Test #: 51；Test #: 111；Sample #: 21；Fuel Sample Material: 2 cm sphere   wake ign |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-26_BASS\Experimental table\PSI-26_Experimental table_BASS.csv | csv_row: 54；date: 7/12/2012；GMT: 194；test_number: 112；as_run: 52；sample: 21 | identity_notes: source_record_id: PSI-26-CSV-r54；raw_material: 2 cm sphere   wake ign；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: Date: 7/12/2012；GMT: 194；As Run Test #: 52；Test #: 112；Sample #: 21；Fuel Sample Material: 2 cm sphere   wake ign |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-26_BASS\Experimental table\PSI-26_Experimental table_BASS.csv | csv_row: 55；date: 7/12/2012；GMT: 194；test_number: 113；as_run: 53；sample: 21 | identity_notes: source_record_id: PSI-26-CSV-r55；raw_material: 2 cm sphere   wake ign；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: Date: 7/12/2012；GMT: 194；As Run Test #: 53；Test #: 113；Sample #: 21；Fuel Sample Material: 2 cm sphere   wake ign |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-26_BASS\Experimental table\PSI-26_Experimental table_BASS.csv | csv_row: 100；date: 4/26/2013；GMT: 113；test_number: 38；as_run: 93；sample: 20 | identity_notes: source_record_id: PSI-26-CSV-r100；raw_material: 1 cm sphere   wake；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: Date: 4/26/2013；GMT: 113；As Run Test #: 93；Test #: 38；Sample #: 20；Fuel Sample Material: 1 cm sphere   wake |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-26_BASS\Experimental table\PSI-26_Experimental table_BASS.csv | csv_row: 101；date: 4/26/2013；GMT: 116；test_number: 39；as_run: 94；sample: 20 | identity_notes: source_record_id: PSI-26-CSV-r101；raw_material: 1 cm wake sphere；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: Date: 4/26/2013；GMT: 116；As Run Test #: 94；Test #: 39；Sample #: 20；Fuel Sample Material: 1 cm wake sphere |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-26_BASS\Experimental table\PSI-26_Experimental table_BASS.csv | csv_row: 102；date: 4/26/2013；GMT: 116；test_number: 40；as_run: 95；sample: 20 | identity_notes: source_record_id: PSI-26-CSV-r102；raw_material: 1 cm wake sphere；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: Date: 4/26/2013；GMT: 116；As Run Test #: 95；Test #: 40；Sample #: 20；Fuel Sample Material: 1 cm wake sphere |

## 缺件與適用範圍

- 來源圖例有同族材料結果，但未找到逐圖/逐試次join；不把圖上O2/流速貼到所有索引record。
- 未支援的第二條結論明列缺口；rawCSV只有date/GMT/Test/AsRun/Sample/material。
