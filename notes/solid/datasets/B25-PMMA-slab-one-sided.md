# PMMA中厚板：one-sided

小資料集 ID：`B25-PMMA-slab-one-sided`

## 資料身份與範圍

| 項目 | 內容 |
| --- | --- |
| NASA investigation | [PSI-25](https://psi.nasa.gov/physci/repo/data/investigations/PSI-25) |
| 材料／配方 | clear cast PMMA |
| 幾何 | slab1–5mm; width1.2/2.2cm perTable5.1 |
| 實驗模式 | opposed, one burning face withbacking |
| 證據角色 | 固體火焰核心資料 |
| 環境 | ISS 微重力／來源指定的地面比較；逐次氣氛與流況不由材料名補值 |
| 資料粒度／共享試片 | 5 筆來源紀錄；獨立燃燒次數未自動確認；a/b、重複sample與階段保持原身份。 |
| 可用數值 | source_bound_observations_available |

## 1. 文獻結果與視覺化程式

### B25-SLAB-RATES　B25-SLAB-RATES

**Burning and Suppression of Solids-II (BASS-II) Summary Report**

20個M試次有明確geometry/velocity/spread表；M6/M12未追蹤。M8同頁10cm/s表值與圖中來源回歸斜率不同，兩版都保留。

- 證據身份：來源觀察。
- 文獻定位：bass-5ffa911fd9b6: physicalp65 Table5.1 and Fig5.2。
- 使用數據部分：literature_locator: physicalp65 Table5.1 and Fig5.2；trial_binding: PI/material/geometry series mapping; only explicit trial IDs in a conclusion apply to individual trials；scope: 逐次索引為可用候選紀錄，不代表文獻使用其全部列。。
- 本組適用層級：本材料／幾何系列文獻結論；只有原文明寫Trial／圖板條件才直接適用。PI/material/geometry series mapping; only explicit trial IDs in a conclusion apply to individual trials M8為雙面2mm×1.2cm，單面頁僅作同章分析脈絡。。
- 使用／控制因子：trials: 20；not_tracked: M6；M12；M8_table_rates_mm_s: 0.057；0.056；0.04；M8_figurefit_slopes_mm_s: 0.0637；0.0557；0.0391；M8_figurefit_source_r2: 0.9575；0.9995；0.9989。
- 來源限制：Fig5.2 R²是原作者position-time擬合，非本輪模型驗證。。
- 搜尋句（改寫）：20個M試次有明確geometry/velocity/spread表；M6/M12未追蹤。M8同頁10cm/s表值與圖中來源回歸斜率不同，兩版都保留。。
- 來源：https://ntrs.nasa.gov/citations/20210011385
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/研究報告與書章/補下載/BASS-II Summary Report_e7fcef281a.pdf>)

### B25-SLAB-FLOW　B25-SLAB-FLOW

**Burning and Suppression of Solids-II (BASS-II) Summary Report**

M17逐段降流時soot減少、末焰變藍；兩側薄板寬度較大通常延燒更快。不同厚度、backing、O2與歷史須分開比較。

- 證據身份：來源觀察。
- 文獻定位：bass-5ffa911fd9b6: physicalpp66-70 Sec5.3-5.6; Figs5.3/5.5/5.8/5.9。
- 使用數據部分：literature_locator: physicalpp66-70 Sec5.3-5.6; Figs5.3/5.5/5.8/5.9；trial_binding: PI/material/geometry series mapping; only explicit trial IDs in a conclusion apply to individual trials；scope: 逐次索引為可用候選紀錄，不代表文獻使用其全部列。。
- 本組適用層級：本材料／幾何系列文獻結論；只有原文明寫Trial／圖板條件才直接適用。PI/material/geometry series mapping; only explicit trial IDs in a conclusion apply to individual trials。
- 使用／控制因子：M17_Table5_1_U_cm_s: 5；4；3；M17_spread_mm_s: 0.053；0.042；0.026。
- 來源限制：原表10→5→3→0顯示與作者選擇的穩態段速度不等價。；本章O2中間歷程是初末點線性內插假設。。
- 搜尋句（改寫）：M17逐段降流時soot減少、末焰變藍；兩側薄板寬度較大通常延燒更快。不同厚度、backing、O2與歷史須分開比較。。
- 來源：https://ntrs.nasa.gov/citations/20210011385
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/研究報告與書章/補下載/BASS-II Summary Report_e7fcef281a.pdf>)

### B25-SLAB-CONFLICT　B25-SLAB-CONFLICT

**Burning and Suppression of Solids-II (BASS-II) Summary Report**

同一弱焰圖的正文稱single-sided、圖說稱two-sided；僅隔離該圖的backing歸屬，不能挑一個標籤當真值。

