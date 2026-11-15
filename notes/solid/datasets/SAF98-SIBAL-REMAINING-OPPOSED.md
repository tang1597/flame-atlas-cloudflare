# Saffire-I 剩餘SIBAL逆流

小資料集 ID：`SAF98-SIBAL-REMAINING-OPPOSED`

## 資料身份與範圍

| 項目 | 內容 |
| --- | --- |
| NASA investigation | [PSI-98](https://psi.nasa.gov/physci/repo/data/investigations/PSI-98) |
| 材料／配方 | name: SIBAL cotton/fiberglass composite；cotton_mass_fraction: 0.75；fiberglass_mass_fraction: 0.25；property_role: source nominal material, not per-coupon assay |
| 幾何 | shape: remaining part of the same original large coupon；remaining_length_role: Source approximate residual, not raw table full dimensions |
| 實驗模式 | direction: opposed；history: after S1 on same physical coupon；gravity: Cygnus orbital microgravity |
| 證據角色 | 實際固體火焰／材料試驗 |
| 環境 | direction: opposed；history: after S1 on same physical coupon；gravity: Cygnus orbital microgravity |
| 資料粒度／共享試片 | Requires exact trial and measurement/operation history; no values manufactured from summary lists. |
| 可用數值 | summary_and_source_analyzed_results_with_source_specific_raw_channels_not_complete_forward_closure |

## 1. 文獻結果與視覺化程式

### SA-F03　Opposed cloth burns retain prior-burn history

**PSI-98_Experimental table_SAFFIRE-1.csv**

Saffire-I 的逆流階段使用首次順流燃燒後的剩餘試片，不能當全新試片的流向控制組。

- 證據身份：source_record_and_publication_context。
- 文獻定位：DATA-PSI-98: S1/S2 rows2–3; SB-ffe6664bb8a8: opposed flame-spread discussion, physical13/Fig13; SB-e38ec36f5481: physical29 TableI。
- 使用數據部分：S1/S2 rows2–3；opposed flame-spread discussion, physical13/Fig13；physical29 TableI。
- 本組適用層級：direct；Only SaffireI residual coupon is established by this finding. Do not import its10cm residual or70s duration to III.。
- 使用／控制因子：S1→S2順序、殘餘試片、流向與熱歷史。
- 來源限制：The summary repeats full nominal sample dimensions; do not interpret them as remaining unburned length.；Do not equate recorded command interval, total trace span and flame lifetime.。
- 搜尋句（改寫）：Saffire-I's opposed burn used the remaining portion after the first concurrent burn. It is not a fresh-coupon orientation control.。
- 來源：https://psi.nasa.gov/physci/repo/data/investigations/PSI-98
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/01_實驗資料/第一批下載/PSI-98_SAFFIRE-I/Experimental table/PSI-98_Experimental table_SAFFIRE-1.csv>)

- 共同來源：**Flame spread: Effects of microgravity and scale**；opposed flame-spread discussion, physical13/Fig13；https://doi.org/10.1016/j.combustflame.2018.10.012

- 共同來源：**Results of Large-Scale Spacecraft Flammability Tests**；physical29 TableI；https://ntrs.nasa.gov/citations/20170008805

### SA-F11　Source condition disagreements must be retained

**PSI-98_Experimental table_SAFFIRE-1.csv**

Saffire 原表與出版物有厚度單位、長寬、流速或計畫／實際條件的差異，均保留來源版本，不挑一個方便的值覆寫。

- 證據身份：source_quality_constraint。
- 文獻定位：DATA-PSI-98: header and rows2–3; DATA-PSI-99: row7; DATA-PSI-100: rows2–3; SB-ffe6664bb8a8: physical6。
- 使用數據部分：header and rows2–3；row7；rows2–3；physical6。
- 本組適用層級：source_quality_not_combustion_result；Apply the named row-specific discrepancy only:98 thickness/length-width;99 sample2-6 material/flow and raw037mm strings;100 planning/summary30 vs source-published25. General quality context does not supply another fire-behavior finding.。
- 使用／控制因子：原單位、材料空格、長寬及計畫／飛行流速版本；屬來源品質。
- 來源限制：Do not overwrite source strings or average versions.；A version/metadata discrepancy is not contradictory combustion physics.；Saffire-III measured anemometry is needed before treating planned/summary flow as the actual local flow.。
- 搜尋句（改寫）：The raw Saffire-I table has thickness-unit and length/width issues; sample2-6 flow differs between CSV and publications; Saffire-III planned/summary flow differs from the published flown condition.。
- 來源：https://psi.nasa.gov/physci/repo/data/investigations/PSI-98
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/01_實驗資料/第一批下載/PSI-98_SAFFIRE-I/Experimental table/PSI-98_Experimental table_SAFFIRE-1.csv>)

