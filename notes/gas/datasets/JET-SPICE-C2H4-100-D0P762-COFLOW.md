# Ethylene, 0.762 mm nozzle, microgravity coflow jet

小資料集 ID：`JET-SPICE-C2H4-100-D0P762-COFLOW`

## 資料身份與範圍

| 項目 | 內容 |
| --- | --- |
| 原始 NASA PSI investigation | [PSI-107](https://psi.nasa.gov/physci/repo/data/investigations/PSI-107) |
| 相關PSI索引（不是原始資料） | 尚未取得／不適用 |
| 材料／配方 | source_label: Ethylene；components_mole_fraction: C2H4: 1.0 |
| 幾何 | fuel_nozzle_inner_diameter_mm: 0.762；coflow_duct_cross_section_mm: 76；76 |
| 實驗模式 | laminar_nonpremixed_coflow_jet; operating sweeps and smoke-point search |
| 證據角色 | 氣體燃燒來源組 |
| 環境 | gravity: ISS microgravity；mode: laminar_nonpremixed_coflow_jet; operating sweeps and smoke-point search |
| 資料粒度／共享試片 | 原始試次／操作／圖上量測的身份見逐次索引，未預設互相一對一。 |
| 可用數值 | source_qualified_smoke_point_axial_luminous_length_only |

## 1. 文獻結果與視覺化程式

### JET-SPICE-C2H4-100-D0P762-COFLOW-OPS　JET-SPICE-C2H4-100-D0P762-COFLOW-OPS

**PSI-107_Experimental table_Spice.csv**

The original table records 12 flow observations for this fuel/nozzle; these are not 12 independent burns. The recorded coflow range is retained without a smoke-point label.

- 證據身份：observed_original_operating_settings。
- 文獻定位：JET-fb0d7e60cf53: Listed CSV logical records。
- 使用數據部分：source_id: JET-fb0d7e60cf53；csv_logical_records_including_header: 15；16；17；18；19；20；21；22；23；24；25；26；record_role: operating_observation_not_independent_burn。
- 本組適用層級：僅本項來源指定案例；逐次配對以data_used為準。
- 使用／控制因子：semantic_key: fuel_composition；source_raw_name: Fuel；unit: mole fraction；value_or_range: C2H4: 1.0；source_ref: source_id: JET-fb0d7e60cf53；locator: Fuel column of the listed records；workbook_mapping_status: pending_exact_cell_join_by_main; no synonym-only assumption；semantic_key: fuel_nozzle_inner_diameter；source_raw_name: Nozzle (mm)；unit: mm；value_or_range: 0.762；source_ref: source_id: JET-fb0d7e60cf53；locator: Nozzle (mm) column；workbook_mapping_status: pending_exact_cell_join_by_main; no synonym-only assumption；semantic_key: oxidizer_coflow_velocity；source_raw_name: Air Rate (cm/s)；unit: cm/s；value_or_range: 16.65；58.96；source_ref: source_id: JET-fb0d7e60cf53；locator: Air Rate (cm/s), listed records；workbook_mapping_status: pending_exact_cell_join_by_main; no synonym-only assumption。
- 來源限制：Only explicit reported numeric values define the range. Missing/censored entries remain missing; row 258 has n/a times and absent flow values.。
- 搜尋句（改寫）：The original table records 12 flow observations for this fuel/nozzle; these are not 12 independent burns. The recorded coflow range is retained without a smoke-point label.。
- 來源：[來源](<https://psi.nasa.gov/physci/repo/data/investigations/PSI-107>)
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/01_實驗資料/第一批下載/PSI-107_SPICE/Experimental table/PSI-107_Experimental table_Spice.csv>)

### JET-SPICE-C2H4-100-D0P762-COFLOW-ENDPOINT　JET-SPICE-C2H4-100-D0P762-COFLOW-ENDPOINT

**386d79d18d59ab1a_PSI-107_Raw Data_SmokePointReview-0g-3.xlsx**

This subgroup has 1 source smoke-point rows, of which 1 pass the existing source-calibration gate. The response is axial luminous length at onset of soot emission while fuel flow is adjusted.

- 證據身份：source_reduced_measured_endpoint。
- 文獻定位：JET-ed43c2b6c1cb: Smoke Point Datasheet rows in trial_index; JET-f579df9652dc: Experimental methods and Table 2。
- 使用數據部分：source_id: JET-ed43c2b6c1cb；sheet: Smoke Point Datasheet；excel_rows: 10；qualified_rows: 10；paper_data_use: Same SPICE campaign; complete publication-55 to workbook-55 point identity is not independently established for every row。
- 本組適用層級：僅本項來源指定案例；逐次配對以data_used為準。
- 使用／控制因子：semantic_key: fuel_composition；source_raw_name: Smoke Point Datasheet mixture / fuel mole fraction；unit: mole fraction；value_or_range: C2H4: 1.0；source_ref: source_id: JET-ed43c2b6c1cb；locator: G/L columns, listed endpoint rows；workbook_mapping_status: pending_exact_cell_join_by_main; no synonym-only assumption；semantic_key: fuel_nozzle_inner_diameter；source_raw_name: Smoke Point Datasheet nozzle diameter；unit: mm；value_or_range: 0.762；source_ref: source_id: JET-ed43c2b6c1cb；locator: H column, listed endpoint rows；workbook_mapping_status: pending_exact_cell_join_by_main; no synonym-only assumption；semantic_key: oxidizer_coflow_velocity；source_raw_name: Smoke Point Datasheet calibrated coflow；unit: cm/s；value_or_range: 17.587015019397825；17.587015019397825；source_ref: source_id: JET-ed43c2b6c1cb；locator: AD column; qualified endpoint rows only, not the full operating-table range；workbook_mapping_status: pending_exact_cell_join_by_main; no synonym-only assumption；semantic_key: smoke_point_axial_luminous_length；source_raw_name: Smoke Point Datasheet S；unit: mm；value_or_range: 105.22075589027847；105.22075589027847；source_ref: source_id: JET-ed43c2b6c1cb；locator: S column; eligible rows only；workbook_mapping_status: pending_exact_cell_join_by_main; no synonym-only assumption。
- 來源限制：Full width/contour not admitted; seven excluded source rows remain indexed with exact reasons.。
- 搜尋句（改寫）：This subgroup has 1 source smoke-point rows, of which 1 pass the existing source-calibration gate. The response is axial luminous length at onset of soot emission while fuel flow is adjusted.。
- 來源：[來源](<https://psi-curation-prod.s3.amazonaws.com/legacy/Filestreamdb/16057/SmokePointReview-0g-3.xlsx>)
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/01_實驗資料/補下載/PSI-107/Raw Data/386d79d18d59ab1a_PSI-107_Raw Data_SmokePointReview-0g-3.xlsx>)

- 共同來源：**Laminar smoke points of coflowing flames in microgravity**；Experimental methods and Table 2；[來源](<https://terpconnect.umd.edu/~pbs/2011%20Dotson%20et%20al.%20FSJ.pdf>)

### JET-SPICE-ENDPOINT-PROTOCOL　JET-SPICE-ENDPOINT-PROTOCOL

**Laminar smoke points of coflowing flames in microgravity**

Fuel flow was manually varied to seek the first soot-emission endpoint; brighter propylene flames and other fuels used different visible transition cues. No soot detector alarm threshold was measured.

- 證據身份：author_measured_protocol。
- 文獻定位：JET-f579df9652dc: Experimental methods and results。
- 使用數據部分：paper_data_use: SPICE 2009 flight campaign, 55 published endpoints; not every operational table record。
- 本組適用層級：僅本項來源指定案例；逐次配對以data_used為準。
- 使用／控制因子：semantic_key: adjusted_fuel_flow；source_raw_name: mass flow meter/manual adjustment；unit: endpoint response；value_or_range: 尚未取得／不適用；source_ref: source_id: JET-f579df9652dc；physical_pdf_pages: 3；4；locator: Experimental methods；workbook_mapping_status: pending_exact_cell_join_by_main; no synonym-only assumption。
- 來源限制：A longer soot-onset flame does not by itself establish a safer operating state or better smoke detection.。
- 搜尋句（改寫）：Fuel flow was manually varied to seek the first soot-emission endpoint; brighter propylene flames and other fuels used different visible transition cues. No soot detector alarm threshold was measured.。
- 來源：[來源](<https://terpconnect.umd.edu/~pbs/2011%20Dotson%20et%20al.%20FSJ.pdf>)
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/02_論文全文/01_期刊論文與作者稿/Laminar smoke points of coflowing flames in microgravity__f579df9652.pdf>)

### JET-SPICE-REFERENCE-CONTEXT　JET-SPICE-REFERENCE-CONTEXT

**Laminar smoke points of coflowing flames in microgravity**

The coflow was calibrated in normal gravity and varied within a nonuniform duct; ISS oxygen was only estimated in a 20–23% range. O2 and pressure are not independently swept casewise inputs.

- 證據身份：author_measurement_context。
- 文獻定位：JET-f579df9652dc: Experimental methods。
- 使用數據部分：paper_data_use: Apparatus/calibration context; no additional flame trials。
- 本組適用層級：僅本項來源指定案例；逐次配對以data_used為準。
- 使用／控制因子：semantic_key: ambient_oxygen_fraction；source_raw_name: estimated oxygen mole fraction；unit: fraction；value_or_range: 0.2；0.23；source_ref: source_id: JET-f579df9652dc；physical_pdf_pages: 3；locator: Experimental methods；workbook_mapping_status: pending_exact_cell_join_by_main; no synonym-only assumption；semantic_key: coflow_spatial_variation；source_raw_name: velocities at other locations；unit: relative approx；value_or_range: 0.1；source_ref: source_id: JET-f579df9652dc；physical_pdf_pages: 3；locator: Hot-sphere/hot-wire calibration；workbook_mapping_status: pending_exact_cell_join_by_main; no synonym-only assumption。
- 來源限制：Do not use these nominal ranges to infer high-O2 lunar-cabin behavior or a joint equipment safety envelope.。
- 搜尋句（改寫）：The coflow was calibrated in normal gravity and varied within a nonuniform duct; ISS oxygen was only estimated in a 20–23% range. O2 and pressure are not independently swept casewise inputs.。
- 來源：[來源](<https://terpconnect.umd.edu/~pbs/2011%20Dotson%20et%20al.%20FSJ.pdf>)
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/02_論文全文/01_期刊論文與作者稿/Laminar smoke points of coflowing flames in microgravity__f579df9652.pdf>)

| Model ID | 公式／預測量 | 展示程式 | 數值比較與限制 |
| --- | --- | --- | --- |
| SPICE-PUBLISHED-EQ7 | Lsp_mm=Af_mixture*(d_mm)^a*(Uair_cm_s)^b；Axial luminous flame length at incipient soot emission (mm) | producer.py · [開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/tools/gas_evidence/models/producer.py>) | runnable；same_source_reproduction；R²（模型全群）=0.8997756724470198；本組: mixture: Ethylene；diameter_mm: 0.762；source_records: 1；source_burn_groups: 1；ordinary_row_r2: 尚未取得／不適用；mae_mm: 16.246086962162508；rmse_mm: 16.246086962162508；score_scope: Same-campaign source-reduced points and published fixed calibration; not an independent holdout or safety score.；門檻: R²≥0.85僅為描述性貼合門檻，非獨立驗證；負R²與不足不隱藏。；Five independent source mixture constants; no shared fitted dilution adjustment is introduced.；Fuel flow was manually adjusted to find each smoke point; this is not a fixed-fuel-flow flame-length predictor.；No prediction at zero coflow, for methane, or at new pressure/oxygen/gravity conditions.；Nozzle and flow controls are restricted to actually represented mixture/nozzle groups and their observed coflow intervals; this does not establish a full joint safety envelope.；55source records are indexed; seven remain excluded for prior calibration-provenance reasons, not their residual size.；Published author uncertainties are estimates, not calibrated model prediction intervals.；direct_PSI107_ISS_source_campaign；published same-campaign correlation replay against original source-reduced measurements |

| 可開啟的圖／工具 | 身份與用途 |
| --- | --- |
| [開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/gas_combustion_evidence_20261115/models/spice_fixed_source_comparison.png>) | 固定已發表係數；同來源校準群重現，不是獨立或跨尺寸盲測 |
| [開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/gas_combustion_evidence_20261115/models/comparison.html>) | 選正確架構；缺資料的研究僅顯示就緒度，不畫假預測 |

## 2. 使用資料與參數總表的因子對照

| 總表原分類 | 來源身份 | 原欄名單位 | 原欄名例 | 總表定位 |
| --- | --- | --- | --- | --- |
| 其他氣體組成／濃度 | 條件或分析量 | 未由欄名確認 | Xf；Nitrogen；where xi is the mole fraction of the ith gases. | '物理參數'!A425:K425 |
| 化學計量混合分率 | 計算／分析參數 | 未由欄名確認 | Re/Zst；mf/Zst；Zst | '物理參數'!A426:K426 |
| 壓力 | 量測或設定 | 未由欄名確認 | Pressure；psia | '物理參數'!A427:K427 |
| 密度 | 量測或來源分析量 | g/l | density(g/l)；Density (g/l) | '物理參數'!A428:K428 |
| 密度 | 量測或來源分析量 | g/m^3 | Density (g/m^3) | '物理參數'!A429:K429 |
| 密度 | 量測或來源分析量 | 未由欄名確認 | HC Density；Density | '物理參數'!A430:K430 |
| 尺寸／幾何 | 裝置或樣本條件 | cm/s | U,probe (cm/s)；(cm/s)；Measured Velocities (cm/s)；U (cm/s)；Fluctuations (cm/s) | '物理參數'!A431:K431 |
| 尺寸／幾何 | 裝置或樣本條件 | mm | Nozzle (mm)；(mm)；Spice ruler (mm) = -14.599*PS reading + 111.04；Spice ruler Reading (mm)；Width (mm)；Nikon (mm) | '物理參數'!A432:K432 |
| 尺寸／幾何 | 裝置或樣本條件 | pixels | Width (pixels) | '物理參數'!A433:K433 |
| 尺寸／幾何 | 裝置或樣本條件 | 未由欄名確認 | mm；13 mm station (z=65) * 36 mm Height (y=10)；13 mm station (z=65) * 57 mm Height (y=-11)；13 mm station (z=65) * 19 mm Height (y=28)；56 mm station (z=108) * 36 mm Height (y=10)；56 mm station (z=108) * 57 mm Height (y=-11)；56 mm station (z=108) * 19 mm Height (y=28)；4mm above the nozzle；Nozzle；length；其餘見原始欄位 | '物理參數'!A434:K434 |
| 影像／光譜設定 | 儀器設定或影像座標 | pixels | Nikon (pixels) | '物理參數'!A435:K435 |
| 影像／光譜設定 | 儀器設定或影像座標 | 未由欄名確認 | Pixel；x264 Pixel；Exposure Comp.；Exceeds frame；Lowest exposure | '物理參數'!A436:K436 |
| 流速／通風 | 量測或設定 | cm/s | Air Rate (cm/s)；Fuel Velocity(cm/s)；Velocity (cm/s) | '物理參數'!A437:K437 |
| 流速／通風 | 量測或設定 | 未由欄名確認 | Anemometer；Velocity；Air Rate；Velocity Ratio | '物理參數'!A438:K438 |
| 溫度 | 量測或設定 | K | Temperature(K) | '物理參數'!A439:K439 |
| 溫度 | 量測或設定 | 未由欄名確認 | Temperature；temperature；Temperature: | '物理參數'!A440:K440 |
| 火焰幾何／延燒 | 影像／來源分析量 | 未由欄名確認 | Flame Height | '物理參數'!A441:K441 |
| 燃燒／點火／老化時間 | 時序或處理條件 | 未由欄名確認 | GMT Flame Off；flame off | '物理參數'!A442:K442 |
| 硬體電壓／電流／功率 | 儀器設定／控制參數 | 未由欄名確認 | Aout Voltage setting (Nominal) | '物理參數'!A443:K443 |
| 硬體電壓／電流／功率 | 原始訊號或狀態 | 未由欄名確認 | Aout Voltage reading (Actual)；Volts；volts；ohms；Voltmeter:；#2 ("Voltmeter")；Probe Voltage Readings (120 readings, 60 sec.) | '物理參數'!A444:K444 |
| 絕熱溫度 | 計算／分析參數 | 未由欄名確認 | Tad；(Tad+Tamb)/2；Tad Fuel | '物理參數'!A445:K445 |
| 質量流率 | 量測或設定 | mg/s | Fuel Rate (mg/s)；HC Fuel Rate (mg/s)；(mg/s) | '物理參數'!A446:K446 |
| 質量流率 | 量測或設定 | 未由欄名確認 | Mass Flow meter call | '物理參數'!A447:K447 |
| 質量／質量損失 | 量測或衍生 | 未由欄名確認 | Molecular weight | '物理參數'!A448:K448 |
| 風扇／流量顯示設定 | 儀器設定 | 未由欄名確認 | FAN；FAN Reading；Fan；Fan reading | '物理參數'!A449:K449 |
| 風扇／流量顯示設定 | 儀器設定／控制參數 | 未由欄名確認 | Fan setting；Fan settings；Fan Dial Setting = 0；Fan Dial Setting = 2；Fan Dial Setting = 4；Fan Dial Setting = 6；Fan Dial Setting = 8；Fan Dial Setting = 10 | '物理參數'!A450:K450 |
| 體積流量／MFC | 量測或設定 | SCCM | FLOW RATE (SCCM) | '物理參數'!A451:K451 |
| 體積流量／MFC | 量測或設定 | sccm | Fuel Rate (sccm)；Flow rate (sccm)；N2 Flow rate (sccm) at Calibration condition | '物理參數'!A452:K452 |
| 體積流量／MFC | 量測或設定 | 未由欄名確認 | Flowrate；Total Fuel Rate；sccm；Fuel Rate；N2 Flow rate (sccm) at STP condition (i.e. T = 273.2K)；SCCM；HC Fuel Rate | '物理參數'!A453:K453 |

以上是該 investigation 的欄位盤點；個別結論實際使用的因子以第1節與下列補充為準。

| 本組實際因子 | 總表定位／未列欄位 | 文獻中的用途 |
| --- | --- | --- |
| JET-SPICE-C2H4-100-D0P762-COFLOW-OPS / fuel_composition | '物理參數'!G425 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| JET-SPICE-C2H4-100-D0P762-COFLOW-OPS / fuel_nozzle_inner_diameter | '物理參數'!G432；'物理參數'!G434 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| JET-SPICE-C2H4-100-D0P762-COFLOW-OPS / oxidizer_coflow_velocity | '物理參數'!G437；'物理參數'!G438 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| JET-SPICE-C2H4-100-D0P762-COFLOW-ENDPOINT / fuel_composition | '物理參數'!G425 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| JET-SPICE-C2H4-100-D0P762-COFLOW-ENDPOINT / fuel_nozzle_inner_diameter | '物理參數'!G432；'物理參數'!G434 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| JET-SPICE-C2H4-100-D0P762-COFLOW-ENDPOINT / oxidizer_coflow_velocity | '物理參數'!G437；'物理參數'!G438 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| JET-SPICE-C2H4-100-D0P762-COFLOW-ENDPOINT / smoke_point_axial_luminous_length | '物理參數'!G441 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| JET-SPICE-ENDPOINT-PROTOCOL / adjusted_fuel_flow | '物理參數'!G446；'物理參數'!G447 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| JET-SPICE-REFERENCE-CONTEXT / ambient_oxygen_fraction | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| JET-SPICE-REFERENCE-CONTEXT / coflow_spatial_variation | '物理參數'!G437；'物理參數'!G438 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |

| 文獻因子／疑點 | 正確讀法或需補資料 |
| --- | --- |
| 速度與幾何 | 原總表將部分cm/s欄列作尺寸；按原單位判讀速度。光學座標／像素不是已校準火焰尺寸。 |

## 3. 共用資料的多項結論比較

| 結論／文獻 | 資料重疊身份 | 共同處 | 不同處／不能合併之處 |
| --- | --- | --- | --- |
| JET-SPICE-C2H4-100-D0P762-COFLOW-OPS；JET-SPICE-C2H4-100-D0P762-COFLOW-ENDPOINT；JET-SPICE-ENDPOINT-PROTOCOL；JET-SPICE-REFERENCE-CONTEXT | 來源系列；精確論文／試次交集仍以每項data_used為準 | 不把多份出版物當獨立實驗。 | 尚未取得完全同試次的多篇結論比較時保留缺口。 |
| JET-1bb111e67a91；JET-0ba8a154fc17；JET-bd980e9e1195；JET-95e76859017d；JET-f579df9652dc | same_SPICE_2009_campaign_or_reports_not_independent_replication | Coflow/nozzle context affects the soot-onset endpoint.；Residence time is a qualitative explanation, not a quantitatively validated universal smoke-point criterion. | source_id: JET-0ba8a154fc17；physical_pages: 6；table: 1；reported_endpoint_count: 52；source_id: JET-95e76859017d；physical_pages: 2；reported_endpoint_count: 52；note: Draft report has editing placeholders; later text also uses55. Do not silently reconcile.；source_id: JET-f579df9652dc；physical_pages: 1；3；reported_endpoint_count: 55；table: 2；Published 55 versus qualified local48 is a source/calibration selection difference, not seven invented missing experiments; exact every-point publication join is not established.；尚未取得／不適用 |

## 4. 消防洞見

| 類別 | 對應證據 | 數據支持的判斷 | 策略／產品構想 | 待驗證 |
| --- | --- | --- | --- | --- |
| 預防 | JET-SPICE-C2H4-100-D0P762-COFLOW-OPS；JET-SPICE-C2H4-100-D0P762-COFLOW-ENDPOINT；JET-SPICE-ENDPOINT-PROTOCOL；JET-SPICE-REFERENCE-CONTEXT | 來源煙點量是指定流況下開始排出soot的發光焰長；它不是任意燃料流率下的焰長、內禀材料常數或安全距離。 | 把燃料、噴口與共流條件一起附在煙點／熱暴露比較上，優先補同工況的熱流與鄰材反應。 | 需同步熱釋放／熱通量與鄰材點燃；不以較短煙點長度直接判定較安全。 |
| 偵測 | JET-SPICE-C2H4-100-D0P762-COFLOW-OPS；JET-SPICE-C2H4-100-D0P762-COFLOW-ENDPOINT；JET-SPICE-ENDPOINT-PROTOCOL；JET-SPICE-REFERENCE-CONTEXT | 煙點端點和偵測器響應／警報門檻不是同一個量；本組沒有配對的警報效能。 | 用來源已核對的煙生成條件安排偵測器挑戰試驗，分開煙生成與輸運。 | 同來源煙粒、氣流、校準與啟用警報真值。 |
| 撲滅／抑制 | 尚未取得／不適用 | 尚未建立本組可直接支持此消防用途的完整量測鏈。 | 先補本組對應的物理端點與資料配對，再設計策略測試。 | 相關系列與方法限制只能提供研究脈絡，不能代替本組產品或操作效能驗證。 |

## 逐次索引

| 原始檔／資料位置 | Trial／Run／列 | 共享身份與保留事項 |
| --- | --- | --- |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\補下載\PSI-107\Raw Data\386d79d18d59ab1a_PSI-107_Raw Data_SmokePointReview-0g-3.xlsx | original_case_id: E7-1；source_row: 10；source_sheet: Smoke Point Datasheet；source_cells: day: Smoke Point Datasheet!A10；case_id: Smoke Point Datasheet!F10；mixture: Smoke Point Datasheet!G10；fuel_mole_fraction: Smoke Point Datasheet!L10；nozzle_mm: Smoke Point Datasheet!H10；nominal_pressure_pa: Smoke Point Datasheet!I10；coflow_cm_s: Smoke Point Datasheet!AD10；air_display: Smoke Point Datasheet!N10；tip_pixel: Smoke Point Datasheet!R10；length_mm: Smoke Point Datasheet!S10；group_id: run_group_audit.json#smokePointRowGroups[row=10]；record_id: PSI-107\|sha256:ed43c2b6c1cb82d1060ed4739a1ea04c68410e53e9f894f8078df0bda1f09fa9\|Smoke Point Datasheet\|row:10；physical_burn_group_id: SPICE-GMT045-IGN-62868；campaign_day: 45；observation_class: source_reduced_smoke_point_endpoint；eligible_scalar_length: True；exclusion_reasons: 尚未取得／不適用；inputs: fuel_mole_fraction: 1.0；burner_inner_diameter_m: 0.000762；oxidizer_coflow_m_s: 0.17587015019397825；targets: smoke_point_axial_luminous_length_m: 0.10522075589027846；maximum_flame_width_m: 尚未取得／不適用；boundary_xy_m: 尚未取得／不適用；source_calibration: length_formula: =R10*Reference!$B$23+Reference!$B$24；tip_pixel_coordinate: 63.0；slope_cell: Reference!B23；slope_mm_per_pixel: -0.22973813307538177；intercept_cell: Reference!B24；intercept_mm: 119.6942582740275；original_cached_length_mm: 105.22075589027845；recomputed_length_mm: 105.22075589027845；length_cache_abs_error_mm: 0.0；coflow_formula: =N10*Reference!$F$10+Reference!$F$11；raw_air_display: 25.0；coflow_slope_cell: Reference!F10；coflow_slope: 0.9402153845089276；coflow_intercept_cell: Reference!F11；coflow_intercept: -5.918369593325366；original_cached_coflow_cm_s: 17.587015019397825；recomputed_coflow_cm_s: 17.587015019397825；coflow_cache_abs_error_cm_s: 0.0；calibration_decision: eligible_original_source | raw_parameters_as_stored: 尚未取得／不適用；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-107_SPICE\Experimental table\PSI-107_Experimental table_Spice.csv | csv_logical_record_including_header: 15；source_cells: GMT date: CSV record 15, column GMT date；GMT ignition: CSV record 15, column GMT ignition；GMT  Flame Off : CSV record 15, column GMT  Flame Off ；Fuel: CSV record 15, column Fuel；Nozzle (mm): CSV record 15, column Nozzle (mm)；Fuel Rate (sccm): CSV record 15, column Fuel Rate (sccm)；Fuel Rate (mg/s): CSV record 15, column Fuel Rate (mg/s)；HC Fuel Rate (mg/s): CSV record 15, column HC Fuel Rate (mg/s)；Air Rate (cm/s): CSV record 15, column Air Rate (cm/s)；verified_endpoint_or_burn_join: False；row_role: within_burn_flow_observation_not_new_burn | raw_parameters_as_stored: GMT date: 45；GMT ignition: 17:11:46；GMT  Flame Off : 17:12:37；Fuel: Ethylene；Nozzle (mm): 0.762；Fuel Rate (sccm): 219；Fuel Rate (mg/s): 4.158；HC Fuel Rate (mg/s): 4.158；Air Rate (cm/s): 33.57；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-107_SPICE\Experimental table\PSI-107_Experimental table_Spice.csv | csv_logical_record_including_header: 16；source_cells: GMT date: CSV record 16, column GMT date；GMT ignition: CSV record 16, column GMT ignition；GMT  Flame Off : CSV record 16, column GMT  Flame Off ；Fuel: CSV record 16, column Fuel；Nozzle (mm): CSV record 16, column Nozzle (mm)；Fuel Rate (sccm): CSV record 16, column Fuel Rate (sccm)；Fuel Rate (mg/s): CSV record 16, column Fuel Rate (mg/s)；HC Fuel Rate (mg/s): CSV record 16, column HC Fuel Rate (mg/s)；Air Rate (cm/s): CSV record 16, column Air Rate (cm/s)；verified_endpoint_or_burn_join: False；row_role: within_burn_flow_observation_not_new_burn | raw_parameters_as_stored: GMT date: 45；GMT ignition: 17:11:46；GMT  Flame Off : 17:12:37；Fuel: Ethylene；Nozzle (mm): 0.762；Fuel Rate (sccm): 221.4；Fuel Rate (mg/s): 4.203；HC Fuel Rate (mg/s): 4.203；Air Rate (cm/s): 33.57；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-107_SPICE\Experimental table\PSI-107_Experimental table_Spice.csv | csv_logical_record_including_header: 17；source_cells: GMT date: CSV record 17, column GMT date；GMT ignition: CSV record 17, column GMT ignition；GMT  Flame Off : CSV record 17, column GMT  Flame Off ；Fuel: CSV record 17, column Fuel；Nozzle (mm): CSV record 17, column Nozzle (mm)；Fuel Rate (sccm): CSV record 17, column Fuel Rate (sccm)；Fuel Rate (mg/s): CSV record 17, column Fuel Rate (mg/s)；HC Fuel Rate (mg/s): CSV record 17, column HC Fuel Rate (mg/s)；Air Rate (cm/s): CSV record 17, column Air Rate (cm/s)；verified_endpoint_or_burn_join: False；row_role: within_burn_flow_observation_not_new_burn | raw_parameters_as_stored: GMT date: 45；GMT ignition: 17:15:05；GMT  Flame Off : 17:15:32；Fuel: Ethylene；Nozzle (mm): 0.762；Fuel Rate (sccm): 109.2；Fuel Rate (mg/s): 2.073；HC Fuel Rate (mg/s): 2.073；Air Rate (cm/s): 34.51；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-107_SPICE\Experimental table\PSI-107_Experimental table_Spice.csv | csv_logical_record_including_header: 18；source_cells: GMT date: CSV record 18, column GMT date；GMT ignition: CSV record 18, column GMT ignition；GMT  Flame Off : CSV record 18, column GMT  Flame Off ；Fuel: CSV record 18, column Fuel；Nozzle (mm): CSV record 18, column Nozzle (mm)；Fuel Rate (sccm): CSV record 18, column Fuel Rate (sccm)；Fuel Rate (mg/s): CSV record 18, column Fuel Rate (mg/s)；HC Fuel Rate (mg/s): CSV record 18, column HC Fuel Rate (mg/s)；Air Rate (cm/s): CSV record 18, column Air Rate (cm/s)；verified_endpoint_or_burn_join: False；row_role: within_burn_flow_observation_not_new_burn | raw_parameters_as_stored: GMT date: 45；GMT ignition: 17:15:05；GMT  Flame Off : 17:15:32；Fuel: Ethylene；Nozzle (mm): 0.762；Fuel Rate (sccm): 109.2；Fuel Rate (mg/s): 2.073；HC Fuel Rate (mg/s): 2.073；Air Rate (cm/s): 35.45；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-107_SPICE\Experimental table\PSI-107_Experimental table_Spice.csv | csv_logical_record_including_header: 19；source_cells: GMT date: CSV record 19, column GMT date；GMT ignition: CSV record 19, column GMT ignition；GMT  Flame Off : CSV record 19, column GMT  Flame Off ；Fuel: CSV record 19, column Fuel；Nozzle (mm): CSV record 19, column Nozzle (mm)；Fuel Rate (sccm): CSV record 19, column Fuel Rate (sccm)；Fuel Rate (mg/s): CSV record 19, column Fuel Rate (mg/s)；HC Fuel Rate (mg/s): CSV record 19, column HC Fuel Rate (mg/s)；Air Rate (cm/s): CSV record 19, column Air Rate (cm/s)；verified_endpoint_or_burn_join: False；row_role: within_burn_flow_observation_not_new_burn | raw_parameters_as_stored: GMT date: 45；GMT ignition: 17:20:46；GMT  Flame Off : 17:21:17；Fuel: Ethylene；Nozzle (mm): 0.762；Fuel Rate (sccm): 231.6；Fuel Rate (mg/s): 4.397；HC Fuel Rate (mg/s): 4.397；Air Rate (cm/s): 58.02；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-107_SPICE\Experimental table\PSI-107_Experimental table_Spice.csv | csv_logical_record_including_header: 20；source_cells: GMT date: CSV record 20, column GMT date；GMT ignition: CSV record 20, column GMT ignition；GMT  Flame Off : CSV record 20, column GMT  Flame Off ；Fuel: CSV record 20, column Fuel；Nozzle (mm): CSV record 20, column Nozzle (mm)；Fuel Rate (sccm): CSV record 20, column Fuel Rate (sccm)；Fuel Rate (mg/s): CSV record 20, column Fuel Rate (mg/s)；HC Fuel Rate (mg/s): CSV record 20, column HC Fuel Rate (mg/s)；Air Rate (cm/s): CSV record 20, column Air Rate (cm/s)；verified_endpoint_or_burn_join: False；row_role: within_burn_flow_observation_not_new_burn | raw_parameters_as_stored: GMT date: 45；GMT ignition: 17:20:47；GMT  Flame Off : 17:21:17；Fuel: Ethylene；Nozzle (mm): 0.762；Fuel Rate (sccm): 231.6；Fuel Rate (mg/s): 4.397；HC Fuel Rate (mg/s): 4.397；Air Rate (cm/s): 58.96；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-107_SPICE\Experimental table\PSI-107_Experimental table_Spice.csv | csv_logical_record_including_header: 21；source_cells: GMT date: CSV record 21, column GMT date；GMT ignition: CSV record 21, column GMT ignition；GMT  Flame Off : CSV record 21, column GMT  Flame Off ；Fuel: CSV record 21, column Fuel；Nozzle (mm): CSV record 21, column Nozzle (mm)；Fuel Rate (sccm): CSV record 21, column Fuel Rate (sccm)；Fuel Rate (mg/s): CSV record 21, column Fuel Rate (mg/s)；HC Fuel Rate (mg/s): CSV record 21, column HC Fuel Rate (mg/s)；Air Rate (cm/s): CSV record 21, column Air Rate (cm/s)；verified_endpoint_or_burn_join: False；row_role: within_burn_flow_observation_not_new_burn | raw_parameters_as_stored: GMT date: 45；GMT ignition: 17:23:03；GMT  Flame Off : 17:23:30；Fuel: Ethylene；Nozzle (mm): 0.762；Fuel Rate (sccm): 114.6；Fuel Rate (mg/s): 2.176；HC Fuel Rate (mg/s): 2.176；Air Rate (cm/s): 57.08；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-107_SPICE\Experimental table\PSI-107_Experimental table_Spice.csv | csv_logical_record_including_header: 22；source_cells: GMT date: CSV record 22, column GMT date；GMT ignition: CSV record 22, column GMT ignition；GMT  Flame Off : CSV record 22, column GMT  Flame Off ；Fuel: CSV record 22, column Fuel；Nozzle (mm): CSV record 22, column Nozzle (mm)；Fuel Rate (sccm): CSV record 22, column Fuel Rate (sccm)；Fuel Rate (mg/s): CSV record 22, column Fuel Rate (mg/s)；HC Fuel Rate (mg/s): CSV record 22, column HC Fuel Rate (mg/s)；Air Rate (cm/s): CSV record 22, column Air Rate (cm/s)；verified_endpoint_or_burn_join: False；row_role: within_burn_flow_observation_not_new_burn | raw_parameters_as_stored: GMT date: 45；GMT ignition: 17:23:03；GMT  Flame Off : 17:23:30；Fuel: Ethylene；Nozzle (mm): 0.762；Fuel Rate (sccm): 114；Fuel Rate (mg/s): 2.164；HC Fuel Rate (mg/s): 2.164；Air Rate (cm/s): 57.08；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-107_SPICE\Experimental table\PSI-107_Experimental table_Spice.csv | csv_logical_record_including_header: 23；source_cells: GMT date: CSV record 23, column GMT date；GMT ignition: CSV record 23, column GMT ignition；GMT  Flame Off : CSV record 23, column GMT  Flame Off ；Fuel: CSV record 23, column Fuel；Nozzle (mm): CSV record 23, column Nozzle (mm)；Fuel Rate (sccm): CSV record 23, column Fuel Rate (sccm)；Fuel Rate (mg/s): CSV record 23, column Fuel Rate (mg/s)；HC Fuel Rate (mg/s): CSV record 23, column HC Fuel Rate (mg/s)；Air Rate (cm/s): CSV record 23, column Air Rate (cm/s)；verified_endpoint_or_burn_join: False；row_role: within_burn_flow_observation_not_new_burn | raw_parameters_as_stored: GMT date: 45；GMT ignition: 17:27:48；GMT  Flame Off : 17:28:21；Fuel: Ethylene；Nozzle (mm): 0.762；Fuel Rate (sccm): 201；Fuel Rate (mg/s): 3.816；HC Fuel Rate (mg/s): 3.816；Air Rate (cm/s): 17.59；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-107_SPICE\Experimental table\PSI-107_Experimental table_Spice.csv | csv_logical_record_including_header: 24；source_cells: GMT date: CSV record 24, column GMT date；GMT ignition: CSV record 24, column GMT ignition；GMT  Flame Off : CSV record 24, column GMT  Flame Off ；Fuel: CSV record 24, column Fuel；Nozzle (mm): CSV record 24, column Nozzle (mm)；Fuel Rate (sccm): CSV record 24, column Fuel Rate (sccm)；Fuel Rate (mg/s): CSV record 24, column Fuel Rate (mg/s)；HC Fuel Rate (mg/s): CSV record 24, column HC Fuel Rate (mg/s)；Air Rate (cm/s): CSV record 24, column Air Rate (cm/s)；verified_endpoint_or_burn_join: False；row_role: within_burn_flow_observation_not_new_burn | raw_parameters_as_stored: GMT date: 45；GMT ignition: 17:27:48；GMT  Flame Off : 17:28:21；Fuel: Ethylene；Nozzle (mm): 0.762；Fuel Rate (sccm): 199.2；Fuel Rate (mg/s): 3.782；HC Fuel Rate (mg/s): 3.782；Air Rate (cm/s): 18.53；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-107_SPICE\Experimental table\PSI-107_Experimental table_Spice.csv | csv_logical_record_including_header: 25；source_cells: GMT date: CSV record 25, column GMT date；GMT ignition: CSV record 25, column GMT ignition；GMT  Flame Off : CSV record 25, column GMT  Flame Off ；Fuel: CSV record 25, column Fuel；Nozzle (mm): CSV record 25, column Nozzle (mm)；Fuel Rate (sccm): CSV record 25, column Fuel Rate (sccm)；Fuel Rate (mg/s): CSV record 25, column Fuel Rate (mg/s)；HC Fuel Rate (mg/s): CSV record 25, column HC Fuel Rate (mg/s)；Air Rate (cm/s): CSV record 25, column Air Rate (cm/s)；verified_endpoint_or_burn_join: False；row_role: within_burn_flow_observation_not_new_burn | raw_parameters_as_stored: GMT date: 45；GMT ignition: 17:29:49；GMT  Flame Off : 17:30:24；Fuel: Ethylene；Nozzle (mm): 0.762；Fuel Rate (sccm): 99；Fuel Rate (mg/s): 1.879；HC Fuel Rate (mg/s): 1.879；Air Rate (cm/s): 16.65；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-107_SPICE\Experimental table\PSI-107_Experimental table_Spice.csv | csv_logical_record_including_header: 26；source_cells: GMT date: CSV record 26, column GMT date；GMT ignition: CSV record 26, column GMT ignition；GMT  Flame Off : CSV record 26, column GMT  Flame Off ；Fuel: CSV record 26, column Fuel；Nozzle (mm): CSV record 26, column Nozzle (mm)；Fuel Rate (sccm): CSV record 26, column Fuel Rate (sccm)；Fuel Rate (mg/s): CSV record 26, column Fuel Rate (mg/s)；HC Fuel Rate (mg/s): CSV record 26, column HC Fuel Rate (mg/s)；Air Rate (cm/s): CSV record 26, column Air Rate (cm/s)；verified_endpoint_or_burn_join: False；row_role: within_burn_flow_observation_not_new_burn | raw_parameters_as_stored: GMT date: 45；GMT ignition: 17:29:48；GMT  Flame Off : 17:30:24；Fuel: Ethylene；Nozzle (mm): 0.762；Fuel Rate (sccm): 114；Fuel Rate (mg/s): 2.164；HC Fuel Rate (mg/s): 2.164；Air Rate (cm/s): 16.65；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |

## 缺件與適用範圍

- Per-case ambient O2, pressure and inlet-temperature measurements are unavailable; nominal/reference context is not a parameter sweep.
- No verified exact master-time join between every operating observation and each endpoint; do not substitute row order or TP/No values.
- Smoke-point length is not general arbitrary-flow flame geometry, an intrinsic fuel property or detector alarm threshold.
- No ignition/extinction/toxic-gas/engineering-safety prediction is established.
