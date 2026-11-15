# SIBAL：opposed

小資料集 ID：`B26-SIBAL-opposed`

## 資料身份與範圍

| 項目 | 內容 |
| --- | --- |
| NASA investigation | [PSI-26](https://psi.nasa.gov/physci/repo/data/investigations/PSI-26) |
| 材料／配方 | 75wt%cotton/25wt%fiberglass per2013manuscript |
| 幾何 | flatstrips;1/2cmwidth |
| 實驗模式 | opposed |
| 證據角色 | 固體火焰核心資料 |
| 環境 | ISS 微重力／來源指定的地面比較；逐次氣氛與流況不由材料名補值 |
| 資料粒度／共享試片 | 4 筆來源紀錄；獨立燃燒次數未自動確認；a/b、重複sample與階段保持原身份。 |
| 可用數值 | source_bound_observations_available |

## 1. 文獻結果與視覺化程式

### B26-SIBAL-OPPOSED　B26-SIBAL-OPPOSED

**Flammability Aspects of Fabric in Opposed and Concurrent Air Flow in Microgravity**

Test9單burn逐段降流至<1cm/s，仍未測得quench，最後耗盡燃料；終點不可標成radiativeextinction。

- 證據身份：來源觀察。
- 文獻定位：bass-434e9b2cade6: Table1Test9/Fig11, paragraphs133-137; paralleldeckp26-30/33。
- 使用數據部分：literature_locator: Table1Test9/Fig11, paragraphs133-137; paralleldeckp26-30/33；trial_binding: ExactTest#join to2013OOXMLTable1; Test5b explicitCSVonly；scope: 逐次索引為可用候選紀錄，不代表文獻使用其全部列。。
- 本組適用層級：本材料／幾何系列文獻結論；只有原文明寫Trial／圖板條件才直接適用。ExactTest#join to2013OOXMLTable1; Test5b explicitCSVonly。
- 使用／控制因子：paper_Test9_initial_flow_cm_s: 10；lowest_flow_cm_s: <1；source_burn_time_s: 90。
- 來源限制：一個burn可有多流速點；sourcepaper_test9不是rawAsRun9。。
- 搜尋句（改寫）：Test9單burn逐段降流至<1cm/s，仍未測得quench，最後耗盡燃料；終點不可標成radiativeextinction。。
- 來源：https://psi.ndc.nasa.gov/mpglobal/api/athena/file/70471/?inline=1&log=1
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/其他研究文件_正文類型待確認/第一批下載/PSI-26_BASS/Science Documents/PSI-26_Science Documents_FlammabilityAspectsofFabric_USNationalCombustion.2013.docx>)

### B26-SIBAL-GRAVITY　B26-SIBAL-GRAVITY

**Flammability Aspects of Fabric in Opposed and Concurrent Air Flow in Microgravity**

來源相片並置的1g順流火焰成長、µg較穩定；指定SIBAL在1g向下不持續，但µg逆流可延燒，僅限所測配置。

- 證據身份：author_image_comparison。
- 文獻定位：bass-d87675b105c4: physicalpp32-35; manuscriptFigs13/14/paragraphs140-143。
- 使用數據部分：literature_locator: physicalpp32-35; manuscriptFigs13/14/paragraphs140-143；trial_binding: ExactTest#join to2013OOXMLTable1; Test5b explicitCSVonly；scope: 逐次索引為可用候選紀錄，不代表文獻使用其全部列。。
- 本組適用層級：本材料／幾何系列文獻結論；只有原文明寫Trial／圖板條件才直接適用。ExactTest#join to2013OOXMLTable1; Test5b explicitCSVonly。
- 使用／控制因子：。
- 來源限制：缺同批材料、完整groundconditions、逐試次rawrate與不確定度，不能給gravity-onlycoefficient。。
- 搜尋句（改寫）：來源相片並置的1g順流火焰成長、µg較穩定；指定SIBAL在1g向下不持續，但µg逆流可延燒，僅限所測配置。。
- 來源：https://psi.ndc.nasa.gov/mpglobal/api/athena/file/70475/?inline=1&log=1
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/簡報與海報/第一批下載/PSI-26_BASS/Presentations/PSI-26_Presentations_Flammability Aspects of Fabric_USNationalCombustion2013.pdf>)

### B26-SIBAL-CONCURRENT　B26-SIBAL-CONCURRENT

**Flammability Aspects of Fabric in Opposed and Concurrent Air Flow in Microgravity**

來源Table1列11個具編號SIBAL試驗；順流base可達穩態但tip/length未必已穩定。Test7與6的2.55/1.21mm/s比較是µg順流/逆流，不是重力對照。

