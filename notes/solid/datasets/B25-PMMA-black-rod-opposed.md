# black PMMA棒：逆流

小資料集 ID：`B25-PMMA-black-rod-opposed`

## 資料身份與範圍

| 項目 | 內容 |
| --- | --- |
| NASA investigation | [PSI-25](https://psi.nasa.gov/physci/repo/data/investigations/PSI-25) |
| 材料／配方 | black cast PMMA, formulationunverified |
| 幾何 | cylindricalrods nominal1/4,3/8,1/2inch |
| 實驗模式 | opposed |
| 證據角色 | 固體火焰核心資料 |
| 環境 | ISS 微重力／來源指定的地面比較；逐次氣氛與流況不由材料名補值 |
| 資料粒度／共享試片 | 24 筆來源紀錄；獨立燃燒次數未自動確認；a/b、重複sample與階段保持原身份。 |
| 可用數值 | source_bound_observations_available |

## 1. 文獻結果與視覺化程式

### B25-BLACK-ROD　B25-BLACK-ROD

**Burning and Suppression of Solids-II (BASS-II) Summary Report**

黑PMMA棒對照顯示flow、O2及直徑耦合；報告稱µg在低至17.5%仍延燒而該1g資料19%以下未延燒。這是指定試驗比較，不是所有PMMA的通用LOC。

- 證據身份：來源觀察。
- 文獻定位：bass-5ffa911fd9b6: physicalpp55-60 Sec4.1, Figs4.1-4.4。
- 使用數據部分：literature_locator: physicalpp55-60 Sec4.1, Figs4.1-4.4；trial_binding: PI/material/geometry series mapping; only explicit trial IDs in a conclusion apply to individual trials；scope: 逐次索引為可用候選紀錄，不代表文獻使用其全部列。。
- 本組適用層級：本材料／幾何系列文獻結論；只有原文明寫Trial／圖板條件才直接適用。PI/material/geometry series mapping; only explicit trial IDs in a conclusion apply to individual trials。
- 使用／控制因子：reported_microgravity_low_O2_vol_percent: 17.5；reported_ground_no_spread_below_O2_vol_percent: 19。
- 來源限制：圖6.4mm/12.7mm等不同diameter面板不可當matched gravity pair。；P群另含3筆clear rod，已獨立分組；不混入black series。。
- 搜尋句（改寫）：黑PMMA棒對照顯示flow、O2及直徑耦合；報告稱µg在低至17.5%仍延燒而該1g資料19%以下未延燒。這是指定試驗比較，不是所有PMMA的通用LOC。。
- 來源：https://ntrs.nasa.gov/citations/20210011385
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/研究報告與書章/補下載/BASS-II Summary Report_e7fcef281a.pdf>)

### B25-ROD-CLEAR-COMPARATOR　B25-ROD-CLEAR-COMPARATOR

**Burning and Suppression of Solids-II (BASS-II) Summary Report**

Fernandez-Pello矩陣有clear/black兩類原始材料名稱；P3a/P3b共用sample215M，P25為217m，不能把P群全部當black或獨立樣本。

- 證據身份：source_trial_metadata。
- 文獻定位：bass-5ffa911fd9b6: physicalp55 Sec4.1 and AppendixA.3pp114-115。
- 使用數據部分：literature_locator: physicalp55 Sec4.1 and AppendixA.3pp114-115；trial_binding: PI/material/geometry series mapping; only explicit trial IDs in a conclusion apply to individual trials；scope: 逐次索引為可用候選紀錄，不代表文獻使用其全部列。。
- 本組適用層級：本材料／幾何系列文獻結論；只有原文明寫Trial／圖板條件才直接適用。PI/material/geometry series mapping; only explicit trial IDs in a conclusion apply to individual trials。
- 使用／控制因子：clear_P_trials: P3a；P3b；P25。
- 來源限制：未找到這3筆各自可轉錄spread數值；黑棒Fig4系列不套用clear。。
- 搜尋句（改寫）：Fernandez-Pello矩陣有clear/black兩類原始材料名稱；P3a/P3b共用sample215M，P25為217m，不能把P群全部當black或獨立樣本。。
- 來源：https://ntrs.nasa.gov/citations/20210011385
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/研究報告與書章/補下載/BASS-II Summary Report_e7fcef281a.pdf>)

