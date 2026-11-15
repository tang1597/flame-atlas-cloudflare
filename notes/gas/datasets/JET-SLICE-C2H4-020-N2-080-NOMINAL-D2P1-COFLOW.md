# SLICE C2H4-020-N2-080, 2.1mm, liftoff/blowout stability plots

小資料集 ID：`JET-SLICE-C2H4-020-N2-080-NOMINAL-D2P1-COFLOW`

## 資料身份與範圍

| 項目 | 內容 |
| --- | --- |
| 原始 NASA PSI investigation | [PSI-106](https://psi.nasa.gov/physci/repo/data/investigations/PSI-106) |
| 相關PSI索引（不是原始資料） | 尚未取得／不適用 |
| 材料／配方 | components_mole_fraction: C2H4: 0.2；N2: 0.8 |
| 幾何 | navigation_class_nozzle_mm: 2.1；literal_source_values_must_be_used: True；reported_diameter_values_mm: source_id: JET-f02f39ba9642；diameter_mm: 2.1；basis: explicit panel legend；exact_equivalence_or_pooling_claimed: False |
| 實驗模式 | laminar_nonpremixed_coflow_diffusion_flame; fuel/coflow ramp to liftoff or blowout |
| 證據角色 | 氣體燃燒來源組 |
| 環境 | gravity: ISS microgravity；normal gravity comparison where shown；mode: laminar_nonpremixed_coflow_diffusion_flame; fuel/coflow ramp to liftoff or blowout |
| 資料粒度／共享試片 | 原始試次／操作／圖上量測的身份見逐次索引，未預設互相一對一。 |
| 可用數值 | source_authored_stability_plot_observations_only; original numeric thresholds and raw trial join missing |

## 1. 文獻結果與視覺化程式

### JET-SLICE-C2H4-020-N2-080-NOMINAL-D2P1-COFLOW-STABILITY-PANEL　JET-SLICE-C2H4-020-N2-080-NOMINAL-D2P1-COFLOW-STABILITY-PANEL

**Microgravity Enhances the Stability of Gas-Jet Diffusion Flames**

The cited panel explicitly includes this fuel/nozzle condition and distinguishes limiting fuel velocity from coflow velocity and liftoff from blowout. The markers/curves are retained as source evidence only; no numeric threshold or raw-trial count is manufactured.

- 證據身份：author_reported_stability_plot_observation。
- 文獻定位：JET-f02f39ba9642: explicit fuel/nozzle legend and labelled Uair/Uj axes; summaryp14; JET-f02f39ba9642: experiment method and source summary。
- 使用數據部分：source_id: JET-f02f39ba9642；physical_pdf_pages: 12；source_group_key: C2H4-020-N2-080; d=2.1mm; explicit legend；role: source_plot_condition_identity_not_original_trial_ID；original_raw_trial_ids: 尚未取得／不適用；numeric_coordinates_admitted: False。
- 本組適用層級：僅本項來源指定案例；逐次配對以data_used為準。
- 使用／控制因子：semantic_key: fuel_composition；source_raw_name: Fuel legend；unit: mole/volume fraction as source gas mixture；value_or_range: C2H4: 0.2；N2: 0.8；source_ref: source_id: JET-f02f39ba9642；physical_pdf_pages: 12；locator: explicit fuel/nozzle legend and labelled Uair/Uj axes; summaryp14；workbook_mapping_status: pending_exact_factor_cell_join；semantic_key: fuel_nozzle_inner_diameter；source_raw_name: d(mm)；unit: mm；value_or_range: 2.1；source_ref: source_id: JET-f02f39ba9642；physical_pdf_pages: 12；locator: explicit fuel/nozzle legend and labelled Uair/Uj axes; summaryp14；workbook_mapping_status: pending_exact_factor_cell_join；semantic_key: oxidizer_coflow_velocity；source_raw_name: Mean Air Velocity；unit: cm/s；value_or_range: 尚未取得／不適用；role: source_varied_axis_not_digitized_numeric_bound；source_ref: source_id: JET-f02f39ba9642；physical_pdf_pages: 12；locator: explicit fuel/nozzle legend and labelled Uair/Uj axes; summaryp14；workbook_mapping_status: pending_exact_factor_cell_join；semantic_key: limiting_fuel_jet_velocity；source_raw_name: Mean Fuel Jet Velocity at lift/blowout；unit: m/s；value_or_range: 尚未取得／不適用；role: observed_source_endpoint_axis; no new coordinates admitted；source_ref: source_id: JET-f02f39ba9642；physical_pdf_pages: 12；locator: explicit fuel/nozzle legend and labelled Uair/Uj axes; summaryp14；workbook_mapping_status: pending_exact_factor_cell_join。
- 來源限制：No threshold coordinates digitized or fitted.；No exact join to Cao geometry points, Giassi CH* sequences or the12date campaign table.；Fuel-stream N2 dilution is not ambient oxygen reduction or an extinguishing-agent delivery experiment.；Apparent matching composition/nozzle does not establish same trial or repeatability.。
- 搜尋句（改寫）：The cited panel explicitly includes this fuel/nozzle condition and distinguishes limiting fuel velocity from coflow velocity and liftoff from blowout. The markers/curves are retained as source evidence only; no numeric threshold or raw-trial count is manufactured.。
- 來源：[來源](<https://psi-curation-prod.s3.amazonaws.com/legacy/Filestreamdb/15985/SLICE%20EP-02%202012%20ASGSR.pdf>)
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/實驗附帶文件/補下載/PSI-106/Raw Data/a9244a0ac96793ad_SLICE EP-02 2012 ASGSR.pdf>)

- 共同來源：**Microgravity Enhances the Stability of Gas-Jet Diffusion Flames**；experiment method and source summary；[來源](<https://psi-curation-prod.s3.amazonaws.com/legacy/Filestreamdb/15985/SLICE%20EP-02%202012%20ASGSR.pdf>)

### JET-SLICE-C2H4-020-N2-080-NOMINAL-D2P1-COFLOW-STABILITY-MECHANISM　JET-SLICE-C2H4-020-N2-080-NOMINAL-D2P1-COFLOW-STABILITY-MECHANISM

**Microgravity Enhances the Stability of Gas-Jet Diffusion Flames**

The authors attribute the stability-limit changes to entrainment/mixing, fuel dilution and propagation behavior. These interpretations support testing a flow-aware control strategy, but do not provide a universal extinction rule or suppression-agent dose.

- 證據身份：author_physical_interpretation_not_independent_validation。
- 文獻定位：JET-f02f39ba9642: explicit fuel/nozzle legend and labelled Uair/Uj axes; summaryp14; JET-f02f39ba9642: experiment method and source summary。
- 使用數據部分：source_id: JET-f02f39ba9642；physical_pdf_pages: 12；source_group_key: C2H4-020-N2-080; d=2.1mm; explicit legend；role: source_plot_condition_identity_not_original_trial_ID；original_raw_trial_ids: 尚未取得／不適用；numeric_coordinates_admitted: False。
- 本組適用層級：僅本項來源指定案例；逐次配對以data_used為準。
- 使用／控制因子：semantic_key: fuel_composition；source_raw_name: Fuel legend；unit: mole/volume fraction as source gas mixture；value_or_range: C2H4: 0.2；N2: 0.8；source_ref: source_id: JET-f02f39ba9642；physical_pdf_pages: 12；locator: explicit fuel/nozzle legend and labelled Uair/Uj axes; summaryp14；workbook_mapping_status: pending_exact_factor_cell_join；semantic_key: fuel_nozzle_inner_diameter；source_raw_name: d(mm)；unit: mm；value_or_range: 2.1；source_ref: source_id: JET-f02f39ba9642；physical_pdf_pages: 12；locator: explicit fuel/nozzle legend and labelled Uair/Uj axes; summaryp14；workbook_mapping_status: pending_exact_factor_cell_join；semantic_key: oxidizer_coflow_velocity；source_raw_name: Mean Air Velocity；unit: cm/s；value_or_range: 尚未取得／不適用；role: source_varied_axis_not_digitized_numeric_bound；source_ref: source_id: JET-f02f39ba9642；physical_pdf_pages: 12；locator: explicit fuel/nozzle legend and labelled Uair/Uj axes; summaryp14；workbook_mapping_status: pending_exact_factor_cell_join；semantic_key: limiting_fuel_jet_velocity；source_raw_name: Mean Fuel Jet Velocity at lift/blowout；unit: m/s；value_or_range: 尚未取得／不適用；role: observed_source_endpoint_axis; no new coordinates admitted；source_ref: source_id: JET-f02f39ba9642；physical_pdf_pages: 12；locator: explicit fuel/nozzle legend and labelled Uair/Uj axes; summaryp14；workbook_mapping_status: pending_exact_factor_cell_join。
- 來源限制：No threshold coordinates digitized or fitted.；No exact join to Cao geometry points, Giassi CH* sequences or the12date campaign table.；Fuel-stream N2 dilution is not ambient oxygen reduction or an extinguishing-agent delivery experiment.；Apparent matching composition/nozzle does not establish same trial or repeatability.。
- 搜尋句（改寫）：The authors attribute the stability-limit changes to entrainment/mixing, fuel dilution and propagation behavior. These interpretations support testing a flow-aware control strategy, but do not provide a universal extinction rule or suppression-agent dose.。
- 來源：[來源](<https://psi-curation-prod.s3.amazonaws.com/legacy/Filestreamdb/15985/SLICE%20EP-02%202012%20ASGSR.pdf>)
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/實驗附帶文件/補下載/PSI-106/Raw Data/a9244a0ac96793ad_SLICE EP-02 2012 ASGSR.pdf>)

- 共同來源：**Microgravity Enhances the Stability of Gas-Jet Diffusion Flames**；experiment method and source summary；[來源](<https://psi-curation-prod.s3.amazonaws.com/legacy/Filestreamdb/15985/SLICE%20EP-02%202012%20ASGSR.pdf>)

### JET-SLICE-STABILITY-GRAVITY-SCOPE　JET-SLICE-STABILITY-GRAVITY-SCOPE

**Microgravity Enhances the Stability of Gas-Jet Diffusion Flames**

The source reports enhanced microgravity stability in low-speed diluted70%CH4/20%C2H4 cases, while high-speed ethane/ethylene cases show a much smaller gravity effect. Thus terrestrial blowout expectations cannot be promoted to a universal microgravity extinguishment rule.

- 證據身份：author_measured_plot_trends_with_scope。
- 文獻定位：JET-f02f39ba9642: explicit panel legends and Summary。
- 使用數據部分：source_group_keys: panel-specific fuel/nozzle cases, not all27prior subsets；numeric_points_digitized: 0；original_raw_trial_ID_join: False。
- 本組適用層級：僅本項來源指定案例；逐次配對以data_used為準。
- 使用／控制因子：semantic_key: fuel_and_flow_regime；source_raw_name: source summary and panel legends；unit: source categorical condition；value_or_range: low_speed: 70%CH4；20%C2H4；high_speed: C2H6；C2H4；source_ref: source_id: JET-f02f39ba9642；physical_pdf_pages: 9；11；12；13；14；workbook_mapping_status: fuel composition + flow regime, not a new numerical bound。
- 來源限制：Source-summary qualitative comparison; not a new gravity-only causal estimate.；The source labels conditions stable/No Flame from experimental flame behavior, not equipment qualification or residual-toxicity clearance.。
- 搜尋句（改寫）：The source reports enhanced microgravity stability in low-speed diluted70%CH4/20%C2H4 cases, while high-speed ethane/ethylene cases show a much smaller gravity effect. Thus terrestrial blowout expectations cannot be promoted to a universal microgravity extinguishment rule.。
- 來源：[來源](<https://psi-curation-prod.s3.amazonaws.com/legacy/Filestreamdb/15985/SLICE%20EP-02%202012%20ASGSR.pdf>)
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/實驗附帶文件/補下載/PSI-106/Raw Data/a9244a0ac96793ad_SLICE EP-02 2012 ASGSR.pdf>)

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
| JET-SLICE-C2H4-020-N2-080-NOMINAL-D2P1-COFLOW-STABILITY-PANEL / fuel_composition | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| JET-SLICE-C2H4-020-N2-080-NOMINAL-D2P1-COFLOW-STABILITY-PANEL / fuel_nozzle_inner_diameter | '物理參數'!G410；'物理參數'!G411 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| JET-SLICE-C2H4-020-N2-080-NOMINAL-D2P1-COFLOW-STABILITY-PANEL / oxidizer_coflow_velocity | '物理參數'!G412；'物理參數'!G413；'物理參數'!G414 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| JET-SLICE-C2H4-020-N2-080-NOMINAL-D2P1-COFLOW-STABILITY-PANEL / limiting_fuel_jet_velocity | '物理參數'!G412；'物理參數'!G413；'物理參數'!G414 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| JET-SLICE-C2H4-020-N2-080-NOMINAL-D2P1-COFLOW-STABILITY-MECHANISM / fuel_composition | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| JET-SLICE-C2H4-020-N2-080-NOMINAL-D2P1-COFLOW-STABILITY-MECHANISM / fuel_nozzle_inner_diameter | '物理參數'!G410；'物理參數'!G411 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| JET-SLICE-C2H4-020-N2-080-NOMINAL-D2P1-COFLOW-STABILITY-MECHANISM / oxidizer_coflow_velocity | '物理參數'!G412；'物理參數'!G413；'物理參數'!G414 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| JET-SLICE-C2H4-020-N2-080-NOMINAL-D2P1-COFLOW-STABILITY-MECHANISM / limiting_fuel_jet_velocity | '物理參數'!G412；'物理參數'!G413；'物理參數'!G414 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| JET-SLICE-STABILITY-GRAVITY-SCOPE / fuel_and_flow_regime | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |

| 文獻因子／疑點 | 正確讀法或需補資料 |
| --- | --- |
| 速度與幾何 | 原總表將部分cm/s欄列作尺寸；按原單位判讀速度。光學座標／像素不是已校準火焰尺寸。 |

## 3. 共用資料的多項結論比較

| 結論／文獻 | 資料重疊身份 | 共同處 | 不同處／不能合併之處 |
| --- | --- | --- | --- |
| JET-SLICE-C2H4-020-N2-080-NOMINAL-D2P1-COFLOW-STABILITY-PANEL；JET-SLICE-C2H4-020-N2-080-NOMINAL-D2P1-COFLOW-STABILITY-MECHANISM；JET-SLICE-STABILITY-GRAVITY-SCOPE | 來源系列；精確論文／試次交集仍以每項data_used為準 | 不把多份出版物當獨立實驗。 | 尚未取得完全同試次的多篇結論比較時保留缺口。 |
| JET-4fc7ff5b5432；JET-84be65105115；JET-fb028bca1f40 | same_SLICE_campaign_different_selected_subsets_and_observables | Buoyancy changes flame transport/shape under the studied conditions.；Source-specific calibration and boundary conditions are necessary. | Cao geometry paper spans40/70/100% methane at a3.24mm diameter inferred from its radius; Ma soot paper focuses100% methane1.59/3.23mm; Giassi CH* paper sequences A/B/C use3.2/.8/1.6mm and distinct velocity ranges.；Luminous geometry, soot volume fraction/temperature, calibrated CH* and computed heat release are different targets. Good shape agreement is not successful soot-quantity prediction.；尚未取得／不適用；尚未取得／不適用 |
| JET-c17adf3a6048；JET-7b44063f19e2；JET-bdaf4f1afd26；JET-6a211cdfa418 | successive_annual_reports_with_overlapping_campaign_and_publication_content | 同來源系列的不同觀測問題。 | 尚未取得／不適用；尚未取得／不適用；Different PDF hashes/years are document editions, not proof of new flight experiments. Specific embedded-paper identity is recorded below where titles are found. |

## 4. 消防洞見

| 類別 | 對應證據 | 數據支持的判斷 | 策略／產品構想 | 待驗證 |
| --- | --- | --- | --- | --- |
| 撲滅／抑制 | JET-SLICE-C2H4-020-N2-080-NOMINAL-D2P1-COFLOW-STABILITY-PANEL；JET-SLICE-C2H4-020-N2-080-NOMINAL-D2P1-COFLOW-STABILITY-MECHANISM；JET-SLICE-STABILITY-GRAVITY-SCOPE | 來源圖板將燃料速度、共流、抬升與吹熄界線分開；指定低速稀釋案例在微重力更穩定，其他高速案例重力差較小。 | 把火源成分／噴口與兩股速度一起辨識，再測試介入；地面吹熄條件不能直接保證微重力全熄。 | 先取得原始數值界線、相同程序與反應終止真值，再比較抑制效率；本輪沒有從圖板捏造閾值。 |
| 預防 | 尚未取得／不適用 | 尚未建立本組可直接支持此消防用途的完整量測鏈。 | 先補本組對應的物理端點與資料配對，再設計策略測試。 | 相關系列與方法限制只能提供研究脈絡，不能代替本組產品或操作效能驗證。 |
| 偵測 | 尚未取得／不適用 | 尚未建立本組可直接支持此消防用途的完整量測鏈。 | 先補本組對應的物理端點與資料配對，再設計策略測試。 | 相關系列與方法限制只能提供研究脈絡，不能代替本組產品或操作效能驗證。 |

## 逐次索引

尚未取得可逐項對照的紀錄。

## 缺件與適用範圍

- Source panel curves and markers are not digitized or turned into synthetic numeric thresholds.
- Original trial IDs, replicate counts, exact ramp histories and casewise pressure/O2 are missing.
- Liftoff, blowout and soot onset are distinct endpoints; source No Flame region is not a residual-fuel/CO safety clearance.
