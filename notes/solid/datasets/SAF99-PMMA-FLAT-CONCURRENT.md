# Saffire-II 平整PMMA厚板順流

小資料集 ID：`SAF99-PMMA-FLAT-CONCURRENT`

## 資料身份與範圍

| 項目 | 內容 |
| --- | --- |
| NASA investigation | [PSI-99](https://psi.nasa.gov/physci/repo/data/investigations/PSI-99) |
| 材料／配方 | name: PMMA；source: Paper binds sample identity; sample2-9 CSV material cell is blank |
| 幾何 | shape: flat slab；length_mm: 290；width_mm: 50；nominal_full_thickness_mm: 10；central_thickness_mm: 未確認 |
| 實驗模式 | direction: concurrent；gravity: Cygnus orbital microgravity |
| 證據角色 | 實際固體火焰／材料試驗 |
| 環境 | direction: concurrent；gravity: Cygnus orbital microgravity |
| 資料粒度／共享試片 | Requires exact trial and measurement/operation history; no values manufactured from summary lists. |
| 可用數值 | summary_and_source_analyzed_results_with_source_specific_raw_channels_not_complete_forward_closure |

## 1. 文獻結果與視覺化程式

### SA-F06　Thick PMMA flames approached a limiting size

**Concurrent Flame Spread Over Two-Sided Thick PMMA Slabs in Microgravity**

有溝槽與平整 PMMA 厚板在微重力強制流中維持上游錨定、接近受限尺寸的火焰；來源的地面向上延燒則持續成長。

- 證據身份：來源分析觀察。
- 文獻定位：SB-0d816518ea68: physical4–5,18; Figs6–8; SB-ffe6664bb8a8: thick-sample results。
- 使用數據部分：physical4–5,18; Figs6–8；thick-sample results。
- 本組適用層級：direct_comparison；Matched source family of2-8/2-9; upward1g appearance is a related comparison, not an otherwise exactly controlled gravity-only pair.。
- 使用／控制因子：PMMA板幾何、火焰前緣與長度；1g向上與微重力強制流。
- 來源限制：Ground and flight comparisons retain geometry, buoyancy, measurement and history differences.；A limiting visible flame does not establish low vapor hazard, no smoldering, no reignition or full safety.。
- 搜尋句（改寫）：The grooved and flat PMMA slab flames remained anchored near the upstream end and approached a limiting size in forced-flow microgravity; the reported ground upward-spread tests continued growing.。
- 來源：https://www.research.ed.ac.uk/en/publications/concurrent-flame-spread-over-two-sided-thick-pmma-slabs-in-microg/
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/02_論文全文/01_期刊論文與作者稿/Concurrent Flame Spread Over Two-Sided Thick PMMA Slabs in Microgravity__0d816518ea.pdf>)

- 共同來源：**Flame spread: Effects of microgravity and scale**；thick-sample results；https://doi.org/10.1016/j.combustflame.2018.10.012

### SA-F07　Groove geometry changed the flame and downstream signals

**Concurrent Flame Spread Over Two-Sided Thick PMMA Slabs in Microgravity**

有溝槽 PMMA 形成缺口，輻射、羽流、煙與壓力／CO2 訊號較平板強；作者將差異連結到燃燒基部的熱回授，不能視為隔離了所有其他因子的因果測試。

- 證據身份：來源觀察及作者推論。
- 文獻定位：SB-0d816518ea68: physical14–18; Figs9–13。
- 使用數據部分：physical14–18; Figs9–13。
- 本組適用層級：direct_comparison；Grooved-minus-flat source outputs; distinguish measured radiometer/CO2 signals, author-inferred flux/burning-rate comparisons and causality.。
- 使用／控制因子：溝槽／平板、radiometer、plume／CO2／壓力／煙；熱回授部分為作者推論。
- 來源限制：One grooved and one flat test are not replicated treatment groups.；Downstream heat flux inferred from a fabric radiation balance is not a direct heat-flux gauge measurement.；Comparative CO2-based burning-rate statements are source estimates, not a measured absolute mass-loss history.。
- 搜尋句（改寫）：The grooved PMMA developed a notch and showed stronger radiation, plume, smoke and pressure/CO2 responses than the flat sample. The authors infer enhanced heat feedback from its altered burning base.。
- 來源：https://www.research.ed.ac.uk/en/publications/concurrent-flame-spread-over-two-sided-thick-pmma-slabs-in-microg/
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/02_論文全文/01_期刊論文與作者稿/Concurrent Flame Spread Over Two-Sided Thick PMMA Slabs in Microgravity__0d816518ea.pdf>)

