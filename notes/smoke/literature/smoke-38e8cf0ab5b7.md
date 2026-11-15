# Smoke Characterization and Feasibility of the Moment Method for Spacecraft Fire Detection

## 文獻身份與實際審閱狀態

| ID | 文件類型 | 版本／年份 | SHA256 | 實體頁／投影片 | 內容審閱狀態 |
| --- | --- | --- | --- | --- | --- |
| SMOKE-38e8cf0ab5b7 | journal_article | AST49(5):299–309;onlineApril8,2015;physicalp1publishercover | 38e8cf0ab5b72b8115aa953facd7e3b9c56bb74e4b4961d8d3370fe4fe636756 | 12 | fulltext_available_targeted_methods_results_conclusions_reviewed |


- https://doi.org/10.1080/02786826.2015.1025124


DOI：10.1080/02786826.2015.1025124

[本機來源](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/02_論文全文/01_期刊論文與作者稿/Smoke Characterization and Feasibility of the Moment Method for Spacecraft Fire Detection__38e8cf0ab5.pdf>)

## 濃縮結論與來源定位

| 結論ID | 結果／轉述 | 證據種類 | 實體頁／圖 | 條件 | 比較群組 |
| --- | --- | --- | --- | --- | --- |
| SMOKE-38e8cf0ab5b7-C01 | 地面桶式煙霧試驗用來檢查粒徑分布形狀；一個或多個返回地面的飛行儀器故障，使多數同步矩資料不可靠，因此無法完成原先希望進行的矩／SMPS 直接驗證。 | measurement_limitation | physical pp5–6;printed302–303;Fig1 | Ground engineering apparatus plus55-gallon drums/dilution andSMPS;SMPSscan2min versus<=30s chamber supply. | DRUM_SMPS_ONLY |
| SMOKE-38e8cf0ab5b7-C02 | 詳細 SMPS／TEM 分析對 Kapton／燈芯的對數常態支持最明確；Silicone 未通過定性一致性檢查，且在 TEM 下不穩定，Pyrell／Teflon 則呈聚集體。地面 SMPS 與返回飛行 TEM 是不同診斷子集，不能推廣為所有試次皆符合對數常態。 | measurement_and_author_interpretation | physical pp6–7,11;printed303–304,308;Figs2–3 | GroundSMPS and returned-flightTEM are different diagnostic subsets. | MATERIAL_LOGNORMAL_VALIDITY |
| SMOKE-38e8cf0ab5b7-C03 | 部分飛行氣膠超出 M1 游離式偵測器的校正範圍，明顯影響粒徑分布重建，Kapton 最可靠。質量等效直徑不使用 M1，與 Kapton、Pyrell、燈芯的選取 TEM 結果仍有可用一致性；但沒有 TEM／SMPS／矩的直接三方驗證。 | measurement_uncertainty_and_author_interpretation | physical p11;printed308;Fig7 | M0/M3 require material-specific calibration/density; selectedKapton,Pyrell,lampwick comparison. | M1_RANGE_LIMIT |
| SMOKE-38e8cf0ab5b7-C04 | 來源區分不依賴分布形狀的矩比值，以及以對數常態為前提的公式，並給出儀器有限粒徑範圍的矩積分式；M1 是積分粒徑濃度，數目平均直徑則是 M1/M0。 | author_equation | physical p3Eqs1–3;p4Eqs4–5;printed300–301 | M1 is integrated diameter concentration;countmean=M1/M0. | MOMENT_FORMULAS |


尚未讀取全文或屬工程／操作文件者，不因列在書目中就取得實驗結論；空白結論不以一般常識補齊。

## 使用哪個資料集的哪些部分

- study_ids: ["PSI-102", "PSI-101"]
- binding_level: campaign_context_not_trial_join
- exact_trial_ids: []
- exact_trial_binding_status: unknown
- known_context: Source conditions and named experiment family where reviewed; no blanket row-to-document join.


## 涉及的參數因子

- sphericity
- lognormality
- M1calibrationrange
- density
- instrumentlimits
- grounddrumdilution
- TEMvolatility


## 公式與視覺化 model code

- {"equation_id": "SMK-MOMENT-RATIOS", "source_physical_pages": [3], "source_equation_numbers": ["1"], "expression": "d_av=M1/M0=L_tot/N_tot", "original_source_equation_id": "SMK-MOMENT-RATIOS", "model_ids": ["SMK-MOMENT-RATIOS"]}
- {"equation_id": "SMK-MASS-DIAMETER", "source_physical_pages": [3], "source_equation_numbers": ["2"], "expression": "d_m=(M3/M0)^(1/3)=(6M_tot/(pi*rho*N_tot))^(1/3)", "original_source_equation_id": "SMK-MASS-DIAMETER", "model_ids": ["SMK-MASS-DIAMETER"]}
- {"equation_id": "SMK-LOGNORMAL-FORWARD", "source_physical_pages": [3], "source_equation_numbers": ["3"], "expression": "d_(p,q)=d_g*exp((q+p/2)*ln(sigma_g)^2)", "original_source_equation_id": "SMK-LOGNORMAL-FORWARD", "model_ids": ["SMK-LOGNORMAL-FORWARD"]}
- {"equation_id": "SMK-LIMITED-RANGE", "source_physical_pages": [4], "source_equation_numbers": ["5"], "expression": "Cumulative-moment response truncation;primary formula required for exact cutoff conventions.", "original_source_equation_id": "SMK-LIMITED-RANGE", "model_ids": ["SMK-LIMITED-RANGE"]}


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
| SMK-LIMITED-RANGE | eta(D)=\[ln(D/Dg)-k*ln(sigma)^2\]/\[sqrt(2)*ln(sigma)\]; F_k(Dlo,Dhi)=0.5*\[erf(eta_hi)-erf(eta_lo)\] | executable_conditionally; conditional_derived_quantity | physics.py::moment_fraction; viewer.js | \["Momentorderk differs from characteristicdiameterp=0.5/1.5 notation.", "Cutoff corrections are not automatically valid for nonspherical/agglomerated or non-lognormal smoke."\] |
