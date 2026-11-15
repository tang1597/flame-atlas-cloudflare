# SAME-DOC-001 Rev. A: Baseline Concept Description Document

## 文獻身份與實際審閱狀態

| ID | 文件類型 | 版本／年份 | SHA256 | 實體頁／投影片 | 內容審閱狀態 |
| --- | --- | --- | --- | --- | --- |
| SMOKE-3eed4b7ecd71 | Engineering concept and planned experiment/design document | SAME-DOC-001 Revision A, approved June 2005. | 3eed4b7ecd71f9e37a3f7a78d7e7a011ff636bb24ec8bcc72ff97a8ac41b598a | {"physical_pdf_pages": 15} | prior_primary_audit_reused_source_bytes_reverified |


- https://psi.nasa.gov/physci/repo/data/investigations/PSI-101
- https://psi.nasa.gov/physci/repo/data/investigations/PSI-102


DOI：Unknown（來源未提供／尚未核對）

[本機來源](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/其他研究文件_正文類型待確認/第一批下載/PSI-102_SAME/Science Documents/PSI-102_Science Documents_SAME_Baseline Concept Description Doc.pdf>)

## 濃縮結論與來源定位

| 結論ID | 結果／轉述 | 證據種類 | 實體頁／圖 | 條件 | 比較群組 |
| --- | --- | --- | --- | --- | --- |
| SMOKE-3eed4b7ecd71-C01 | A future numerical code is proposed to predict droplet growth from pyrolysis rate, vapor thermodynamics and flow. | future_work | physicalp7,Section2.3 | {"planned_flow_cm_s": \[5, 10\], "planned_massloss_mg_min": \[1, 2\], "planned_aging_min": \[1, 20\], "planned_model_inputs": \["Pyrolysis rate", "Thermodynamic properties of pyrolysis vapor", "Flow environment"\], "available_fixed_model": false} | Unknown（來源未提供／尚未核對） |
| SMOKE-3eed4b7ecd71-C02 | The anticipated twenty-point matrix uses five SAME-1 materials, 5/10 cm/s flow, 1/2 mg/min mass loss and 1/20 minute aging. | design_or_operations | physicalp13,Section6.4,Table1 | {"planned_flow_cm_s": \[5, 10\], "planned_massloss_mg_min": \[1, 2\], "planned_aging_min": \[1, 20\], "planned_model_inputs": \["Pyrolysis rate", "Thermodynamic properties of pyrolysis vapor", "Flow environment"\], "available_fixed_model": false} | Unknown（來源未提供／尚未核對） |
| SMOKE-3eed4b7ecd71-C03 | Wire-wrapped cylindrical samples and DBP liquid held on cotton wick are described, with preflight/postflight weighing planned. | design_or_operations | physicalp11,Section4.1item10 | {"sources": \["Teflon", "Kapton", "Silicone", "Cellulose", "Dibutyl phthalate on cotton wick"\], "heater": "Baseline stainless steel wire", "status": "Design concept"} | Unknown（來源未提供／尚未核對） |


尚未讀取全文或屬工程／操作文件者，不因列在書目中就取得實驗結論；空白結論不以一般常識補齊。

## 使用哪個資料集的哪些部分

- study_ids: ["PSI-101", "PSI-102"]
- binding_level: campaign_context_not_trial_join
- exact_trial_ids: []
- exact_trial_binding_status: unknown
- known_context: Source conditions and named experiment family where reviewed; no blanket row-to-document join.


## 涉及的參數因子

- {"factor": "source_conditions", "values": {"design_conditions": {"planned_flow_cm_s": [5, 10], "planned_massloss_mg_min": [1, 2], "planned_aging_min": [1, 20], "planned_model_inputs": ["Pyrolysis rate", "Thermodynamic properties of pyrolysis vapor", "Flow environment"], "available_fixed_model": false}, "material_conditions": {"sources": ["Teflon", "Kapton", "Silicone", "Cellulose", "Dibutyl phthalate on cotton wick"], "heater": "Baseline stainless steel wire", "status": "Design concept"}}, "status": "source_condition_context_not_per_trial_controls", "source_locator": ["pp2-4:approvalandcontents", "p7:objectivesandfuturecode", "pp8-11:hardwareandmaterialdefinitions", "p13:plannedTable1matrix"]}


## 公式與視覺化 model code

Unknown；此處沒有補入推測值。


固定方程與來源快取比較、矩反演及分布重建的程式名稱是 `tools/smoke_evidence/physics.py` 與 `tools/smoke_evidence/viewer.js`。這是工具對照，不表示本文件提出或驗證了全部模型；逐式契約見 [MODELS.md](../MODELS.md)。

## 共用數據與結論差異

[CONCLUSION_COMPARISON.md](../CONCLUSION_COMPARISON.md) 對照本文件的結論。相同研究族、圖形或材料不能自動算成獨立重複；只有明確身份重疊才能宣稱同一資料。

## 適用限制與消防延伸

- Design/future work is not actual Earth measurement or an executable fixed model.
- All PSI-101/102 aliases share the same SHA256 and count once.
- Hardware resource pressures cannot be treated as combustion-atmosphere pressure.


可支持的預防、偵測、抑制研究問題及尚待驗證的產品構想見 [整合報告](../SMOKE_SYNTHESIS.md)。

## 本文結論的明確模型／程式對照

來源尚未提供可核對的項目；不填成 0。
