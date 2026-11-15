# Smoke Aerosol Measurement Experiment (SAME): Final Report

## 文獻身份與實際審閱狀態

| ID | 文件類型 | 版本／年份 | SHA256 | 實體頁／投影片 | 內容審閱狀態 |
| --- | --- | --- | --- | --- | --- |
| SMOKE-af91c96d22d9 | finalresearchreportwithmomentderivation,instrumentcalibration,flightexperimentsandappendedconferencepapers | {"source": "March15,2010FinalReport,projectperiodNovember1,2000-April14,2009;sharedcopybyte-identicaltophase4report.", "prior_review": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\output\\earth_space_transfer_20261114\\phase4_earth_experiment_search\\role_E\\same_102\\candidates.json"} | af91c96d22d93bbefbc0f2c5e1cc06e24813f532e5379b3fec9f121cccb22193 | {"physical_pdf_pages": 68} | prior_primary_audit_reused_source_bytes_reverified |


- https://psi.nasa.gov/physci/repo/data/investigations/PSI-102


DOI：Unknown（來源未提供／尚未核對）

[本機來源](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/研究報告與書章/第一批下載/PSI-102_SAME/Reports/PSI-102_Reports_SAME_Final Science Report.pdf>)

## 濃縮結論與來源定位

| 結論ID | 結果／轉述 | 證據種類 | 實體頁／圖 | 條件 | 比較群組 |
| --- | --- | --- | --- | --- | --- |
| SMOKE-af91c96d22d9-C01 | 報告推導校正後氣膠矩的換算及以對數常態假設重建分布的方法；它沒有提供由材料燃燒條件預測煙霧生成的動態模型，校正、形態與分布假設仍須保留。 | calculation | physicalpp15-19 | P-Trak measuresM0;calibrated ionization measuresM1;source-specific TEOM calibration corrects the DustTrak mass-related response. | Unknown（來源未提供／尚未核對） |
| SMOKE-af91c96d22d9-C02 | 最終結果中的 DustTrak 響應採用各來源專屬的 TEOM 校正；其適用性仍以相關粒徑分布未顯著改變為前提。 | measurement | physicalp23,calibrationdiscussion | P-Trak measuresM0;calibrated ionization measuresM1;source-specific TEOM calibration corrects the DustTrak mass-related response. | Unknown（來源未提供／尚未核對） |
| SMOKE-af91c96d22d9-C03 | 老化曲線呈現粒子數目下降、質量相關訊號相對穩定；作者將其解釋為凝聚且壁面損失有限。這不是獨立辨識的損失率，也不能唯一證明成分或完整粒徑分布。 | author_interpretation | physicalp27Fig13 | Resistively heated wire,approximately3mm cylindrical source,approximately60s heating,2-8cm/s air flow,and controlled aging10-1800s. Exact grades,pressure and oxygen concentration remain unknown. | Unknown（來源未提供／尚未核對） |
| SMOKE-af91c96d22d9-C04 | 附錄 E 收錄四種固體材料既有的 1g 比較資料，與前期整理重複；表中沒有 DBP 地面比較，不能另計為新的獨立實驗批次。 | measurement | physicalp64Table1 | Teflon,Kapton,cellulose/cotton lamp wick and silicone rubber;DBP on a porous wick is the reference. Ground DOP droplets and polystyrene spheres are different calibration materials. | Unknown（來源未提供／尚未核對） |


尚未讀取全文或屬工程／操作文件者，不因列在書目中就取得實驗結論；空白結論不以一般常識補齊。

## 使用哪個資料集的哪些部分

- study_ids: ["PSI-102"]
- binding_level: campaign_context_not_trial_join
- exact_trial_ids: []
- exact_trial_binding_status: unknown
- known_context: Source conditions and named experiment family where reviewed; no blanket row-to-document join.


## 涉及的參數因子

- {"factor": "source_conditions", "values": {"materials": "Teflon,Kapton,cellulose/cotton lamp wick and silicone rubber;DBP on a porous wick is the reference. Ground DOP droplets and polystyrene spheres are different calibration materials.", "generation": "Resistively heated wire,approximately3mm cylindrical source,approximately60s heating,2-8cm/s air flow,and controlled aging10-1800s. Exact grades,pressure and oxygen concentration remain unknown.", "instrument_model": "P-Trak measuresM0;calibrated ionization measuresM1;source-specific TEOM calibration corrects the DustTrak mass-related response.", "models": ["P5S-M1", "P5S-M2", "P5S-M3", "P5S-M4", "P5S-M5"]}, "status": "source_condition_context_not_per_trial_controls", "source_locator": ["p3abstract/materials", "pp15-19Eqs1-13", "pp20-23hardware/calibration", "p24operations", "pp25-28traces/Table1/morphologylimits", "pp30-31references/publicationlist", "AppendixEphysicalpp59-68,especiallyp64Table1"]}


## 公式與視覺化 model code

- {"equation_id": "SMOKE-LOGNORMAL-INVERSE", "expression": "D_g=sqrt(d_count^3/d_mass); sigma_g=exp(sqrt(ln(d_mass/d_count)))", "source_physical_pages": [18], "source_equation_numbers": ["7", "8"], "role": "measurement_inversion", "required_inputs": ["compatible d_count andd_mass", "lognormal assumption", "d_mass>=d_count>0"], "applicability": "Lognormal distribution with source-compatible detector response and morphology", "no_new_execution": true, "audit_path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\output\\equation_reproduction_20261115\\equation_inventory.json", "original_source_equation_id": "SMOKE-LOGNORMAL-INVERSE", "model_ids": ["SMK-LOGNORMAL-INVERSE"]}
- {"equation_id": "SMOKE-MOMENT-RATIOS", "expression": "M_i=integral D^i f_N(D)dD; d_count=M1/M0; d_mass=(M3/M0)^(1/3)", "source_physical_pages": [15, 16, 17, 18, 19], "source_equation_numbers": [], "role": "measurement_inversion", "required_inputs": ["compatible calibratedM0,M1,M3", "particle density for mass-equivalent conversion", "consistent diameter/volume units"], "applicability": "Source calibration and size-range/morphology assumptions; opticalmass is material-dependent", "no_new_execution": true, "audit_path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\output\\equation_reproduction_20261115\\equation_inventory.json", "original_source_equation_id": "SMOKE-MOMENT-RATIOS", "model_ids": ["SMK-MOMENT-RATIOS", "SMK-MASS-DIAMETER"]}


固定方程與來源快取比較、矩反演及分布重建的程式名稱是 `tools/smoke_evidence/physics.py` 與 `tools/smoke_evidence/viewer.js`。這是工具對照，不表示本文件提出或驗證了全部模型；逐式契約見 [MODELS.md](../MODELS.md)。

## 共用數據與結論差異

[CONCLUSION_COMPARISON.md](../CONCLUSION_COMPARISON.md) 對照本文件的結論。相同研究族、圖形或材料不能自動算成獨立重複；只有明確身份重疊才能宣稱同一資料。

## 適用限制與消防延伸

- Frozen phase4 quotations and locators are reused; no prior-phase source/output is changed.
- Literal equation-edition issues are identified inP5S-M1 rather than silently corrected and executed.
- Calibration aerosol identity does not establish matched fire-smoke chemistry.


可支持的預防、偵測、抑制研究問題及尚待驗證的產品構想見 [整合報告](../SMOKE_SYNTHESIS.md)。

## 本文結論的明確模型／程式對照

| 模型ID／名稱 | 來源公式 | 可執行／比較角色 | 展示 code 名稱 | 適用限制 |
| --- | --- | --- | --- | --- |
| SMK-MOMENT-RATIOS | M_k=integral D^k f_N(D)dD; d_count=M1/M0; d_average_mass=(M3/M0)^(1/3) | executable_after_unit_calibration_range_gate; measurement_inversion | physics.py::moment_diameters; viewer.js | \["No lognormal assumption required for the two diameter ratios.", "M3 is a size moment, not a mass concentration until density/geometric conversion is supplied.", "d_average_mass is cube-mean diameter, not mass-weighted meanD43."\] |
| SMK-MASS-DIAMETER | dm_um=(6000*Cmass_mg_m3/(pi*rho_g_cm3*N_cm3))^(1/3); M3_um3_cm3=6000*Cmass_mg_m3/(pi*rho_g_cm3) | executable_for_source_approved_rows; same_source_algebraic_reproduction | physics.py::mass_to_m3; physics.py::mass_moment_diameter; viewer.js | \["Do not reapply TEOM/DustTrak correction already included in BH.", "Density is an author assumption, not an independently measured aerosol density.", "Raw optical proxy alone is not admissible as calibrated mass."\] |
| SMK-LOGNORMAL-INVERSE | Dg=sqrt(d_count^3/dm); sigma_g=exp(sqrt(ln(dm/d_count))) | executable_conditionally; measurement_inversion | physics.py::lognormal_parameters; viewer.js | \["dm>=d_count>0; no absolute-value repair of invalid negative logarithm.", "sigma=1 is a monodisperse limit; do not evaluate an ordinary continuous PDF with ln(sigma)=0.", "SAMERAppendixFEq7ambiguoustypography is preserved; executable formula uses unambiguous SAME2010 Eqs7–10."\] |
| SMK-LOGNORMAL-FORWARD | f_N(D)=N/\[sqrt(2*pi)*D*ln(sigma)\]*exp\[-(ln(D/Dg))^2/(2*ln(sigma)^2)\]; M_k=N*Dg^k*exp(0.5*k^2*ln(sigma)^2) | executable_as_reconstruction_or_declared_sensitivity; same_source_reconstruction_if_inverse_inputs | physics.py::lognormal_pdf; physics.py::lognormal_moment; viewer.js | \["The moment formula is an explicit mathematical integral of sourceEq3, not a new calibrated transport law.", "Do not mix f_N,dN/dlnD,anddN/dlog10D y-axis units.", "Arbitrary PSD not determined by three moments; morphology/size-range assumptions remain."\] |

## 同一容器內的原始論文

| 附錄論文 | 來源頁與身份 | 是否為另一個獨立資料集 |
| --- | --- | --- |
| [Smoke Particle Sizes in Low-Gravity and Implications for Spacecraft Smoke Detector Design](<same2010-appb-2009-01-2468.md>) | physicalpp35–41,printedB1–B7;p42blank | 否；保留論文版次，容器SHA及資料血緣不重複計數 |
| [Properties of Smoke from Overheated Materials in Low-Gravity](<same2010-appc-aiaa2009-956.md>) | physicalpp43–49,printedC1–C7;p50blank | 否；保留論文版次，容器SHA及資料血緣不重複計數 |
| [Measurement of Smoke Particle Size under Low-Gravity Conditions](<same2010-appd-2008-01-2089.md>) | physicalpp51–58,printedD1–D8 | 否；保留論文版次，容器SHA及資料血緣不重複計數 |
| [Spacecraft Fire Detection: Smoke Properties and Transport in Low-Gravity](<smoke-cfac1e9e6ad1.md>) | physicalpp59–67,printedE1–E9 | 否；保留論文版次，容器SHA及資料血緣不重複計數 |