### SA-F08　Flow restart released a strong residual-smoke signal

**Concurrent Flame Spread Over Two-Sided Thick PMMA Slabs in Microgravity**

溝槽 PMMA 燃燒結束後，為準備平板試驗而重新啟動流道，來源記錄殘留煙被帶出並產生該序列最大的前向散射訊號。這是作者對該操作序列的觀察；目前原檔的時鐘配對尚未完成，未宣稱重新重現該峰值。

- 證據身份：同操作序列的作者觀察。
- 文獻定位：SB-0d816518ea68: physical17–18, Fig13。
- 使用數據部分：physical17–18, Fig13。
- 本組適用層級：direct_same_sequence；One2-8-to-2-9 recovery/preparation sequence, not two independent smoke-spike replications. Paper observation; source clock/raw spike not reproduced.。
- 使用／控制因子：流道重啟、殘留煙、前向散射與2-8→2-9時序；電壓非警報真值。
- 來源限制：The exact absolute event-time join and raw-signal spike have not been reconstructed by this inventory.；This is not a new measured alarm delay, reignition or a quantified safe-restart interval.；Agglomeration and PMMA-vapor condensation are alternative author hypotheses, not uniquely identified mechanisms.；Local duct flow and continuing Cygnus vehicle ventilation must not be conflated.。
- 搜尋句（改寫）：After the grooved-sample burn ended, restarting Saffire duct flow to prepare the flat-sample test flushed residual smoke; the source reports the largest forward-scatter signal of that sequence during this restart.。
- 來源：https://www.research.ed.ac.uk/en/publications/concurrent-flame-spread-over-two-sided-thick-pmma-slabs-in-microg/
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/02_論文全文/01_期刊論文與作者稿/Concurrent Flame Spread Over Two-Sided Thick PMMA Slabs in Microgravity__0d816518ea.pdf>)

### SA-F09　A concentration may rise after flameout because of mixing

**Concurrent Flame Spread Over Two-Sided Thick PMMA Slabs in Microgravity**

PMMA 可見火焰熄滅後，壓力下降時 CO2 仍稍升；作者指出感測器處的延遲混合可以造成此反應。單一 CO2 訊號不能據此證明仍有持續燃燒。

- 證據身份：來源觀察及作者假說。
- 文獻定位：SB-0d816518ea68: physical16, Fig12 discussion。
- 使用數據部分：physical16, Fig12 discussion。
- 本組適用層級：direct_same_source_signal_with_author_interpretation；Post-visible-flameout CO2 behavior and author mixing explanation; not independent chemistry proof.。
- 使用／控制因子：可見熄焰、CO2、壓力及取樣位置；非反應速率直接量測。
- 來源限制：The rise is not proof of continued chemical burning, and mixing is an explanation rather than a uniquely inverted transport kernel.；The paper states unknown occupied free volume prevents quantitative absolute heat-release or burning-rate calculation from those signals alone.。
- 搜尋句（改寫）：The PMMA source reports a small further CO2 increase while pressure falls after visible extinction; the authors explain that delayed mixing at the sensor can produce that response.。
- 來源：https://www.research.ed.ac.uk/en/publications/concurrent-flame-spread-over-two-sided-thick-pmma-slabs-in-microg/
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/02_論文全文/01_期刊論文與作者稿/Concurrent Flame Spread Over Two-Sided Thick PMMA Slabs in Microgravity__0d816518ea.pdf>)

### SA-F10　Reduced-pressure ground comparisons are conditional

**Buoyancy effects on concurrent flame spread over thick PMMA**

地面厚 PMMA 壓力系列中，降低壓力時表面火焰前緣進展變慢，接近引用的 Saffire-II 平板飛行比較；材料、幾何、流場及量的定義仍須分別匹配。