| Model ID | 公式／預測量 | 展示程式 | 數值比較與限制 |
| --- | --- | --- | --- |
| PMMA-ROD-BOUNDARY-REPLAY | BASS-II PMMA rod boundary and steady profile；BASS-II PMMA rod boundary and steady profile | reproduce_solid_models.py · [開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/solid_combustion_evidence_20261115/models/reproduce_solid_models.py>) | 目前未執行／尚未閉合；缺少完整輸入與對應目標；Matched original stable/extinction numeric pairs with calibrated local velocity；Independent profile/temperature measurements and resolved heat-feedback closure；Eq6.1 coefficients are source-calibrated. Eq6.6-6.8 uses measured regression as input; it cannot independently predict that regression. Full Eq6.5 feedback closure/signs remain unresolved. |

| 可開啟的圖／工具 | 身份與用途 |
| --- | --- |
| [開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/solid_combustion_evidence_20261115/models/gas_balance_audit/pmma_conditional_endpoint_comparison.png>) | 僅raw材料明寫PMMA之39列；逐列納入身份見gas_endpoint_diagnostic.json，不是整組均納入 |

## 2. 使用資料與參數總表的因子對照

| 總表原分類 | 來源身份 | 原欄名單位 | 原欄名例 | 總表定位 |
| --- | --- | --- | --- | --- |
| 一氧化碳濃度 | 量測通道 | ppm | Initial CO (ppm)；Final CO (ppm) | '物理參數'!A139:K139 |
| 二氧化碳濃度 | 量測或條件值 | 未由欄名確認 | Initial CO2 % by vol；Final CO2 % by vol | '物理參數'!A140:K140 |
| 尺寸／幾何 | 裝置或樣本條件 | 未由欄名確認 | U cm/s* | '物理參數'!A141:K141 |
| 影像／光譜設定 | 儀器設定或影像座標 | 未由欄名確認 | Total Frames Shot | '物理參數'!A142:K142 |
| 氧濃度 | 量測或條件值 | 未由欄名確認 | Calibrated initial O2 % by vol；Calibrated final O2 % by vol | '物理參數'!A143:K143 |
| 熱通量／輻射 | 儀器設定／控制參數 | 未由欄名確認 | Radiometer gain (1000 250 50 10) | '物理參數'!A144:K144 |
| 風扇／流量顯示設定 | 儀器設定 | 未由欄名確認 | Flow restrictor；Fan display；Air display；Fan Calibration data；Fan Display；Air Display；Fan V | '物理參數'!A145:K145 |

以上是該 investigation 的欄位盤點；個別結論實際使用的因子以第1節與下列補充為準。

| 本組實際因子 | 總表定位／未列欄位 | 文獻中的用途 |
| --- | --- | --- |
| 材料／配方／幾何 | '實驗總覽'!E12 | 文獻選樣身份；逐次厚度、支撐與歷史另由原文補齊 |
| 環境／流向／重力 | '實驗總覽'!F12 | 環境摘要，非本組全部逐次聯合條件 |
| 尺寸／幾何 / U cm/s* | '物理參數'!G141 | 原欄U cm/s*是速度，雖總表分類為尺寸；先核對校準與試次 |
| 氧濃度 / Calibrated initial O2 % by vol；Calibrated final O2 % by vol | '物理參數'!G143 | 是否為模型輸入、控制條件或量測輸出，依第1節文獻定位逐項核對 |
| 熱通量／輻射 / Radiometer gain (1000 250 50 10) | '物理參數'!G144 | Radiometer gain是設定；不能當熱通量讀值 |
| 厚度、支撐、前緣位置／延燒速度與熱物性 | 需文獻／原始影像補欄位；本總表未提供全部閉合數值 | 選擇薄片／厚板／棒模型並核對同一observable |

| 文獻因子／疑點 | 正確讀法或需補資料 |
| --- | --- |
| 需補因子 | 燃料厚度/寬度/直徑、燒面/backing、模式、點火/預熱歷史需由原文/原始表逐項補；workbook不是完整聯合試驗條件。 |

## 3. 共用資料的多項結論比較

