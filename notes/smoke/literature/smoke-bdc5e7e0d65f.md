# Particle Morphology and Size Results from the Smoke Aerosol Measurement Experiment-2

## 文獻身份與實際審閱狀態

| ID | 文件類型 | 版本／年份 | SHA256 | 實體頁／投影片 | 內容審閱狀態 |
| --- | --- | --- | --- | --- | --- |
| SMOKE-bdc5e7e0d65f | conference_paper | AIAA2012-3536 author copy;13physical pages | bdc5e7e0d65f569c2c4a0b8899870d2d47e8f0d644cfe033a450d9fd892375aa | 13 | fulltext_available_targeted_methods_results_conclusions_reviewed |


- https://ntrs.nasa.gov/citations/20130000422
- https://ntrs.nasa.gov/api/citations/20130000422/downloads/20130000422.pdf


DOI：10.2514/6.2012-3536

[本機來源](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/02_論文全文/02_會議論文與預印本/Particle Morphology and Size Results from the Smoke Aerosol Measurement Experiment-2__bdc5e7e0d6.pdf>)

## 濃縮結論與來源定位

| 結論ID | 結果／轉述 | 證據種類 | 實體頁／圖 | 條件 | 比較群組 |
| --- | --- | --- | --- | --- | --- |
| SMOKE-bdc5e7e0d65f-C01 | 在燈芯、Kapton 與 Teflon 的受測子集中，管道流速降低伴隨較大的矩等效粒徑。來源直線只是擬合描述，不是普遍輸送定律；作者估計粒徑重複性為 ±15%，本次沒有重新擬合。 | measurement_reduction | physical pp7–9,Figs6–8 | Fixed material-specific wire temperature; author estimates diameter repeatability±15%. | SAME_FLOW_PARTICLE_SIZE |
| SMOKE-bdc5e7e0d65f-C02 | 在分析資料中，MPASS 雙角度訊號後處理使相對響應變異約降至單通道的一半或更低。這是以同步 SAME 參考量測建立的同資料經驗關聯，不是獨立保留資料驗證、實測誤報率或合格的灰塵排除能力。 | source_fitted_correlation | physical pp9–10,Figs9–10 | Third-order least-squares correlation used simultaneous SAME reference measurements from points withSNR>2. | MPASS_SAME_DATA_CORRELATION |
| SMOKE-bdc5e7e0d65f-C03 | Pyrell 從 8 cm/s 下近似碎形的聚集體，變為無外加流動案例中的合併球體；作者將此與改變的熱場／輸送場聯繫。無外加流動仍有擴散與熱膨脹運動，原圖 13 兩種流動標籤都寫燈芯 Run 80 的歧義也須保留。 | measurement_and_author_interpretation | physical pp11–12,Fig13 | Microgravity heated-wire plume; diffusion/thermal expansion persist. | SAME_FLOW_MORPHOLOGY |
| SMOKE-bdc5e7e0d65f-C04 | 幾何平均粒徑與分布寬度需要對數常態假設；數目平均直徑及平均質量對應直徑則不需要。各項換算仍須具備相容且經校正的 M0／M1／M3 與密度換算。 | author_equation | physical pp3–4,Eqs1–7; p7Table1 | Compatible calibratedM0/M1/M3 and density conversion still required. | MOMENT_ASSUMPTIONS |


尚未讀取全文或屬工程／操作文件者，不因列在書目中就取得實驗結論；空白結論不以一般常識補齊。

## 使用哪個資料集的哪些部分

- study_ids: ["PSI-102", "PSI-101"]
- binding_level: campaign_context_not_trial_join
- exact_trial_ids: []
- exact_trial_binding_status: unknown
- known_context: Source conditions and named experiment family where reviewed; no blanket row-to-document join.


## 涉及的參數因子

- material
- wire heating baseline target1–2mg sample loss/60s
- flow nominal8cm/s,down to2 and no-flow
- aging11–1800s abstract
- M1 range andM3density/material calibration
- SAME1TEM contamination
- MPASSsame-dataSNRselection


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
| SMK-LOGNORMAL-INVERSE | Dg=sqrt(d_count^3/dm); sigma_g=exp(sqrt(ln(dm/d_count))) | executable_conditionally; measurement_inversion | physics.py::lognormal_parameters; viewer.js | \["dm>=d_count>0; no absolute-value repair of invalid negative logarithm.", "sigma=1 is a monodisperse limit; do not evaluate an ordinary continuous PDF with ln(sigma)=0.", "SAMERAppendixFEq7ambiguoustypography is preserved; executable formula uses unambiguous SAME2010 Eqs7–10."\] |
| SMK-LOGNORMAL-FORWARD | f_N(D)=N/\[sqrt(2*pi)*D*ln(sigma)\]*exp\[-(ln(D/Dg))^2/(2*ln(sigma)^2)\]; M_k=N*Dg^k*exp(0.5*k^2*ln(sigma)^2) | executable_as_reconstruction_or_declared_sensitivity; same_source_reconstruction_if_inverse_inputs | physics.py::lognormal_pdf; physics.py::lognormal_moment; viewer.js | \["The moment formula is an explicit mathematical integral of sourceEq3, not a new calibrated transport law.", "Do not mix f_N,dN/dlnD,anddN/dlog10D y-axis units.", "Arbitrary PSD not determined by three moments; morphology/size-range assumptions remain."\] |
