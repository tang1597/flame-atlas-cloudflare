# clear PMMA棒：軸向stagnation

小資料集 ID：`B25-PMMA-clear-rod-stagnation`

## 資料身份與範圍

| 項目 | 內容 |
| --- | --- |
| NASA investigation | [PSI-25](https://psi.nasa.gov/physci/repo/data/investigations/PSI-25) |
| 材料／配方 | clear cast PMMA |
| 幾何 | cylindricalrod diameterfactor |
| 實驗模式 | axialstagnation/envelope; quench/blowoffhistory |
| 證據角色 | 固體火焰核心資料 |
| 環境 | ISS 微重力／來源指定的地面比較；逐次氣氛與流況不由材料名補值 |
| 資料粒度／共享試片 | 25 筆來源紀錄；獨立燃燒次數未自動確認；a/b、重複sample與階段保持原身份。 |
| 可用數值 | source_bound_observations_available |

## 1. 文獻結果與視覺化程式

### B25-ROD-IGNITION　B25-ROD-IGNITION

**Burning and Suppression of Solids-II (BASS-II) Summary Report**

clear棒點火時間與已預熱後維持燃燒界限不同；低O2較大棒最長約230s才穩定。

- 證據身份：source_observation_and_author_interpretation。
- 文獻定位：bass-5ffa911fd9b6: physicalpp75-77 Sec6.1.3/6.1.4.1 Fig6.2。
- 使用數據部分：literature_locator: physicalpp75-77 Sec6.1.3/6.1.4.1 Fig6.2；trial_binding: PI/material/geometry series mapping; only explicit trial IDs in a conclusion apply to individual trials；scope: 逐次索引為可用候選紀錄，不代表文獻使用其全部列。。
- 本組適用層級：本材料／幾何系列文獻結論；只有原文明寫Trial／圖板條件才直接適用。PI/material/geometry series mapping; only explicit trial IDs in a conclusion apply to individual trials。
- 使用／控制因子：longest_ignition_s_approx: 230；sustained_ignition_lower_O2_approx: 14.5；developed_flame_final_O2_low: 13.6。
- 來源限制：~14.5及13.6不構成所有材料/尺寸安全預設。。
- 搜尋句（改寫）：clear棒點火時間與已預熱後維持燃燒界限不同；低O2較大棒最長約230s才穩定。。
- 來源：https://ntrs.nasa.gov/citations/20210011385
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/研究報告與書章/補下載/BASS-II Summary Report_e7fcef281a.pdf>)

### B25-ROD-QUENCH　B25-ROD-QUENCH

**Burning and Suppression of Solids-II (BASS-II) Summary Report**

r=.476cm案例由14.8降至13.6%O2，來源整理穩態回退率.0385mm/s；火焰aspectL/W至.5、末流量改變超過100s後才quenched，保留固相延遲。

- 證據身份：來源觀察。
- 文獻定位：bass-5ffa911fd9b6: physicalpp77-80 Fig6.4/6.6。
- 使用數據部分：literature_locator: physicalpp77-80 Fig6.4/6.6；trial_binding: PI/material/geometry series mapping; only explicit trial IDs in a conclusion apply to individual trials；scope: 逐次索引為可用候選紀錄，不代表文獻使用其全部列。。
- 本組適用層級：本材料／幾何系列文獻結論；只有原文明寫Trial／圖板條件才直接適用。PI/material/geometry series mapping; only explicit trial IDs in a conclusion apply to individual trials。
- 使用／控制因子：r_cm: 0.476；O2_initial_final: 14.8；13.6；regression_mm_s: 0.0385；aspect_at_extinction: 0.5；after_last_flow_change_s: >100。
- 來源限制：此細節案例尚無已證原CSV trialjoin，不把其條件貼至所有O試次。。
- 搜尋句（改寫）：r=.476cm案例由14.8降至13.6%O2，來源整理穩態回退率.0385mm/s；火焰aspectL/W至.5、末流量改變超過100s後才quenched，保留固相延遲。。
- 來源：https://ntrs.nasa.gov/citations/20210011385
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/研究報告與書章/補下載/BASS-II Summary Report_e7fcef281a.pdf>)

