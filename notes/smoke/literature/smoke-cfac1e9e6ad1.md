# Spacecraft Fire Detection: Smoke Properties and Transport in Low-Gravity

## 文獻身份與實際審閱狀態

| ID | 文件類型 | 版本／年份 | SHA256 | 實體頁／投影片 | 內容審閱狀態 |
| --- | --- | --- | --- | --- | --- |
| SMOKE-cfac1e9e6ad1 | conference_paper | AIAA2008-806;9physical pages | cfac1e9e6ad128c0d072f51f995537e0acd18518bb5ccf92983cb2467f69cd7c | 9 | fulltext_available_targeted_methods_results_conclusions_reviewed |


- https://ntrs.nasa.gov/citations/20080012612
- https://ntrs.nasa.gov/api/citations/20080012612/downloads/20080012612.pdf


DOI：10.2514/6.2008-806

[本機來源](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/02_論文全文/02_會議論文與預印本/Spacecraft Fire Detection_ Smoke Properties and Transport in Low-Gravity__cfac1e9e6a.pdf>)

## 濃縮結論與來源定位

| 結論ID | 結果／轉述 | 證據種類 | 實體頁／圖 | 條件 | 比較群組 |
| --- | --- | --- | --- | --- | --- |
| SMOKE-cfac1e9e6ad1-C01 | 初步數目平均直徑表列 Silicone 263 nm、燈芯 248 nm、Kapton 114 nm，分別比選取的 1g 結果高 53%、65%、58%；Teflon 為 223 nm，未列百分比。這些是該版校正的 M1/M0 結果，不應與後續平均質量對應直徑混用。 | measurement_reduction | physical p6,Table1 | SAME1 baseline; count meanM1/M0; edition-specific calibration. | EARLY_1G_COUNT_MEAN |
| SMOKE-cfac1e9e6ad1-C02 | Destiny 的 CFD 模型預測警報時間受通風、煙源位置／強度與障礙物影響，在這些計算情境中混合作用主導輸送。它是特定模型假設下的計算，不是太空艙實驗的預設條件或本次新做的 CFD。 | computation | physical pp6–8,Figs5–9 | FDS4.0.7LES;modelg=0;inert walls293K;propane source0.023m²,57.6kW/m²;1.46/2.95/8.47mg/s. | DESTINY_CFD |


尚未讀取全文或屬工程／操作文件者，不因列在書目中就取得實驗結論；空白結論不以一般常識補齊。

## 使用哪個資料集的哪些部分

- study_ids: ["PSI-102"]
- binding_level: campaign_context_not_trial_join
- exact_trial_ids: []
- exact_trial_binding_status: unknown
- known_context: Source conditions and named experiment family where reviewed; no blanket row-to-document join.


## 涉及的參數因子

- material
- countmeanversusmassmean
- preliminary calibration
- CFDventilation/source/obstruction


## 公式與視覺化 model code

Unknown；此處沒有補入推測值。


固定方程與來源快取比較、矩反演及分布重建的程式名稱是 `tools/smoke_evidence/physics.py` 與 `tools/smoke_evidence/viewer.js`。這是工具對照，不表示本文件提出或驗證了全部模型；逐式契約見 [MODELS.md](../MODELS.md)。

## 共用數據與結論差異

[CONCLUSION_COMPARISON.md](../CONCLUSION_COMPARISON.md) 對照本文件的結論。相同研究族、圖形或材料不能自動算成獨立重複；只有明確身份重疊才能宣稱同一資料。

## 適用限制與消防延伸

- No scientific result inferred from folder or filename; full content review not yet performed.


可支持的預防、偵測、抑制研究問題及尚待驗證的產品構想見 [整合報告](../SMOKE_SYNTHESIS.md)。

## 本文結論的明確模型／程式對照

| 模型ID／名稱 | 來源公式 | 可執行／比較角色 | 展示 code 名稱 | 適用限制 |
| --- | --- | --- | --- | --- |
| SMK-MOMENT-RATIOS | M_k=integral D^k f_N(D)dD; d_count=M1/M0; d_average_mass=(M3/M0)^(1/3) | executable_after_unit_calibration_range_gate; measurement_inversion | physics.py::moment_diameters; viewer.js | \["No lognormal assumption required for the two diameter ratios.", "M3 is a size moment, not a mass concentration until density/geometric conversion is supplied.", "d_average_mass is cube-mean diameter, not mass-weighted meanD43."\] |
| SMK-MASS-DIAMETER | dm_um=(6000*Cmass_mg_m3/(pi*rho_g_cm3*N_cm3))^(1/3); M3_um3_cm3=6000*Cmass_mg_m3/(pi*rho_g_cm3) | executable_for_source_approved_rows; same_source_algebraic_reproduction | physics.py::mass_to_m3; physics.py::mass_moment_diameter; viewer.js | \["Do not reapply TEOM/DustTrak correction already included in BH.", "Density is an author assumption, not an independently measured aerosol density.", "Raw optical proxy alone is not admissible as calibrated mass."\] |