| 結論／文獻 | 資料重疊身份 | 共同處 | 不同處／不能合併之處 |
| --- | --- | --- | --- |
| B25-BLACK-ROD；B25-ROD-CLEAR-COMPARATOR | PI/material/geometry series mapping; only explicit trial IDs in a conclusion apply to individual trials | 上述結論保留同材料系列各自觀察。 | 未確認完全同試次的第二篇獨立分析時不聲稱跨文獻一致；實驗觀察與作者解釋亦不互換。 |

## 4. 消防洞見

| 類別 | 對應證據 | 數據支持的判斷 | 策略／產品構想 | 待驗證 |
| --- | --- | --- | --- | --- |
| 預防 | B25-BLACK-ROD | 指定棒狀材料在不同重力／氧／流場的維持與點燃界限不同，且存在預熱延遲。 | 地面材料篩選與低重力持續燃燒分開評估，保留直徑及熱歷史。 | 同批配方、幾何、點火程序與局部流場的配對試驗。 |
| 偵測 | 尚未取得／不適用 | 尚未建立本組可直接支持此用途的數據結論。 | 先補對應資料與試次匹配，再決定可測試策略；此處是研究缺口。 | 需本組材料、幾何、操作歷史與對應端點的量測；相近系列不能代替。 |
| 撲滅／抑制 | 尚未取得／不適用 | 尚未建立本組可直接支持此用途的數據結論。 | 先補對應資料與試次匹配，再決定可測試策略；此處是研究缺口。 | 需本組材料、幾何、操作歷史與對應端點的量測；相近系列不能代替。 |

## 逐次索引

