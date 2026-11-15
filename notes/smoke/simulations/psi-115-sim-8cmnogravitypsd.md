# 8 cm/s microgravity-labelled author simulation

## 資料身份與展示 code

| ID | 角色 | 是否為量測試次 | 來源SHA256 |
| --- | --- | --- | --- |
| PSI-115-SIM-8cmNoGravityPSD | source_calculation | False | 80a3e6a37912d474c38ee3d49ea8af58dd8da31fc809470e202c7a396a2588d2 |


[原始作者計算檔](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/01_實驗資料/補下載/PSI-115/Analyzed Data/f89835432ada9e02_PSI-115_Analyzed Data_8cmNoGravityPSD.dat>)

[作者曲線互動圖](<../viewer/viewer.html?simulation=PSI-115-SIM-8cmNoGravityPSD&view=simulation>)，展示程式為 `tools/smoke_evidence/viewer.js`；未執行新的耦合求解器。

## 條件與來源部分

- material_context: DBP surrogate, per existing author-report audit; not material-specific Kapton/Teflon smoke chemistry.
- nominal_velocity_cm_s: 8
- velocity_basis: Case filename plus existing report Table3 audit; copied case context, no new conversion.
- gravity_case_label: NoGravity
- numeric_gravity_m_s2: Unknown（來源未提供／尚未核對）
- omitted_process_case_label: []
- all_other_process_settings: Not independently encoded/verified in the two-column snapshot.
- report_context_time_s: 7
- source_file_time_s: Unknown（來源未提供／尚未核對）
- sampling_time_provenance: Reported paper context at7s, not a per-file header, independent acquisition timestamp or measured datetime.
- pressure: Unknown（來源未提供／尚未核對）
- oxygen_fraction: Unknown（來源未提供／尚未核對）
- local_temperature_field: Unknown（來源未提供／尚未核對）
- local_velocity_field: Unknown（來源未提供／尚未核對）


