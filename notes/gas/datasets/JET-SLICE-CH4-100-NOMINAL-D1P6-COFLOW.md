# SLICE CH4-100, nominal 1.6 mm hardware class

小資料集 ID：`JET-SLICE-CH4-100-NOMINAL-D1P6-COFLOW`

## 資料身份與範圍

| 項目 | 內容 |
| --- | --- |
| 原始 NASA PSI investigation | [PSI-106](https://psi.nasa.gov/physci/repo/data/investigations/PSI-106) |
| 相關PSI索引（不是原始資料） | 尚未取得／不適用 |
| 材料／配方 | components_mole_fraction: CH4: 1.0 |
| 幾何 | navigation_class_nozzle_mm: 1.6；literal_source_values_must_be_used: True；reported_diameter_values_mm: source_id: JET-84be65105115；diameter_mm: 1.59；basis: author experimental setup p7；exact_equivalence_or_pooling_claimed: False；note: 3.2/3.23/3.24 and 1.6/1.59 are different source-reported descriptions of nominal hardware classes, not evidence of controlled scale-up trials. |
| 實驗模式 | laminar_nonpremixed_coflow_diffusion_flame |
| 證據角色 | 氣體燃燒來源組 |
| 環境 | gravity: ISS microgravity；Yale engineering-unit normal gravity；mode: laminar_nonpremixed_coflow_diffusion_flame |
| 資料粒度／共享試片 | 原始試次／操作／圖上量測的身份見逐次索引，未預設互相一對一。 |
| 可用數值 | source_paper_conditions_or_optical_diagnostics_only |

## 1. 文獻結果與視覺化程式

### JET-SLICE-CH4-100-NOMINAL-D1P6-COFLOW-SOOT-SCOPE　JET-SLICE-CH4-100-NOMINAL-D1P6-COFLOW-SOOT-SCOPE

**An experimental and computational study on soot formation in a coflow jet flame under microgravity and normal gravity**

The soot paper specifically studies pure methane with 1.59 and 3.23 mm nozzles; the quantified main gravity comparison in Fig.3 uses the 3.23 mm nozzle. The smaller-nozzle subgroup must not inherit the Fig.3 conditions or 4–8 ratio.

- 證據身份：author_reported_experimental_scope。
- 文獻定位：JET-84be65105115: physical_pdf_pages: 7；15；figure: 3。
- 使用數據部分：paper_data_use: pure-methane soot subset; exact original image/test IDs and 1.59 mm numeric result table not recovered。
- 本組適用層級：僅本項來源指定案例；逐次配對以data_used為準。
- 使用／控制因子：semantic_key: fuel_composition；source_raw_name: 100% CH4；unit: mole fraction；value_or_range: CH4: 1.0；source_ref: source_id: JET-84be65105115；physical_pdf_pages: 7；locator: Section 2；workbook_mapping_status: pending_exact_cell_join_by_main; no synonym-only assumption；semantic_key: fuel_nozzle_inner_diameter；source_raw_name: fuel nozzles；unit: mm；value_or_range: 1.59；source_ref: source_id: JET-84be65105115；physical_pdf_pages: 7；locator: Section 2；workbook_mapping_status: pending_exact_cell_join_by_main; no synonym-only assumption。
- 來源限制：Source temperature/soot fields are optically reduced quantities, not raw RGB counts or measured oxygen consumption.。
- 搜尋句（改寫）：The soot paper specifically studies pure methane with 1.59 and 3.23 mm nozzles; the quantified main gravity comparison in Fig.3 uses the 3.23 mm nozzle. The smaller-nozzle subgroup must not inherit the Fig.3 conditions or 4–8 ratio.。
- 來源：[來源](<https://ntrs.nasa.gov/citations/20140017780>)
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/02_論文全文/02_會議論文與預印本/An experimental and computational study of soot formation in a coflow jet flame under microgravity a__84be651051.pdf>)

| Model ID | 公式／預測量 | 展示程式 | 數值比較與限制 |
| --- | --- | --- | --- |
| READINESS-PSI-106 | 原文方程／模型參見MODEL_INVENTORY；本次尚未閉合；SLICE geometry (inputs missing) | 未實作 · 尚未取得本機檔案 | 未執行／缺閉合輸入；來源就緒度盤點，不是數值預測；R²（模型全群）=N/A；尚未取得／不適用；Paper-digitized scalar geometry exists, but no closed source-fixed L/R model can be forward-compared fairly.；Full MC-Smooth solver, chemistry/transport/radiation and matched boundary conditions；Original numeric geometry and trial P/O2/T; measured liftoff for lifted flames |

| 可開啟的圖／工具 | 身份與用途 |
| --- | --- |
| [開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/gas_combustion_evidence_20261115/models/comparison.html>) | 選正確架構；缺資料的研究僅顯示就緒度，不畫假預測 |

## 2. 使用資料與參數總表的因子對照

| 總表原分類 | 來源身份 | 原欄名單位 | 原欄名例 | 總表定位 |
| --- | --- | --- | --- | --- |
| 壓力 | 量測或設定 | 未由欄名確認 | Pressure Trans V；psia；Atomospheric Pressure | '物理參數'!A407:K407 |
| 密度 | 量測或來源分析量 | g/l | density(g/l)；Density (g/l) | '物理參數'!A408:K408 |
| 尺寸／幾何 | 裝置或樣本條件 | cm/s | (cm/s)；Measured Velocities (cm/s)；U,probe (cm/s)；u2 (cm/s)；U (cm/s)；Fluctuations (cm/s) | '物理參數'!A409:K409 |
| 尺寸／幾何 | 裝置或樣本條件 | mm | Secondary Nozzle Dia (mm)；step(mm)；(mm) | '物理參數'!A410:K410 |
| 尺寸／幾何 | 裝置或樣本條件 | 未由欄名確認 | Position；mm；13 mm station (z=65) * 36 mm Height (y=10)；13 mm station (z=65) * 57 mm Height (y=-11)；13 mm station (z=65) * 19 mm Height (y=28)；56 mm station (z=108) * 36 mm Height (y=10)；56 mm station (z=108) * 57 mm Height (y=-11)；56 mm station (z=108) * 19 mm Height (y=28)；4mm above the nozzle；mm floor scale；其餘見原始欄位 | '物理參數'!A411:K411 |
| 流速／通風 | 量測或設定 | cm/s | Fuel Velocity(cm/s)；Calibration Velocity (cm/s) | '物理參數'!A412:K412 |
| 流速／通風 | 量測或設定 | m/s | air velocity (m/s)；velocity (m/s) | '物理參數'!A413:K413 |
| 流速／通風 | 量測或設定 | 未由欄名確認 | Anemometer V；Anemometer；Velocity；Air to Match velocity globally；Anemometer Model；Min Velocity；Max Velocity；Velocity [m/s] | '物理參數'!A414:K414 |
| 溫度 | 量測或設定 | K | Temperature(K) | '物理參數'!A415:K415 |
| 溫度 | 量測或設定 | 未由欄名確認 | temperature；Temperature:；20.0 Deg C；250.0 Deg C | '物理參數'!A416:K416 |
| 硬體電壓／電流／功率 | 儀器設定／控制參數 | 未由欄名確認 | Aout Voltage setting (Nominal) | '物理參數'!A417:K417 |
| 硬體電壓／電流／功率 | 原始訊號或狀態 | 未由欄名確認 | Probe Voltage Readings (2000 readings, 5 sec.)；Voltage/Torr Input；Aout Voltage reading (Actual)；Volts；volts；ohms；Voltmeter:；Probe Voltage Readings (120 readings, 60 sec.)；Bridge Voltage [E]；voltage (volt) | '物理參數'!A418:K418 |
| 質量／質量損失 | 量測或衍生 | kg/kmol | Moleculare Weight (kg/kmol) | '物理參數'!A419:K419 |
| 風扇／流量顯示設定 | 儀器設定 | 未由欄名確認 | Fan；FAN；FAN Reading；Fan reading；fan；fan display | '物理參數'!A420:K420 |
| 風扇／流量顯示設定 | 儀器設定／控制參數 | 未由欄名確認 | Fan Dial Setting = 0；Fan Dial Setting = 2；Fan Dial Setting = 4；Fan Dial Setting = 6；Fan Dial Setting = 8；Fan Dial Setting = 10；Fan setting；Fan settings | '物理參數'!A421:K421 |
| 體積流量／MFC | 量測或設定 | SCCM | FLOW RATE (SCCM) | '物理參數'!A422:K422 |
| 體積流量／MFC | 量測或設定 | sccm | Flow rate (sccm)；N2 Flow rate (sccm) at Calibration condition | '物理參數'!A423:K423 |
| 體積流量／MFC | 量測或設定 | 未由欄名確認 | Flowrate；N2 Flow rate (sccm) at STP condition (i.e. T = 273.2K)；SCCM；sccm | '物理參數'!A424:K424 |

以上是該 investigation 的欄位盤點；個別結論實際使用的因子以第1節與下列補充為準。

| 本組實際因子 | 總表定位／未列欄位 | 文獻中的用途 |
| --- | --- | --- |
| JET-SLICE-CH4-100-NOMINAL-D1P6-COFLOW-SOOT-SCOPE / fuel_composition | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| JET-SLICE-CH4-100-NOMINAL-D1P6-COFLOW-SOOT-SCOPE / fuel_nozzle_inner_diameter | '物理參數'!G410；'物理參數'!G411 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |

| 文獻因子／疑點 | 正確讀法或需補資料 |
| --- | --- |
| 速度與幾何 | 原總表將部分cm/s欄列作尺寸；按原單位判讀速度。光學座標／像素不是已校準火焰尺寸。 |

## 3. 共用資料的多項結論比較

| 結論／文獻 | 資料重疊身份 | 共同處 | 不同處／不能合併之處 |
| --- | --- | --- | --- |
| JET-SLICE-CH4-100-NOMINAL-D1P6-COFLOW-SOOT-SCOPE | 來源系列；精確論文／試次交集仍以每項data_used為準 | 不把多份出版物當獨立實驗。 | 尚未取得完全同試次的多篇結論比較時保留缺口。 |
| JET-4fc7ff5b5432；JET-84be65105115；JET-fb028bca1f40 | same_SLICE_campaign_different_selected_subsets_and_observables | Buoyancy changes flame transport/shape under the studied conditions.；Source-specific calibration and boundary conditions are necessary. | Cao geometry paper spans40/70/100% methane at a3.24mm diameter inferred from its radius; Ma soot paper focuses100% methane1.59/3.23mm; Giassi CH* paper sequences A/B/C use3.2/.8/1.6mm and distinct velocity ranges.；Luminous geometry, soot volume fraction/temperature, calibrated CH* and computed heat release are different targets. Good shape agreement is not successful soot-quantity prediction.；尚未取得／不適用；尚未取得／不適用 |
| JET-c17adf3a6048；JET-7b44063f19e2；JET-bdaf4f1afd26；JET-6a211cdfa418 | successive_annual_reports_with_overlapping_campaign_and_publication_content | 同來源系列的不同觀測問題。 | 尚未取得／不適用；尚未取得／不適用；Different PDF hashes/years are document editions, not proof of new flight experiments. Specific embedded-paper identity is recorded below where titles are found. |

## 4. 消防洞見

| 類別 | 對應證據 | 數據支持的判斷 | 策略／產品構想 | 待驗證 |
| --- | --- | --- | --- | --- |
| 預防 | 尚未取得／不適用 | 尚未建立本組可直接支持此消防用途的完整量測鏈。 | 先補本組對應的物理端點與資料配對，再設計策略測試。 | 相關系列與方法限制只能提供研究脈絡，不能代替本組產品或操作效能驗證。 |
| 偵測 | 尚未取得／不適用 | 尚未建立本組可直接支持此消防用途的完整量測鏈。 | 先補本組對應的物理端點與資料配對，再設計策略測試。 | 相關系列與方法限制只能提供研究脈絡，不能代替本組產品或操作效能驗證。 |
| 撲滅／抑制 | 尚未取得／不適用 | 尚未建立本組可直接支持此消防用途的完整量測鏈。 | 先補本組對應的物理端點與資料配對，再設計策略測試。 | 相關系列與方法限制只能提供研究脈絡，不能代替本組產品或操作效能驗證。 |

## 逐次索引

尚未取得可逐項對照的紀錄。

## 缺件與適用範圍

- 目前不足兩項可適用的來源結論；尚未完成多結論比較，不以研究目的湊數。
- Original per-trial geometry tables/replicate identifiers are missing; no new R² or fitting.
- No exact trial join between publication points, campaign date table and raw image/setting records is established.
- Measured luminous, modified luminous, soot-temperature and CH* boundaries are distinct; geometry is not heat release or extinction.
- Pressure, oxygen and inlet temperature lack complete paired experimental values; 298 K is a simulation assumption where stated.