- 證據身份：來源標示衝突待解。
- 文獻定位：bass-5ffa911fd9b6: physicalp66 body vsphysicalp67 Fig5.4(e,f)caption。
- 使用數據部分：literature_locator: physicalp66 body vsphysicalp67 Fig5.4(e,f)caption；trial_binding: PI/material/geometry series mapping; only explicit trial IDs in a conclusion apply to individual trials；scope: 逐次索引為可用候選紀錄，不代表文獻使用其全部列。。
- 本組適用層級：本材料／幾何系列文獻結論；只有原文明寫Trial／圖板條件才直接適用。PI/material/geometry series mapping; only explicit trial IDs in a conclusion apply to individual trials Fig5.4(e,f)受熱面未解，不計本組直接結果。。
- 使用／控制因子：。
- 來源限制：不把衝突圖綁成新的獨立試次；Table5.1的明確M試次欄位另存。。
- 搜尋句（改寫）：同一弱焰圖的正文稱single-sided、圖說稱two-sided；僅隔離該圖的backing歸屬，不能挑一個標籤當真值。。
- 來源：https://ntrs.nasa.gov/citations/20210011385
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/研究報告與書章/補下載/BASS-II Summary Report_e7fcef281a.pdf>)

### B25-SLAB-MODEL　B25-SLAB-MODEL

**Burning and Suppression of Solids-II (BASS-II) Summary Report**

FDS5.5.3 DNS例用3mm、平均10cm/s、.389×.376mm網格；225kW/m²是計算HRR。模型延燒快於實驗，作者提出調整物性/反應及網格驗證，未完成可靠全域預測。

- 證據身份：來源模型計算。
- 文獻定位：bass-5ffa911fd9b6: physicalpp68-71 Sec5.5-5.7 Figs5.6-5.9。
- 使用數據部分：literature_locator: physicalpp68-71 Sec5.5-5.7 Figs5.6-5.9；trial_binding: PI/material/geometry series mapping; only explicit trial IDs in a conclusion apply to individual trials；scope: 逐次索引為可用候選紀錄，不代表文獻使用其全部列。。
- 本組適用層級：本材料／幾何系列文獻結論；只有原文明寫Trial／圖板條件才直接適用。PI/material/geometry series mapping; only explicit trial IDs in a conclusion apply to individual trials。
- 使用／控制因子：model_peak_kW_m2: 225；grid_mm: 0.389；0.376。
- 來源限制：不是量測熱通量；沒有找到該例可執行原始FDS輸入檔。。
- 搜尋句（改寫）：FDS5.5.3 DNS例用3mm、平均10cm/s、.389×.376mm網格；225kW/m²是計算HRR。模型延燒快於實驗，作者提出調整物性/反應及網格驗證，未完成可靠全域預測。。
- 來源：https://ntrs.nasa.gov/citations/20210011385
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/研究報告與書章/補下載/BASS-II Summary Report_e7fcef281a.pdf>)

尚未取得可逐項對照的紀錄。

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
| B25-SLAB-RATES；B25-SLAB-FLOW；B25-SLAB-CONFLICT；B25-SLAB-MODEL | 同報告M系列；M8為雙面2mm×1.2cm，該來源分析差異只對應M8，不移作單面或其餘M試次 | 文獻表與影像回歸在部分流速段接近，模型同樣重視氣流與受熱面。 | M8的10cm/s表值與圖斜率不一致；Fig5.4正文／圖說受熱面標籤衝突屬另一圖，不能推翻Table5.1對M8的明確欄位；DNS也有延燒過快而非全面驗證。 |

## 4. 消防洞見

| 類別 | 對應證據 | 數據支持的判斷 | 策略／產品構想 | 待驗證 |
| --- | --- | --- | --- | --- |
| 預防 | B25-SLAB-RATES；B25-SLAB-MODEL | 來源包含不同受熱面／模型過預測或來源分析差異，不能以同材料名選任一預測器。 | 模型選擇先匹配幾何、受熱面、observable與試次身份。 | 補原始前緣軌跡及可執行原模型邊界條件，再作盲測。 |
| 偵測 | B25-SLAB-FLOW | 來源記錄變藍、soot減少或可見焰消失等光學變化；未提供本組煙警報效能。 | 把弱焰與減煙狀態納入偵測器挑戰試驗，保留熱／氣體獨立訊號。 | 匹配煙源、輸運、校準與啟用警報真值；不得由焰色推算漏報率。 |
| 撲滅／抑制 | 尚未取得／不適用 | 尚未建立本組可直接支持此用途的數據結論。 | 先補對應資料與試次匹配，再決定可測試策略；此處是研究缺口。 | 需本組材料、幾何、操作歷史與對應端點的量測；相近系列不能代替。 |

