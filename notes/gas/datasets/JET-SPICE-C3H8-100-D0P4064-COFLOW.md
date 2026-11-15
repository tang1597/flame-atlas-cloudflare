# Propane, 0.4064 mm nozzle, microgravity coflow jet

小資料集 ID：`JET-SPICE-C3H8-100-D0P4064-COFLOW`

## 資料身份與範圍

| 項目 | 內容 |
| --- | --- |
| 原始 NASA PSI investigation | [PSI-107](https://psi.nasa.gov/physci/repo/data/investigations/PSI-107) |
| 相關PSI索引（不是原始資料） | 尚未取得／不適用 |
| 材料／配方 | source_label: Propane；components_mole_fraction: C3H8: 1.0 |
| 幾何 | fuel_nozzle_inner_diameter_mm: 0.4064；coflow_duct_cross_section_mm: 76；76 |
| 實驗模式 | laminar_nonpremixed_coflow_jet; operating sweeps and smoke-point search |
| 證據角色 | 氣體燃燒來源組 |
| 環境 | gravity: ISS microgravity；mode: laminar_nonpremixed_coflow_jet; operating sweeps and smoke-point search |
| 資料粒度／共享試片 | 原始試次／操作／圖上量測的身份見逐次索引，未預設互相一對一。 |
| 可用數值 | operating_settings_only_no_admitted_smoke_point_geometry |

## 1. 文獻結果與視覺化程式

### JET-SPICE-C3H8-100-D0P4064-COFLOW-OPS　JET-SPICE-C3H8-100-D0P4064-COFLOW-OPS

**PSI-107_Experimental table_Spice.csv**

The original table records 16 flow observations for this fuel/nozzle; these are not 16 independent burns. The recorded coflow range is retained without a smoke-point label.

- 證據身份：observed_original_operating_settings。
- 文獻定位：JET-fb0d7e60cf53: Listed CSV logical records。
- 使用數據部分：source_id: JET-fb0d7e60cf53；csv_logical_records_including_header: 70；71；72；73；74；75；76；77；78；79；80；81；82；83；84；85；record_role: operating_observation_not_independent_burn。
- 本組適用層級：僅本項來源指定案例；逐次配對以data_used為準。
- 使用／控制因子：semantic_key: fuel_composition；source_raw_name: Fuel；unit: mole fraction；value_or_range: C3H8: 1.0；source_ref: source_id: JET-fb0d7e60cf53；locator: Fuel column of the listed records；workbook_mapping_status: pending_exact_cell_join_by_main; no synonym-only assumption；semantic_key: fuel_nozzle_inner_diameter；source_raw_name: Nozzle (mm)；unit: mm；value_or_range: 0.4064；source_ref: source_id: JET-fb0d7e60cf53；locator: Nozzle (mm) column；workbook_mapping_status: pending_exact_cell_join_by_main; no synonym-only assumption；semantic_key: oxidizer_coflow_velocity；source_raw_name: Air Rate (cm/s)；unit: cm/s；value_or_range: 14.77；33.57；source_ref: source_id: JET-fb0d7e60cf53；locator: Air Rate (cm/s), listed records；workbook_mapping_status: pending_exact_cell_join_by_main; no synonym-only assumption。
- 來源限制：Only explicit reported numeric values define the range. Missing/censored entries remain missing; row 258 has n/a times and absent flow values.。
- 搜尋句（改寫）：The original table records 16 flow observations for this fuel/nozzle; these are not 16 independent burns. The recorded coflow range is retained without a smoke-point label.。
- 來源：[來源](<https://psi.nasa.gov/physci/repo/data/investigations/PSI-107>)
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/01_實驗資料/第一批下載/PSI-107_SPICE/Experimental table/PSI-107_Experimental table_Spice.csv>)

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

尚未取得可逐項對照的紀錄。

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
| JET-SPICE-C3H8-100-D0P4064-COFLOW-OPS / fuel_composition | '物理參數'!G425 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| JET-SPICE-C3H8-100-D0P4064-COFLOW-OPS / fuel_nozzle_inner_diameter | '物理參數'!G432；'物理參數'!G434 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| JET-SPICE-C3H8-100-D0P4064-COFLOW-OPS / oxidizer_coflow_velocity | '物理參數'!G437；'物理參數'!G438 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| JET-SPICE-ENDPOINT-PROTOCOL / adjusted_fuel_flow | '物理參數'!G446；'物理參數'!G447 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| JET-SPICE-REFERENCE-CONTEXT / ambient_oxygen_fraction | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| JET-SPICE-REFERENCE-CONTEXT / coflow_spatial_variation | '物理參數'!G437；'物理參數'!G438 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |

| 文獻因子／疑點 | 正確讀法或需補資料 |
| --- | --- |
| 速度與幾何 | 原總表將部分cm/s欄列作尺寸；按原單位判讀速度。光學座標／像素不是已校準火焰尺寸。 |

## 3. 共用資料的多項結論比較

| 結論／文獻 | 資料重疊身份 | 共同處 | 不同處／不能合併之處 |
| --- | --- | --- | --- |
| JET-SPICE-C3H8-100-D0P4064-COFLOW-OPS；JET-SPICE-ENDPOINT-PROTOCOL；JET-SPICE-REFERENCE-CONTEXT | 來源系列；精確論文／試次交集仍以每項data_used為準 | 不把多份出版物當獨立實驗。 | 尚未取得完全同試次的多篇結論比較時保留缺口。 |
| JET-1bb111e67a91；JET-0ba8a154fc17；JET-bd980e9e1195；JET-95e76859017d；JET-f579df9652dc | same_SPICE_2009_campaign_or_reports_not_independent_replication | Coflow/nozzle context affects the soot-onset endpoint.；Residence time is a qualitative explanation, not a quantitatively validated universal smoke-point criterion. | source_id: JET-0ba8a154fc17；physical_pages: 6；table: 1；reported_endpoint_count: 52；source_id: JET-95e76859017d；physical_pages: 2；reported_endpoint_count: 52；note: Draft report has editing placeholders; later text also uses55. Do not silently reconcile.；source_id: JET-f579df9652dc；physical_pages: 1；3；reported_endpoint_count: 55；table: 2；Published 55 versus qualified local48 is a source/calibration selection difference, not seven invented missing experiments; exact every-point publication join is not established.；尚未取得／不適用 |

## 4. 消防洞見

| 類別 | 對應證據 | 數據支持的判斷 | 策略／產品構想 | 待驗證 |
| --- | --- | --- | --- | --- |
| 預防 | JET-SPICE-C3H8-100-D0P4064-COFLOW-OPS；JET-SPICE-ENDPOINT-PROTOCOL；JET-SPICE-REFERENCE-CONTEXT | 來源煙點量是指定流況下開始排出soot的發光焰長；它不是任意燃料流率下的焰長、內禀材料常數或安全距離。 | 把燃料、噴口與共流條件一起附在煙點／熱暴露比較上，優先補同工況的熱流與鄰材反應。 | 需同步熱釋放／熱通量與鄰材點燃；不以較短煙點長度直接判定較安全。 |
| 偵測 | JET-SPICE-C3H8-100-D0P4064-COFLOW-OPS；JET-SPICE-ENDPOINT-PROTOCOL；JET-SPICE-REFERENCE-CONTEXT | 煙點端點和偵測器響應／警報門檻不是同一個量；本組沒有配對的警報效能。 | 用來源已核對的煙生成條件安排偵測器挑戰試驗，分開煙生成與輸運。 | 同來源煙粒、氣流、校準與啟用警報真值。 |
| 撲滅／抑制 | 尚未取得／不適用 | 尚未建立本組可直接支持此消防用途的完整量測鏈。 | 先補本組對應的物理端點與資料配對，再設計策略測試。 | 相關系列與方法限制只能提供研究脈絡，不能代替本組產品或操作效能驗證。 |

## 逐次索引

| 原始檔／資料位置 | Trial／Run／列 | 共享身份與保留事項 |
| --- | --- | --- |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-107_SPICE\Experimental table\PSI-107_Experimental table_Spice.csv | csv_logical_record_including_header: 70；source_cells: GMT date: CSV record 70, column GMT date；GMT ignition: CSV record 70, column GMT ignition；GMT  Flame Off : CSV record 70, column GMT  Flame Off ；Fuel: CSV record 70, column Fuel；Nozzle (mm): CSV record 70, column Nozzle (mm)；Fuel Rate (sccm): CSV record 70, column Fuel Rate (sccm)；Fuel Rate (mg/s): CSV record 70, column Fuel Rate (mg/s)；HC Fuel Rate (mg/s): CSV record 70, column HC Fuel Rate (mg/s)；Air Rate (cm/s): CSV record 70, column Air Rate (cm/s)；verified_endpoint_or_burn_join: False；row_role: within_burn_flow_observation_not_new_burn | raw_parameters_as_stored: GMT date: 52；GMT ignition: 12.01.47；GMT  Flame Off : 12.04.10；Fuel: Propane；Nozzle (mm): 0.4064；Fuel Rate (sccm): 53.28；Fuel Rate (mg/s): 1.59；HC Fuel Rate (mg/s): 1.59；Air Rate (cm/s): 33.57；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-107_SPICE\Experimental table\PSI-107_Experimental table_Spice.csv | csv_logical_record_including_header: 71；source_cells: GMT date: CSV record 71, column GMT date；GMT ignition: CSV record 71, column GMT ignition；GMT  Flame Off : CSV record 71, column GMT  Flame Off ；Fuel: CSV record 71, column Fuel；Nozzle (mm): CSV record 71, column Nozzle (mm)；Fuel Rate (sccm): CSV record 71, column Fuel Rate (sccm)；Fuel Rate (mg/s): CSV record 71, column Fuel Rate (mg/s)；HC Fuel Rate (mg/s): CSV record 71, column HC Fuel Rate (mg/s)；Air Rate (cm/s): CSV record 71, column Air Rate (cm/s)；verified_endpoint_or_burn_join: False；row_role: within_burn_flow_observation_not_new_burn | raw_parameters_as_stored: GMT date: 52；GMT ignition: 12.01.47；GMT  Flame Off : 12.04.10；Fuel: Propane；Nozzle (mm): 0.4064；Fuel Rate (sccm): 42.12；Fuel Rate (mg/s): 1.257；HC Fuel Rate (mg/s): 1.257；Air Rate (cm/s): 33.57；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-107_SPICE\Experimental table\PSI-107_Experimental table_Spice.csv | csv_logical_record_including_header: 72；source_cells: GMT date: CSV record 72, column GMT date；GMT ignition: CSV record 72, column GMT ignition；GMT  Flame Off : CSV record 72, column GMT  Flame Off ；Fuel: CSV record 72, column Fuel；Nozzle (mm): CSV record 72, column Nozzle (mm)；Fuel Rate (sccm): CSV record 72, column Fuel Rate (sccm)；Fuel Rate (mg/s): CSV record 72, column Fuel Rate (mg/s)；HC Fuel Rate (mg/s): CSV record 72, column HC Fuel Rate (mg/s)；Air Rate (cm/s): CSV record 72, column Air Rate (cm/s)；verified_endpoint_or_burn_join: False；row_role: within_burn_flow_observation_not_new_burn | raw_parameters_as_stored: GMT date: 52；GMT ignition: 12:21:19；GMT  Flame Off : 12:22:38；Fuel: Propane；Nozzle (mm): 0.4064；Fuel Rate (sccm): 35.64；Fuel Rate (mg/s): 1.063；HC Fuel Rate (mg/s): 1.063；Air Rate (cm/s): 32.63；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-107_SPICE\Experimental table\PSI-107_Experimental table_Spice.csv | csv_logical_record_including_header: 73；source_cells: GMT date: CSV record 73, column GMT date；GMT ignition: CSV record 73, column GMT ignition；GMT  Flame Off : CSV record 73, column GMT  Flame Off ；Fuel: CSV record 73, column Fuel；Nozzle (mm): CSV record 73, column Nozzle (mm)；Fuel Rate (sccm): CSV record 73, column Fuel Rate (sccm)；Fuel Rate (mg/s): CSV record 73, column Fuel Rate (mg/s)；HC Fuel Rate (mg/s): CSV record 73, column HC Fuel Rate (mg/s)；Air Rate (cm/s): CSV record 73, column Air Rate (cm/s)；verified_endpoint_or_burn_join: False；row_role: within_burn_flow_observation_not_new_burn | raw_parameters_as_stored: GMT date: 52；GMT ignition: 12:21:19；GMT  Flame Off : 12:22:38；Fuel: Propane；Nozzle (mm): 0.4064；Fuel Rate (sccm): 17.64；Fuel Rate (mg/s): 0.526；HC Fuel Rate (mg/s): 0.526；Air Rate (cm/s): 32.63；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-107_SPICE\Experimental table\PSI-107_Experimental table_Spice.csv | csv_logical_record_including_header: 74；source_cells: GMT date: CSV record 74, column GMT date；GMT ignition: CSV record 74, column GMT ignition；GMT  Flame Off : CSV record 74, column GMT  Flame Off ；Fuel: CSV record 74, column Fuel；Nozzle (mm): CSV record 74, column Nozzle (mm)；Fuel Rate (sccm): CSV record 74, column Fuel Rate (sccm)；Fuel Rate (mg/s): CSV record 74, column Fuel Rate (mg/s)；HC Fuel Rate (mg/s): CSV record 74, column HC Fuel Rate (mg/s)；Air Rate (cm/s): CSV record 74, column Air Rate (cm/s)；verified_endpoint_or_burn_join: False；row_role: within_burn_flow_observation_not_new_burn | raw_parameters_as_stored: GMT date: 52；GMT ignition: 12.21.19；GMT  Flame Off : 12.22.38；Fuel: Propane；Nozzle (mm): 0.4064；Fuel Rate (sccm): 35.64；Fuel Rate (mg/s): 1.063；HC Fuel Rate (mg/s): 1.063；Air Rate (cm/s): 33.57；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-107_SPICE\Experimental table\PSI-107_Experimental table_Spice.csv | csv_logical_record_including_header: 75；source_cells: GMT date: CSV record 75, column GMT date；GMT ignition: CSV record 75, column GMT ignition；GMT  Flame Off : CSV record 75, column GMT  Flame Off ；Fuel: CSV record 75, column Fuel；Nozzle (mm): CSV record 75, column Nozzle (mm)；Fuel Rate (sccm): CSV record 75, column Fuel Rate (sccm)；Fuel Rate (mg/s): CSV record 75, column Fuel Rate (mg/s)；HC Fuel Rate (mg/s): CSV record 75, column HC Fuel Rate (mg/s)；Air Rate (cm/s): CSV record 75, column Air Rate (cm/s)；verified_endpoint_or_burn_join: False；row_role: within_burn_flow_observation_not_new_burn | raw_parameters_as_stored: GMT date: 52；GMT ignition: 12.21.19；GMT  Flame Off : 12.22.38；Fuel: Propane；Nozzle (mm): 0.4064；Fuel Rate (sccm): 16.92；Fuel Rate (mg/s): 0.505；HC Fuel Rate (mg/s): 0.505；Air Rate (cm/s): 32.63；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-107_SPICE\Experimental table\PSI-107_Experimental table_Spice.csv | csv_logical_record_including_header: 76；source_cells: GMT date: CSV record 76, column GMT date；GMT ignition: CSV record 76, column GMT ignition；GMT  Flame Off : CSV record 76, column GMT  Flame Off ；Fuel: CSV record 76, column Fuel；Nozzle (mm): CSV record 76, column Nozzle (mm)；Fuel Rate (sccm): CSV record 76, column Fuel Rate (sccm)；Fuel Rate (mg/s): CSV record 76, column Fuel Rate (mg/s)；HC Fuel Rate (mg/s): CSV record 76, column HC Fuel Rate (mg/s)；Air Rate (cm/s): CSV record 76, column Air Rate (cm/s)；verified_endpoint_or_burn_join: False；row_role: within_burn_flow_observation_not_new_burn | raw_parameters_as_stored: GMT date: 52；GMT ignition: 12:26:14；GMT  Flame Off : 12:27:28；Fuel: Propane；Nozzle (mm): 0.4064；Fuel Rate (sccm): 53.64；Fuel Rate (mg/s): 1.601；HC Fuel Rate (mg/s): 1.601；Air Rate (cm/s): 26.99；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-107_SPICE\Experimental table\PSI-107_Experimental table_Spice.csv | csv_logical_record_including_header: 77；source_cells: GMT date: CSV record 77, column GMT date；GMT ignition: CSV record 77, column GMT ignition；GMT  Flame Off : CSV record 77, column GMT  Flame Off ；Fuel: CSV record 77, column Fuel；Nozzle (mm): CSV record 77, column Nozzle (mm)；Fuel Rate (sccm): CSV record 77, column Fuel Rate (sccm)；Fuel Rate (mg/s): CSV record 77, column Fuel Rate (mg/s)；HC Fuel Rate (mg/s): CSV record 77, column HC Fuel Rate (mg/s)；Air Rate (cm/s): CSV record 77, column Air Rate (cm/s)；verified_endpoint_or_burn_join: False；row_role: within_burn_flow_observation_not_new_burn | raw_parameters_as_stored: GMT date: 52；GMT ignition: 12:26:14；GMT  Flame Off : 12:27:28；Fuel: Propane；Nozzle (mm): 0.4064；Fuel Rate (sccm): 27.36；Fuel Rate (mg/s): 0.816；HC Fuel Rate (mg/s): 0.816；Air Rate (cm/s): 26.99；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-107_SPICE\Experimental table\PSI-107_Experimental table_Spice.csv | csv_logical_record_including_header: 78；source_cells: GMT date: CSV record 78, column GMT date；GMT ignition: CSV record 78, column GMT ignition；GMT  Flame Off : CSV record 78, column GMT  Flame Off ；Fuel: CSV record 78, column Fuel；Nozzle (mm): CSV record 78, column Nozzle (mm)；Fuel Rate (sccm): CSV record 78, column Fuel Rate (sccm)；Fuel Rate (mg/s): CSV record 78, column Fuel Rate (mg/s)；HC Fuel Rate (mg/s): CSV record 78, column HC Fuel Rate (mg/s)；Air Rate (cm/s): CSV record 78, column Air Rate (cm/s)；verified_endpoint_or_burn_join: False；row_role: within_burn_flow_observation_not_new_burn | raw_parameters_as_stored: GMT date: 52；GMT ignition: 12.26.44；GMT  Flame Off : 12.27.28；Fuel: Propane；Nozzle (mm): 0.4064；Fuel Rate (sccm): 53.64；Fuel Rate (mg/s): 1.601；HC Fuel Rate (mg/s): 1.601；Air Rate (cm/s): 26.99；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-107_SPICE\Experimental table\PSI-107_Experimental table_Spice.csv | csv_logical_record_including_header: 79；source_cells: GMT date: CSV record 79, column GMT date；GMT ignition: CSV record 79, column GMT ignition；GMT  Flame Off : CSV record 79, column GMT  Flame Off ；Fuel: CSV record 79, column Fuel；Nozzle (mm): CSV record 79, column Nozzle (mm)；Fuel Rate (sccm): CSV record 79, column Fuel Rate (sccm)；Fuel Rate (mg/s): CSV record 79, column Fuel Rate (mg/s)；HC Fuel Rate (mg/s): CSV record 79, column HC Fuel Rate (mg/s)；Air Rate (cm/s): CSV record 79, column Air Rate (cm/s)；verified_endpoint_or_burn_join: False；row_role: within_burn_flow_observation_not_new_burn | raw_parameters_as_stored: GMT date: 52；GMT ignition: 12.26.44；GMT  Flame Off : 12.27.28；Fuel: Propane；Nozzle (mm): 0.4064；Fuel Rate (sccm): 27；Fuel Rate (mg/s): 0.806；HC Fuel Rate (mg/s): 0.806；Air Rate (cm/s): 26.99；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-107_SPICE\Experimental table\PSI-107_Experimental table_Spice.csv | csv_logical_record_including_header: 80；source_cells: GMT date: CSV record 80, column GMT date；GMT ignition: CSV record 80, column GMT ignition；GMT  Flame Off : CSV record 80, column GMT  Flame Off ；Fuel: CSV record 80, column Fuel；Nozzle (mm): CSV record 80, column Nozzle (mm)；Fuel Rate (sccm): CSV record 80, column Fuel Rate (sccm)；Fuel Rate (mg/s): CSV record 80, column Fuel Rate (mg/s)；HC Fuel Rate (mg/s): CSV record 80, column HC Fuel Rate (mg/s)；Air Rate (cm/s): CSV record 80, column Air Rate (cm/s)；verified_endpoint_or_burn_join: False；row_role: within_burn_flow_observation_not_new_burn | raw_parameters_as_stored: GMT date: 52；GMT ignition: 12.28.52；GMT  Flame Off : 12.30.32；Fuel: Propane；Nozzle (mm): 0.4064；Fuel Rate (sccm): 65.52；Fuel Rate (mg/s): 1.955；HC Fuel Rate (mg/s): 1.955；Air Rate (cm/s): 14.77；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-107_SPICE\Experimental table\PSI-107_Experimental table_Spice.csv | csv_logical_record_including_header: 81；source_cells: GMT date: CSV record 81, column GMT date；GMT ignition: CSV record 81, column GMT ignition；GMT  Flame Off : CSV record 81, column GMT  Flame Off ；Fuel: CSV record 81, column Fuel；Nozzle (mm): CSV record 81, column Nozzle (mm)；Fuel Rate (sccm): CSV record 81, column Fuel Rate (sccm)；Fuel Rate (mg/s): CSV record 81, column Fuel Rate (mg/s)；HC Fuel Rate (mg/s): CSV record 81, column HC Fuel Rate (mg/s)；Air Rate (cm/s): CSV record 81, column Air Rate (cm/s)；verified_endpoint_or_burn_join: False；row_role: within_burn_flow_observation_not_new_burn | raw_parameters_as_stored: GMT date: 52；GMT ignition: 12.28.52；GMT  Flame Off : 12.30.32；Fuel: Propane；Nozzle (mm): 0.4064；Fuel Rate (sccm): 32.4；Fuel Rate (mg/s): 0.967；HC Fuel Rate (mg/s): 0.967；Air Rate (cm/s): 14.77；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-107_SPICE\Experimental table\PSI-107_Experimental table_Spice.csv | csv_logical_record_including_header: 82；source_cells: GMT date: CSV record 82, column GMT date；GMT ignition: CSV record 82, column GMT ignition；GMT  Flame Off : CSV record 82, column GMT  Flame Off ；Fuel: CSV record 82, column Fuel；Nozzle (mm): CSV record 82, column Nozzle (mm)；Fuel Rate (sccm): CSV record 82, column Fuel Rate (sccm)；Fuel Rate (mg/s): CSV record 82, column Fuel Rate (mg/s)；HC Fuel Rate (mg/s): CSV record 82, column HC Fuel Rate (mg/s)；Air Rate (cm/s): CSV record 82, column Air Rate (cm/s)；verified_endpoint_or_burn_join: False；row_role: within_burn_flow_observation_not_new_burn | raw_parameters_as_stored: GMT date: 52；GMT ignition: 12:42:47；GMT  Flame Off : 12:44:26；Fuel: Propane；Nozzle (mm): 0.4064；Fuel Rate (sccm): 93.24；Fuel Rate (mg/s): 2.782；HC Fuel Rate (mg/s): 2.782；Air Rate (cm/s): 16.65；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-107_SPICE\Experimental table\PSI-107_Experimental table_Spice.csv | csv_logical_record_including_header: 83；source_cells: GMT date: CSV record 83, column GMT date；GMT ignition: CSV record 83, column GMT ignition；GMT  Flame Off : CSV record 83, column GMT  Flame Off ；Fuel: CSV record 83, column Fuel；Nozzle (mm): CSV record 83, column Nozzle (mm)；Fuel Rate (sccm): CSV record 83, column Fuel Rate (sccm)；Fuel Rate (mg/s): CSV record 83, column Fuel Rate (mg/s)；HC Fuel Rate (mg/s): CSV record 83, column HC Fuel Rate (mg/s)；Air Rate (cm/s): CSV record 83, column Air Rate (cm/s)；verified_endpoint_or_burn_join: False；row_role: within_burn_flow_observation_not_new_burn | raw_parameters_as_stored: GMT date: 52；GMT ignition: 12:42:47；GMT  Flame Off : 12:44:26；Fuel: Propane；Nozzle (mm): 0.4064；Fuel Rate (sccm): 45；Fuel Rate (mg/s): 1.343；HC Fuel Rate (mg/s): 1.343；Air Rate (cm/s): 15.71；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-107_SPICE\Experimental table\PSI-107_Experimental table_Spice.csv | csv_logical_record_including_header: 84；source_cells: GMT date: CSV record 84, column GMT date；GMT ignition: CSV record 84, column GMT ignition；GMT  Flame Off : CSV record 84, column GMT  Flame Off ；Fuel: CSV record 84, column Fuel；Nozzle (mm): CSV record 84, column Nozzle (mm)；Fuel Rate (sccm): CSV record 84, column Fuel Rate (sccm)；Fuel Rate (mg/s): CSV record 84, column Fuel Rate (mg/s)；HC Fuel Rate (mg/s): CSV record 84, column HC Fuel Rate (mg/s)；Air Rate (cm/s): CSV record 84, column Air Rate (cm/s)；verified_endpoint_or_burn_join: False；row_role: within_burn_flow_observation_not_new_burn | raw_parameters_as_stored: GMT date: 52；GMT ignition: 12.42.47；GMT  Flame Off : 尚未取得／不適用；Fuel: Propane；Nozzle (mm): 0.4064；Fuel Rate (sccm): 93.24；Fuel Rate (mg/s): 2.782；HC Fuel Rate (mg/s): 2.782；Air Rate (cm/s): 16.65；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-107_SPICE\Experimental table\PSI-107_Experimental table_Spice.csv | csv_logical_record_including_header: 85；source_cells: GMT date: CSV record 85, column GMT date；GMT ignition: CSV record 85, column GMT ignition；GMT  Flame Off : CSV record 85, column GMT  Flame Off ；Fuel: CSV record 85, column Fuel；Nozzle (mm): CSV record 85, column Nozzle (mm)；Fuel Rate (sccm): CSV record 85, column Fuel Rate (sccm)；Fuel Rate (mg/s): CSV record 85, column Fuel Rate (mg/s)；HC Fuel Rate (mg/s): CSV record 85, column HC Fuel Rate (mg/s)；Air Rate (cm/s): CSV record 85, column Air Rate (cm/s)；verified_endpoint_or_burn_join: False；row_role: within_burn_flow_observation_not_new_burn | raw_parameters_as_stored: GMT date: 52；GMT ignition: 12.42.47；GMT  Flame Off : 尚未取得／不適用；Fuel: Propane；Nozzle (mm): 0.4064；Fuel Rate (sccm): 45；Fuel Rate (mg/s): 1.343；HC Fuel Rate (mg/s): 1.343；Air Rate (cm/s): 15.71；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |

## 缺件與適用範圍

- Per-case ambient O2, pressure and inlet-temperature measurements are unavailable; nominal/reference context is not a parameter sweep.
- No verified exact master-time join between every operating observation and each endpoint; do not substitute row order or TP/No values.
- Smoke-point length is not general arbitrary-flow flame geometry, an intrinsic fuel property or detector alarm threshold.
- No ignition/extinction/toxic-gas/engineering-safety prediction is established.
- No source-qualified smoke-point length for this fuel/nozzle, even though operation records exist; no R² is calculated.
