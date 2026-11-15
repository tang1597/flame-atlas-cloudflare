# PMMA薄膜：逆流、100–400µm

小資料集 ID：`B25-PMMA-film-opposed`

## 資料身份與範圍

| 項目 | 內容 |
| --- | --- |
| NASA investigation | [PSI-25](https://psi.nasa.gov/physci/repo/data/investigations/PSI-25) |
| 材料／配方 | PMMA film; grade/color notspecifiedinCSV |
| 幾何 | flat thin film; thickness/width factors |
| 實驗模式 | opposed |
| 證據角色 | 固體火焰核心資料 |
| 環境 | ISS 微重力／來源指定的地面比較；逐次氣氛與流況不由材料名補值 |
| 資料粒度／共享試片 | 22 筆來源紀錄；獨立燃燒次數未自動確認；a/b、重複sample與階段保持原身份。 |
| 可用數值 | source_bound_observations_available |

## 1. 文獻結果與視覺化程式

### B25-FILM-THERMAL　B25-FILM-THERMAL

**Burning and Suppression of Solids-II (BASS-II) Summary Report**

薄片熱控極限可用半厚度反比式描述；100µm地面平均2.0mm/s與ISS同厚度最大約2.2mm/s是不同統計/流況，不形成純重力比。

- 證據身份：來源量測與理論分列。
- 文獻定位：bass-5ffa911fd9b6: physicalpp39-50 Sec2.3; Eq2.11 p49, Eq2.12/Fig2.21 p50。
- 使用數據部分：literature_locator: physicalpp39-50 Sec2.3; Eq2.11 p49, Eq2.12/Fig2.21 p50；trial_binding: PI/material/geometry series mapping; only explicit trial IDs in a conclusion apply to individual trials；scope: 逐次索引為可用候選紀錄，不代表文獻使用其全部列。。
- 本組適用層級：本材料／幾何系列文獻結論；只有原文明寫Trial／圖板條件才直接適用。PI/material/geometry series mapping; only explicit trial IDs in a conclusion apply to individual trials。
- 使用／控制因子：ground100um_mean_mm_s: 2.0；ISS100um_max_approx_mm_s: 2.2。
- 來源限制：厚度數值來自原文，不是使用者workbook直接枚舉條件。；F_adb4.89與F_expt4.76為不同來源角色，不互換。。
- 搜尋句（改寫）：薄片熱控極限可用半厚度反比式描述；100µm地面平均2.0mm/s與ISS同厚度最大約2.2mm/s是不同統計/流況，不形成純重力比。。
- 來源：https://ntrs.nasa.gov/citations/20210011385
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/研究報告與書章/補下載/BASS-II Summary Report_e7fcef281a.pdf>)

### B25-FILM-REGIMES　B25-FILM-REGIMES

**Radiative, thermal, and kinetic regimes of opposed-flow flame spread: A comparison between experiment and theory**

100/200µm PMMA的影像/延燒整理涵蓋輻射、熱控、動力學區；原文提醒流速與延燒點配對有顯著不確定性，profile形狀宜作定性。

- 證據身份：來源觀察。
- 文獻定位：bass-22a24ed44135: physicalpp3-7 Figs2/4/5/7/8。
- 使用數據部分：literature_locator: physicalpp3-7 Figs2/4/5/7/8；trial_binding: PI/material/geometry series mapping; only explicit trial IDs in a conclusion apply to individual trials；scope: 逐次索引為可用候選紀錄，不代表文獻使用其全部列。。
- 本組適用層級：本材料／幾何系列文獻結論；只有原文明寫Trial／圖板條件才直接適用。PI/material/geometry series mapping; only explicit trial IDs in a conclusion apply to individual trials。
- 使用／控制因子：radiative_extinction_approx_cm_s: 1；blowoff_approx_cm_s: 45。
- 來源限制：單次burn中多次變速不是獨立試驗。；paper Test15/Test6等與CSV B-prefix的精確join尚未逐案證實，先不貼一對一標籤。。
- 搜尋句（改寫）：100/200µm PMMA的影像/延燒整理涵蓋輻射、熱控、動力學區；原文提醒流速與延燒點配對有顯著不確定性，profile形狀宜作定性。。
- 來源：https://doi.org/10.1016/j.proci.2016.06.025
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/02_論文全文/01_期刊論文與作者稿/Radiative, thermal, and kinetic regimes of opposed-flow flame spread_ A comparison between experimen__22a24ed441.pdf>)