## 逐次索引

| 原始檔／資料位置 | Trial／Run／列 | 共享身份與保留事項 |
| --- | --- | --- |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 28；date: 2/20/2014；GMT: 51；test_number: M1；as_run: 尚未取得／不適用；sample: 222 | identity_notes: source_record_id: PSI-25-CSV-r28；raw_material: 1 mm thick PMMA   1 sided   2 cm；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Miller；Test #: M1；Date: 2/20/2014；GMT: 51；Sample #: 222；Fuel Sample Material: 1 mm thick PMMA   1 sided   2 cm；Flow restrictor: 2；Fan display: 58   54；Air display: 10  8；Radiometer gain   (1000   250   50   10): 50；Total Frames Shot: 304；Calibrated  initial O2 % by vol : 22.2；Calibrated final O2 % by vol: 21.9；Initial CO2 % by vol: 0.45；Final CO2 % by vol: 0.61；Initial CO (ppm): 0；Final CO (ppm): 60 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 29；date: 2/20/2014；GMT: 51；test_number: M2；as_run: 尚未取得／不適用；sample: 224 | identity_notes: source_record_id: PSI-25-CSV-r29；raw_material: 3 mm thick PMMA 1 sided    2 cm wide；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Miller；Test #: M2；Date: 2/20/2014；GMT: 51；Sample #: 224；Fuel Sample Material: 3 mm thick PMMA 1 sided    2 cm wide；Flow restrictor: 0；Fan display: 116 (pot 9.3)    89   80   84；Air display: 20  15  13   14；Radiometer gain   (1000   250   50   10): 50；Total Frames Shot: 262；Calibrated  initial O2 % by vol : 22.2；Calibrated final O2 % by vol: 21.2；Initial CO2 % by vol: 0.46；Final CO2 % by vol: 1.33；Initial CO (ppm): 12；Final CO (ppm): 325 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 30；date: 7/11/2014；GMT: 192；test_number: M3；as_run: 尚未取得／不適用；sample: 226m | identity_notes: source_record_id: PSI-25-CSV-r30；raw_material: 2 cm wide   5 mm thick 1 sided PMMA；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Miller；Test #: M3；Date: 7/11/2014；GMT: 192；Sample #: 226m；Fuel Sample Material: 2 cm wide   5 mm thick 1 sided PMMA；Flow restrictor: 2；Fan display: 3.0  3.1  3.2  6.4  5.5  5.4；Air display: 10   20  18；Radiometer gain   (1000   250   50   10): 250>50>250；Total Frames Shot: 223；Calibrated  initial O2 % by vol : 20.8；Calibrated final O2 % by vol: 19.7；Initial CO2 % by vol: 0.33；Final CO2 % by vol: 1.18；Initial CO (ppm): 11；Final CO (ppm): 300 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 41；date: 2/20/2014；GMT: 51；test_number: M14；as_run: 尚未取得／不適用；sample: 223 | identity_notes: source_record_id: PSI-25-CSV-r41；raw_material: 2mm thick PMMA   1 sided   2 cm wide；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Miller；Test #: M14；Date: 2/20/2014；GMT: 51；Sample #: 223；Fuel Sample Material: 2mm thick PMMA   1 sided   2 cm wide；Flow restrictor: 2；Fan display: pot 2.4   1.87  (54)；Air display: 10   ~8；Radiometer gain   (1000   250   50   10): 50；Total Frames Shot: 259；Calibrated  initial O2 % by vol : 22.2；Calibrated final O2 % by vol: 21.6；Initial CO2 % by vol: 0.45；Final CO2 % by vol: 0.98；Initial CO (ppm): 0；Final CO (ppm): 198 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 42；date: 7/7/2014；GMT: 188；test_number: M15；as_run: 尚未取得／不適用；sample: 225m | identity_notes: source_record_id: PSI-25-CSV-r42；raw_material: 2 cm   4 mm 1 sided PMMA slab；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Miller；Test #: M15；Date: 7/7/2014；GMT: 188；Sample #: 225m；Fuel Sample Material: 2 cm   4 mm 1 sided PMMA slab；Flow restrictor: 2；Fan display: ignited 10   adjusted down then up to 20   down in incrments to 15；Air display: 10   8  7  8  10  20  18  16  15；Radiometer gain   (1000   250   50   10): 10   250；Total Frames Shot: 153；Calibrated  initial O2 % by vol : 21；Calibrated final O2 % by vol: 20；Initial CO2 % by vol: 0.37；Final CO2 % by vol: 1.1；Initial CO (ppm): 1；Final CO (ppm): 220 |

## 缺件與適用範圍

- reportwidth1.2/2.2cm andCSV1/2cm retained as sourcevariants.
