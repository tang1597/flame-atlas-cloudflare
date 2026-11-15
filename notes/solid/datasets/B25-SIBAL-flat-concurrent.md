# SIBAL薄織物：順流

小資料集 ID：`B25-SIBAL-flat-concurrent`

## 資料身份與範圍

| 項目 | 內容 |
| --- | --- |
| NASA investigation | [PSI-25](https://psi.nasa.gov/physci/repo/data/investigations/PSI-25) |
| 材料／配方 | cotton/fiberglassSIBAL |
| 幾何 | flatwovenstrips; nominal1/2cm vs1.2/2.2cm publication |
| 實驗模式 | concurrent |
| 證據角色 | 固體火焰核心資料 |
| 環境 | ISS 微重力／來源指定的地面比較；逐次氣氛與流況不由材料名補值 |
| 資料粒度／共享試片 | 27 筆來源紀錄；獨立燃燒次數未自動確認；a/b、重複sample與階段保持原身份。 |
| 可用數值 | source_bound_observations_available |

## 1. 文獻結果與視覺化程式

### B25-SIBAL-FLOW　B25-SIBAL-FLOW

**Burning and Suppression of Solids-II (BASS-II) Summary Report**

SIBAL順流quenching得到1–5cm/s分支，較低O2所需quenchflow較高；1.2cm窄樣本下界未解析，最低O2平坦區亦未由此變速程序確認。

- 證據身份：來源觀察。
- 文獻定位：bass-5ffa911fd9b6: physicalpp101-109 Sec7.1; Table7.1p104/Fig7.7p108。
- 使用數據部分：literature_locator: physicalpp101-109 Sec7.1; Table7.1p104/Fig7.7p108；trial_binding: PI/material/geometry series mapping; only explicit trial IDs in a conclusion apply to individual trials；scope: 逐次索引為可用候選紀錄，不代表文獻使用其全部列。。
- 本組適用層級：本材料／幾何系列文獻結論；只有原文明寫Trial／圖板條件才直接適用。PI/material/geometry series mapping; only explicit trial IDs in a conclusion apply to individual trials。
- 使用／控制因子：quenching_range_cm_s: 1；5；quenching_cases: 6；wide_cases_among_quench: 4。
- 來源限制：不是通用fan-off消防程序；1/2cm CSV與1.2/2.2cm文稿寬度兩種標示保留。。
- 搜尋句（改寫）：SIBAL順流quenching得到1–5cm/s分支，較低O2所需quenchflow較高；1.2cm窄樣本下界未解析，最低O2平坦區亦未由此變速程序確認。。
- 來源：https://ntrs.nasa.gov/citations/20210011385
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/研究報告與書章/補下載/BASS-II Summary Report_e7fcef281a.pdf>)

### B25-T20　B25-T20

**Burning and Suppression of Solids-II (BASS-II) Summary Report**

T20/sample144m在17.2%O2初末、11→3cm/s後快速熄滅；無熄滅秒數。

- 證據身份：來源觀察。
- 文獻定位：bass-5ffa911fd9b6: physicalp120TableA.6T20 + p104Table7.1GMT190-T20。
- 使用數據部分：literature_locator: physicalp120TableA.6T20 + p104Table7.1GMT190-T20；trial_binding: PI/material/geometry series mapping; only explicit trial IDs in a conclusion apply to individual trials；scope: 逐次索引為可用候選紀錄，不代表文獻使用其全部列。。
- 本組適用層級：本材料／幾何系列文獻結論；只有原文明寫Trial／圖板條件才直接適用。PI/material/geometry series mapping; only explicit trial IDs in a conclusion apply to individual trials。
- 使用／控制因子：flow_readout_cm_s: 11；3；O2_initial_final: 17.2；17.2；CO_initial_final_ppm: 20；34。
- 來源限制：不是PMMA O18；氣體初末不識別降流造成CO或熄滅後產氣。。
- 搜尋句（改寫）：T20/sample144m在17.2%O2初末、11→3cm/s後快速熄滅；無熄滅秒數。。
- 來源：https://ntrs.nasa.gov/citations/20210011385
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/研究報告與書章/補下載/BASS-II Summary Report_e7fcef281a.pdf>)

