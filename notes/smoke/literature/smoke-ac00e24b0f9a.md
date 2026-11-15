# Smoke Aerosol Measurement Experiment (SAME): Operations Manual

## 文獻身份與實際審閱狀態

| ID | 文件類型 | 版本／年份 | SHA256 | 實體頁／投影片 | 內容審閱狀態 |
| --- | --- | --- | --- | --- | --- |
| SMOKE-ac00e24b0f9a | Hardware/software operations and troubleshooting manual | SAME-DOC-007, January 2007. | ac00e24b0f9a0388c3ac5097cca67591112c9992c0c9d40a6810ca5ba7289f36 | {"physical_pdf_pages": 33} | prior_primary_audit_reused_source_bytes_reverified |


- https://psi.nasa.gov/physci/repo/data/investigations/PSI-101
- https://psi.nasa.gov/physci/repo/data/investigations/PSI-102


DOI：Unknown（來源未提供／尚未核對）

[本機來源](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/其他研究文件_正文類型待確認/第一批下載/PSI-101_SAME-R/Science Documents/PSI-101_Science Documents_SAME_Operations Manual_007.pdf>)

## 濃縮結論與來源定位

| 結論ID | 結果／轉述 | 證據種類 | 實體頁／圖 | 條件 | 比較群組 |
| --- | --- | --- | --- | --- | --- |
| SMOKE-ac00e24b0f9a-C01 | Missing P-Trak serial readings use the sentinel -999. | design_or_operations | physicalp19,Section8.0 | {"PTrak_sampling_Hz": 1, "missing_sentinel": -999, "zero_fill_allowed": false} | Unknown（來源未提供／尚未核對） |
| SMOKE-ac00e24b0f9a-C02 | Incorrect heater offset correction can make reported resistance smaller than the actual resistance. | design_or_operations | physicalpp9,17-18 | {"utility_default_max_offset_uV": 200, "checklist_threshold_uV": 50, "utility_retries": 3, "note": "The checklist and utility have distinct thresholds; do not collapse them into a universal correction."} | Unknown（來源未提供／尚未核對） |
| SMOKE-ac00e24b0f9a-C03 | Fill and exhaust timing have documented dependencies on configured leak flow and inlet velocity. | design_or_operations | physicalp19 | {"example_FillLeakRate_LPM": 0.3, "example_maximum_inlet_velocity_cm_s": 9.8, "below_2_cm_s_requires_timing_adjustment": true} | Unknown（來源未提供／尚未核對） |


尚未讀取全文或屬工程／操作文件者，不因列在書目中就取得實驗結論；空白結論不以一般常識補齊。

## 使用哪個資料集的哪些部分

- study_ids: ["PSI-101", "PSI-102"]
- binding_level: campaign_context_not_trial_join
- exact_trial_ids: []
- exact_trial_binding_status: unknown
- known_context: Source conditions and named experiment family where reviewed; no blanket row-to-document join.


## 涉及的參數因子

- {"factor": "source_conditions", "values": {"missing_data_conditions": {"PTrak_sampling_Hz": 1, "missing_sentinel": -999, "zero_fill_allowed": false}, "heater_conditions": {"utility_default_max_offset_uV": 200, "checklist_threshold_uV": 50, "utility_retries": 3, "note": "The checklist and utility have distinct thresholds; do not collapse them into a universal correction."}, "timing_conditions": {"example_FillLeakRate_LPM": 0.3, "example_maximum_inlet_velocity_cm_s": 9.8, "below_2_cm_s_requires_timing_adjustment": true}}, "status": "source_condition_context_not_per_trial_controls", "source_locator": ["pp1-4:titleandcontents", "pp9-11:testchecklists", "pp17-18:heateroffsetcorrection", "p19:knownissues"]}


## 公式與視覺化 model code

Unknown；此處沒有補入推測值。


固定方程與來源快取比較、矩反演及分布重建的程式名稱是 `tools/smoke_evidence/physics.py` 與 `tools/smoke_evidence/viewer.js`。這是工具對照，不表示本文件提出或驗證了全部模型；逐式契約見 [MODELS.md](../MODELS.md)。

## 共用數據與結論差異

[CONCLUSION_COMPARISON.md](../CONCLUSION_COMPARISON.md) 對照本文件的結論。相同研究族、圖形或材料不能自動算成獨立重複；只有明確身份重疊才能宣稱同一資料。

## 適用限制與消防延伸

- No scientific model, measured ground dataset or ignition/extinction law is supplied.
- Operational text was read as source evidence; no hardware/software commands were executed.
- An individual data anomaly cannot be explained without its logged context.


可支持的預防、偵測、抑制研究問題及尚待驗證的產品構想見 [整合報告](../SMOKE_SYNTHESIS.md)。

## 本文結論的明確模型／程式對照

來源尚未提供可核對的項目；不填成 0。