- 證據身份：published_ground_and_flight_comparison。
- 文獻定位：SB-ea30d9a92d21: physical1,5–6,8–11。
- 使用數據部分：physical1,5–6,8–11。
- 本組適用層級：direct_ground_comparison；Reuses flight2-9 and adds ground40/60/80/100kPa slabs. Ground150mm vs flight290mm and front definitions differ.。
- 使用／控制因子：地面40/60/80/100kPa、厚PMMA前緣與飛行2-9；尺寸／端點不同。
- 來源限制：Ground length/holder, ignition, mixed convection and front definition differ from flight; pressure is not a pure gravity knob.；No joint enriched-oxygen/low-pressure/partial-gravity qualification is created.。
- 搜尋句（改寫）：The ground thick-PMMA pressure series reported slower surface-front progress as pressure was reduced, approaching a reused Saffire-II flat-slab flight comparison.。
- 來源：https://ntrs.nasa.gov/citations/20200000557
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/02_論文全文/01_期刊論文與作者稿/Buoyancy effects on concurrent flame spread over thick PMMA__ea30d9a92d.pdf>)

| Model ID | 公式／預測量 | 展示程式 | 數值比較與限制 |
| --- | --- | --- | --- |
| SAFFIRE-II-SEALED-ENERGY-BLOCKED | Saffire-II material and enclosure data；Saffire-II material and enclosure data | reproduce_solid_models.py · [開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/solid_combustion_evidence_20261115/models/reproduce_solid_models.py>) | 目前未執行／尚未閉合；缺少完整輸入與對應目標；Compatible numeric front position/time and source-bound thick-slab closure；Actual flow/vent and heat-release/heat-transfer histories；Reported burn duration is not a front-traverse time; no generic spread or pressure prediction is fabricated from it. Thick slab/rod/thin-sheet regimes remain separate. |

| 可開啟的圖／工具 | 身份與用途 |
| --- | --- |
| [開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/solid_combustion_evidence_20261115/signal_audit/sample9_native_signals.png>) | 來源校準值：風扇控制、RPM、風速與CO2，非新校準或熄焰判定 |
| [開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/solid_combustion_evidence_20261115/signal_audit/detection_pairability_coverage.png>) | 煙訊號時基／資料結構稽核，尚無verified跨時鐘join |

## 2. 使用資料與參數總表的因子對照

| 總表原分類 | 來源身份 | 原欄名單位 | 原欄名例 | 總表定位 |
| --- | --- | --- | --- | --- |
| 二氧化碳濃度 | 量測或條件值 | 未由欄名確認 | CO2 | '物理參數'!A282:K282 |
| 光電／離子偵測訊號 | 儀器原始訊號 | V | FIZ1 Smoke Detector Obscuration (V)；FIZ 2 Smoke Detector Obscuration (V)；FIZ 1 Smoke Detector Scatterometer (V)；FIZ 2 Smoke Detector Scatterometer (V) | '物理參數'!A283:K283 |
| 光電／離子偵測訊號 | 儀器原始訊號 | 未由欄名確認 | FIZ 2 Obscuration | '物理參數'!A284:K284 |
| 壓力 | 量測或設定 | 未由欄名確認 | Ambient Pressure；PSIA | '物理參數'!A285:K285 |
| 尺寸／幾何 | 裝置或樣本條件 | cm | Sample Width (cm) | '物理參數'!A286:K286 |
| 尺寸／幾何 | 裝置或樣本條件 | 未由欄名確認 | Samle Thickness；Sample Length；cm/sec；mw/cm^2 | '物理參數'!A287:K287 |
| 影像／光譜設定 | 儀器設定或影像座標 | 未由欄名確認 | Camera 1；Camera 2；Camera 1 Trigger；Camera 2 Trigger；Camera 1 Power Control；Camera 2 Power Control | '物理參數'!A288:K288 |
| 氧濃度 | 量測或條件值 | 未由欄名確認 | Percent O2 (Note 1)；O2；O2 & CO2 Power Control | '物理參數'!A289:K289 |
| 流速／通風 | 量測或設定 | cm/s | Air Flow (cm/s) | '物理參數'!A290:K290 |
| 流速／通風 | 量測或設定 | 未由欄名確認 | Anemometer 1；Anemometer 2；Anemometer Power Control 1&2；Anemometer1；Anemometer2 | '物理參數'!A291:K291 |
| 溫度 | 量測或設定 | degC | PCM Air Temp (degC) | '物理參數'!A292:K292 |
| 溫度 | 量測或設定 | 未由欄名確認 | Plume Temp 1 (TC1)；Plume Temp 2 (TC2)；Plume Temp 3 (TC3)；Plume Temp 4 (TC4)；Plume Temp 5 (TC5)；Plume Temp 6 (TC6)；Sample Temp 1 (TC7)；Sample Temp 2 (TC8)；Sample Temp 3 (TC9)；Sample Temp 4 (TC10)；其餘見原始欄位 | '物理參數'!A293:K293 |
| 火焰幾何／延燒 | 影像／來源分析量 | 未由欄名確認 | ?-g Burn Length；?-g Spread Length；1-g Burn Length；1-g Spread Rate | '物理參數'!A294:K294 |
| 熱通量／輻射 | 量測通道或來源分析量 | 未由欄名確認 | Radiometer 1；Radiometer 2；Radiometer 3；Radiometer 4；Radiometer Temp 1；Radiometer Temp 2；Radiometer Temp 3；Radiometer Temp 4；Radiometer1Value；Radiometer2Value；其餘見原始欄位 | '物理參數'!A295:K295 |
| 燃燒／點火／老化時間 | 時序或處理條件 | s | Burn Time (s) | '物理參數'!A296:K296 |
| 硬體電壓／電流／功率 | 原始訊號或狀態 | 未由欄名確認 | LED Power 1；Volts | '物理參數'!A297:K297 |
| 風扇／流量顯示設定 | 儀器設定 | Pa | FIZ 1 Cabin Fan delta P (Pa)；FIZ 2 Cabin Fan Delta P (Pa) | '物理參數'!A298:K298 |
| 風扇／流量顯示設定 | 儀器設定 | 未由欄名確認 | Average Fan Speed；Fan Speed Control；Test Section Fan Power Control；Fan Tach /100；FanTachometer | '物理參數'!A299:K299 |
| 點火功率／電壓／電流 | 量測或設定 | W | Ignition Power (W) | '物理參數'!A300:K300 |
| 點火功率／電壓／電流 | 量測或設定 | s | Ignition Time (s) | '物理參數'!A301:K301 |
| 點火功率／電壓／電流 | 量測或設定 | 未由欄名確認 | Igniter Current；Igniter Voltage；Igniter Voltage Set Point；Igniter Power Enable | '物理參數'!A302:K302 |