### B25-FILM-RADIATIVE　B25-FILM-RADIATIVE

**The critical flow velocity for radiative extinction in opposed-flow flame spread in a microgravity environment: A comparison of experimental, computational, and theoretical results**

可見焰消失與radiometer斜率改變可區分影像端點；計算的100–400µm薄片在21%O2所得臨界流速1.5cm/s、16%時3.5cm/s屬模型結果，不當新量測門檻。

- 證據身份：來源量測與計算分列。
- 文獻定位：bass-60c325260228: physicalpp3-6 Figs4-7/Table1。
- 使用數據部分：literature_locator: physicalpp3-6 Figs4-7/Table1；trial_binding: PI/material/geometry series mapping; only explicit trial IDs in a conclusion apply to individual trials；scope: 逐次索引為可用候選紀錄，不代表文獻使用其全部列。。
- 本組適用層級：本材料／幾何系列文獻結論；只有原文明寫Trial／圖板條件才直接適用。PI/material/geometry series mapping; only explicit trial IDs in a conclusion apply to individual trials。
- 使用／控制因子：computed_Vcr_21O2_cm_s: 1.5；computed_Vcr_16O2_cm_s: 3.5。
- 來源限制：光學焰消失不是量得全部化學反應終止。。
- 搜尋句（改寫）：可見焰消失與radiometer斜率改變可區分影像端點；計算的100–400µm薄片在21%O2所得臨界流速1.5cm/s、16%時3.5cm/s屬模型結果，不當新量測門檻。。
- 來源：https://doi.org/10.1016/j.combustflame.2015.10.023
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/02_論文全文/01_期刊論文與作者稿/The critical flow velocity for radiative extinction in opposed-flow flame spread in a microgravity e__60c3252602.pdf>)

| Model ID | 公式／預測量 | 展示程式 | 數值比較與限制 |
| --- | --- | --- | --- |
| SOLID-PMMA-THIN-THERMAL | Vf=(2.34e-8 m²/s)×F_adb/τ_half；F_adb=4.89；τ_half=t_full/2；BASS-II PMMA thin-sheet thermal limit | reproduce_solid_models.py · [開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/solid_combustion_evidence_20261115/models/reproduce_solid_models.py>) | runnable；固定原式前向比較（非獨立驗證）；Original numeric front-position/spread trajectories, exact trial IDs and per-point statistics；Case-specific proof of thermal-regime eligibility; low-flow radiation/high-flow kinetics are not modeled；F_adb and prefactor are fixed by source; no coefficient is estimated. Original numeric spread trajectories/trial IDs are missing. R2 N/A. |

| 可開啟的圖／工具 | 身份與用途 |
| --- | --- |
| [開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/solid_combustion_evidence_20261115/models/comparison.html>) | 薄片熱控式與來源取點；PSI62僅共享benchmark參考，不是FGM重現 |
| [開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/solid_combustion_evidence_20261115/models/pmma_thin_model_vs_paper_observations.png>) | 固定物理公式與文獻圖上點比較 |
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
| B25-FILM-THERMAL；B25-FILM-REGIMES；B25-FILM-RADIATIVE | 同BASS-II薄膜計畫；圖上點到CSV逐次ID尚未全部確認 | 厚度與流動會改變延燒；純熱控極限可作厚度反比參考。 | 熱控式忽略的低流輻射熄滅／高流動力學限制由其他分析補充；F_adb、F_expt和圖內223/t不能互換。 |

## 4. 消防洞見

