# An Overview of Smoke Detection and Spacecraft Fire Safety in Low Gravity

## 文獻身份與實際審閱狀態

| ID | 文件類型 | 版本／年份 | SHA256 | 實體頁／投影片 | 內容審閱狀態 |
| --- | --- | --- | --- | --- | --- |
| SMOKE-f3c38f50d223 | scientific_review_presentation | AAAR October6,2020;16-slide NASA deck | f3c38f50d2230cace828d51c0c8562d035aa76a1604b5cb1f7d4c17263d7ed3f | 16 | fulltext_available_targeted_review_presentation_reviewed |


- https://ntrs.nasa.gov/citations/20205008167
- https://ntrs.nasa.gov/api/citations/20205008167/downloads/AAAR%202020%20Platform%20v1.pdf


DOI：Unknown（來源未提供／尚未核對）

[本機來源](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/簡報與海報/補下載/An Overview of Smoke Detection and Spacecraft Fire Safety in Low Gravity_40810d63c6.pdf>)

## 濃縮結論與來源定位

| 結論ID | 結果／轉述 | 證據種類 | 實體頁／圖 | 條件 | 比較群組 |
| --- | --- | --- | --- | --- | --- |
| SMOKE-f3c38f50d223-C01 | 綜述彙整 SAME 已發表結果：粒徑隨材料與流動條件改變，ISS 偵測器對較小 Kapton／Teflon 煙霧響應較弱。這些引用既有研究，不是新的獨立實驗。 | source_author_secondary_synthesis | slides5–6 | Cites2013/2015/2018 SAME publications. | OVERVIEW_SYNTHESIS |
| SMOKE-f3c38f50d223-C02 | 作者綜述通風、障礙物、過濾及煙源／偵測器位置對警報時間的影響，並指出月塵與部分重力仍需額外資格驗證。簡報把第一階矩簡寫為平均粒徑的地方，仍須依正式公式區分 M1 與 M1/M0。 | author_synthesis_and_proposal | slides4,8–12 | Slide9summarizes priorCFD/vehicle studies;lunar points are outlook. | VENTILATION_QUALIFICATION |


尚未讀取全文或屬工程／操作文件者，不因列在書目中就取得實驗結論；空白結論不以一般常識補齊。

## 使用哪個資料集的哪些部分

- study_ids: []
- binding_level: campaign_context_not_trial_join
- exact_trial_ids: []
- exact_trial_binding_status: unknown


## 涉及的參數因子

- ventilation
- obstructions
- backgrounddust
- filtration
- size/morphology
- partialgravity


## 公式與視覺化 model code

Unknown；此處沒有補入推測值。


固定方程與來源快取比較、矩反演及分布重建的程式名稱是 `tools/smoke_evidence/physics.py` 與 `tools/smoke_evidence/viewer.js`。這是工具對照，不表示本文件提出或驗證了全部模型；逐式契約見 [MODELS.md](../MODELS.md)。

## 共用數據與結論差異

[CONCLUSION_COMPARISON.md](../CONCLUSION_COMPARISON.md) 對照本文件的結論。相同研究族、圖形或材料不能自動算成獨立重複；只有明確身份重疊才能宣稱同一資料。

## 適用限制與消防延伸

Unknown；此處沒有補入推測值。


可支持的預防、偵測、抑制研究問題及尚待驗證的產品構想見 [整合報告](../SMOKE_SYNTHESIS.md)。

## 本文結論的明確模型／程式對照

| 模型ID／名稱 | 來源公式 | 可執行／比較角色 | 展示 code 名稱 | 適用限制 |
| --- | --- | --- | --- | --- |
| SMK-MOMENT-RATIOS | M_k=integral D^k f_N(D)dD; d_count=M1/M0; d_average_mass=(M3/M0)^(1/3) | executable_after_unit_calibration_range_gate; measurement_inversion | physics.py::moment_diameters; viewer.js | \["No lognormal assumption required for the two diameter ratios.", "M3 is a size moment, not a mass concentration until density/geometric conversion is supplied.", "d_average_mass is cube-mean diameter, not mass-weighted meanD43."\] |
| SMK-MASS-DIAMETER | dm_um=(6000*Cmass_mg_m3/(pi*rho_g_cm3*N_cm3))^(1/3); M3_um3_cm3=6000*Cmass_mg_m3/(pi*rho_g_cm3) | executable_for_source_approved_rows; same_source_algebraic_reproduction | physics.py::mass_to_m3; physics.py::mass_moment_diameter; viewer.js | \["Do not reapply TEOM/DustTrak correction already included in BH.", "Density is an author assumption, not an independently measured aerosol density.", "Raw optical proxy alone is not admissible as calibrated mass."\] |