| 原始檔／資料位置 | Trial／Run／列 | 共享身份與保留事項 |
| --- | --- | --- |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 75；date: 6/16/2014；GMT: 167；test_number: P1；as_run: 尚未取得／不適用；sample: 185M | identity_notes: source_record_id: PSI-25-CSV-r75；raw_material: 1/4" black rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Fernandez-Pello；Test #: P1；Date: 6/16/2014；GMT: 167；Sample #: 185M；Fuel Sample Material: 1/4" black rod；Flow restrictor: 2；Fan display: 尚未取得／不適用；Air display: 5  2   slow decr to ext；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 307；Calibrated  initial O2 % by vol : 17.7；Calibrated final O2 % by vol: 17.5；Initial CO2 % by vol: 0.27；Final CO2 % by vol: 0.44；Initial CO (ppm): 1；Final CO (ppm): 14 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 76；date: 6/16/2014；GMT: 167；test_number: P2；as_run: 尚未取得／不適用；sample: 188M | identity_notes: source_record_id: PSI-25-CSV-r76；raw_material: 1/4" black rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Fernandez-Pello；Test #: P2；Date: 6/16/2014；GMT: 167；Sample #: 188M；Fuel Sample Material: 1/4" black rod；Flow restrictor: 2；Fan display: 尚未取得／不適用；Air display: 5   2.5   2 (pot .9   .5   .35.  .33)；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 303；Calibrated  initial O2 % by vol : 17.4；Calibrated final O2 % by vol: 17.2；Initial CO2 % by vol: 0.44；Final CO2 % by vol: 0.66；Initial CO (ppm): 14；Final CO (ppm): 26 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 79；date: 7/3/2014；GMT: 184；test_number: P4；as_run: 尚未取得／不適用；sample: 197m | identity_notes: source_record_id: PSI-25-CSV-r79；raw_material: 3/8" black rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Fernandez-Pello；Test #: P4；Date: 7/3/2014；GMT: 184；Sample #: 197m；Fuel Sample Material: 3/8" black rod；Flow restrictor: 2；Fan display: 48   41；Air display: 5   pots 0.4   0.36   0.32   0.308   .3   off；Radiometer gain   (1000   250   50   10): 50；Total Frames Shot: 297；Calibrated  initial O2 % by vol : 18.5；Calibrated final O2 % by vol: 17.1；Initial CO2 % by vol: 0.62；Final CO2 % by vol: 1.8；Initial CO (ppm): 64；Final CO (ppm): 493 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 80；date: 7/14/2014；GMT: 195；test_number: P5；as_run: 尚未取得／不適用；sample: 202m | identity_notes: source_record_id: PSI-25-CSV-r80；raw_material: 0.5" black rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Fernandez-Pello；Test #: P5；Date: 7/14/2014；GMT: 195；Sample #: 202m；Fuel Sample Material: 0.5" black rod；Flow restrictor: 2；Fan display: Fan pot 1.5 (5cm/s)   0.9   0.4   0.36   0.32   0.308   0.3   0.29   0.28   0 ext；Air display: 5 down to ext；Radiometer gain   (1000   250   50   10): 250>50；Total Frames Shot: 313；Calibrated  initial O2 % by vol : 19.3；Calibrated final O2 % by vol: 17.6；Initial CO2 % by vol: 0.32；Final CO2 % by vol: 1.67；Initial CO (ppm): 0；Final CO (ppm): 525 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 81；date: 7/3/2014；GMT: 184；test_number: P6；as_run: 尚未取得／不適用；sample: 186m | identity_notes: source_record_id: PSI-25-CSV-r81；raw_material: 1/4" black rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Fernandez-Pello；Test #: P6；Date: 7/3/2014；GMT: 184；Sample #: 186m；Fuel Sample Material: 1/4" black rod；Flow restrictor: 2；Fan display: 48   41；Air display: 5   pots 0.4   0.36   0.32   0.31   off；Radiometer gain   (1000   250   50   10): 50；Total Frames Shot: 162；Calibrated  initial O2 % by vol : 18.9；Calibrated final O2 % by vol: 18.5；Initial CO2 % by vol: 0.3；Final CO2 % by vol: 0.62；Initial CO (ppm): 0；Final CO (ppm): 64 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 82；date: 7/3/2014；GMT: 184；test_number: P8；as_run: 尚未取得／不適用；sample: 197m | identity_notes: source_record_id: PSI-25-CSV-r82；raw_material: 3/8" black rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Fernandez-Pello；Test #: P8；Date: 7/3/2014；GMT: 184；Sample #: 197m；Fuel Sample Material: 3/8" black rod；Flow restrictor: 2；Fan display: 48   62   75；Air display: 5   would not stay lit   10   15 ibid；Radiometer gain   (1000   250   50   10): 50；Total Frames Shot: 66；Calibrated  initial O2 % by vol : 16.4；Calibrated final O2 % by vol: 16.3；Initial CO2 % by vol: 0.72；Final CO2 % by vol: 0.81；Initial CO (ppm): 44；Final CO (ppm): 69 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 83；date: 7/14/2014；GMT: 195；test_number: P9；as_run: 尚未取得／不適用；sample: 202m | identity_notes: source_record_id: PSI-25-CSV-r83；raw_material: 0.5" black rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Fernandez-Pello；Test #: P9；Date: 7/14/2014；GMT: 195；Sample #: 202m；Fuel Sample Material: 0.5" black rod；Flow restrictor: 2；Fan display: Fan pot 1.5 (5cm/s)   0.9   0.4   0.36   0.32   0.3   0.28 ext；Air display: 5 down to ext；Radiometer gain   (1000   250   50   10): 50；Total Frames Shot: 148；Calibrated  initial O2 % by vol : 17.6；Calibrated final O2 % by vol: 17.1；Initial CO2 % by vol: 1.67；Final CO2 % by vol: 2.1；Initial CO (ppm): 525；Final CO (ppm): 535 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 84；date: 7/3/2014；GMT: 184；test_number: P10；as_run: 尚未取得／不適用；sample: 187m | identity_notes: source_record_id: PSI-25-CSV-r84；raw_material: 1/4" black rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Fernandez-Pello；Test #: P10；Date: 7/3/2014；GMT: 184；Sample #: 187m；Fuel Sample Material: 1/4" black rod；Flow restrictor: 2；Fan display: 48   41；Air display: 5   pots 0.4   0.36   0.32   0.31   0.30 extinguished；Radiometer gain   (1000   250   50   10): 50；Total Frames Shot: 221；Calibrated  initial O2 % by vol : 17；Calibrated final O2 % by vol: 16.4；Initial CO2 % by vol: 0.29；Final CO2 % by vol: 0.72；Initial CO (ppm): 2；Final CO (ppm): 44 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 85；date: 7/29/2014；GMT: 210；test_number: P12；as_run: 尚未取得／不適用；sample: 199m | identity_notes: source_record_id: PSI-25-CSV-r85；raw_material: 3/8" black rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Fernandez-Pello；Test #: P12；Date: 7/29/2014；GMT: 210；Sample #: 199m；Fuel Sample Material: 3/8" black rod；Flow restrictor: 2；Fan display: 60  52  48  44.5  42  41.5  41 (2.6  1.6  1.2  .75  .5  .4  .36  0.34)；Air display: 5   3  2  1   0.5   lower；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 273；Calibrated  initial O2 % by vol : 17.5；Calibrated final O2 % by vol: 16.8；Initial CO2 % by vol: 0.29；Final CO2 % by vol: 0.95；Initial CO (ppm): 2；Final CO (ppm): 57 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 86；date: 7/14/2014；GMT: 195；test_number: P13a；as_run: 尚未取得／不適用；sample: 203m | identity_notes: source_record_id: PSI-25-CSV-r86；raw_material: 0.5" black rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Fernandez-Pello；Test #: P13a；Date: 7/14/2014；GMT: 195；Sample #: 203m；Fuel Sample Material: 0.5" black rod；Flow restrictor: 2；Fan display: Fan pot 1.1 (5cm/s)   0.4   0.36   0.32   0.3   0.28   0.26   0 ext；Air display: 5 down to ext；Radiometer gain   (1000   250   50   10): 50；Total Frames Shot: 255；Calibrated  initial O2 % by vol : 20.7；Calibrated final O2 % by vol: 19.1；Initial CO2 % by vol: 0.36；Final CO2 % by vol: 1.63；Initial CO (ppm): 38；Final CO (ppm): 450 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 87；date: 7/14/2014；GMT: 195；test_number: P13b；as_run: 尚未取得／不適用；sample: 203m | identity_notes: source_record_id: PSI-25-CSV-r87；raw_material: 0.5" black rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Fernandez-Pello；Test #: P13b；Date: 7/14/2014；GMT: 195；Sample #: 203m；Fuel Sample Material: 0.5" black rod；Flow restrictor: 2；Fan display: Fan pot 1.3 (5cm/s)   0.4   0.36   0.32 ext；Air display: 5 down to ext；Radiometer gain   (1000   250   50   10): 50；Total Frames Shot: 94；Calibrated  initial O2 % by vol : 20.6；Calibrated final O2 % by vol: 20.2；Initial CO2 % by vol: 0.41；Final CO2 % by vol: 0.62；Initial CO (ppm): 5；Final CO (ppm): 72 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 88；date: 6/23/2014；GMT: 174；test_number: P14；as_run: 尚未取得／不適用；sample: 189M | identity_notes: source_record_id: PSI-25-CSV-r88；raw_material: 1/4 blac rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Fernandez-Pello；Test #: P14；Date: 6/23/2014；GMT: 174；Sample #: 189M；Fuel Sample Material: 1/4 blac rod；Flow restrictor: 2；Fan display: 46   41；Air display: 5   low (.85   .4   .32)；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 162；Calibrated  initial O2 % by vol : 18.4；Calibrated final O2 % by vol: 18；Initial CO2 % by vol: 0.34；Final CO2 % by vol: 0.62；Initial CO (ppm): 3；Final CO (ppm): 90 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 89；date: 6/23/2014；GMT: 174；test_number: P15；as_run: 尚未取得／不適用；sample: 190M | identity_notes: source_record_id: PSI-25-CSV-r89；raw_material: 1/4 black rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Fernandez-Pello；Test #: P15；Date: 6/23/2014；GMT: 174；Sample #: 190M；Fuel Sample Material: 1/4 black rod；Flow restrictor: 2；Fan display: 46   41；Air display: 5   (0.36)；Radiometer gain   (1000   250   50   10): 250   50；Total Frames Shot: 170；Calibrated  initial O2 % by vol : 18；Calibrated final O2 % by vol: 17.5；Initial CO2 % by vol: 0.62；Final CO2 % by vol: 1.11；Initial CO (ppm): 90；Final CO (ppm): 108 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 90；date: 7/22/2014；GMT: 203；test_number: P16；as_run: 尚未取得／不適用；sample: 191m | identity_notes: source_record_id: PSI-25-CSV-r90；raw_material: 1/4" black rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Fernandez-Pello；Test #: P16；Date: 7/22/2014；GMT: 203；Sample #: 191m；Fuel Sample Material: 1/4" black rod；Flow restrictor: 2；Fan display: 49  62  44  41.5  41 (pots 1.3   2.8   0.7   0.4   0.36   0.32)；Air display: 5  8  2  low；Radiometer gain   (1000   250   50   10): 250  50；Total Frames Shot: 129；Calibrated  initial O2 % by vol : 18.2；Calibrated final O2 % by vol: 17.4；Initial CO2 % by vol: 0.3；Final CO2 % by vol: 0.92；Initial CO (ppm): 0；Final CO (ppm): 56 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 91；date: 7/29/2014；GMT: 210；test_number: P17；as_run: 尚未取得／不適用；sample: 192m | identity_notes: source_record_id: PSI-25-CSV-r91；raw_material: 1/4"  black rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Fernandez-Pello；Test #: P17；Date: 7/29/2014；GMT: 210；Sample #: 192m；Fuel Sample Material: 1/4"  black rod；Flow restrictor: 2；Fan display: 60  52  48  233  48  41 (2.6   1.6   1.2   10   1.2   0.36   0.34)；Air display: 5   3   2   22   2   low；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 186；Calibrated  initial O2 % by vol : 16.8；Calibrated final O2 % by vol: 16.5；Initial CO2 % by vol: 0.95；Final CO2 % by vol: 1.34；Initial CO (ppm): 57；Final CO (ppm): 68 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 92；date: 7/30/2014；GMT: 211；test_number: P18；as_run: 尚未取得／不適用；sample: 193m | identity_notes: source_record_id: PSI-25-CSV-r92；raw_material: 1/4" black rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Fernandez-Pello；Test #: P18；Date: 7/30/2014；GMT: 211；Sample #: 193m；Fuel Sample Material: 1/4" black rod；Flow restrictor: 2；Fan display: 55  47  etc (pot 1  2  1  2   etc)；Air display: 2  0  2  0  etc；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 280；Calibrated  initial O2 % by vol : 20；Calibrated final O2 % by vol: 19；Initial CO2 % by vol: 0.34；Final CO2 % by vol: 1.2；Initial CO (ppm): 1；Final CO (ppm): 26 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 93；date: 7/22/2014；GMT: 203；test_number: P19；as_run: 尚未取得／不適用；sample: 194m | identity_notes: source_record_id: PSI-25-CSV-r93；raw_material: 1/4" black rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Fernandez-Pello；Test #: P19；Date: 7/22/2014；GMT: 203；Sample #: 194m；Fuel Sample Material: 1/4" black rod；Flow restrictor: 2；Fan display: 49  62  44  41.5  122   41 (pots 1.3   2.8   0.7   0.4   0.36   10.   0.32)；Air display: 5  8  2  max   0；Radiometer gain   (1000   250   50   10): 250   50；Total Frames Shot: 279；Calibrated  initial O2 % by vol : 17.5；Calibrated final O2 % by vol: 16.7；Initial CO2 % by vol: 0.9；Final CO2 % by vol: 1.61；Initial CO (ppm): 54；Final CO (ppm): 94 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 94；date: 7/30/2014；GMT: 211；test_number: P20；as_run: 尚未取得／不適用；sample: 195m | identity_notes: source_record_id: PSI-25-CSV-r94；raw_material: 1/4" black rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Fernandez-Pello；Test #: P20；Date: 7/30/2014；GMT: 211；Sample #: 195m；Fuel Sample Material: 1/4" black rod；Flow restrictor: 2；Fan display: 55  47  etc (pot 1  2  1  2   etc)；Air display: 2  0  2  0  etc；Radiometer gain   (1000   250   50   10): 50；Total Frames Shot: 311；Calibrated  initial O2 % by vol : 19；Calibrated final O2 % by vol: 18.2；Initial CO2 % by vol: 0.34；Final CO2 % by vol: 1.05；Initial CO (ppm): 2；Final CO (ppm): 78 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 95；date: 6/23/2014；GMT: 174；test_number: P21a；as_run: 尚未取得／不適用；sample: 196M | identity_notes: source_record_id: PSI-25-CSV-r95；raw_material: 1/4 black rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Fernandez-Pello；Test #: P21a；Date: 6/23/2014；GMT: 174；Sample #: 196M；Fuel Sample Material: 1/4 black rod；Flow restrictor: 2；Fan display: 46；Air display: 5；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 57；Calibrated  initial O2 % by vol : 16.3；Calibrated final O2 % by vol: 16.3；Initial CO2 % by vol: 0.96；Final CO2 % by vol: 1；Initial CO (ppm): 86；Final CO (ppm): 94 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 96；date: 6/23/2014；GMT: 174；test_number: P21b；as_run: 尚未取得／不適用；sample: 196M | identity_notes: source_record_id: PSI-25-CSV-r96；raw_material: 1/4" black rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Fernandez-Pello；Test #: P21b；Date: 6/23/2014；GMT: 174；Sample #: 196M；Fuel Sample Material: 1/4" black rod；Flow restrictor: 2；Fan display: 46；Air display: 5；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 14；Calibrated  initial O2 % by vol : 16.3；Calibrated final O2 % by vol: 16.3；Initial CO2 % by vol: 1；Final CO2 % by vol: 1.03；Initial CO (ppm): 94；Final CO (ppm): 98 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 97；date: 7/8/2014；GMT: 189；test_number: P22a；as_run: 尚未取得／不適用；sample: 200m | identity_notes: source_record_id: PSI-25-CSV-r97；raw_material: 3/8" black rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Fernandez-Pello；Test #: P22a；Date: 7/8/2014；GMT: 189；Sample #: 200m；Fuel Sample Material: 3/8" black rod；Flow restrictor: 2；Fan display: 5   0.36   0.32 ext after some time；Air display: 5   down to ext；Radiometer gain   (1000   250   50   10): 250>50；Total Frames Shot: 83；Calibrated  initial O2 % by vol : 20.8；Calibrated final O2 % by vol: 0.6；Initial CO2 % by vol: 0.32；Final CO2 % by vol: none；Initial CO (ppm): 4；Final CO (ppm): none |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 98；date: 7/8/2014；GMT: 189；test_number: P22b；as_run: 尚未取得／不適用；sample: 200m | identity_notes: source_record_id: PSI-25-CSV-r98；raw_material: 3/8" black rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Fernandez-Pello；Test #: P22b；Date: 7/8/2014；GMT: 189；Sample #: 200m；Fuel Sample Material: 3/8" black rod；Flow restrictor: 2；Fan display: 5   p.36   0.34   0.33   0.32   0.31 ext；Air display: 5 down to ext；Radiometer gain   (1000   250   50   10): 50；Total Frames Shot: 155；Calibrated  initial O2 % by vol : 20；Calibrated final O2 % by vol: 39.1；Initial CO2 % by vol: none；Final CO2 % by vol: 1.09；Initial CO (ppm): none；Final CO (ppm): 239 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 99；date: 7/30/2014；GMT: 211；test_number: P23；as_run: 尚未取得／不適用；sample: 201m | identity_notes: source_record_id: PSI-25-CSV-r99；raw_material: 3/8" black rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Fernandez-Pello；Test #: P23；Date: 7/30/2014；GMT: 211；Sample #: 201m；Fuel Sample Material: 3/8" black rod；Flow restrictor: 2；Fan display: 55  47  etc (pot 1  2  1  2   etc)；Air display: 2  0  2  0  etc；Radiometer gain   (1000   250   50   10): 50；Total Frames Shot: 242；Calibrated  initial O2 % by vol : 18.2；Calibrated final O2 % by vol: 17；Initial CO2 % by vol: 1.05；Final CO2 % by vol: 2.08；Initial CO (ppm): 78；Final CO (ppm): 159 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 100；date: 7/30/2014；GMT: 211；test_number: P24；as_run: 尚未取得／不適用；sample: 819L | identity_notes: source_record_id: PSI-25-CSV-r100；raw_material: 3/8" black rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Fernandez-Pello；Test #: P24；Date: 7/30/2014；GMT: 211；Sample #: 819L；Fuel Sample Material: 3/8" black rod；Flow restrictor: 2；Fan display: 55  47  etc (pot 1  2  1  2   etc)；Air display: 2  0  2  0  etc；Radiometer gain   (1000   250   50   10): 250>50；Total Frames Shot: 308；Calibrated  initial O2 % by vol : 19；Calibrated final O2 % by vol: 17.5；Initial CO2 % by vol: 1.2；Final CO2 % by vol: 2.24；Initial CO (ppm): 26；Final CO (ppm): 260 |

## 缺件與適用範圍

- P3a/b andP25 clear separated; paperLink2018 labelsB16/B19 mustnotjoinCSVthinfilmB16/B19.