| 類別 | 對應證據 | 數據支持的判斷 | 策略／產品構想 | 待驗證 |
| --- | --- | --- | --- | --- |
| 預防 | B25-FILM-THERMAL；B25-FILM-REGIMES；B25-FILM-RADIATIVE | 熱控厚度反比式只描述指定區域的延燒速度；低流輻射與高流動力學限制另有來源證據。 | 材料配置比較同時標示厚度與火焰區域，不把較慢延燒視為不會點燃。 | 補相同observable的逐次原始軌跡與未參與校準條件。 |
| 偵測 | B25-FILM-RADIATIVE | 來源記錄變藍、soot減少或可見焰消失等光學變化；未提供本組煙警報效能。 | 把弱焰與減煙狀態納入偵測器挑戰試驗，保留熱／氣體獨立訊號。 | 匹配煙源、輸運、校準與啟用警報真值；不得由焰色推算漏報率。 |
| 撲滅／抑制 | 尚未取得／不適用 | 尚未建立本組可直接支持此用途的數據結論。 | 先補對應資料與試次匹配，再決定可測試策略；此處是研究缺口。 | 需本組材料、幾何、操作歷史與對應端點的量測；相近系列不能代替。 |

## 逐次索引

| 原始檔／資料位置 | Trial／Run／列 | 共享身份與保留事項 |
| --- | --- | --- |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 2；date: 2/19/2014；GMT: 50；test_number: B1；as_run: 尚未取得／不適用；sample: 147 | identity_notes: source_record_id: PSI-25-CSV-r2；raw_material: 100 micron PMMA film   2 cm wide；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Bhattacharjee；Test #: B1；Date: 2/19/2014；GMT: 50；Sample #: 147；Fuel Sample Material: 100 micron PMMA film   2 cm wide；Flow restrictor: 2；Fan display: 62；Air display: 5；Radiometer gain   (1000   250   50   10): 50；Total Frames Shot: 57；Calibrated  initial O2 % by vol : 22.2；Calibrated final O2 % by vol: 22.2；Initial CO2 % by vol: 0.44；Final CO2 % by vol: 0.44；Initial CO (ppm): 0；Final CO (ppm): 6 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 3；date: 2/19/2014；GMT: 50；test_number: B2；as_run: 尚未取得／不適用；sample: 155 | identity_notes: source_record_id: PSI-25-CSV-r3；raw_material: 200 micron PMMA film   2 cm wide；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Bhattacharjee；Test #: B2；Date: 2/19/2014；GMT: 50；Sample #: 155；Fuel Sample Material: 200 micron PMMA film   2 cm wide；Flow restrictor: 2；Fan display: 62；Air display: 5；Radiometer gain   (1000   250   50   10): 50；Total Frames Shot: none；Calibrated  initial O2 % by vol : 22.2；Calibrated final O2 % by vol: 1.6；Initial CO2 % by vol: 0.44；Final CO2 % by vol: 尚未取得／不適用；Initial CO (ppm): 6；Final CO (ppm): 尚未取得／不適用 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 4；date: 2/19/2014；GMT: 50；test_number: B3；as_run: 尚未取得／不適用；sample: 148 | identity_notes: source_record_id: PSI-25-CSV-r4；raw_material: 100 micron film   2 cm wide；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Bhattacharjee；Test #: B3；Date: 2/19/2014；GMT: 50；Sample #: 148；Fuel Sample Material: 100 micron film   2 cm wide；Flow restrictor: 2；Fan display: 47；Air display: 2；Radiometer gain   (1000   250   50   10): 50；Total Frames Shot: 253；Calibrated  initial O2 % by vol : 22.2；Calibrated final O2 % by vol: 21.8；Initial CO2 % by vol: 0.43；Final CO2 % by vol: 0.49；Initial CO (ppm): 12；Final CO (ppm): 19 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 5；date: 2/19/2014；GMT: 50；test_number: B4；as_run: 尚未取得／不適用；sample: 159 | identity_notes: source_record_id: PSI-25-CSV-r5；raw_material: 300 micron PMMA film   2 cm wide ；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Bhattacharjee；Test #: B4；Date: 2/19/2014；GMT: 50；Sample #: 159；Fuel Sample Material: 300 micron PMMA film   2 cm wide ；Flow restrictor: 2；Fan display: 61；Air display: 5；Radiometer gain   (1000   250   50   10): 50；Total Frames Shot: 137；Calibrated  initial O2 % by vol : 22.2；Calibrated final O2 % by vol: 22.2；Initial CO2 % by vol: 0.44；Final CO2 % by vol: 0.51；Initial CO (ppm): -1；Final CO (ppm): 10 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 6；date: 2/19/2014；GMT: 50；test_number: B5；as_run: 尚未取得／不適用；sample: 156 | identity_notes: source_record_id: PSI-25-CSV-r6；raw_material: 200 micron  2 cm wide ；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Bhattacharjee；Test #: B5；Date: 2/19/2014；GMT: 50；Sample #: 156；Fuel Sample Material: 200 micron  2 cm wide ；Flow restrictor: 2；Fan display: 59；Air display: 5；Radiometer gain   (1000   250   50   10): 50；Total Frames Shot: 206；Calibrated  initial O2 % by vol : 22.2；Calibrated final O2 % by vol: 21.9；Initial CO2 % by vol: 0.43；Final CO2 % by vol: 0.43；Initial CO (ppm): 0；Final CO (ppm): 12 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 7；date: 7/7/2014；GMT: 188；test_number: B6；as_run: 尚未取得／不適用；sample: 153m | identity_notes: source_record_id: PSI-25-CSV-r7；raw_material: 2 cm 0.1 mm PMMA film；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Bhattacharjee；Test #: B6；Date: 7/7/2014；GMT: 188；Sample #: 153m；Fuel Sample Material: 2 cm 0.1 mm PMMA film；Flow restrictor: 2；Fan display: 0.9   1.3   2.75；Air display: 3   5   approaching 10；Radiometer gain   (1000   250   50   10): 10；Total Frames Shot: 80；Calibrated  initial O2 % by vol : 21；Calibrated final O2 % by vol: 20.9；Initial CO2 % by vol: 0.33；Final CO2 % by vol: 0.41；Initial CO (ppm): 0；Final CO (ppm): 0.3 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 8；date: 2/19/2014；GMT: 50；test_number: B7；as_run: 尚未取得／不適用；sample: 161 | identity_notes: source_record_id: PSI-25-CSV-r8；raw_material: 400 micron film   2 cm wide；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Bhattacharjee；Test #: B7；Date: 2/19/2014；GMT: 50；Sample #: 161；Fuel Sample Material: 400 micron film   2 cm wide；Flow restrictor: 2；Fan display: 47；Air display: 2；Radiometer gain   (1000   250   50   10): 50；Total Frames Shot: 84；Calibrated  initial O2 % by vol : 22.2；Calibrated final O2 % by vol: 22.1；Initial CO2 % by vol: 0.45；Final CO2 % by vol: 0.51；Initial CO (ppm): 1；Final CO (ppm): 17 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 9；date: 7/7/2014；GMT: 188；test_number: B8；as_run: 尚未取得／不適用；sample: 157m | identity_notes: source_record_id: PSI-25-CSV-r9；raw_material: 2 cm   0.2 mm PMMA film；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Bhattacharjee；Test #: B8；Date: 7/7/2014；GMT: 188；Sample #: 157m；Fuel Sample Material: 2 cm   0.2 mm PMMA film；Flow restrictor: 0；Fan display: 1.4    incr to 10.0；Air display: 10   max；Radiometer gain   (1000   250   50   10): 10；Total Frames Shot: 226；Calibrated  initial O2 % by vol : 21；Calibrated final O2 % by vol: 20.5；Initial CO2 % by vol: 0.33；Final CO2 % by vol: 0.58；Initial CO (ppm): 0；Final CO (ppm): 131 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 10；date: 7/7/2014；GMT: 188；test_number: B9；as_run: 尚未取得／不適用；sample: 154m | identity_notes: source_record_id: PSI-25-CSV-r10；raw_material: 2 cm   0.1 mm PMMA film；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Bhattacharjee；Test #: B9；Date: 7/7/2014；GMT: 188；Sample #: 154m；Fuel Sample Material: 2 cm   0.1 mm PMMA film；Flow restrictor: 2；Fan display: 0.6   0.35；Air display: 2   <1；Radiometer gain   (1000   250   50   10): 10；Total Frames Shot: 45；Calibrated  initial O2 % by vol : 21；Calibrated final O2 % by vol: 20.9；Initial CO2 % by vol: 0.33；Final CO2 % by vol: 0.35；Initial CO (ppm): 0；Final CO (ppm): 10 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 11；date: 7/7/2014；GMT: 188；test_number: B10；as_run: 尚未取得／不適用；sample: 173m | identity_notes: source_record_id: PSI-25-CSV-r11；raw_material: 1 cm   0.2 mm PMMA film；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Bhattacharjee；Test #: B10；Date: 7/7/2014；GMT: 188；Sample #: 173m；Fuel Sample Material: 1 cm   0.2 mm PMMA film；Flow restrictor: 2；Fan display: 1.7 (52)   1.25   0.9   0.6   0.4   0.35；Air display: 5  4  3  2  1；Radiometer gain   (1000   250   50   10): 10；Total Frames Shot: 123；Calibrated  initial O2 % by vol : 21；Calibrated final O2 % by vol: 20.8；Initial CO2 % by vol: 0.33；Final CO2 % by vol: 0.44；Initial CO (ppm): 0；Final CO (ppm): 23 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 12；date: 7/7/2014；GMT: 188；test_number: B11；as_run: 尚未取得／不適用；sample: 158m | identity_notes: source_record_id: PSI-25-CSV-r12；raw_material: 2 cm   0.2 mm PMMA film；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Bhattacharjee；Test #: B11；Date: 7/7/2014；GMT: 188；Sample #: 158m；Fuel Sample Material: 2 cm   0.2 mm PMMA film；Flow restrictor: 2；Fan display: 2.5 (59)   1.3   0.7   0.5   0.35；Air display: 5   3   1   <1；Radiometer gain   (1000   250   50   10): 10；Total Frames Shot: 131；Calibrated  initial O2 % by vol : 21；Calibrated final O2 % by vol: 20.7；Initial CO2 % by vol: 0.33；Final CO2 % by vol: 0.47；Initial CO (ppm): 0；Final CO (ppm): 46 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 13；date: 2/19/2014；GMT: 50；test_number: B12；as_run: 尚未取得／不適用；sample: 160 | identity_notes: source_record_id: PSI-25-CSV-r13；raw_material: 300 micron film   2 cm wide；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Bhattacharjee；Test #: B12；Date: 2/19/2014；GMT: 50；Sample #: 160；Fuel Sample Material: 300 micron film   2 cm wide；Flow restrictor: 2；Fan display: 46.5；Air display: 2；Radiometer gain   (1000   250   50   10): 50；Total Frames Shot: 160；Calibrated  initial O2 % by vol : 22.2；Calibrated final O2 % by vol: 22.1；Initial CO2 % by vol: 0.51；Final CO2 % by vol: 0.56；Initial CO (ppm): 17；Final CO (ppm): 33 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 14；date: 7/7/2014；GMT: 188；test_number: B13；as_run: 尚未取得／不適用；sample: 162m | identity_notes: source_record_id: PSI-25-CSV-r14；raw_material: 2 cm   0.4 mm thick film；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Bhattacharjee；Test #: B13；Date: 7/7/2014；GMT: 188；Sample #: 162m；Fuel Sample Material: 2 cm   0.4 mm thick film；Flow restrictor: 2；Fan display: 3.5 (68)    1.7   1.25   0.9   0.6   0.4   0.35；Air display: 10   5  4  3  2  1；Radiometer gain   (1000   250   50   10): 10；Total Frames Shot: 311；Calibrated  initial O2 % by vol : 21；Calibrated final O2 % by vol: 20.5；Initial CO2 % by vol: 0.33；Final CO2 % by vol: 0.65；Initial CO (ppm): 0；Final CO (ppm): 61 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 15；date: 7/2/2014；GMT: 183；test_number: B14；as_run: 尚未取得／不適用；sample: 174m | identity_notes: source_record_id: PSI-25-CSV-r15；raw_material: 1 cm wide 200 micron thick PMMA；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Bhattacharjee；Test #: B14；Date: 7/2/2014；GMT: 183；Sample #: 174m；Fuel Sample Material: 1 cm wide 200 micron thick PMMA；Flow restrictor: 2；Fan display: pot 0.9   0.5 and down；Air display: 5  3  2   ext；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 44；Calibrated  initial O2 % by vol : 15；Calibrated final O2 % by vol: none；Initial CO2 % by vol: 0；Final CO2 % by vol: none；Initial CO (ppm): 0.2；Final CO (ppm): none |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 16；date: 7/7/2014；GMT: 188；test_number: B15；as_run: 尚未取得／不適用；sample: 149m | identity_notes: source_record_id: PSI-25-CSV-r16；raw_material: 2 cm   0.1 mm PMMA film；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Bhattacharjee；Test #: B15；Date: 7/7/2014；GMT: 188；Sample #: 149m；Fuel Sample Material: 2 cm   0.1 mm PMMA film；Flow restrictor: 0；Fan display: 1.4 (50) incr to 10.0 pot；Air display: 10   max；Radiometer gain   (1000   250   50   10): 10；Total Frames Shot: 122；Calibrated  initial O2 % by vol : 21；Calibrated final O2 % by vol: 20.8；Initial CO2 % by vol: 0.33；Final CO2 % by vol: 0.43；Initial CO (ppm): 0；Final CO (ppm): 22 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 17；date: 7/2/2014；GMT: 183；test_number: B16；as_run: 尚未取得／不適用；sample: 150m | identity_notes: source_record_id: PSI-25-CSV-r17；raw_material: 2 cm 100 micron thick PMMA；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Bhattacharjee；Test #: B16；Date: 7/2/2014；GMT: 183；Sample #: 150m；Fuel Sample Material: 2 cm 100 micron thick PMMA；Flow restrictor: 2；Fan display: 44 (pot 0.68)；Air display: 3  0.5 pot   0.4 pot；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 94；Calibrated  initial O2 % by vol : 17.3；Calibrated final O2 % by vol: 17.2；Initial CO2 % by vol: 0.47；Final CO2 % by vol: 0.51；Initial CO (ppm): 103；Final CO (ppm): 119 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 18；date: 7/2/2014；GMT: 183；test_number: B17；as_run: 尚未取得／不適用；sample: 175m | identity_notes: source_record_id: PSI-25-CSV-r18；raw_material: 1 cm wide 200 micron thick PMMA；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Bhattacharjee；Test #: B17；Date: 7/2/2014；GMT: 183；Sample #: 175m；Fuel Sample Material: 1 cm wide 200 micron thick PMMA；Flow restrictor: 2；Fan display: pot 1.2 (48)    0.9   0.4 ；Air display: 5   3    pot 0.4；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 190；Calibrated  initial O2 % by vol : 17.5；Calibrated final O2 % by vol: 17.4；Initial CO2 % by vol: 0.2；Final CO2 % by vol: 0.34；Initial CO (ppm): 0；Final CO (ppm): 47 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 19；date: 7/2/2014；GMT: 183；test_number: B18；as_run: 尚未取得／不適用；sample: 176m | identity_notes: source_record_id: PSI-25-CSV-r19；raw_material: 1 cm wide 200 micron thick PMMA；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Bhattacharjee；Test #: B18；Date: 7/2/2014；GMT: 183；Sample #: 176m；Fuel Sample Material: 1 cm wide 200 micron thick PMMA；Flow restrictor: 0；Fan display: pot 1.02 (47)   incr to 7.0；Air display: 10   blowoff；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 152；Calibrated  initial O2 % by vol : 17.4；Calibrated final O2 % by vol: 17.4；Initial CO2 % by vol: 0.34；Final CO2 % by vol: 0.42；Initial CO (ppm): 47；Final CO (ppm): 78 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 20；date: 7/2/2014；GMT: 183；test_number: B19；as_run: 尚未取得／不適用；sample: 151m | identity_notes: source_record_id: PSI-25-CSV-r20；raw_material: 2 cm 100 micron thick PMMA；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Bhattacharjee；Test #: B19；Date: 7/2/2014；GMT: 183；Sample #: 151m；Fuel Sample Material: 2 cm 100 micron thick PMMA；Flow restrictor: 0；Fan display: 47 (pot 1.05)   incr to pot 6.0；Air display: 10   blowoff；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 95；Calibrated  initial O2 % by vol : 17.3；Calibrated final O2 % by vol: 17.2；Initial CO2 % by vol: 0.51；Final CO2 % by vol: 0.57；Initial CO (ppm): 119；Final CO (ppm): 131 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 21；date: 7/2/2014；GMT: 183；test_number: B20；as_run: 尚未取得／不適用；sample: 152m | identity_notes: source_record_id: PSI-25-CSV-r21；raw_material: 2 cm 100 micron thick PMMA；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Bhattacharjee；Test #: B20；Date: 7/2/2014；GMT: 183；Sample #: 152m；Fuel Sample Material: 2 cm 100 micron thick PMMA；Flow restrictor: 2；Fan display: 48   pot 0.9   0.5；Air display: 5   3      pot 0.5；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 111；Calibrated  initial O2 % by vol : 17.4；Calibrated final O2 % by vol: 17.4；Initial CO2 % by vol: 0.42；Final CO2 % by vol: 0.47；Initial CO (ppm): 78；Final CO (ppm): 103 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 22；date: 8/4/2014；GMT: 216；test_number: B21；as_run: 尚未取得／不適用；sample: 174m | identity_notes: source_record_id: PSI-25-CSV-r22；raw_material: 1 cm wide 200 micron thick PMMA；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Bhattacharjee；Test #: B21；Date: 8/4/2014；GMT: 216；Sample #: 174m；Fuel Sample Material: 1 cm wide 200 micron thick PMMA；Flow restrictor: 1；Fan display: 53   and down；Air display: 5 down to ext；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 88；Calibrated  initial O2 % by vol : 20.8；Calibrated final O2 % by vol: 20.6；Initial CO2 % by vol: 0.36；Final CO2 % by vol: 0.44；Initial CO (ppm): -1；Final CO (ppm): 18 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-25_BASS-II\Experimental table\PSI-25_Experimental table_BASS-II.csv | csv_row: 23；date: 8/4/2014；GMT: 216；test_number: B22；as_run: 尚未取得／不適用；sample: 176m | identity_notes: source_record_id: PSI-25-CSV-r23；raw_material: 1 cm wide 200 micron thick PMMA；independent_burn_count: 尚未取得／不適用；raw_parameters_as_stored: PI: Bhattacharjee；Test #: B22；Date: 8/4/2014；GMT: 216；Sample #: 176m；Fuel Sample Material: 1 cm wide 200 micron thick PMMA；Flow restrictor: 1；Fan display: 53   42   41   40.5；Air display: 5   2   0；Radiometer gain   (1000   250   50   10): 250；Total Frames Shot: 77；Calibrated  initial O2 % by vol : 20.7；Calibrated final O2 % by vol: 20.5；Initial CO2 % by vol: 0.41；Final CO2 % by vol: 0.47；Initial CO (ppm): -1；Final CO (ppm): 10 |

## 缺件與適用範圍

- B2 finalO2字面1.6與reportA.1p112一致但異常，未校正/不進可燃下界主張。
- B14 finalO2=none保留unknown。