以上是該 investigation 的欄位盤點；個別結論實際使用的因子以第1節與下列補充為準。

| 本組實際因子 | 總表定位／未列欄位 | 文獻中的用途 |
| --- | --- | --- |
| 材料／配方／幾何 | '實驗總覽'!E16 | 文獻選樣身份；逐次厚度、支撐與歷史另由原文補齊 |
| 環境／流向／重力 | '實驗總覽'!F16 | 環境摘要，非本組全部逐次聯合條件 |
| 尺寸／幾何 / Sample Width (cm) | '物理參數'!G286 | 是否為模型輸入、控制條件或量測輸出，依第1節文獻定位逐項核對 |
| 尺寸／幾何 / Samle Thickness；Sample Length；cm/sec；mw/cm^2 | '物理參數'!G287 | 是否為模型輸入、控制條件或量測輸出，依第1節文獻定位逐項核對 |
| 氧濃度 / Percent O2 (Note 1)；O2；O2 & CO2 Power Control | '物理參數'!G289 | 是否為模型輸入、控制條件或量測輸出，依第1節文獻定位逐項核對 |
| 流速／通風 / Air Flow (cm/s) | '物理參數'!G290 | 是否為模型輸入、控制條件或量測輸出，依第1節文獻定位逐項核對 |
| 流速／通風 / Anemometer 1；Anemometer 2；Anemometer Power Control 1&2；Anemometer1；Anemometer2 | '物理參數'!G291 | 是否為模型輸入、控制條件或量測輸出，依第1節文獻定位逐項核對 |
| 溫度 / PCM Air Temp (degC) | '物理參數'!G292 | 是否為模型輸入、控制條件或量測輸出，依第1節文獻定位逐項核對 |
| 溫度 / Plume Temp 1 (TC1)；Plume Temp 2 (TC2)；Plume Temp 3 (TC3)；Plume Temp 4 (TC4)；Plume Temp 5 (TC5)；Plume Temp 6 (TC6)；Sample Temp 1 (TC7)；Sample Temp 2 (TC8)；Sample Temp 3 (TC9)；Sample Temp 4 (TC10)；其餘見原始欄位 | '物理參數'!G293 | 是否為模型輸入、控制條件或量測輸出，依第1節文獻定位逐項核對 |
| 火焰幾何／延燒 / ?-g Burn Length；?-g Spread Length；1-g Burn Length；1-g Spread Rate | '物理參數'!G294 | 是否為模型輸入、控制條件或量測輸出，依第1節文獻定位逐項核對 |
| 熱通量／輻射 / Radiometer 1；Radiometer 2；Radiometer 3；Radiometer 4；Radiometer Temp 1；Radiometer Temp 2；Radiometer Temp 3；Radiometer Temp 4；Radiometer1Value；Radiometer2Value；其餘見原始欄位 | '物理參數'!G295 | 是否為模型輸入、控制條件或量測輸出，依第1節文獻定位逐項核對 |
| 燃燒／點火／老化時間 / Burn Time (s) | '物理參數'!G296 | 是否為模型輸入、控制條件或量測輸出，依第1節文獻定位逐項核對 |