- {"kind": "raw_author_simulation_snapshot", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\補下載\\PSI-115\\Analyzed Data\\f89835432ada9e02_PSI-115_Analyzed Data_8cmNoGravityPSD.dat", "sha256": "80a3e6a37912d474c38ee3d49ea8af58dd8da31fc809470e202c7a396a2588d2", "fresh_sha256_matches_prior_audit": true, "prior_audit_sha256": "80a3e6a37912d474c38ee3d49ea8af58dd8da31fc809470e202c7a396a2588d2", "source_lines": {"first": 1, "last": 44}, "particle_node_line_mapping": [{"node": 2, "line": 1}, {"node": 3, "line": 2}, {"node": 4, "line": 3}, {"node": 5, "line": 4}, {"node": 6, "line": 5}, {"node": 7, "line": 6}, {"node": 8, "line": 7}, {"node": 9, "line": 8}, {"node": 10, "line": 9}, {"node": 11, "line": 10}, {"node": 12, "line": 11}, {"node": 13, "line": 12}, {"node": 14, "line": 13}, {"node": 15, "line": 14}, {"node": 16, "line": 15}, {"node": 17, "line": 16}, {"node": 18, "line": 17}, {"node": 19, "line": 18}, {"node": 20, "line": 19}, {"node": 21, "line": 20}, {"node": 22, "line": 21}, {"node": 23, "line": 22}, {"node": 24, "line": 23}, {"node": 25, "line": 24}, {"node": 26, "line": 25}, {"node": 27, "line": 26}, {"node": 28, "line": 27}, {"node": 29, "line": 28}, {"node": 30, "line": 29}, {"node": 31, "line": 30}, {"node": 32, "line": 31}, {"node": 33, "line": 32}, {"node": 34, "line": 33}, {"node": 35, "line": 34}, {"node": 36, "line": 35}, {"node": 37, "line": 36}, {"node": 38, "line": 37}, {"node": 39, "line": 38}, {"node": 40, "line": 39}, {"node": 41, "line": 40}, {"node": 42, "line": 41}, {"node": 43, "line": 42}, {"node": 44, "line": 43}, {"node": 45, "line": 44}]}
- {"kind": "previous_source_audit", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\output\\earth_space_transfer_20261114\\phase5_shared_document_review\\role_E\\modeling\\model_audit.json", "sha256": "347449f26f926988f677e1c853028b792e74dbe0eb939df82f3bffee41948a9e", "json_pointer": "/case_results/5"}
- {"doc_id": "SMOKE-487108f951ba", "title": "Utilization of the SAME Data for Advanced Modeling and Simulation of Smoke Generation in Microgravity", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\03_其他文件\\研究報告與書章\\第一批下載\\PSI-115_research\\Reports\\PSI-115_Reports_NNX17AF08A_FinalReport.pdf", "sha256": "487108f951ba8ec9042464ae7c70a8190fa63c4b1141f8b1dfe19d697bd9752c", "edition": "Final August15,2020;25 physicalPDF pages", "locators": ["physical p7 Eq23 particle-node sums", "physical p9 node grid", "physical p10 reported effective state at7s", "physical p21 Table3; modified-case Table4 physicalp25"], "officialURLs": ["https://psi.nasa.gov/physci/repo/data/investigations/PSI-115", "https://doi.org/10.60555/q0v5-1v28"], "evidence_role": "source_calculation"}
- {"doc_id": "SMOKE-754cd3b7e1f1", "title": "PSI Data Organization Document: Utilization of the Smoke Aerosol Measurement Experiment Data for Advanced Modeling and Simulation of Smoke Generation in Micro-Gravity", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\03_其他文件\\其他研究文件_正文類型待確認\\第一批下載\\PSI-115_research\\Science Documents\\PSI-115_Science Documents_DataOrganizationDocument.pdf", "sha256": "754cd3b7e1f1334f7de75abbdc0fac2687bc451c76d36245b66a5315c01d7253", "locators": ["physical p1 simulation case organization"], "evidence_role": "source_documentation", "caution": "Guide refers modified cases toTable3; prior audit locates modified-case table asTable4,p25 in final report. Preserve edition wording."}


## 多個可支持結論

- {"text": "This archived snapshot supplies an actual author-computed node-distribution curve for its labelled case.", "evidence_kind": "source_calculation", "source_locator": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\補下載\\PSI-115\\Analyzed Data\\f89835432ada9e02_PSI-115_Analyzed Data_8cmNoGravityPSD.dat:lines1–44", "limitation": "The source ordinate unit and absolute normalization are unspecified."}


- 本快照提供作者對該標籤條件的節點分布；不等於獨立實驗量測。
- 節點1單體另存，不併入粒子節點2至45；缺值不補0。
- 原始縱軸的物理單位與絕對正規化未明，無法由此直接取得濃度、警報時刻或消防效能。

## 使用文獻、因子及跨案例比較

- [SMOKE-487108f951ba](<../literature/smoke-487108f951ba.md>)
- [SMOKE-754cd3b7e1f1](<../literature/smoke-754cd3b7e1f1.md>)


- SMK-E115-COUPLED


來源條件與 [Excel因子對照](../FACTOR_MAP.md) 僅依已定位資訊比對；缺少的氧濃度、壓力、局部溫度與速度場保持Unknown。各案例共同與不同處見 [作者模擬集合](../AUTHOR_SIMULATIONS.md)，消防延伸見 [整合報告](../SMOKE_SYNTHESIS.md)。

## 限制

- All curves are archived author calculations, including Gravity/EarthGravity-labelled cases; none is an acquired1g measurement.
- Two-column .dat files contain node ordinals and unlabelled ordinates, without units or absolute concentration normalization.
- Plot particle nodes2..45 only; preserve monomer node1 separately and absent values asnull, notzero.
- No node-to-diameter, density, concentration, probability or time conversion is applied.
- One snapshot does not supply the local spatial/time state, collision kernel, transport/thermal fields or largest-node boundary rule needed to rerun the coupled model.
- Differences between archived curves are source simulation results, not independent experimental validation or detector qualification.


單體節點原值：{"node": 1, "present": false, "value": null, "source_decimal_token": null, "included_in_points": false, "unit": "source ordinate (unit unspecified)"}。
