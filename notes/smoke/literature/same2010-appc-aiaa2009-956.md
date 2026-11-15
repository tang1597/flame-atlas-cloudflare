# Properties of Smoke from Overheated Materials in Low-Gravity

## 文獻身份與實際審閱狀態

| ID | 文件類型 | 版本／年份 | SHA256 | 實體頁／投影片 | 內容審閱狀態 |
| --- | --- | --- | --- | --- | --- |
| SAME2010-APPC-AIAA2009-956 | embedded_conference_paper | Unknown（來源未提供／尚未核對） | af91c96d22d93bbefbc0f2c5e1cc06e24813f532e5379b3fec9f121cccb22193 | Unknown（來源未提供／尚未核對） | embedded_primary_work_targeted_pages_reviewed |


- https://ntrs.nasa.gov/citations/20120012884


DOI：Unknown（來源未提供／尚未核對）

[本機來源](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/研究報告與書章/第一批下載/PSI-102_SAME/Reports/PSI-102_Reports_SAME_Final Science Report.pdf>)

## 濃縮結論與來源定位

| 結論ID | 結果／轉述 | 證據種類 | 實體頁／圖 | 條件 | 比較群組 |
| --- | --- | --- | --- | --- | --- |
| SAME2010-APPC-AIAA2009-956-C01 | 初步 Mie／對數常態迭代換算在部分案例不收斂；表 1 將 Silicone 的算術平均與質量相關直徑列為 N/A。雙峰分布只是作者提出的可能解釋，不能由不收斂直接證明。 | source_model_reconstruction_limitation | physicalp48,printedC6,Table1 | Unknown（來源未提供／尚未核對） | Unknown（來源未提供／尚未核對） |


尚未讀取全文或屬工程／操作文件者，不因列在書目中就取得實驗結論；空白結論不以一般常識補齊。

## 使用哪個資料集的哪些部分

- study_ids: ["PSI-102"]
- binding_level: SAME1 source subsection; no automatic exact raw-trial join
- exact_trial_ids: []


## 涉及的參數因子

Unknown；此處沒有補入推測值。


## 公式與視覺化 model code

Unknown；此處沒有補入推測值。


固定方程與來源快取比較、矩反演及分布重建的程式名稱是 `tools/smoke_evidence/physics.py` 與 `tools/smoke_evidence/viewer.js`。這是工具對照，不表示本文件提出或驗證了全部模型；逐式契約見 [MODELS.md](../MODELS.md)。

## 共用數據與結論差異

[CONCLUSION_COMPARISON.md](../CONCLUSION_COMPARISON.md) 對照本文件的結論。相同研究族、圖形或材料不能自動算成獨立重複；只有明確身份重疊才能宣稱同一資料。

## 適用限制與消防延伸

- Embedded in the parent report; not another independent dataset or file SHA.


可支持的預防、偵測、抑制研究問題及尚待驗證的產品構想見 [整合報告](../SMOKE_SYNTHESIS.md)。

## 本文結論的明確模型／程式對照

| 模型ID／名稱 | 來源公式 | 可執行／比較角色 | 展示 code 名稱 | 適用限制 |
| --- | --- | --- | --- | --- |
| SMK-MOMENT-RATIOS | M_k=integral D^k f_N(D)dD; d_count=M1/M0; d_average_mass=(M3/M0)^(1/3) | executable_after_unit_calibration_range_gate; measurement_inversion | physics.py::moment_diameters; viewer.js | \["No lognormal assumption required for the two diameter ratios.", "M3 is a size moment, not a mass concentration until density/geometric conversion is supplied.", "d_average_mass is cube-mean diameter, not mass-weighted meanD43."\] |
| SMK-MASS-DIAMETER | dm_um=(6000*Cmass_mg_m3/(pi*rho_g_cm3*N_cm3))^(1/3); M3_um3_cm3=6000*Cmass_mg_m3/(pi*rho_g_cm3) | executable_for_source_approved_rows; same_source_algebraic_reproduction | physics.py::mass_to_m3; physics.py::mass_moment_diameter; viewer.js | \["Do not reapply TEOM/DustTrak correction already included in BH.", "Density is an author assumption, not an independently measured aerosol density.", "Raw optical proxy alone is not admissible as calibrated mass."\] |
| SMK-LOGNORMAL-INVERSE | Dg=sqrt(d_count^3/dm); sigma_g=exp(sqrt(ln(dm/d_count))) | executable_conditionally; measurement_inversion | physics.py::lognormal_parameters; viewer.js | \["dm>=d_count>0; no absolute-value repair of invalid negative logarithm.", "sigma=1 is a monodisperse limit; do not evaluate an ordinary continuous PDF with ln(sigma)=0.", "SAMERAppendixFEq7ambiguoustypography is preserved; executable formula uses unambiguous SAME2010 Eqs7–10."\] |
| SMK-LOGNORMAL-FORWARD | f_N(D)=N/\[sqrt(2*pi)*D*ln(sigma)\]*exp\[-(ln(D/Dg))^2/(2*ln(sigma)^2)\]; M_k=N*Dg^k*exp(0.5*k^2*ln(sigma)^2) | executable_as_reconstruction_or_declared_sensitivity; same_source_reconstruction_if_inverse_inputs | physics.py::lognormal_pdf; physics.py::lognormal_moment; viewer.js | \["The moment formula is an explicit mathematical integral of sourceEq3, not a new calibrated transport law.", "Do not mix f_N,dN/dlnD,anddN/dlog10D y-axis units.", "Arbitrary PSD not determined by three moments; morphology/size-range assumptions remain."\] |