尚未取得可逐項對照的紀錄。

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
| B25-SIBAL-FLOW；B25-T20 | PI/material/geometry series mapping; only explicit trial IDs in a conclusion apply to individual trials | 上述結論保留同材料系列各自觀察。 | 未確認完全同試次的第二篇獨立分析時不聲稱跨文獻一致；實驗觀察與作者解釋亦不互換。 |

## 4. 消防洞見

| 類別 | 對應證據 | 數據支持的判斷 | 策略／產品構想 | 待驗證 |
| --- | --- | --- | --- | --- |
| 撲滅／抑制 | B25-SIBAL-FLOW；B25-T20 | 指定案例降流後熄滅，但另有低流仍燃至燃料耗盡的來源；介入成效具材料與狀態依賴。 | 以火焰／熱反應回饋檢驗降流，而非採跨材料固定流速作停止條件。 | 同幾何、氧與熱歷史的流速介入試驗，區分耗盡與全局熄滅。 |
| 預防 | 尚未取得／不適用 | 尚未建立本組可直接支持此用途的數據結論。 | 先補對應資料與試次匹配，再決定可測試策略；此處是研究缺口。 | 需本組材料、幾何、操作歷史與對應端點的量測；相近系列不能代替。 |
| 偵測 | 尚未取得／不適用 | 尚未建立本組可直接支持此用途的數據結論。 | 先補對應資料與試次匹配，再決定可測試策略；此處是研究缺口。 | 需本組材料、幾何、操作歷史與對應端點的量測；相近系列不能代替。 |

## 逐次索引

