# PSI Data Organization Document: Utilization of the Smoke Aerosol Measurement Experiment Data for Advanced Modeling and Simulation of Smoke Generation in Micro-Gravity

## 文獻身份與實際審閱狀態

| ID | 文件類型 | 版本／年份 | SHA256 | 實體頁／投影片 | 內容審閱狀態 |
| --- | --- | --- | --- | --- | --- |
| SMOKE-754cd3b7e1f1 | simulation-data organization guide, not a new experiment or research poster | undated1page PSI data organization guide | 754cd3b7e1f1334f7de75abbdc0fac2687bc451c76d36245b66a5315c01d7253 | {"physical_pdf_pages": 1} | prior_primary_audit_reused_source_bytes_reverified |


- https://psi.nasa.gov/physci/repo/data/investigations/PSI-115


DOI：Unknown（來源未提供／尚未核對）

[本機來源](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/其他研究文件_正文類型待確認/第一批下載/PSI-115_research/Science Documents/PSI-115_Science Documents_DataOrganizationDocument.pdf>)

## 濃縮結論與來源定位

| 結論ID | 結果／轉述 | 證據種類 | 實體頁／圖 | 條件 | 比較群組 |
| --- | --- | --- | --- | --- | --- |
| SMOKE-754cd3b7e1f1-C01 | EarthGravity and Microgravity folders contain simulation figure data. Cases distinguish velocity and the removal of settling/thermophoresis or rotation of the source. | design_or_operations | p1 | Table3 copied from finalreport | Unknown（來源未提供／尚未核對） |


尚未讀取全文或屬工程／操作文件者，不因列在書目中就取得實驗結論；空白結論不以一般常識補齊。

## 使用哪個資料集的哪些部分

- study_ids: ["PSI-115"]
- binding_level: campaign_context_not_trial_join
- exact_trial_ids: []
- exact_trial_binding_status: unknown
- known_context: Source conditions and named experiment family where reviewed; no blanket row-to-document join.


## 涉及的參數因子

- {"factor": "source_conditions", "values": {"case1_m_s": 0.08, "case2_m_s": 0.1, "sampling_time_s": 7, "NS": "no settling", "NT": "no thermophoresis", "R": "heated source rotated90degrees"}, "status": "source_condition_context_not_per_trial_controls", "source_locator": ["physicalp1 wholepage and embedded Table3"]}


## 公式與視覺化 model code

Unknown；此處沒有補入推測值。


固定方程與來源快取比較、矩反演及分布重建的程式名稱是 `tools/smoke_evidence/physics.py` 與 `tools/smoke_evidence/viewer.js`。這是工具對照，不表示本文件提出或驗證了全部模型；逐式契約見 [MODELS.md](../MODELS.md)。

## 共用數據與結論差異

[CONCLUSION_COMPARISON.md](../CONCLUSION_COMPARISON.md) 對照本文件的結論。相同研究族、圖形或材料不能自動算成獨立重複；只有明確身份重疊才能宣稱同一資料。

## 適用限制與消防延伸

- Provides organization, not raw measurements or the simulation solver.
- Text points modified cases to Table3 although final report modified-case table isTable4(p25); preserve edition wording and check original table.


可支持的預防、偵測、抑制研究問題及尚待驗證的產品構想見 [整合報告](../SMOKE_SYNTHESIS.md)。

## 本文結論的明確模型／程式對照

來源尚未提供可核對的項目；不填成 0。