| 文獻因子／疑點 | 正確讀法或需補資料 |
| --- | --- |
| FIZ偵測訊號 | 原始電壓不是已啟用警報結果；Sample8/9與Cygnus時鐘配對未確認。 |

## 3. 共用資料的多項結論比較

| 結論／文獻 | 資料重疊身份 | 共同處 | 不同處／不能合併之處 |
| --- | --- | --- | --- |
| SB-ffe6664bb8a8；SB-0d816518ea68；SB-ea30d9a92d21 | same_flight_datum_shared_across_publications_with_new_ground_comparator | Limiting/anchored microgravity PMMA flame descriptions are compatible; the ground pressure paper reuses sample9. | Geometry-specific details, ground pressure conditions and endpoint methods differ; do not turn these into paper disagreement. |

## 4. 消防洞見

| 類別 | 對應證據 | 數據支持的判斷 | 策略／產品構想 | 待驗證 |
| --- | --- | --- | --- | --- |
| 預防 | SA-F06 | 限制火焰或熱解區的長度，仍不表示燃料路徑停止消耗與傳播。 | 測試材料路徑隔斷與鄰材熱暴露，作為獨立於火焰長度的防火設計項。 | 同材料／支撐下的隔斷距離、熱劑量及鄰材點燃試驗；尚無通用距離。 |
| 偵測 | SA-F08；SA-F09 | 該PMMA操作序列在流道重啟後出現較強前向散射煙訊號；CO2在熄焰後稍升，作者另以延遲混合解釋。 | 將通風重啟列為熄火後的監測階段，保留煙與熱／氣體的獨立狀態。 | 需可核對時鐘、取樣路徑、啟用狀態與真實警報結果；目前未重現原始散射峰。 |
| 撲滅／抑制 | 尚未取得／不適用 | 尚未建立本組可直接支持此用途的數據結論。 | 先補對應資料與試次匹配，再決定可測試策略；此處是研究缺口。 | 需本組材料、幾何、操作歷史與對應端點的量測；相近系列不能代替。 |

## 逐次索引

| 原始檔／資料位置 | Trial／Run／列 | 共享身份與保留事項 |
| --- | --- | --- |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-99_SAFFIRE-II\Experimental table\PSI-99_Experimental table_SAFFIRE-2.csv | trial: 2-9；row: 10；source_record: 尚未取得／不適用 | identity_notes: burn_trial；raw_parameters_as_stored: Sample Number: 2-9；Material: 尚未取得／不適用；Samle Thickness : 1 cm；Sample Length : 29 cm；Sample Width (cm): 5 cm；Air Flow (cm/s): 20 cm/s；Percent O2 (Note 1): 22.0 to 21.9；Ignition Power (W): 97 W；Ignition Time (s): 30 s；Burn Time (s): 900 s；Flow Direction: Concurrent；?-g Burn Length: ~ 10 cm (note 4)；?-g Spread Length: Note 4；1-g Burn Length: Complete；1-g Spread Rate: Acceleratory；Camera 1: S9C1；Camera 2: n/a |

## 缺件與適用範圍

- Same campaign sequential tests, not independent replications.
- Local duct flow-off differs from vehicle ventilation.
- Absolute heat release fromCO2 lacks known vehicle free volume.
- 尚未建立全火焰形狀／艙室安全的閉合預測。