### B25-O18-RECOVERY　B25-O18-RECOVERY

**Burning and Suppression of Solids-II (BASS-II) Summary Report**

O18一次局部吹離後9mm洞在降流7s閉合，55s後另一次10mm洞持續>60s未復原；是同一演變burn，不是兩次獨立成功率。

- 證據身份：來源觀察。
- 文獻定位：bass-5ffa911fd9b6: physicalpp81-82 Figs6.7/6.8; AppendixA.5 p118 O18/sample212m。
- 使用數據部分：literature_locator: physicalpp81-82 Figs6.7/6.8; AppendixA.5 p118 O18/sample212m；trial_binding: PI/material/geometry series mapping; only explicit trial IDs in a conclusion apply to individual trials；scope: 逐次索引為可用候選紀錄，不代表文獻使用其全部列。。
- 本組適用層級：本材料／幾何系列文獻結論；只有原文明寫Trial／圖板條件才直接適用。PI/material/geometry series mapping; only explicit trial IDs in a conclusion apply to individual trials。
- 使用／控制因子：first_hole_mm: 9；first_closure_s: 7；second_hole_mm: 10；second_persistence_s: >60。
- 來源限制：CO523→816ppm與O215.2→14.5為初末值，不能當兩次洞事件的同步量測。。
- 搜尋句（改寫）：O18一次局部吹離後9mm洞在降流7s閉合，55s後另一次10mm洞持續>60s未復原；是同一演變burn，不是兩次獨立成功率。。
- 來源：https://ntrs.nasa.gov/citations/20210011385
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/研究報告與書章/補下載/BASS-II Summary Report_e7fcef281a.pdf>)

### B25-ROD-BOUNDARY　B25-ROD-BOUNDARY

**Burning and Suppression of Solids-II (BASS-II) Summary Report**

最低可燃區約13.5%O2、標準化stretch8–12s⁻¹；standoff量測與估計convectiveheatflux/criticalT須分開。低氧CO/CO2比增加是來源群組觀察，不給暴露安全判定。

- 證據身份：source_measurement_empirical_boundary_and_inference。
- 文獻定位：bass-5ffa911fd9b6: physicalpp83-87 Figs6.9-6.16; Eq6.1。
- 使用數據部分：literature_locator: physicalpp83-87 Figs6.9-6.16; Eq6.1；trial_binding: PI/material/geometry series mapping; only explicit trial IDs in a conclusion apply to individual trials；scope: 逐次索引為可用候選紀錄，不代表文獻使用其全部列。。
- 本組適用層級：本材料／幾何系列文獻結論；只有原文明寫Trial／圖板條件才直接適用。PI/material/geometry series mapping; only explicit trial IDs in a conclusion apply to individual trials。
- 使用／控制因子：minimum_O2_vol_percent_approx: 13.5；normalized_stretch_min_s_inv: 8；12。
- 來源限制：臨界T與兩區能量balance是推導/反演，不是溫度直接量測。；O11/O14黑棒不可無條件套clear材質反演參數。。
- 搜尋句（改寫）：最低可燃區約13.5%O2、標準化stretch8–12s⁻¹；standoff量測與估計convectiveheatflux/criticalT須分開。低氧CO/CO2比增加是來源群組觀察，不給暴露安全判定。。
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
| B25-ROD-IGNITION；B25-ROD-QUENCH；B25-O18-RECOVERY；B25-ROD-BOUNDARY | PI/material/geometry series mapping; only explicit trial IDs in a conclusion apply to individual trials | 上述結論保留同材料系列各自觀察。 | 未確認完全同試次的第二篇獨立分析時不聲稱跨文獻一致；實驗觀察與作者解釋亦不互換。 |

## 4. 消防洞見