| 原始檔／資料位置 | Trial／Run／列 | 共享身份與保留事項 |
| --- | --- | --- |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 102；date: 2/14/2014；GMT: 45；test_number: T1；as_run: 尚未取得／不適用；sample: 128 | identity_notes: source_record_id: PSI-25-CSV-r102；raw_material: 2 cm SIBAL；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: T'ien；Test #: T1；Date: 2/14/2014；GMT: 45；Sample #: 128；Fuel Sample Material: 2 cm SIBAL；Flow restrictor: 2；Fan display: 80；Air display: 10；Radiometer gain   (1000   250   50   10): 50；Total Frames Shot: 85；Calibrated  initial O2 % by vol : 18.5；Calibrated final O2 % by vol: 18.5；Initial CO2 % by vol: 0.35；Final CO2 % by vol: 0.41；Initial CO (ppm): 0；Final CO (ppm): 40 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 103；date: 2/14/2014；GMT: 45；test_number: T2；as_run: 尚未取得／不適用；sample: 129 | identity_notes: source_record_id: PSI-25-CSV-r103；raw_material: 2 cm SIBAL；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: T'ien；Test #: T2；Date: 2/14/2014；GMT: 45；Sample #: 129；Fuel Sample Material: 2 cm SIBAL；Flow restrictor: 2；Fan display: 80   59   55；Air display: 9   5   4；Radiometer gain   (1000   250   50   10): 50；Total Frames Shot: 100；Calibrated  initial O2 % by vol : 18.5；Calibrated final O2 % by vol: 18.5；Initial CO2 % by vol: 0.41；Final CO2 % by vol: 0.45；Initial CO (ppm): 40；Final CO (ppm): 78 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 105；date: 2/14/2014；GMT: 45；test_number: T4；as_run: 尚未取得／不適用；sample: 130 | identity_notes: source_record_id: PSI-25-CSV-r105；raw_material: 2 cm SIBAL；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: T'ien；Test #: T4；Date: 2/14/2014；GMT: 45；Sample #: 130；Fuel Sample Material: 2 cm SIBAL；Flow restrictor: 2；Fan display: 80   46；Air display: 9  1；Radiometer gain   (1000   250   50   10): 50；Total Frames Shot: 97；Calibrated  initial O2 % by vol : 18.7；Calibrated final O2 % by vol: 18.7；Initial CO2 % by vol: 0.44；Final CO2 % by vol: 0.45；Initial CO (ppm): 59；Final CO (ppm): 72 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 106；date: 4/10/2014；GMT: 100；test_number: T5；as_run: 尚未取得／不適用；sample: 131 | identity_notes: source_record_id: PSI-25-CSV-r106；raw_material: 2 cm SIBAL；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: T'ien；Test #: T5；Date: 4/10/2014；GMT: 100；Sample #: 131；Fuel Sample Material: 2 cm SIBAL；Flow restrictor: 2；Fan display: 2.72   0.50   0.42；Air display: 10   2   1；Radiometer gain   (1000   250   50   10): 50；Total Frames Shot: 100；Calibrated  initial O2 % by vol : 18.8；Calibrated final O2 % by vol: 18.9；Initial CO2 % by vol: 0.2；Final CO2 % by vol: 0.25；Initial CO (ppm): 2；Final CO (ppm): 41 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 107；date: 4/10/2014；GMT: 100；test_number: T6；as_run: 尚未取得／不適用；sample: 132 | identity_notes: source_record_id: PSI-25-CSV-r107；raw_material: 2 cm SIBAL；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: T'ien；Test #: T6；Date: 4/10/2014；GMT: 100；Sample #: 132；Fuel Sample Material: 2 cm SIBAL；Flow restrictor: 2；Fan display: 尚未取得／不適用；Air display: 5  2  1   <1；Radiometer gain   (1000   250   50   10): 50；Total Frames Shot: 117；Calibrated  initial O2 % by vol : 18.8；Calibrated final O2 % by vol: 18.8；Initial CO2 % by vol: 0.24；Final CO2 % by vol: 0.28；Initial CO (ppm): 39；Final CO (ppm): 77 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 109；date: 6/24/2018；GMT: 175；test_number: T9；as_run: 尚未取得／不適用；sample: 133M | identity_notes: source_record_id: PSI-25-CSV-r109；raw_material: 2 cm SIBAL；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: T'ien；Test #: T9；Date: 6/24/2018；GMT: 175；Sample #: 133M；Fuel Sample Material: 2 cm SIBAL；Flow restrictor: 2；Fan display: pot 2.5；Air display: 10；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 48；Calibrated  initial O2 % by vol : 16.4；Calibrated final O2 % by vol: 16.4；Initial CO2 % by vol: 0.3；Final CO2 % by vol: 0.31；Initial CO (ppm): 0；Final CO (ppm): 9 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 110；date: 6/24/2014；GMT: 175；test_number: T10；as_run: 尚未取得／不適用；sample: 134M | identity_notes: source_record_id: PSI-25-CSV-r110；raw_material: 2 cm SIBAL；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: T'ien；Test #: T10；Date: 6/24/2014；GMT: 175；Sample #: 134M；Fuel Sample Material: 2 cm SIBAL；Flow restrictor: 2；Fan display: pot 1.1；Air display: 5；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 43；Calibrated  initial O2 % by vol : 16.4；Calibrated final O2 % by vol: 16.5；Initial CO2 % by vol: 0.31；Final CO2 % by vol: 0.33；Initial CO (ppm): 9；Final CO (ppm): 14 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 111；date: 6/27/2014；GMT: 178；test_number: T11；as_run: 尚未取得／不適用；sample: 135m | identity_notes: source_record_id: PSI-25-CSV-r111；raw_material: 2 cm SIBAL；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: T'ien；Test #: T11；Date: 6/27/2014；GMT: 178；Sample #: 135m；Fuel Sample Material: 2 cm SIBAL；Flow restrictor: 2；Fan display: 48；Air display: 5；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 109；Calibrated  initial O2 % by vol : 17.1；Calibrated final O2 % by vol: 17；Initial CO2 % by vol: 0.35；Final CO2 % by vol: 0.39；Initial CO (ppm): 1；Final CO (ppm): 45 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 112；date: 6/27/2014；GMT: 178；test_number: T12；as_run: 尚未取得／不適用；sample: 136m | identity_notes: source_record_id: PSI-25-CSV-r112；raw_material: 2 cm SIBAL；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: T'ien；Test #: T12；Date: 6/27/2014；GMT: 178；Sample #: 136m；Fuel Sample Material: 2 cm SIBAL；Flow restrictor: 2；Fan display: pot 1.1；Air display: 5；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 39；Calibrated  initial O2 % by vol : 16.8；Calibrated final O2 % by vol: 16.9；Initial CO2 % by vol: 0.7；Final CO2 % by vol: 0.7；Initial CO (ppm): 113；Final CO (ppm): 117 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 113；date: 4/10/2014；GMT: 100；test_number: T13；as_run: 尚未取得／不適用；sample: 137 | identity_notes: source_record_id: PSI-25-CSV-r113；raw_material: 2 cm SIBAL；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: T'ien；Test #: T13；Date: 4/10/2014；GMT: 100；Sample #: 137；Fuel Sample Material: 2 cm SIBAL；Flow restrictor: 2；Fan display: 尚未取得／不適用；Air display: 5  1；Radiometer gain   (1000   250   50   10): 50；Total Frames Shot: 55；Calibrated  initial O2 % by vol : 17.5；Calibrated final O2 % by vol: 17.6；Initial CO2 % by vol: 0.19；Final CO2 % by vol: 0.2；Initial CO (ppm): 2；Final CO (ppm): 12 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 114；date: 6/27/2014；GMT: 178；test_number: T14；as_run: 尚未取得／不適用；sample: 140m | identity_notes: source_record_id: PSI-25-CSV-r114；raw_material: 2 cm SIBAL；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: T'ien；Test #: T14；Date: 6/27/2014；GMT: 178；Sample #: 140m；Fuel Sample Material: 2 cm SIBAL；Flow restrictor: 2；Fan display: 尚未取得／不適用；Air display: 5  3；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 119；Calibrated  initial O2 % by vol : 16.9；Calibrated final O2 % by vol: 16.9；Initial CO2 % by vol: 0.7；Final CO2 % by vol: 0.72；Initial CO (ppm): 117；Final CO (ppm): 152 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 115；date: 2/14/2014；GMT: 45；test_number: T15；as_run: 尚未取得／不適用；sample: 138 | identity_notes: source_record_id: PSI-25-CSV-r115；raw_material: 2 cm SIBAL；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: T'ien；Test #: T15；Date: 2/14/2014；GMT: 45；Sample #: 138；Fuel Sample Material: 2 cm SIBAL；Flow restrictor: 0；Fan display: 80122；Air display: 9   29；Radiometer gain   (1000   250   50   10): 50；Total Frames Shot: 46；Calibrated  initial O2 % by vol : 18.7；Calibrated final O2 % by vol: 18.7；Initial CO2 % by vol: 0.45；Final CO2 % by vol: 0.51；Initial CO (ppm): 72；Final CO (ppm): 102 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 116；date: 4/10/2014；GMT: 100；test_number: T16；as_run: 尚未取得／不適用；sample: 139 | identity_notes: source_record_id: PSI-25-CSV-r116；raw_material: 2 cm SIBAL；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: T'ien；Test #: T16；Date: 4/10/2014；GMT: 100；Sample #: 139；Fuel Sample Material: 2 cm SIBAL；Flow restrictor: 2；Fan display: 尚未取得／不適用；Air display: 5  3；Radiometer gain   (1000   250   50   10): 50；Total Frames Shot: 100；Calibrated  initial O2 % by vol : 17.6；Calibrated final O2 % by vol: 17.5；Initial CO2 % by vol: 0.21；Final CO2 % by vol: 0.21；Initial CO (ppm): 17；Final CO (ppm): 41 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 117；date: 6/27/2014；GMT: 178；test_number: T17；as_run: 尚未取得／不適用；sample: 142m | identity_notes: source_record_id: PSI-25-CSV-r117；raw_material: 2 cm SIBAL；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: T'ien；Test #: T17；Date: 6/27/2014；GMT: 178；Sample #: 142m；Fuel Sample Material: 2 cm SIBAL；Flow restrictor: 0；Fan display: 尚未取得／不適用；Air display: 6   53；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 83；Calibrated  initial O2 % by vol : 16.9；Calibrated final O2 % by vol: 16.9；Initial CO2 % by vol: 0.72；Final CO2 % by vol: 0.75；Initial CO (ppm): 152；Final CO (ppm): 190 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 118；date: 6/24/2018；GMT: 175；test_number: T18；as_run: 尚未取得／不適用；sample: 141M | identity_notes: source_record_id: PSI-25-CSV-r118；raw_material: 2 cm SIBAL；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: T'ien；Test #: T18；Date: 6/24/2018；GMT: 175；Sample #: 141M；Fuel Sample Material: 2 cm SIBAL；Flow restrictor: 2；Fan display: 尚未取得／不適用；Air display: 5  2；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 49；Calibrated  initial O2 % by vol : 17.4；Calibrated final O2 % by vol: 17.4；Initial CO2 % by vol: 0.36；Final CO2 % by vol: 0.38；Initial CO (ppm): 2；Final CO (ppm): 22 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 119；date: 7/9/2014；GMT: 190；test_number: T19；as_run: 尚未取得／不適用；sample: 143m | identity_notes: source_record_id: PSI-25-CSV-r119；raw_material: 1 cm SIBAL；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: T'ien；Test #: T19；Date: 7/9/2014；GMT: 190；Sample #: 143m；Fuel Sample Material: 1 cm SIBAL；Flow restrictor: 2；Fan display: 68.5   pot 3.6；Air display: 11；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 73；Calibrated  initial O2 % by vol : 17.2；Calibrated final O2 % by vol: 17.2；Initial CO2 % by vol: 0.29；Final CO2 % by vol: 0.31；Initial CO (ppm): 1；Final CO (ppm): 20 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 120；date: 7/9/2014；GMT: 190；test_number: T20；as_run: 尚未取得／不適用；sample: 144m | identity_notes: source_record_id: PSI-25-CSV-r120；raw_material: 1 cm SIBAL；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: T'ien；Test #: T20；Date: 7/9/2014；GMT: 190；Sample #: 144m；Fuel Sample Material: 1 cm SIBAL；Flow restrictor: 2；Fan display: 3.6   0.9；Air display: 11   3；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 117；Calibrated  initial O2 % by vol : 17.2；Calibrated final O2 % by vol: 17.2；Initial CO2 % by vol: 0.31；Final CO2 % by vol: 0.31；Initial CO (ppm): 20；Final CO (ppm): 34 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 121；date: 7/9/2014；GMT: 190；test_number: T21；as_run: 尚未取得／不適用；sample: 145m | identity_notes: source_record_id: PSI-25-CSV-r121；raw_material: 1 cm SIBAL；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: T'ien；Test #: T21；Date: 7/9/2014；GMT: 190；Sample #: 145m；Fuel Sample Material: 1 cm SIBAL；Flow restrictor: 0；Fan display: 1.6 pot   52；Air display: 11   max(47)；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 151；Calibrated  initial O2 % by vol : 17.2；Calibrated final O2 % by vol: 17.2；Initial CO2 % by vol: 0.31；Final CO2 % by vol: 0.32；Initial CO (ppm): 34；Final CO (ppm): 45 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 122；date: 7/9/2014；GMT: 190；test_number: T22；as_run: 尚未取得／不適用；sample: 146m | identity_notes: source_record_id: PSI-25-CSV-r122；raw_material: 1 cm SIBAL；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: T'ien；Test #: T22；Date: 7/9/2014；GMT: 190；Sample #: 146m；Fuel Sample Material: 1 cm SIBAL；Flow restrictor: 2；Fan display: 3.4   1.7；Air display: 10   5；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 38；Calibrated  initial O2 % by vol : 17.1；Calibrated final O2 % by vol: 17；Initial CO2 % by vol: 0.59；Final CO2 % by vol: 0.62；Initial CO (ppm): 140；Final CO (ppm): 162 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 123；date: 7/9/2014；GMT: 190；test_number: T23；as_run: 尚未取得／不適用；sample: 133m | identity_notes: source_record_id: PSI-25-CSV-r123；raw_material: 2 cm Sibal   moved igniter；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: T'ien；Test #: T23；Date: 7/9/2014；GMT: 190；Sample #: 133m；Fuel Sample Material: 2 cm Sibal   moved igniter；Flow restrictor: 2；Fan display: 3.3   66；Air display: 10；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 203；Calibrated  initial O2 % by vol : 17.2；Calibrated final O2 % by vol: 17.3；Initial CO2 % by vol: 0.32；Final CO2 % by vol: 0.32；Initial CO (ppm): 45；Final CO (ppm): 49 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 124；date: 7/9/2014；GMT: 190；test_number: T24；as_run: 尚未取得／不適用；sample: 133m | identity_notes: source_record_id: PSI-25-CSV-r124；raw_material: 1 cm SIBAL   top side ign；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: T'ien；Test #: T24；Date: 7/9/2014；GMT: 190；Sample #: 133m；Fuel Sample Material: 1 cm SIBAL   top side ign；Flow restrictor: 2；Fan display: 3.3 66；Air display: 10；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 130；Calibrated  initial O2 % by vol : 18.2；Calibrated final O2 % by vol: 18.2；Initial CO2 % by vol: 0.51；Final CO2 % by vol: 0.53；Initial CO (ppm): 85；Final CO (ppm): 107 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 125；date: 8/4/2014；GMT: 216；test_number: T25；as_run: 尚未取得／不適用；sample: 138m | identity_notes: source_record_id: PSI-25-CSV-r125；raw_material: 2 cm SIBAL；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: T'ien；Test #: T25；Date: 8/4/2014；GMT: 216；Sample #: 138m；Fuel Sample Material: 2 cm SIBAL；Flow restrictor: 1；Fan display: 53   45；Air display: 5   2.5；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 75；Calibrated  initial O2 % by vol : 20.8；Calibrated final O2 % by vol: 20.7；Initial CO2 % by vol: 0.36；Final CO2 % by vol: 0.39；Initial CO (ppm): -1；Final CO (ppm): 17 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 126；date: 8/4/2014；GMT: 216；test_number: T26；as_run: 尚未取得／不適用；sample: 137m | identity_notes: source_record_id: PSI-25-CSV-r126；raw_material: 2 cm SIBAL；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: T'ien；Test #: T26；Date: 8/4/2014；GMT: 216；Sample #: 137m；Fuel Sample Material: 2 cm SIBAL；Flow restrictor: 1；Fan display: 53   45；Air display: 5   2.5；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 87；Calibrated  initial O2 % by vol : 20.8；Calibrated final O2 % by vol: 20.7；Initial CO2 % by vol: 0.36；Final CO2 % by vol: 0.43；Initial CO (ppm): -1；Final CO (ppm): 24 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 127；date: 8/4/2014；GMT: 216；test_number: T27；as_run: 尚未取得／不適用；sample: 146m | identity_notes: source_record_id: PSI-25-CSV-r127；raw_material: 1 cm SIBAL；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: T'ien；Test #: T27；Date: 8/4/2014；GMT: 216；Sample #: 146m；Fuel Sample Material: 1 cm SIBAL；Flow restrictor: 1；Fan display: 53   45；Air display: 5   2；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 58；Calibrated  initial O2 % by vol : 20.7；Calibrated final O2 % by vol: 20.6；Initial CO2 % by vol: 0.41；Final CO2 % by vol: 0.42；Initial CO (ppm): -1；Final CO (ppm): 9 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 128；date: 8/4/2014；GMT: 216；test_number: T28a；as_run: 尚未取得／不適用；sample: 144m | identity_notes: source_record_id: PSI-25-CSV-r128；raw_material: 1 cm SIBAL；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: T'ien；Test #: T28a；Date: 8/4/2014；GMT: 216；Sample #: 144m；Fuel Sample Material: 1 cm SIBAL；Flow restrictor: 1；Fan display: 53；Air display: 5；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 19；Calibrated  initial O2 % by vol : 20.7；Calibrated final O2 % by vol: 0.9；Initial CO2 % by vol: 0.41；Final CO2 % by vol: none；Initial CO (ppm): -1；Final CO (ppm): none |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 129；date: 8/4/2014；GMT: 216；test_number: T28b；as_run: 尚未取得／不適用；sample: 144m | identity_notes: source_record_id: PSI-25-CSV-r129；raw_material: 1 cm SIBAL；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: T'ien；Test #: T28b；Date: 8/4/2014；GMT: 216；Sample #: 144m；Fuel Sample Material: 1 cm SIBAL；Flow restrictor: 1；Fan display: 53；Air display: 5；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 27；Calibrated  initial O2 % by vol : 20.7；Calibrated final O2 % by vol: 40.4；Initial CO2 % by vol: none；Final CO2 % by vol: 0.42；Initial CO (ppm): none；Final CO (ppm): 2 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 130；date: 8/4/2014；GMT: 216；test_number: T29；as_run: 尚未取得／不適用；sample: 145m | identity_notes: source_record_id: PSI-25-CSV-r130；raw_material: 1 cm SIBAL；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: T'ien；Test #: T29；Date: 8/4/2014；GMT: 216；Sample #: 145m；Fuel Sample Material: 1 cm SIBAL；Flow restrictor: 1；Fan display: 53   43；Air display: 5   2(?)；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 60；Calibrated  initial O2 % by vol : 20.7；Calibrated final O2 % by vol: 20.5；Initial CO2 % by vol: 0.41；Final CO2 % by vol: 0.44；Initial CO (ppm): -1；Final CO (ppm): 10 |

## 缺件與適用範圍

- T28a/b sample144m曾在T20用過，保留歷史而非新replicates。
