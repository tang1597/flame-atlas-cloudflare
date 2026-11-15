# Saffire-II PMMA引燃段與Nomex目標

小資料集 ID：`SAF99-NOMEX-TARGET-PMMA-PILOT`

## 資料身份與範圍

| 項目 | 內容 |
| --- | --- |
| NASA investigation | [PSI-99](https://psi.nasa.gov/physci/repo/data/investigations/PSI-99) |
| 材料／配方 | burning_pilot: PMMA；target: Nomex HT90-40；target_outcome: not ignited under the source protocol |
| 幾何 | shape: staged PMMA strip upstream of Nomex target；source_lengths_cm: 5；24；nominal_width_cm: 5；raw_thicknesses: 0.85 and0.37mm |
| 實驗模式 | direction: concurrent；gravity: Cygnus orbital microgravity；mode: flame transfer from pilot to target |
| 證據角色 | 實際固體火焰／材料試驗 |
| 環境 | direction: concurrent；gravity: Cygnus orbital microgravity；mode: flame transfer from pilot to target |
| 資料粒度／共享試片 | Requires exact trial and measurement/operation history; no values manufactured from summary lists. |
| 可用數值 | summary_and_source_analyzed_results_with_source_specific_raw_channels_not_complete_forward_closure |

## 1. 文獻結果與視覺化程式

### SA-F05　PMMA pilot burning is separate from Nomex ignition

**PSI-99_Experimental table_SAFFIRE-2.csv**

Saffire-II sample2-7 中 PMMA 引燃段被消耗，但下游 Nomex 目標在該操作程序下沒有點燃。這不是 Nomex 本體已燃燒後的自熄量測。

- 證據身份：source_summary_observation。
- 文獻定位：DATA-PSI-99: row8 and Note2; SB-0d816518ea68: physical5 sample-card description。
- 使用數據部分：row8 and Note2；physical5 sample-card description。
- 本組適用層級：direct；2-7 PMMA pilot consumed, Nomex target not ignited in this protocol; not an extinguished Nomex flame.。
- 使用／控制因子：PMMA先導火與Nomex目標、引燃暴露、目標未點燃端點。
- 來源限制：The reported burn duration belongs to the staged PMMA/Nomex setup and is not Nomex burning lifetime or an endurance rating.；Do not label PMMA and Nomex as a single burning chemical material.。
- 搜尋句（改寫）：In Saffire-II sample2-7 the PMMA portion was consumed, while the downstream Nomex target did not ignite under the source protocol.。
- 來源：https://psi.nasa.gov/physci/repo/data/investigations/PSI-99
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/01_實驗資料/第一批下載/PSI-99_SAFFIRE-II/Experimental table/PSI-99_Experimental table_SAFFIRE-2.csv>)

- 共同來源：**Concurrent Flame Spread Over Two-Sided Thick PMMA Slabs in Microgravity**；physical5 sample-card description；https://www.research.ed.ac.uk/en/publications/concurrent-flame-spread-over-two-sided-thick-pmma-slabs-in-microg/

| Model ID | 公式／預測量 | 展示程式 | 數值比較與限制 |
| --- | --- | --- | --- |
| SAFFIRE-II-SEALED-ENERGY-BLOCKED | Saffire-II material and enclosure data；Saffire-II material and enclosure data | reproduce_solid_models.py · [開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/solid_combustion_evidence_20261115/models/reproduce_solid_models.py>) | 目前未執行／尚未閉合；缺少完整輸入與對應目標；Compatible numeric front position/time and source-bound thick-slab closure；Actual flow/vent and heat-release/heat-transfer histories；Reported burn duration is not a front-traverse time; no generic spread or pressure prediction is fabricated from it. Thick slab/rod/thin-sheet regimes remain separate. |

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
| SA-F05 | 來源紀錄／出版物；逐次索引如上 | 多項觀察保留各自來源角色。 | 沒有建立完全同條件的獨立重複；不同試次、統計量或模型量不能互當。 |

## 4. 消防洞見

| 類別 | 對應證據 | 數據支持的判斷 | 策略／產品構想 | 待驗證 |
| --- | --- | --- | --- | --- |
| 預防 | SA-F05 | 未點燃、瞬間閃燃、不維持及不延燒是不同端點；配方與引燃暴露不同時不能合併成材料合格標籤。 | 材料選擇表保留完整配方與先導火／點火程序，分列各端點。 | 對應配方與程序的重複試驗；不得將PMMA先導火當Nomex本體燃燒。 |
| 偵測 | 尚未取得／不適用 | 尚未建立本組可直接支持此用途的數據結論。 | 先補對應資料與試次匹配，再決定可測試策略；此處是研究缺口。 | 需本組材料、幾何、操作歷史與對應端點的量測；相近系列不能代替。 |
| 撲滅／抑制 | 尚未取得／不適用 | 尚未建立本組可直接支持此用途的數據結論。 | 先補對應資料與試次匹配，再決定可測試策略；此處是研究缺口。 | 需本組材料、幾何、操作歷史與對應端點的量測；相近系列不能代替。 |

## 逐次索引

| 原始檔／資料位置 | Trial／Run／列 | 共享身份與保留事項 |
| --- | --- | --- |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-99_SAFFIRE-II\Experimental table\PSI-99_Experimental table_SAFFIRE-2.csv | trial: 2-7；row: 8；source_record: 尚未取得／不適用 | identity_notes: burn_trial；raw_parameters_as_stored: Sample Number: 2-7；Material: PMMA & Nomex；Samle Thickness : 0.85 and 0.37 mm；Sample Length : 5 and 24 cm；Sample Width (cm): 5 cm；Air Flow (cm/s): 20 cm/s；Percent O2 (Note 1): ~ 22.1；Ignition Power (W): 80 W；Ignition Time (s): 9.2 s；Burn Time (s): 140 s；Flow Direction: Concurrent；?-g Burn Length: 5 cm & 0 (note 2)；?-g Spread Length: n/a (Nomex)；1-g Burn Length: ~ 0 (Nomex)；1-g Spread Rate: n/a (Nomex)；Camera 1: S7C1；Camera 2: n/a |

## 缺件與適用範圍

- 不足兩項有來源結論；多結論比較尚未完成，不以目的或推測湊數。
- PMMA pilot combustion is not Nomex combustion.
- The setup burn duration is not a Nomex burn time.
- 尚未建立全火焰形狀／艙室安全的閉合預測。