| 類別 | 對應證據 | 數據支持的判斷 | 策略／產品構想 | 待驗證 |
| --- | --- | --- | --- | --- |
| 預防 | B25-ROD-IGNITION；B25-ROD-BOUNDARY | 指定棒狀材料在不同重力／氧／流場的維持與點燃界限不同，且存在預熱延遲。 | 地面材料篩選與低重力持續燃燒分開評估，保留直徑及熱歷史。 | 同批配方、幾何、點火程序與局部流場的配對試驗。 |
| 撲滅／抑制 | B25-O18-RECOVERY；B25-ROD-QUENCH | 指定演變火焰可局部脫離後恢復，且固相熱歷史使最後熄焰有延遲。 | 抑制確認同時檢查火焰包覆、表面溫度及後續恢復。 | 獨立燃燒重複；局部洞消失或一次變流不是抑制成功率。 |
| 偵測 | 尚未取得／不適用 | 尚未建立本組可直接支持此用途的數據結論。 | 先補對應資料與試次匹配，再決定可測試策略；此處是研究缺口。 | 需本組材料、幾何、操作歷史與對應端點的量測；相近系列不能代替。 |

## 逐次索引

| 原始檔／資料位置 | Trial／Run／列 | 共享身份與保留事項 |
| --- | --- | --- |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 48；date: 2/18/2014；GMT: 49；test_number: O1；as_run: 尚未取得／不適用；sample: 207 | identity_notes: source_record_id: PSI-25-CSV-r48；raw_material: 1/4" clear rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Olson；Test #: O1；Date: 2/18/2014；GMT: 49；Sample #: 207；Fuel Sample Material: 1/4" clear rod；Flow restrictor: 2；Fan display: 89  62  50  41；Air display: 20  10  5  2  1；Radiometer gain   (1000   250   50   10): 50；Total Frames Shot: 62；Calibrated  initial O2 % by vol : 22.2；Calibrated final O2 % by vol: 21.7；Initial CO2 % by vol: 0.44；Final CO2 % by vol: 0.85；Initial CO (ppm): -1；Final CO (ppm): 51 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 49；date: 2/18/2014；GMT: 49；test_number: O2；as_run: 尚未取得／不適用；sample: 204 | identity_notes: source_record_id: PSI-25-CSV-r49；raw_material: 1/4" clear rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Olson；Test #: O2；Date: 2/18/2014；GMT: 49；Sample #: 204；Fuel Sample Material: 1/4" clear rod；Flow restrictor: 2；Fan display: .54 pot   0.45 pot；Air display: 0；Radiometer gain   (1000   250   50   10): 50；Total Frames Shot: 287；Calibrated  initial O2 % by vol : 22.2；Calibrated final O2 % by vol: 21.9；Initial CO2 % by vol: 0.44；Final CO2 % by vol: 0.59；Initial CO (ppm): -1；Final CO (ppm): 23 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 50；date: 6/13/2014；GMT: 164；test_number: O3a；as_run: 尚未取得／不適用；sample: 205M | identity_notes: source_record_id: PSI-25-CSV-r50；raw_material: 1/4" clear rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Olson；Test #: O3a；Date: 6/13/2014；GMT: 164；Sample #: 205M；Fuel Sample Material: 1/4" clear rod；Flow restrictor: 2；Fan display: 尚未取得／不適用；Air display: 5  3；Radiometer gain   (1000   250   50   10): 1000；Total Frames Shot: 85；Calibrated  initial O2 % by vol : 18；Calibrated final O2 % by vol: 18；Initial CO2 % by vol: 0.25；Final CO2 % by vol: 0.28；Initial CO (ppm): 16；Final CO (ppm): 22 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 51；date: 6/13/2014；GMT: 164；test_number: O3b；as_run: 尚未取得／不適用；sample: 205M | identity_notes: source_record_id: PSI-25-CSV-r51；raw_material: 1/4" clear rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Olson；Test #: O3b；Date: 6/13/2014；GMT: 164；Sample #: 205M；Fuel Sample Material: 1/4" clear rod；Flow restrictor: 2；Fan display: 尚未取得／不適用；Air display: 5  3  2  1  low；Radiometer gain   (1000   250   50   10): 1000   250；Total Frames Shot: 306；Calibrated  initial O2 % by vol : 18；Calibrated final O2 % by vol: 17.7；Initial CO2 % by vol: 0.28；Final CO2 % by vol: 0.53；Initial CO (ppm): 22；Final CO (ppm): 116 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 52；date: 7/8/2014；GMT: 189；test_number: O4；as_run: 尚未取得／不適用；sample: 216m | identity_notes: source_record_id: PSI-25-CSV-r52；raw_material: 3/8"clear rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Olson；Test #: O4；Date: 7/8/2014；GMT: 189；Sample #: 216m；Fuel Sample Material: 3/8"clear rod；Flow restrictor: 2；Fan display: 5   0.7   0.5   0.4   0.36 ext；Air display: 5   down to ext；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 249；Calibrated  initial O2 % by vol : 14.8；Calibrated final O2 % by vol: 13.6；Initial CO2 % by vol: 0.72；Final CO2 % by vol: 1.72；Initial CO (ppm): 290；Final CO (ppm): OR |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 53；date: 7/21/2014；GMT: 202；test_number: O5a；as_run: 尚未取得／不適用；sample: 220m | identity_notes: source_record_id: PSI-25-CSV-r53；raw_material: 1/2" clear PMMA rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Olson；Test #: O5a；Date: 7/21/2014；GMT: 202；Sample #: 220m；Fuel Sample Material: 1/2" clear PMMA rod；Flow restrictor: 2；Fan display: 1.3   2.7   1.3   0.7   0.45. 4.0；Air display: 5  10  5   2   0 (49   62   49   44   42)；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 164；Calibrated  initial O2 % by vol : 15.1；Calibrated final O2 % by vol: 14.2；Initial CO2 % by vol: 0.25；Final CO2 % by vol: 1.05；Initial CO (ppm): -2；Final CO (ppm): 496 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 54；date: 7/21/2014；GMT: 202；test_number: O5b；as_run: 尚未取得／不適用；sample: 220m | identity_notes: source_record_id: PSI-25-CSV-r54；raw_material: 1/2" clear PMMA rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Olson；Test #: O5b；Date: 7/21/2014；GMT: 202；Sample #: 220m；Fuel Sample Material: 1/2" clear PMMA rod；Flow restrictor: 2；Fan display: 1.3；Air display: 49   5 cm/s；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 2；Calibrated  initial O2 % by vol : 14.2；Calibrated final O2 % by vol: 14.1；Initial CO2 % by vol: 1.05；Final CO2 % by vol: 1.14；Initial CO (ppm): 496；Final CO (ppm): 590 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 55；date: 6/26/2014；GMT: 177；test_number: O6；as_run: 尚未取得／不適用；sample: 206M | identity_notes: source_record_id: PSI-25-CSV-r55；raw_material: 1/4" clear rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Olson；Test #: O6；Date: 6/26/2014；GMT: 177；Sample #: 206M；Fuel Sample Material: 1/4" clear rod；Flow restrictor: 2；Fan display: 5   .36  .32  .31  .305   out .275；Air display: see fan；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 241；Calibrated  initial O2 % by vol : 16.7；Calibrated final O2 % by vol: 16；Initial CO2 % by vol: 0.32；Final CO2 % by vol: 0.74；Initial CO (ppm): 1；Final CO (ppm): 232 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 56；date: 6/26/2014；GMT: 177；test_number: O7；as_run: 尚未取得／不適用；sample: 214m | identity_notes: source_record_id: PSI-25-CSV-r56；raw_material: 1/4" clear rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Olson；Test #: O7；Date: 6/26/2014；GMT: 177；Sample #: 214m；Fuel Sample Material: 1/4" clear rod；Flow restrictor: 2；Fan display: 5   .36  .32  ..305   blowoff fan max 10；Air display: 尚未取得／不適用；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 254；Calibrated  initial O2 % by vol : 16；Calibrated final O2 % by vol: 15.5；Initial CO2 % by vol: 0.74；Final CO2 % by vol: 1.27；Initial CO (ppm): 232；Final CO (ppm): 512 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 57；date: 6/26/2014；GMT: 177；test_number: O8a；as_run: 尚未取得／不適用；sample: 208m | identity_notes: source_record_id: PSI-25-CSV-r57；raw_material: 1/4" clear rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Olson；Test #: O8a；Date: 6/26/2014；GMT: 177；Sample #: 208m；Fuel Sample Material: 1/4" clear rod；Flow restrictor: 2；Fan display: 5   .36  .32  .31   extinguished；Air display: 尚未取得／不適用；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 133；Calibrated  initial O2 % by vol : 15.7；Calibrated final O2 % by vol: 15.3；Initial CO2 % by vol: 1.23；Final CO2 % by vol: 1.44；Initial CO (ppm): 436；Final CO (ppm): 536 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 58；date: 6/26/2014；GMT: 177；test_number: O8b；as_run: 尚未取得／不適用；sample: 208m | identity_notes: source_record_id: PSI-25-CSV-r58；raw_material: 1/4" clear rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Olson；Test #: O8b；Date: 6/26/2014；GMT: 177；Sample #: 208m；Fuel Sample Material: 1/4" clear rod；Flow restrictor: 2；Fan display: 5  .36  .32  .31 blowoff fan pot 6.0；Air display: 尚未取得／不適用；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 152；Calibrated  initial O2 % by vol : 15.5；Calibrated final O2 % by vol: 15.2；Initial CO2 % by vol: 1.44；Final CO2 % by vol: 1.74；Initial CO (ppm): 536；Final CO (ppm): 660 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 59；date: 6/26/2014；GMT: 177；test_number: O9；as_run: 尚未取得／不適用；sample: 209m | identity_notes: source_record_id: PSI-25-CSV-r59；raw_material: 1/4" clear rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Olson；Test #: O9；Date: 6/26/2014；GMT: 177；Sample #: 209m；Fuel Sample Material: 1/4" clear rod；Flow restrictor: 2；Fan display: 5   .36  .32 blowoff pt 4.0；Air display: 尚未取得／不適用；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 154；Calibrated  initial O2 % by vol : 15；Calibrated final O2 % by vol: 14.8；Initial CO2 % by vol: 1.74；Final CO2 % by vol: 1.96；Initial CO (ppm): 660；Final CO (ppm): 794 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 60；date: 7/22/2014；GMT: 213；test_number: O10；as_run: 尚未取得／不適用；sample: 210m | identity_notes: source_record_id: PSI-25-CSV-r60；raw_material: 1/4" clear rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Olson；Test #: O10；Date: 7/22/2014；GMT: 213；Sample #: 210m；Fuel Sample Material: 1/4" clear rod；Flow restrictor: 2；Fan display: 49  44  41   122 (1.3   0.7   0.4   0.36   0.32   10)；Air display: 5  2   0   max；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 172；Calibrated  initial O2 % by vol : 16.7；Calibrated final O2 % by vol: 16.1；Initial CO2 % by vol: 1.61；Final CO2 % by vol: 2.1；Initial CO (ppm): 94；Final CO (ppm): 287 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 62；date: 7/8/2014；GMT: 189；test_number: O12；as_run: 尚未取得／不適用；sample: 217m | identity_notes: source_record_id: PSI-25-CSV-r62；raw_material: 3/8" clear rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Olson；Test #: O12；Date: 7/8/2014；GMT: 189；Sample #: 217m；Fuel Sample Material: 3/8" clear rod；Flow restrictor: 2；Fan display: pots 1.4   3   0.9   0.7；Air display: no ign at any flow；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 52；Calibrated  initial O2 % by vol : 13.6；Calibrated final O2 % by vol: 13.5；Initial CO2 % by vol: 1.72；Final CO2 % by vol: 1.71；Initial CO (ppm): OR；Final CO (ppm): OR |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 63；date: 7/21/2014；GMT: 202；test_number: O13a；as_run: 尚未取得／不適用；sample: 221m | identity_notes: source_record_id: PSI-25-CSV-r63；raw_material: 1/2" clear PMMA rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Olson；Test #: O13a；Date: 7/21/2014；GMT: 202；Sample #: 221m；Fuel Sample Material: 1/2" clear PMMA rod；Flow restrictor: 2；Fan display: 1.3   0.7   0.45   0.36   0.32   0.31；Air display: 49  44  42  41  41  40.5 (5   2   0)；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 199；Calibrated  initial O2 % by vol : 15.9；Calibrated final O2 % by vol: 14.6；Initial CO2 % by vol: 0.91；Final CO2 % by vol: 1.85；Initial CO (ppm): 389；Final CO (ppm): 950 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 64；date: 7/21/2014；GMT: 202；test_number: O13b；as_run: 尚未取得／不適用；sample: 221m | identity_notes: source_record_id: PSI-25-CSV-r64；raw_material: 1/2" clear PMMA rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Olson；Test #: O13b；Date: 7/21/2014；GMT: 202；Sample #: 221m；Fuel Sample Material: 1/2" clear PMMA rod；Flow restrictor: 2；Fan display: 1.3   0.9；Air display: 7   4? (49   ?)；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 6；Calibrated  initial O2 % by vol : 14.6；Calibrated final O2 % by vol: 14.4；Initial CO2 % by vol: 1.85；Final CO2 % by vol: 2.09；Initial CO (ppm): 950；Final CO (ppm): over |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 66；date: 7/28/2014；GMT: 209；test_number: O15a；as_run: 尚未取得／不適用；sample: 218m | identity_notes: source_record_id: PSI-25-CSV-r66；raw_material: 3/8" clear rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Olson；Test #: O15a；Date: 7/28/2014；GMT: 209；Sample #: 218m；Fuel Sample Material: 3/8" clear rod；Flow restrictor: 2；Fan display: 57.5   47   42   41 (2.3   1.0   0.5   0.35   0.32)；Air display: 5  0；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 124；Calibrated  initial O2 % by vol : 17.1；Calibrated final O2 % by vol: 16.7；Initial CO2 % by vol: 0.27；Final CO2 % by vol: 0.62；Initial CO (ppm): 0；Final CO (ppm): 176 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 67；date: 7/28/2014；GMT: 209；test_number: O15b；as_run: 尚未取得／不適用；sample: 218m | identity_notes: source_record_id: PSI-25-CSV-r67；raw_material: 3/8" clear rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Olson；Test #: O15b；Date: 7/28/2014；GMT: 209；Sample #: 218m；Fuel Sample Material: 3/8" clear rod；Flow restrictor: 2；Fan display: 57.5   42   41   40 (2.3   0.5   0.35   0.34   0.33   0.32   0.31   0.30   0.29   0.28   0.27)；Air display: 5   0；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 316；Calibrated  initial O2 % by vol : 16.7；Calibrated final O2 % by vol: 15.6；Initial CO2 % by vol: 0.62；Final CO2 % by vol: 1.63；Initial CO (ppm): 176；Final CO (ppm): 751 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 68；date: 7/29/2014；GMT: 210；test_number: O16；as_run: 尚未取得／不適用；sample: 219m | identity_notes: source_record_id: PSI-25-CSV-r68；raw_material: 3/8"clear rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Olson；Test #: O16；Date: 7/29/2014；GMT: 210；Sample #: 219m；Fuel Sample Material: 3/8"clear rod；Flow restrictor: 2；Fan display: 60 (2.6)；Air display: 5；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 10 postburn only；Calibrated  initial O2 % by vol : 14.5；Calibrated final O2 % by vol: 14.5；Initial CO2 % by vol: 0.27；Final CO2 % by vol: 0.32；Initial CO (ppm): 2；Final CO (ppm): 33 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 69；date: 7/22/2014；GMT: 203；test_number: O17；as_run: 尚未取得／不適用；sample: 211m | identity_notes: source_record_id: PSI-25-CSV-r69；raw_material: 1/4" clear rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Olson；Test #: O17；Date: 7/22/2014；GMT: 203；Sample #: 211m；Fuel Sample Material: 1/4" clear rod；Flow restrictor: 2；Fan display: 49   46.5   44   42  41  72   decr (1.3   1.0   0.7   0.5   0.4   4.0   decr )；Air display: 3   0   11；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 174；Calibrated  initial O2 % by vol : 15.1；Calibrated final O2 % by vol: 14.3；Initial CO2 % by vol: 0.31；Final CO2 % by vol: 0.9；Initial CO (ppm): 2；Final CO (ppm): 377 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 70；date: 7/28/2014；GMT: 209；test_number: O18；as_run: 尚未取得／不適用；sample: 212m | identity_notes: source_record_id: PSI-25-CSV-r70；raw_material: 1/4" clear rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Olson；Test #: O18；Date: 7/28/2014；GMT: 209；Sample #: 212m；Fuel Sample Material: 1/4" clear rod；Flow restrictor: 2；Fan display: 57  51  47  72  51  72  51  47 (2.3   1.5   1.0   4.0   1.5   4.0   1.5   1.0)；Air display: 5  2  0  11  2  11  2  0；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 176；Calibrated  initial O2 % by vol : 15.2；Calibrated final O2 % by vol: 14.5；Initial CO2 % by vol: 1.45；Final CO2 % by vol: 1.94；Initial CO (ppm): 523；Final CO (ppm): 816 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 71；date: 8/1/2014；GMT: 213；test_number: O19；as_run: 尚未取得／不適用；sample: 213m | identity_notes: source_record_id: PSI-25-CSV-r71；raw_material: 1/4" clear rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Olson；Test #: O19；Date: 8/1/2014；GMT: 213；Sample #: 213m；Fuel Sample Material: 1/4" clear rod；Flow restrictor: 1；Fan display: 52   and down；Air display: 5 down to ext；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 266；Calibrated  initial O2 % by vol : 15.3；Calibrated final O2 % by vol: 14.6；Initial CO2 % by vol: 0.86；Final CO2 % by vol: 1.51；Initial CO (ppm): 352；Final CO (ppm): 686 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 72；date: 2/26/2016；GMT: 57；test_number: O20；as_run: 尚未取得／不適用；sample: 204m | identity_notes: source_record_id: PSI-25-CSV-r72；raw_material: 1/4" clear rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Olson；Test #: O20；Date: 2/26/2016；GMT: 57；Sample #: 204m；Fuel Sample Material: 1/4" clear rod；Flow restrictor: 0；Fan display: 49 (1.3 pot)   pots 7   8  9   10；Air display: 5   8    incr to max 38.5；Radiometer gain   (1000   250   50   10): 50；Total Frames Shot: video；Calibrated  initial O2 % by vol : 16.5；Calibrated final O2 % by vol: 15.9；Initial CO2 % by vol: 0.2；Final CO2 % by vol: 0.57；Initial CO (ppm): -3；Final CO (ppm): 57 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 73；date: 2/26/2016；GMT: 57；test_number: O21；as_run: 尚未取得／不適用；sample: 219m | identity_notes: source_record_id: PSI-25-CSV-r73；raw_material: 3/8" clear rod；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Olson；Test #: O21；Date: 2/26/2016；GMT: 57；Sample #: 219m；Fuel Sample Material: 3/8" clear rod；Flow restrictor: 0；Fan display: 46 (pot 0.8)    pot 7   10；Air display: incr to 28；Radiometer gain   (1000   250   50   10): 50；Total Frames Shot: video；Calibrated  initial O2 % by vol : 15.9；Calibrated final O2 % by vol: 15.4；Initial CO2 % by vol: 0.53；Final CO2 % by vol: 0.95；Initial CO (ppm): 52；Final CO (ppm): 187 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 74；date: 2/26/2016；GMT: 57；test_number: O22；as_run: 尚未取得／不適用；sample: 220m | identity_notes: source_record_id: PSI-25-CSV-r74；raw_material: 1/2" clear rod ；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Olson；Test #: O22；Date: 2/26/2016；GMT: 57；Sample #: 220m；Fuel Sample Material: 1/2" clear rod ；Flow restrictor: 0；Fan display: 49 (pot 1.1)   blowoff pot 5   out at fan 87；Air display: 4 incr to 26.5；Radiometer gain   (1000   250   50   10): 50；Total Frames Shot: video；Calibrated  initial O2 % by vol : 15.4；Calibrated final O2 % by vol: 14.9；Initial CO2 % by vol: 0.92；Final CO2 % by vol: 1.33；Initial CO (ppm): 185；Final CO (ppm): 322 |

## 缺件與適用範圍

- Oa/b或重用sample不能當獨立樣本；black與clear的反演參數不默認相同。
