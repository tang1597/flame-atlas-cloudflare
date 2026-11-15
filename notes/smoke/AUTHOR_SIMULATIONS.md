# PSI-115 作者模擬資料集合

本集合另列作者計算，不併入 SAME／SAME-R 的量測試次數。Gravity／EarthGravity 檔名也是模擬條件，不能當成地球實驗。

- id: PSI-115-author-PSD-snapshots
- title: PSI-115 archived author particle-node distribution snapshots
- study_id: PSI-115
- evidence_role: source_calculation
- independent_experimental_validation_count: 0
- model_ids: ["SMK-E115-COUPLED"]
- source_report: {"doc_id": "SMOKE-487108f951ba", "title": "Utilization of the SAME Data for Advanced Modeling and Simulation of Smoke Generation in Microgravity", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\03_其他文件\\研究報告與書章\\第一批下載\\PSI-115_research\\Reports\\PSI-115_Reports_NNX17AF08A_FinalReport.pdf", "sha256": "487108f951ba8ec9042464ae7c70a8190fa63c4b1141f8b1dfe19d697bd9752c", "edition": "Final August15,2020;25 physicalPDF pages", "locators": ["physical p7 Eq23 particle-node sums", "physical p9 node grid", "physical p10 reported effective state at7s", "physical p21 Table3; modified-case Table4 physicalp25"], "officialURLs": ["https://psi.nasa.gov/physci/repo/data/investigations/PSI-115", "https://doi.org/10.60555/q0v5-1v28"], "evidence_role": "source_calculation"}

## 各組作者快照

| 快照 | 證據角色 | 來源 SHA256 | 節點與單體 |
| --- | --- | --- | --- |
| [10 cm/s Earth-gravity-labelled author simulation](<simulations/psi-115-sim-10cmgravitypsd.md>) | source_calculation | f67f2ff614eff26a3b0e75db967820b55727c889d0d063d05ac289f16af8f0a2 | {"particle_nodes": {"first": 2, "last": 45, "count": 44, "basis": "Existing author-report Eq23 audit"}, "monomer_node_1": {"node": 1, "present": false, "value": null, "source_decimal_token": null, "included_in_points": false, "unit": "source ordinate (unit unspecified)"}} |
| [8 cm/s microgravity-labelled author simulation without thermophoresis](<simulations/psi-115-sim-8cmnogravitynotf-psd.md>) | source_calculation | 2fcee7dc9098fa0a700bfe4f73c7267b9dcd1b25744e846e54391c6faef2fcde | {"particle_nodes": {"first": 2, "last": 45, "count": 44, "basis": "Existing author-report Eq23 audit"}, "monomer_node_1": {"node": 1, "present": true, "value": 5.135307512096175e+20, "source_decimal_token": "5.13530751209617490E+020", "included_in_points": false, "unit": "source ordinate (unit unspecified)"}} |
| [10 cm/s microgravity-labelled author simulation](<simulations/psi-115-sim-10cmnogravitypsd.md>) | source_calculation | 32f39f6a51baef37f2e5c770965e17037647aae72f77133e0b227bb4709ecdf1 | {"particle_nodes": {"first": 2, "last": 45, "count": 44, "basis": "Existing author-report Eq23 audit"}, "monomer_node_1": {"node": 1, "present": false, "value": null, "source_decimal_token": null, "included_in_points": false, "unit": "source ordinate (unit unspecified)"}} |
| [8 cm/s Earth-gravity-labelled author simulation](<simulations/psi-115-sim-8cmgravitypsd.md>) | source_calculation | ef90fed1159c851566687c892d889d0b845d96b2b206fbcdf31199d5e9082f5a | {"particle_nodes": {"first": 2, "last": 45, "count": 44, "basis": "Existing author-report Eq23 audit"}, "monomer_node_1": {"node": 1, "present": false, "value": null, "source_decimal_token": null, "included_in_points": false, "unit": "source ordinate (unit unspecified)"}} |
| [8 cm/s Earth-gravity-labelled author simulation without settling](<simulations/psi-115-sim-8cmgravityns-psd.md>) | source_calculation | 9bdaac8bbd2d663f8db0f78fed4cbb290e0b6d2a3e4fa3fb8818a9f75bdacee1 | {"particle_nodes": {"first": 2, "last": 45, "count": 44, "basis": "Existing author-report Eq23 audit"}, "monomer_node_1": {"node": 1, "present": true, "value": 5.057837365741776e+20, "source_decimal_token": "5.05783736574177575E+020", "included_in_points": false, "unit": "source ordinate (unit unspecified)"}} |
| [8 cm/s microgravity-labelled author simulation](<simulations/psi-115-sim-8cmnogravitypsd.md>) | source_calculation | 80a3e6a37912d474c38ee3d49ea8af58dd8da31fc809470e202c7a396a2588d2 | {"particle_nodes": {"first": 2, "last": 45, "count": 44, "basis": "Existing author-report Eq23 audit"}, "monomer_node_1": {"node": 1, "present": false, "value": null, "source_decimal_token": null, "included_in_points": false, "unit": "source ordinate (unit unspecified)"}} |

## 跨案例比較與消防研究意義

- 這些既有曲線可檢視不同流速、重力標籤和省略過程的作者計算差異；其他參數與運算邊界未完整閉合，不將差異全部歸因於單一物理過程。
- 粒子節點及未標單位的縱軸保留來源值；沒有絕對濃度、偵測器響應或警報校正，不能轉成漏報率或安全界限。
- 可作為後續採樣位置、輸送與氣膠演化的研究假說，仍需配對實測與完整模型輸入驗證。

- all_requested_case_results_parsed: True
- all_fresh_SHA_match_previous_audit: True
- node_ordinals_exactly_2_through_45: True
- monomer_not_zero_filled: True
- all_ordinates_finite: True
- units_not_invented: True
- no_new_model_runs: True
- no_old_output_modifications: True