- 證據身份：來源觀察。
- 文獻定位：bass-434e9b2cade6: OOXML Table1; bodyparagraphs118-122,140-142/Figs7/8/12; paralleldeckp20-24/31。
- 使用數據部分：literature_locator: OOXML Table1; bodyparagraphs118-122,140-142/Figs7/8/12; paralleldeckp20-24/31；trial_binding: ExactTest#join to2013OOXMLTable1; Test5b explicitCSVonly；scope: 逐次索引為可用候選紀錄，不代表文獻使用其全部列。。
- 本組適用層級：本材料／幾何系列文獻結論；只有原文明寫Trial／圖板條件才直接適用。ExactTest#join to2013OOXMLTable1; Test5b explicitCSVonly。
- 使用／控制因子：Test7_concurrent_base_mm_s: 2.55；Test6_opposed_mm_s: 1.21；flow_approx_cm_s: 10。
- 來源限制：稿件/簡報共用資料，不新增replicates。；正式CSV的Test欄而非AsRun欄才與Table1對應。。
- 搜尋句（改寫）：來源Table1列11個具編號SIBAL試驗；順流base可達穩態但tip/length未必已穩定。Test7與6的2.55/1.21mm/s比較是µg順流/逆流，不是重力對照。。
- 來源：https://psi.ndc.nasa.gov/mpglobal/api/athena/file/70471/?inline=1&log=1
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/其他研究文件_正文類型待確認/第一批下載/PSI-26_BASS/Science Documents/PSI-26_Science Documents_FlammabilityAspectsofFabric_USNationalCombustion.2013.docx>)

| Model ID | 公式／預測量 | 展示程式 | 數值比較與限制 |
| --- | --- | --- | --- |
| BASS-SIBAL-CORRELATION-REPLAY | width2cm: V_F[mm/s]=-0.20*U_inf[cm/s]+0.56; width1cm: V_F[mm/s]=-0.15*U_inf[cm/s]+0.07；BASS SIBAL spread correlation | reproduce_solid_models.py · [開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/solid_combustion_evidence_20261115/models/reproduce_solid_models.py>) | 目前未執行／尚未閉合；缺少完整輸入與對應目標；Original image-derived numeric spread targets with same steady-flow segment；Exact source-fit point membership and geometry/flow sign mapping；Published width-specific signed-flow lines exist; no original numeric spread-target pair is joined in the local matrices. Missing target stays unavailable. |

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
| B26-SIBAL-OPPOSED；B26-SIBAL-GRAVITY；B26-SIBAL-CONCURRENT | 2013 manuscript Table1 Test# 已和原CSV Test#對應；不是用AsRun號誤配 | 順／逆流都需保留火焰前端、底端及材料耗盡的不同端點。 | Test7/6是同微重力不同流向；不能當重力控制組。穩態base不代表tip與長度都穩態；Test9耗盡不等於熄滅。 |

## 4. 消防洞見

| 類別 | 對應證據 | 數據支持的判斷 | 策略／產品構想 | 待驗證 |
| --- | --- | --- | --- | --- |
| 撲滅／抑制 | B26-SIBAL-OPPOSED | 指定案例降流後熄滅，但另有低流仍燃至燃料耗盡的來源；介入成效具材料與狀態依賴。 | 以火焰／熱反應回饋檢驗降流，而非採跨材料固定流速作停止條件。 | 同幾何、氧與熱歷史的流速介入試驗，區分耗盡與全局熄滅。 |
| 預防 | 尚未取得／不適用 | 尚未建立本組可直接支持此用途的數據結論。 | 先補對應資料與試次匹配，再決定可測試策略；此處是研究缺口。 | 需本組材料、幾何、操作歷史與對應端點的量測；相近系列不能代替。 |
| 偵測 | 尚未取得／不適用 | 尚未建立本組可直接支持此用途的數據結論。 | 先補對應資料與試次匹配，再決定可測試策略；此處是研究缺口。 | 需本組材料、幾何、操作歷史與對應端點的量測；相近系列不能代替。 |

## 逐次索引

| 原始檔／資料位置 | Trial／Run／列 | 共享身份與保留事項 |
| --- | --- | --- |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-26_BASS\Experimental table\PSI-26_Experimental table_BASS.csv | csv_row: 46；date: 6/29/2012；GMT: 181；test_number: 5b；as_run: 44；sample: 9 | identity_notes: source_record_id: PSI-26-CSV-r46；raw_material: SIBAL 2 cm   opposed flow ；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: Date: 6/29/2012；GMT: 181；As Run Test #: 44；Test #: 5b；Sample #: 9；Fuel Sample Material: SIBAL 2 cm   opposed flow  |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-26_BASS\Experimental table\PSI-26_Experimental table_BASS.csv | csv_row: 47；date: 7/3/2012；GMT: 185；test_number: 6；as_run: 45；sample: 8 | identity_notes: source_record_id: PSI-26-CSV-r47；raw_material: SIBAL 2 cm；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: Date: 7/3/2012；GMT: 185；As Run Test #: 45；Test #: 6；Sample #: 8；Fuel Sample Material: SIBAL 2 cm |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-26_BASS\Experimental table\PSI-26_Experimental table_BASS.csv | csv_row: 57；date: 7/19/2012；GMT: 201；test_number: 3；as_run: 55；sample: 6 | identity_notes: source_record_id: PSI-26-CSV-r57；raw_material: SIBAL 2 cm；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: Date: 7/19/2012；GMT: 201；As Run Test #: 55；Test #: 3；Sample #: 6；Fuel Sample Material: SIBAL 2 cm |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-26_BASS\Experimental table\PSI-26_Experimental table_BASS.csv | csv_row: 69；date: 8/9/2012；GMT: 222；test_number: 9；as_run: 66；sample: 7 | identity_notes: source_record_id: PSI-26-CSV-r69；raw_material: SIBAL 2 cm；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: Date: 8/9/2012；GMT: 222；As Run Test #: 66；Test #: 9；Sample #: 7；Fuel Sample Material: SIBAL 2 cm |

## 缺件與適用範圍

- Test5b只有CSV明示opposed，不在2013Table1。