- 共同來源：**PSI-99_Experimental table_SAFFIRE-2.csv**；row7；https://psi.nasa.gov/physci/repo/data/investigations/PSI-99

- 共同來源：**PSI-100_Experimental table_SAFFIRE-3.csv**；rows2–3；https://psi.nasa.gov/physci/repo/data/investigations/PSI-100

- 共同來源：**Flame spread: Effects of microgravity and scale**；physical6；https://doi.org/10.1016/j.combustflame.2018.10.012

| Model ID | 公式／預測量 | 展示程式 | 數值比較與限制 |
| --- | --- | --- | --- |
| SAFFIRE-I-SEALED-ENERGY-BLOCKED | Saffire-I enclosure energy balance；Saffire-I enclosure energy balance | reproduce_solid_models.py · [開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/solid_combustion_evidence_20261115/models/reproduce_solid_models.py>) | 目前未執行／尚未閉合；缺少完整輸入與對應目標；Time-resolved inflow/outflow and leakage；Independent heat-release/burn history, wall heat transfer and radiation state；Related2012model is a sealed ground chamber; actual flight requires vent/leak, heat-release and heat-transfer closure. Conditional O2 diagnostic is a separate reconstruction, not a pressure/flame prediction. |

## 2. 使用資料與參數總表的因子對照

| 總表原分類 | 來源身份 | 原欄名單位 | 原欄名例 | 總表定位 |
| --- | --- | --- | --- | --- |
| 二氧化碳濃度 | 量測或條件值 | 未由欄名確認 | CO2 | '物理參數'!A266:K266 |
| 壓力 | 量測或設定 | 未由欄名確認 | Ambient Pressure；PSIA | '物理參數'!A267:K267 |
| 尺寸／幾何 | 裝置或樣本條件 | cm | Sample Thickness (cm)；Sample Length (cm)；Sample Width (cm) | '物理參數'!A268:K268 |
| 尺寸／幾何 | 裝置或樣本條件 | 未由欄名確認 | cm/sec；mw/cm^2 | '物理參數'!A269:K269 |
| 影像／光譜設定 | 儀器設定或影像座標 | 未由欄名確認 | Camera 1；Camera 2；Camera 1 Trigger；Camera 2 Trigger；Camera 1 Power Control；Camera 2 Power Control；Exposure | '物理參數'!A270:K270 |
| 氧濃度 | 量測或條件值 | 未由欄名確認 | Percent O2；O2；O2 & CO2 Power Control | '物理參數'!A271:K271 |
| 流速／通風 | 量測或設定 | cm/s | Air Flow (cm/s) | '物理參數'!A272:K272 |
| 流速／通風 | 量測或設定 | 未由欄名確認 | Anemometer 1；Anemometer 2；Anemometer Power Control 1&2 | '物理參數'!A273:K273 |
| 溫度 | 量測或設定 | 未由欄名確認 | Plume Temp 1 (TC1)；Plume Temp 2 (TC2)；Plume Temp 3 (TC3)；Plume Temp 4 (TC4)；Plume Temp 5 (TC5)；Plume Temp 6 (TC6)；Sample Temp 1 (TC7)；Sample Temp 2 (TC8)；Sample Temp 3 (TC9)；Sample Temp 4 (TC10)；其餘見原始欄位 | '物理參數'!A274:K274 |
| 熱通量／輻射 | 量測通道或來源分析量 | 未由欄名確認 | Radiometer 1；Radiometer 2；Radiometer 3；Radiometer 4；Radiometer Temp 1；Radiometer Temp 2；Radiometer Temp 3；Radiometer Temp 4 | '物理參數'!A275:K275 |
| 燃燒／點火／老化時間 | 時序或處理條件 | s | Burn Time (s) | '物理參數'!A276:K276 |
| 硬體電壓／電流／功率 | 原始訊號或狀態 | 未由欄名確認 | LED Power 1；Volts | '物理參數'!A277:K277 |
| 風扇／流量顯示設定 | 儀器設定 | 未由欄名確認 | Average Fan Speed；Fan Speed Control；Test Section Fan Power Control；Fan Tach /100 | '物理參數'!A278:K278 |
| 點火功率／電壓／電流 | 量測或設定 | W | Ignition Power (W) | '物理參數'!A279:K279 |
| 點火功率／電壓／電流 | 量測或設定 | s | Ignition Time (s) | '物理參數'!A280:K280 |
| 點火功率／電壓／電流 | 量測或設定 | 未由欄名確認 | Igniter Current；Igniter Voltage；Igniter Voltage Set Point；Igniter Power Enable | '物理參數'!A281:K281 |

以上是該 investigation 的欄位盤點；個別結論實際使用的因子以第1節與下列補充為準。

