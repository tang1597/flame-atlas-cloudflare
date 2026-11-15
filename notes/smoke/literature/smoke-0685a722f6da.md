# Evaluation of Low-Gravity Smoke Particulate for Spacecraft Fire Detection

## 文獻身份與實際審閱狀態

| ID | 文件類型 | 版本／年份 | SHA256 | 實體頁／投影片 | 內容審閱狀態 |
| --- | --- | --- | --- | --- | --- |
| SMOKE-0685a722f6da | research_presentation | 19-slide2013 deck with conflicting2011/50thAIAA stale footer | 0685a722f6da522c7365534a8c284e5e38da3425d3fca7ec92ff38cbbe8fa9b6 | 19 | fulltext_available_targeted_methods_results_conclusions_reviewed |


- https://ntrs.nasa.gov/citations/20140006585
- https://ntrs.nasa.gov/api/citations/20140006585/downloads/20140006585.pdf


DOI：Unknown（來源未提供／尚未核對）

[本機來源](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/簡報與海報/補下載/Evaluation of Low-Gravity Smoke Particulate for Spacecraft Fire Detection_8ac72da1e3.pdf>)

## 濃縮結論與來源定位

| 結論ID | 結果／轉述 | 證據種類 | 實體頁／圖 | 條件 | 比較群組 |
| --- | --- | --- | --- | --- | --- |
| SMOKE-0685a722f6da-C01 | 簡報彙整流速降低及老化增加時的粒徑增大，並展示 8 cm/s 下的地面／飛行質量等效直徑比較；各圖對應的材料溫度與老化設定須分開保留。 | measurement_summary_presentation | physical slides16–18 | Slide16fixedmaterialtemperature/noaging;slide17fixedtemperature/8cm/s. | FLOW_AGING_PRESENTATION |
| SMOKE-0685a722f6da-C02 | 作者提出多矩感測，以涵蓋不同煙霧粒徑並排除干擾粒子；簡報尚未建立合格的誤報性能，仍需更廣的材料、流動與背景測試矩陣。 | author_proposal | physical slide19 | Broad material/flow/background matrix beyond this experiment remains. | MULTIMOMENT_RESEARCH |


尚未讀取全文或屬工程／操作文件者，不因列在書目中就取得實驗結論；空白結論不以一般常識補齊。

## 使用哪個資料集的哪些部分

- study_ids: ["PSI-102", "PSI-101"]
- binding_level: campaign_context_not_trial_join
- exact_trial_ids: []
- exact_trial_binding_status: unknown
- known_context: Source conditions and named experiment family where reviewed; no blanket row-to-document join.


## 涉及的參數因子

- material
- flow
- aging
- gravitycomparison
- detectorconcept


## 公式與視覺化 model code

Unknown；此處沒有補入推測值。


固定方程與來源快取比較、矩反演及分布重建的程式名稱是 `tools/smoke_evidence/physics.py` 與 `tools/smoke_evidence/viewer.js`。這是工具對照，不表示本文件提出或驗證了全部模型；逐式契約見 [MODELS.md](../MODELS.md)。

## 共用數據與結論差異

[CONCLUSION_COMPARISON.md](../CONCLUSION_COMPARISON.md) 對照本文件的結論。相同研究族、圖形或材料不能自動算成獨立重複；只有明確身份重疊才能宣稱同一資料。

## 適用限制與消防延伸

- No scientific result inferred from folder or filename; full content review not yet performed.
- Title-slide May2013 conflicts with stale2011/50thAIAA footers;do not date experiments bytemplate.
- Same underlying SAME data as the conferencepaper.


可支持的預防、偵測、抑制研究問題及尚待驗證的產品構想見 [整合報告](../SMOKE_SYNTHESIS.md)。

## 本文結論的明確模型／程式對照

| 模型ID／名稱 | 來源公式 | 可執行／比較角色 | 展示 code 名稱 | 適用限制 |
| --- | --- | --- | --- | --- |
| SMK-MOMENT-RATIOS | M_k=integral D^k f_N(D)dD; d_count=M1/M0; d_average_mass=(M3/M0)^(1/3) | executable_after_unit_calibration_range_gate; measurement_inversion | physics.py::moment_diameters; viewer.js | \["No lognormal assumption required for the two diameter ratios.", "M3 is a size moment, not a mass concentration until density/geometric conversion is supplied.", "d_average_mass is cube-mean diameter, not mass-weighted meanD43."\] |
| SMK-MASS-DIAMETER | dm_um=(6000*Cmass_mg_m3/(pi*rho_g_cm3*N_cm3))^(1/3); M3_um3_cm3=6000*Cmass_mg_m3/(pi*rho_g_cm3) | executable_for_source_approved_rows; same_source_algebraic_reproduction | physics.py::mass_to_m3; physics.py::mass_moment_diameter; viewer.js | \["Do not reapply TEOM/DustTrak correction already included in BH.", "Density is an author assumption, not an independently measured aerosol density.", "Raw optical proxy alone is not admissible as calibrated mass."\] |
