# clear PMMA棒：逆流

小資料集 ID：`B25-PMMA-clear-rod-opposed`

## 資料身份與範圍

| 項目 | 內容 |
| --- | --- |
| NASA investigation | [PSI-25](https://psi.nasa.gov/physci/repo/data/investigations/PSI-25) |
| 材料／配方 | clear cast PMMA, formulationunverified |
| 幾何 | cylindricalrods nominal1/4,3/8,1/2inch |
| 實驗模式 | opposed |
| 證據角色 | 固體火焰核心資料 |
| 環境 | ISS 微重力／來源指定的地面比較；逐次氣氛與流況不由材料名補值 |
| 資料粒度／共享試片 | 3 筆來源紀錄；獨立燃燒次數未自動確認；a/b、重複sample與階段保持原身份。 |
| 可用數值 | limited_source_or_trial_join_gap |

## 1. 文獻結果與視覺化程式

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
| B25-ROD-CLEAR-COMPARATOR | 原表索引或相近來源案例；精確試次連結未決 | 可確認的材料與原紀錄身份列在逐次索引。 | 尚未取得多項可直接套用的結論；不製造第二個結論或衝突。 |

## 4. 消防洞見

| 類別 | 對應證據 | 數據支持的判斷 | 策略／產品構想 | 待驗證 |
| --- | --- | --- | --- | --- |
| 預防 | 尚未取得／不適用 | 尚未建立本組可直接支持此用途的數據結論。 | 先補對應資料與試次匹配，再決定可測試策略；此處是研究缺口。 | 需本組材料、幾何、操作歷史與對應端點的量測；相近系列不能代替。 |
| 偵測 | 尚未取得／不適用 | 尚未建立本組可直接支持此用途的數據結論。 | 先補對應資料與試次匹配，再決定可測試策略；此處是研究缺口。 | 需本組材料、幾何、操作歷史與對應端點的量測；相近系列不能代替。 |
| 撲滅／抑制 | 尚未取得／不適用 | 尚未建立本組可直接支持此用途的數據結論。 | 先補對應資料與試次匹配，再決定可測試策略；此處是研究缺口。 | 需本組材料、幾何、操作歷史與對應端點的量測；相近系列不能代替。 |

## 逐次索引

| 原始檔／資料位置 | Trial／Run／列 | 共享身份與保留事項 |
| --- | --- | --- |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 77；date: 6/16/2014；GMT: 167；test_number: P3a；as_run: 尚未取得／不適用；sample: 215M | identity_notes: source_record_id: PSI-25-CSV-r77；raw_material: 1/4" clear rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Fernandez-Pello；Test #: P3a；Date: 6/16/2014；GMT: 167；Sample #: 215M；Fuel Sample Material: 1/4" clear rod；Flow restrictor: 2；Fan display: 尚未取得／不適用；Air display: 5   2.5 (1.15   .5   .35   .33. .32   .315   .31   .3)；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 304；Calibrated  initial O2 % by vol : 17.7；Calibrated final O2 % by vol: 17.4；Initial CO2 % by vol: 0.27；Final CO2 % by vol: 0.51；Initial CO (ppm): 2；Final CO (ppm): 33 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 78；date: 6/16/2014；GMT: 167；test_number: P3b；as_run: 尚未取得／不適用；sample: 215M | identity_notes: source_record_id: PSI-25-CSV-r78；raw_material: 1/4 clear rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Fernandez-Pello；Test #: P3b；Date: 6/16/2014；GMT: 167；Sample #: 215M；Fuel Sample Material: 1/4 clear rod；Flow restrictor: 2；Fan display: 尚未取得／不適用；Air display: 5   very low (0.85   0.32   0.31   0.305   0.30   0.295)；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 303；Calibrated  initial O2 % by vol : 17.4；Calibrated final O2 % by vol: 16.8；Initial CO2 % by vol: 0.51；Final CO2 % by vol: none；Initial CO (ppm): 33；Final CO (ppm): 79 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 101；date: 7/8/2014；GMT: 189；test_number: P25；as_run: 尚未取得／不適用；sample: 217m | identity_notes: source_record_id: PSI-25-CSV-r101；raw_material: 3/8" clear rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Fernandez-Pello；Test #: P25；Date: 7/8/2014；GMT: 189；Sample #: 217m；Fuel Sample Material: 3/8" clear rod；Flow restrictor: 2；Fan display: 5   p.36   0.34   0.33   0.32   0.31 ext；Air display: 5 down to ext；Radiometer gain   (1000   250   50   10): 50；Total Frames Shot: 246；Calibrated  initial O2 % by vol : 20.9；Calibrated final O2 % by vol: 20.2；Initial CO2 % by vol: 0.38；Final CO2 % by vol: 1；Initial CO (ppm): 43；Final CO (ppm): 205 |

## 缺件與適用範圍

- 不足兩項有來源結論；多結論比較尚未完成，不以目的或推測湊數。
- Blackseriesnumericplotsdonotvalidateclearcomparator; exactratejoinmissing.