| 本組實際因子 | 總表定位／未列欄位 | 文獻中的用途 |
| --- | --- | --- |
| 材料／配方／幾何 | '實驗總覽'!E15 | 文獻選樣身份；逐次厚度、支撐與歷史另由原文補齊 |
| 環境／流向／重力 | '實驗總覽'!F15 | 環境摘要，非本組全部逐次聯合條件 |
| 尺寸／幾何 / Sample Thickness (cm)；Sample Length (cm)；Sample Width (cm) | '物理參數'!G268 | 是否為模型輸入、控制條件或量測輸出，依第1節文獻定位逐項核對 |
| 尺寸／幾何 / cm/sec；mw/cm^2 | '物理參數'!G269 | 是否為模型輸入、控制條件或量測輸出，依第1節文獻定位逐項核對 |
| 氧濃度 / Percent O2；O2；O2 & CO2 Power Control | '物理參數'!G271 | 是否為模型輸入、控制條件或量測輸出，依第1節文獻定位逐項核對 |
| 流速／通風 / Air Flow (cm/s) | '物理參數'!G272 | 是否為模型輸入、控制條件或量測輸出，依第1節文獻定位逐項核對 |
| 流速／通風 / Anemometer 1；Anemometer 2；Anemometer Power Control 1&2 | '物理參數'!G273 | 是否為模型輸入、控制條件或量測輸出，依第1節文獻定位逐項核對 |
| 溫度 / Plume Temp 1 (TC1)；Plume Temp 2 (TC2)；Plume Temp 3 (TC3)；Plume Temp 4 (TC4)；Plume Temp 5 (TC5)；Plume Temp 6 (TC6)；Sample Temp 1 (TC7)；Sample Temp 2 (TC8)；Sample Temp 3 (TC9)；Sample Temp 4 (TC10)；其餘見原始欄位 | '物理參數'!G274 | 是否為模型輸入、控制條件或量測輸出，依第1節文獻定位逐項核對 |
| 熱通量／輻射 / Radiometer 1；Radiometer 2；Radiometer 3；Radiometer 4；Radiometer Temp 1；Radiometer Temp 2；Radiometer Temp 3；Radiometer Temp 4 | '物理參數'!G275 | 是否為模型輸入、控制條件或量測輸出，依第1節文獻定位逐項核對 |
| 燃燒／點火／老化時間 / Burn Time (s) | '物理參數'!G276 | 是否為模型輸入、控制條件或量測輸出，依第1節文獻定位逐項核對 |

尚未取得可逐項對照的紀錄。

## 3. 共用資料的多項結論比較

| 結論／文獻 | 資料重疊身份 | 共同處 | 不同處／不能合併之處 |
| --- | --- | --- | --- |
| SA-F03；SA-F11 | 來源紀錄／出版物；逐次索引如上 | 多項觀察保留各自來源角色。 | 沒有建立完全同條件的獨立重複；不同試次、統計量或模型量不能互當。 |

## 4. 消防洞見

| 類別 | 對應證據 | 數據支持的判斷 | 策略／產品構想 | 待驗證 |
| --- | --- | --- | --- | --- |
| 預防 | 尚未取得／不適用 | 尚未建立本組可直接支持此用途的數據結論。 | 先補對應資料與試次匹配，再決定可測試策略；此處是研究缺口。 | 需本組材料、幾何、操作歷史與對應端點的量測；相近系列不能代替。 |
| 偵測 | 尚未取得／不適用 | 尚未建立本組可直接支持此用途的數據結論。 | 先補對應資料與試次匹配，再決定可測試策略；此處是研究缺口。 | 需本組材料、幾何、操作歷史與對應端點的量測；相近系列不能代替。 |
| 撲滅／抑制 | 尚未取得／不適用 | 尚未建立本組可直接支持此用途的數據結論。 | 先補對應資料與試次匹配，再決定可測試策略；此處是研究缺口。 | 需本組材料、幾何、操作歷史與對應端點的量測；相近系列不能代替。 |

## 逐次索引

| 原始檔／資料位置 | Trial／Run／列 | 共享身份與保留事項 |
| --- | --- | --- |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-98_SAFFIRE-I\Experimental table\PSI-98_Experimental table_SAFFIRE-1.csv | trial: S2；row: 3；source_record: 尚未取得／不適用 | identity_notes: burn_trial；raw_parameters_as_stored: Sample Number : S2；Material: SIBAL Fabric；Sample Thickness (cm): 0.37；Sample Length (cm): 40.6；Sample Width (cm): 94；Air Flow (cm/s): 20；Percent O2: ~ 21.5；Ignition Power (W): 182；Ignition Time (s): 8；Burn Time (s): 70；Flow Direction : Opposed；Camera 1: S2C1；Camera 2: S2C2 |

## 缺件與適用範圍

- Not an independent fresh-material orientation control.
- Local Sample2 workbook exists; exact sensor-to-flame time window still needs source-defined alignment.
- 尚未建立全火焰形狀／艙室安全的閉合預測。
