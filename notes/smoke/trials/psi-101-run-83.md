# PSI-101-run-83 煙霧資料與研究判讀

本卡的單位是來源身份分組的一個試次。新鮮／老化分率、重複排序視圖及感測器時間樣本不自動算成新的火災。

## 身份與資料範圍

| 研究 | 來源身份 | 材料標籤 | 日期原值 | 摘要觀測列數 | 可連結檔案數 |
| --- | --- | --- | --- | --- | --- |
| PSI-101 | canonical_summary_group_not_independent_execution_count | \[{"raw": "Teflon", "canonical_family": "Teflon", "source_locator": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "B64"}}\] | \[{"date_value": 40416, "date_cell": "I64", "gmt_value": 239, "gmt_cell": "H64", "source_sheet": "SAME R Results", "date_encoding": "Excel serial when numeric; date-year comes from source style/context, not imputed from GMT"}, {"date_value": 40417, "date_cell": "I65", "gmt_value": 239, "gmt_cell": "H65", "source_sheet": "SAME R Results", "date_encoding": "Excel serial when numeric; date-year comes from source style/context, not imputed from GMT"}\] | 2 | 4 |

- {"type": "fraction_date_difference", "source_date_values": [40416, 40417], "resolution": "Source dates retained per fraction; not silently merged or interpreted as separate smoke generations."}


其中 2 個檔案連結只屬檔名候選。未核對檔案內部身份／日期者，不當成已確認的本試次原始量測；下方來源表保留 method 與 status。

## 文獻研究結果與本試次的關係

精確對上本試次摘要身份的已核對文獻數：0。這是出版表格與目前摘要資料的對照，不代表原始感測器／TEM影像也已對上。下表其餘項目是同研究的背景或方法脈絡，不能據此宣稱作者使用了本試次所有列。

| 文獻／展示資料 | 類型／審閱狀態 | 使用範圍與精確試次連結 |
| --- | --- | --- |
| [60089MFHA415 Ignitor Wire Coil Assembly (for 0 .250 OD samples)](<../literature/smoke-3a00d49f4c76.md>) | engineering_or_operations_document; identity_and_container_only_no_scientific_conclusions_inferred | {"study_ids": \["PSI-101"\], "binding_level": "campaign_context_not_trial_join", "exact_trial_ids": \[\], "exact_trial_binding_status": "unknown", "known_context": "Source conditions and named experiment family where reviewed; no blanket row-to-document join."} |
| [60089MFHA417-B Kapton Sample Assembly](<../literature/smoke-c2623fa3831d.md>) | engineering_or_operations_document; identity_and_container_only_no_scientific_conclusions_inferred | {"study_ids": \["PSI-101"\], "binding_level": "campaign_context_not_trial_join", "exact_trial_ids": \[\], "exact_trial_binding_status": "unknown", "known_context": "Source conditions and named experiment family where reviewed; no blanket row-to-document join."} |
| [60089MFHD413 Teflon Sample Part](<../literature/smoke-aabcd516772d.md>) | engineering_or_operations_document; identity_and_container_only_no_scientific_conclusions_inferred | {"study_ids": \["PSI-101"\], "binding_level": "campaign_context_not_trial_join", "exact_trial_ids": \[\], "exact_trial_binding_status": "unknown", "known_context": "Source conditions and named experiment family where reviewed; no blanket row-to-document join."} |
| [60089MFHA416-A Silicone Sample Assembly](<../literature/smoke-b7361a83d3ac.md>) | engineering_or_operations_document; identity_and_container_only_no_scientific_conclusions_inferred | {"study_ids": \["PSI-101"\], "binding_level": "campaign_context_not_trial_join", "exact_trial_ids": \[\], "exact_trial_binding_status": "unknown", "known_context": "Source conditions and named experiment family where reviewed; no blanket row-to-document join."} |
| [60089MFHA414-A Lampwick Sample Assembly](<../literature/smoke-996b31e7126a.md>) | engineering_or_operations_document; identity_and_container_only_no_scientific_conclusions_inferred | {"study_ids": \["PSI-101"\], "binding_level": "campaign_context_not_trial_join", "exact_trial_ids": \[\], "exact_trial_binding_status": "unknown", "known_context": "Source conditions and named experiment family where reviewed; no blanket row-to-document join."} |
| [S1171MFHA401 Pyrell Sample Assembly](<../literature/smoke-bdf16837754f.md>) | engineering_or_operations_document; identity_and_container_only_no_scientific_conclusions_inferred | {"study_ids": \["PSI-101"\], "binding_level": "campaign_context_not_trial_join", "exact_trial_ids": \[\], "exact_trial_binding_status": "unknown", "known_context": "Source conditions and named experiment family where reviewed; no blanket row-to-document join."} |
| [60089MFHA410-A Teflon Sample Assembly](<../literature/smoke-db190ce58655.md>) | engineering_or_operations_document; identity_and_container_only_no_scientific_conclusions_inferred | {"study_ids": \["PSI-101"\], "binding_level": "campaign_context_not_trial_join", "exact_trial_ids": \[\], "exact_trial_binding_status": "unknown", "known_context": "Source conditions and named experiment family where reviewed; no blanket row-to-document join."} |
| [60089MFHA419 Silicone Ignitor Wire Coil Assembly](<../literature/smoke-3245d0e4917e.md>) | engineering_or_operations_document; identity_and_container_only_no_scientific_conclusions_inferred | {"study_ids": \["PSI-101"\], "binding_level": "campaign_context_not_trial_join", "exact_trial_ids": \[\], "exact_trial_binding_status": "unknown", "known_context": "Source conditions and named experiment family where reviewed; no blanket row-to-document join."} |
| [60089MFHD509 P-Trak Condenser Tube Modification](<../literature/smoke-ff80b858803f.md>) | engineering_or_operations_document; identity_and_container_only_no_scientific_conclusions_inferred | {"study_ids": \["PSI-101"\], "binding_level": "campaign_context_not_trial_join", "exact_trial_ids": \[\], "exact_trial_binding_status": "unknown", "known_context": "Source conditions and named experiment family where reviewed; no blanket row-to-document join."} |
| [60089MFHA432-A Kapton Ignitor Wire Coil Assembly](<../literature/smoke-5a079a55014d.md>) | engineering_or_operations_document; identity_and_container_only_no_scientific_conclusions_inferred | {"study_ids": \["PSI-101"\], "binding_level": "campaign_context_not_trial_join", "exact_trial_ids": \[\], "exact_trial_binding_status": "unknown", "known_context": "Source conditions and named experiment family where reviewed; no blanket row-to-document join."} |
| [60089MFHA411 Teflon Ignitor Wire Coil Assembly](<../literature/smoke-edfa693a5e48.md>) | engineering_or_operations_document; identity_and_container_only_no_scientific_conclusions_inferred | {"study_ids": \["PSI-101"\], "binding_level": "campaign_context_not_trial_join", "exact_trial_ids": \[\], "exact_trial_binding_status": "unknown", "known_context": "Source conditions and named experiment family where reviewed; no blanket row-to-document join."} |
| [Drawing_SAME Aging Chamber](<../literature/smoke-3968aeb41d3a.md>) | engineering_or_operations_document; identity_and_container_only_no_scientific_conclusions_inferred | {"study_ids": \["PSI-101"\], "binding_level": "campaign_context_not_trial_join", "exact_trial_ids": \[\], "exact_trial_binding_status": "unknown", "known_context": "Source conditions and named experiment family where reviewed; no blanket row-to-document join."} |
| [60089MFHD126-B Smoke Generation Tube](<../literature/smoke-63aefebcfec2.md>) | engineering_or_operations_document; identity_and_container_only_no_scientific_conclusions_inferred | {"study_ids": \["PSI-101"\], "binding_level": "campaign_context_not_trial_join", "exact_trial_ids": \[\], "exact_trial_binding_status": "unknown", "known_context": "Source conditions and named experiment family where reviewed; no blanket row-to-document join."} |
| [SAME-DOC-001 Rev. A: Baseline Concept Description Document](<../literature/smoke-3eed4b7ecd71.md>) | Engineering concept and planned experiment/design document; prior_primary_audit_reused_source_bytes_reverified | {"study_ids": \["PSI-101", "PSI-102"\], "binding_level": "campaign_context_not_trial_join", "exact_trial_ids": \[\], "exact_trial_binding_status": "unknown", "known_context": "Source conditions and named experiment family where reviewed; no blanket row-to-document join."} |
| [60089MFHP000-C SAME Fluids System Schematic](<../literature/smoke-bf9cb1366821.md>) | engineering_or_operations_document; identity_and_container_only_no_scientific_conclusions_inferred | {"study_ids": \["PSI-101"\], "binding_level": "campaign_context_not_trial_join", "exact_trial_ids": \[\], "exact_trial_binding_status": "unknown", "known_context": "Source conditions and named experiment family where reviewed; no blanket row-to-document join."} |
| [PSI-102_Reference Data_SAME_Software Description Document](<../literature/smoke-e6b4b119f7ad.md>) | engineering_requirements_or_software_operations; identity_and_container_only_no_scientific_conclusions_inferred | {"study_ids": \["PSI-101", "PSI-102"\], "binding_level": "campaign_context_not_trial_join", "exact_trial_ids": \[\], "exact_trial_binding_status": "unknown", "known_context": "Source conditions and named experiment family where reviewed; no blanket row-to-document join."} |
| [80089MFHP000-E SAME Fluids System Schematic](<../literature/smoke-4db42228ca36.md>) | engineering_or_operations_document; identity_and_container_only_no_scientific_conclusions_inferred | {"study_ids": \["PSI-101"\], "binding_level": "campaign_context_not_trial_join", "exact_trial_ids": \[\], "exact_trial_binding_status": "unknown", "known_context": "Source conditions and named experiment family where reviewed; no blanket row-to-document join."} |
| [60089MFHA150-B Aging Chamber Assembly](<../literature/smoke-fe2d380bd432.md>) | engineering_or_operations_document; identity_and_container_only_no_scientific_conclusions_inferred | {"study_ids": \["PSI-101"\], "binding_level": "campaign_context_not_trial_join", "exact_trial_ids": \[\], "exact_trial_binding_status": "unknown", "known_context": "Source conditions and named experiment family where reviewed; no blanket row-to-document join."} |
| [PSI-101_Reference Data_SAME_Software Requirement Document_004 Rev D](<../literature/smoke-ea41d0a9db34.md>) | engineering_requirements_or_software_operations; identity_and_container_only_no_scientific_conclusions_inferred | {"study_ids": \["PSI-101", "PSI-102"\], "binding_level": "campaign_context_not_trial_join", "exact_trial_ids": \[\], "exact_trial_binding_status": "unknown", "known_context": "Source conditions and named experiment family where reviewed; no blanket row-to-document join."} |
| [Smoke Aerosol Measurement Experiment (SAME): Operations Manual](<../literature/smoke-ac00e24b0f9a.md>) | Hardware/software operations and troubleshooting manual; prior_primary_audit_reused_source_bytes_reverified | {"study_ids": \["PSI-101", "PSI-102"\], "binding_level": "campaign_context_not_trial_join", "exact_trial_ids": \[\], "exact_trial_binding_status": "unknown", "known_context": "Source conditions and named experiment family where reviewed; no blanket row-to-document join."} |
| [Fluids Control Unit, Schematic, left side-1](<../literature/smoke-71fc3a90db8c.md>) | engineering_or_operations_document; identity_and_container_only_no_scientific_conclusions_inferred | {"study_ids": \["PSI-101"\], "binding_level": "campaign_context_not_trial_join", "exact_trial_ids": \[\], "exact_trial_binding_status": "unknown", "known_context": "Source conditions and named experiment family where reviewed; no blanket row-to-document join."} |
| [80089MFHP000-E SAME Fluids System Schematic, right side-1](<../literature/smoke-f0bcddc0e733.md>) | engineering_or_operations_document; identity_and_container_only_no_scientific_conclusions_inferred | {"study_ids": \["PSI-101"\], "binding_level": "campaign_context_not_trial_join", "exact_trial_ids": \[\], "exact_trial_binding_status": "unknown", "known_context": "Source conditions and named experiment family where reviewed; no blanket row-to-document join."} |
| [SAME_Wire_Report](<../literature/smoke-78784625aaff.md>) | engineering_or_operations_document; identity_and_container_only_no_scientific_conclusions_inferred | {"study_ids": \["PSI-101", "PSI-102"\], "binding_level": "campaign_context_not_trial_join", "exact_trial_ids": \[\], "exact_trial_binding_status": "unknown", "known_context": "Source conditions and named experiment family where reviewed; no blanket row-to-document join."} |
| [Smoke Aerosol Measurement Experiment Re-flight (SAMER)](<../literature/smoke-65381e2715eb.md>) | Final experimental research report with engineering calculations, appendices and a reproduced2012conference manuscript; prior_primary_audit_reused_source_bytes_reverified | {"study_ids": \["PSI-101"\], "binding_level": "campaign_context_not_trial_join", "exact_trial_ids": \[\], "exact_trial_binding_status": "unknown", "known_context": "Source conditions and named experiment family where reviewed; no blanket row-to-document join."} |
| [SAME_EIRD](<../literature/smoke-941dca3ccf71.md>) | engineering_or_operations_document; identity_and_container_only_no_scientific_conclusions_inferred | {"study_ids": \["PSI-101", "PSI-102"\], "binding_level": "campaign_context_not_trial_join", "exact_trial_ids": \[\], "exact_trial_binding_status": "unknown", "known_context": "Source conditions and named experiment family where reviewed; no blanket row-to-document join."} |
| [Smoke Aerosol Measurement Experiment-2: Comparison of Flight Experiment Results with Ground Test Results](<../literature/smoke-0e8480e701f4.md>) | Research conference slide deck, with measured ground/flight comparison and separate simulation illustrations; prior_primary_audit_reused_source_bytes_reverified | {"study_ids": \["PSI-101", "PSI-102"\], "binding_level": "campaign_context_not_trial_join", "exact_trial_ids": \[\], "exact_trial_binding_status": "unknown", "known_context": "Source conditions and named experiment family where reviewed; no blanket row-to-document join."} |
| [Measurement of Smoke Particle Size under Low-Gravity Conditions](<../literature/smoke-95325b626e6a.md>) | Legacy PowerPoint research deck presenting preliminary SAME-1results and engineering context; prior_primary_audit_reused_source_bytes_reverified | {"study_ids": \["PSI-101", "PSI-102"\], "binding_level": "campaign_context_not_trial_join", "exact_trial_ids": \[\], "exact_trial_binding_status": "unknown", "known_context": "Source conditions and named experiment family where reviewed; no blanket row-to-document join."} |
| [Detection of Smoke from Microgravity Fires](<../literature/smoke-ace2a1841b1a.md>) | research conference presentation with experimental charts/tables and model explanation; not rawimagealbum; prior_primary_audit_reused_source_bytes_reverified | {"study_ids": \["PSI-101", "PSI-102", "PSI-47"\], "binding_level": "campaign_context_not_trial_join", "exact_trial_ids": \[\], "exact_trial_binding_status": "unknown", "known_context": "Source conditions and named experiment family where reviewed; no blanket row-to-document join."} |
| [Particle Morphology and Size Results from the Smoke Aerosol Measurement Experiment-2](<../literature/smoke-6e2800c0985e.md>) | Research conference slide deck with flight measurements, historical theoretical aging comparisons and future work; prior_primary_audit_reused_source_bytes_reverified | {"study_ids": \["PSI-101", "PSI-102"\], "binding_level": "campaign_context_not_trial_join", "exact_trial_ids": \[\], "exact_trial_binding_status": "unknown", "known_context": "Source conditions and named experiment family where reviewed; no blanket row-to-document join."} |
| [Particle Morphology and Size Results from the Smoke Aerosol Measurement Experiment-2](<../literature/smoke-bdc5e7e0d65f.md>) | conference_paper; fulltext_available_targeted_methods_results_conclusions_reviewed | {"study_ids": \["PSI-102", "PSI-101"\], "binding_level": "campaign_context_not_trial_join", "exact_trial_ids": \[\], "exact_trial_binding_status": "unknown", "known_context": "Source conditions and named experiment family where reviewed; no blanket row-to-document join."} |
| [“SMOKE:” Characterization of Smoke Particulate for Spacecraft Fire Detection](<../literature/smoke-36c89dea3ec8.md>) | primary laboratory experimental article; prior_primary_audit_reused_source_bytes_reverified | {"study_ids": \["PSI-101", "PSI-102"\], "binding_level": "campaign_context_not_trial_join", "exact_trial_ids": \[\], "exact_trial_binding_status": "unknown", "known_context": "Source conditions and named experiment family where reviewed; no blanket row-to-document join."} |
| [Evaluation of Low-Gravity Smoke Particulate for Spacecraft Fire Detection](<../literature/smoke-0685a722f6da.md>) | research_presentation; fulltext_available_targeted_methods_results_conclusions_reviewed | {"study_ids": \["PSI-102", "PSI-101"\], "binding_level": "campaign_context_not_trial_join", "exact_trial_ids": \[\], "exact_trial_binding_status": "unknown", "known_context": "Source conditions and named experiment family where reviewed; no blanket row-to-document join."} |
| [Sample descriptions tables](<../literature/smoke-715cd2c45607.md>) | data_companion_material_table_or_note; identity_and_container_only_no_scientific_conclusions_inferred | {"study_ids": \["PSI-101"\], "binding_level": "campaign_context_not_trial_join", "exact_trial_ids": \[\], "exact_trial_binding_status": "unknown", "known_context": "Source conditions and named experiment family where reviewed; no blanket row-to-document join."} |
| [ISS Coagulation](<../literature/smoke-9fb2a74c848d.md>) | data_companion_material_table_or_note; identity_and_container_only_no_scientific_conclusions_inferred | {"study_ids": \["PSI-101"\], "binding_level": "campaign_context_not_trial_join", "exact_trial_ids": \[\], "exact_trial_binding_status": "unknown", "known_context": "Source conditions and named experiment family where reviewed; no blanket row-to-document join."} |
| [SAME: Verification Plan and Engineering Requirements Document (VPERD)](<../literature/smoke-72a7264cc600.md>) | engineering_requirements_or_software_operations; identity_and_container_only_no_scientific_conclusions_inferred | {"study_ids": \["PSI-101"\], "binding_level": "campaign_context_not_trial_join", "exact_trial_ids": \[\], "exact_trial_binding_status": "unknown", "known_context": "Source conditions and named experiment family where reviewed; no blanket row-to-document join."} |
| [Evaluation of Low-Gravity Smoke Particulate for Spacecraft Fire Detection](<../literature/smoke-6250b4549563.md>) | conference_paper; fulltext_available_targeted_methods_results_conclusions_reviewed | {"study_ids": \["PSI-102", "PSI-101"\], "binding_level": "campaign_context_not_trial_join", "exact_trial_ids": \[\], "exact_trial_binding_status": "unknown", "known_context": "Source conditions and named experiment family where reviewed; no blanket row-to-document join."} |
| [Evaluation of Spacecraft Smoke Detector Performance in the Low-Gravity Environment](<../literature/smoke-87e219e20754.md>) | journal_author_manuscript; fulltext_available_targeted_methods_results_conclusions_reviewed | {"study_ids": \["PSI-102", "PSI-101"\], "binding_level": "selected_canonical_summary_rows_verified_raw_sensor_and_TEM_files_unknown", "exact_trial_ids": \["PSI-101-run-54", "PSI-101-run-55", "PSI-101-run-62", "PSI-101-run-63", "PSI-101-run-64", "PSI-101-run-94"\], "exact_trial_binding_status": "unknown", "known_context": "Source conditions and named experiment family where reviewed; no blanket row-to-document join.", "reported_test_labels": \["Table1:54,55,94,62,63,64;exact rawsensor-file joins not established"\], "selected_record_ids": \["PSI-101-run-54-row-11", "PSI-101-run-55-row-13", "PSI-101-run-94-row-84", "PSI-101-run-62-row-25", "PSI-101-run-62-row-26", "PSI-101-run-63-row-27", "PSI-101-run-63-row-28", "PSI-101-run-64-row-29", "PSI-101-run-64-row-30"\], "raw_sensor_join": "unknown", "raw_TEM_image_join": "unknown"} |
| [Smoke Characterization and Feasibility of the Moment Method for Spacecraft Fire Detection](<../literature/smoke-38e8cf0ab5b7.md>) | journal_article; fulltext_available_targeted_methods_results_conclusions_reviewed | {"study_ids": \["PSI-102", "PSI-101"\], "binding_level": "campaign_context_not_trial_join", "exact_trial_ids": \[\], "exact_trial_binding_status": "unknown", "known_context": "Source conditions and named experiment family where reviewed; no blanket row-to-document join."} |
| [Response of Smoke Detectors to Monodisperse Aerosols](<../literature/smoke-b41d8cfef139.md>) | primary laboratory experimental article; prior_primary_audit_reused_source_bytes_reverified | {"study_ids": \["PSI-101", "PSI-102", "PSI-47"\], "binding_level": "campaign_context_not_trial_join", "exact_trial_ids": \[\], "exact_trial_binding_status": "unknown", "known_context": "Source conditions and named experiment family where reviewed; no blanket row-to-document join."} |


### 本試次的已核對出版表格資料

來源尚未提供可核對的項目；不填成 0。


[開啟矩公式與TEM實驗方法對照](<../viewer/viewer.html?trial=PSI-101-run-83&view=methods>)。TEM是獨立的量測技術，但這裡使用相同飛行樣本；校正／密度／選模的保留樣本獨立性未證實，不能稱為獨立預測驗證。完整血緣及印列差異見 [PUBLICATION_DATA_BINDINGS.md](../PUBLICATION_DATA_BINDINGS.md)。

## 使用的資料部分與參數因子

下列快取值依原欄位保留。來源計算量、量測輸入、設定與狀態旗標分列；來源公式未被修正或重新擬合。

| 來源記錄 | 欄位／因子 | 原始值或快取 | 單位 | 儲存格／來源定位 | 量的角色 |
| --- | --- | --- | --- | --- | --- |
| PSI-101-run-83-row-64 | Carousel | 4 | Unknown（來源未提供／尚未核對） | A64 | source_reported_value |
| PSI-101-run-83-row-64 | Sample Type | Teflon | Unknown（來源未提供／尚未核對） | B64 | source_reported_value |
| PSI-101-run-83-row-64 | Sample ID | T05 | Unknown（來源未提供／尚未核對） | C64 | source_reported_value |
| PSI-101-run-83-row-64 | Test ID Number | 36 T | Unknown（來源未提供／尚未核對） | D64 | source_reported_value |
| PSI-101-run-83-row-64 | Position in Carousel | 5 | Unknown（來源未提供／尚未核對） | E64 | source_reported_value |
| PSI-101-run-83-row-64 | SAME # | 83 | Unknown（來源未提供／尚未核對） | F64 | source_reported_value |
| PSI-101-run-83-row-64 | Description | Mid temp aging | Unknown（來源未提供／尚未核對） | G64 | source_reported_value |
| PSI-101-run-83-row-64 | GMT | 239 | Unknown（來源未提供／尚未核對） | H64 | source_reported_value |
| PSI-101-run-83-row-64 | Date (EST) | 40416 | Unknown（來源未提供／尚未核對） | I64 | source_reported_value |
| PSI-101-run-83-row-64 | Inlet Velocity (cm/sec) | 8.1 | cm/s | K64 | source_reported_value |
| PSI-101-run-83-row-64 | Rt/R0 | 1.448 | dimensionless | L64 | source_reported_value |
| PSI-101-run-83-row-64 | Duration (sec) | 60 | s | M64 | source_reported_value |
| PSI-101-run-83-row-64 | Primary Aging Duration (sec) | 11 | s | N64 | source_reported_value |
| PSI-101-run-83-row-64 | Primary Mixing Duration (sec) | 8 | s | O64 | source_reported_value |
| PSI-101-run-83-row-64 | PreAge Thermal Precipitator | n | Unknown（來源未提供／尚未核對） | P64 | source_reported_value |
| PSI-101-run-83-row-64 | PreAge Thermal Precipitator Duration | n | Unknown（來源未提供／尚未核對） | Q64 | source_reported_value |
| PSI-101-run-83-row-64 | Net Aging  Duration | 30.333333333333332 | Unknown（來源未提供／尚未核對） | R64 | source_reported_value |
| PSI-101-run-83-row-64 | Primary Aging Therm Precip | y | Unknown（來源未提供／尚未核對） | S64 | source_reported_value |
| PSI-101-run-83-row-64 | Primary Aging Therm Precip Duration | 60 | Unknown（來源未提供／尚未核對） | T64 | source_reported_value |
| PSI-101-run-83-row-64 | Use STS Detector | n | Unknown（來源未提供／尚未核對） | U64 | source_reported_value |
| PSI-101-run-83-row-64 | Use Comm Diag A | y | Unknown（來源未提供／尚未核對） | V64 | source_reported_value |
| PSI-101-run-83-row-64 | Use Comm Diag B | y | Unknown（來源未提供／尚未核對） | W64 | source_reported_value |
| PSI-101-run-83-row-64 | Diluting A | n | Unknown（來源未提供／尚未核對） | X64 | source_reported_value |
| PSI-101-run-83-row-64 | Diluting B | n | Unknown（來源未提供／尚未核對） | Y64 | source_reported_value |
| PSI-101-run-83-row-64 | Cyclone Inlet on CDA (MPASS) | y | Unknown（來源未提供／尚未核對） | Z64 | source_reported_value |
| PSI-101-run-83-row-64 | Impactor Inlet on CDB | 10 | Unknown（來源未提供／尚未核對） | AA64 | source_reported_value |
| PSI-101-run-83-row-64 | Use P-Trak | y | Unknown（來源未提供／尚未核對） | AB64 | source_reported_value |
| PSI-101-run-83-row-64 | Aerosol Concentration To P-Trak | 0.0519567251427413 | Unknown（來源未提供／尚未核對） | AC64 | source_reported_value |
| PSI-101-run-83-row-64 | Secondary Diagnostics Volume %  | 58 | % | AE64 | source_reported_value |
| PSI-101-run-83-row-64 | Secondary Aging Duration (sec) | 480 | s | AF64 | source_reported_value |
| PSI-101-run-83-row-64 | Secondary Mixing Duration (sec) | 0 | s | AG64 | source_reported_value |
| PSI-101-run-83-row-64 | STSDetector | n | Unknown（來源未提供／尚未核對） | AH64 | source_reported_value |
| PSI-101-run-83-row-64 | Comm Diag A | y | Unknown（來源未提供／尚未核對） | AI64 | source_reported_value |
| PSI-101-run-83-row-64 | Comm Diag B | y | Unknown（來源未提供／尚未核對） | AJ64 | source_reported_value |
| PSI-101-run-83-row-64 | Diluting A | n | Unknown（來源未提供／尚未核對） | AK64 | source_reported_value |
| PSI-101-run-83-row-64 | Diluting B | n | Unknown（來源未提供／尚未核對） | AL64 | source_reported_value |
| PSI-101-run-83-row-64 | Ues PTrak | y | Unknown（來源未提供／尚未核對） | AM64 | source_reported_value |
| PSI-101-run-83-row-64 | Aerosol Concentration To P-Trak | 0.0519567251427413 | Unknown（來源未提供／尚未核對） | AN64 | source_formula_cached_result |
| PSI-101-run-83-row-64 | ISS Detector Scatter (volts) | 1.7692875000000003 | V | AR64 | source_reported_value |
| PSI-101-run-83-row-64 | STS Detector (volts) | 0 | V | AS64 | source_reported_value |
| PSI-101-run-83-row-64 | STS Detector offset (volts) | 0 | V | AT64 | source_reported_value |
| PSI-101-run-83-row-64 | Ion A (volts) Mpass_3rd | 0.20867914999999998 | V | AU64 | source_reported_value |
| PSI-101-run-83-row-64 | Ion A offset V0 (volts) | 0.026794425 | V | AV64 | source_reported_value |
| PSI-101-run-83-row-64 | Ion B (volts) | 6.8408975 | V | AW64 | source_reported_value |
| PSI-101-run-83-row-64 | Ion B offset V0 (volts) | 4.730316499999999 | V | AX64 | source_reported_value |
| PSI-101-run-83-row-64 | Ptrak (PT/cc) | 107645 | #/cm^3 | AY64 | source_reported_value |
| PSI-101-run-83-row-64 | DustTrak A (mg/m3) Mpass_2nd | 0.2772216 | mg/m^3 | AZ64 | source_reported_value |
| PSI-101-run-83-row-64 | DustTrak A (mg/m3) Mpass_2nd offset | 0.078613275 | mg/m^3 | BA64 | source_reported_value |
| PSI-101-run-83-row-64 | DustTrak B (mg/m3) | 17.034399999999994 | mg/m^3 | BB64 | source_reported_value |
| PSI-101-run-83-row-64 | Ion B Delta (volts) | 2.1105810000000007 | V | BC64 | source_formula_cached_result |
| PSI-101-run-83-row-64 | M0 best Diameter (#/cm3) | 3535853.9755014894 | #/cm^3 | BD64 | source_formula_cached_result |
| PSI-101-run-83-row-64 | M1 (mm/cm3) | 494.67025905930427 | mm/cm^3 | BE64 | source_formula_cached_result |
| PSI-101-run-83-row-64 |  Mpass_3rd offset and dilution corrected | 0.18188472499999997 | Unknown（來源未提供／尚未核對） | BF64 | source_formula_cached_result |
| PSI-101-run-83-row-64 | DustTrak A (mg/m3) Mpass_2nd  offset, dilution and Gain corrected | 0.04965208125000001 | mg/m^3 | BG64 | source_formula_cached_result |
| PSI-101-run-83-row-64 | DustTrak B calibratred and corrected for dilution (mg/m3) | 38.49774399999998 | mg/m^3 | BH64 | source_formula_cached_result |
| PSI-101-run-83-row-64 | M1/M0 (micro-m)--AMD | 0.1399012126877059 | um | BI64 | source_formula_cached_result |
| PSI-101-run-83-row-64 | Diameter of Average mass (micro-m) | 0.2114332174563457 | um | BJ64 | source_formula_cached_result |
| PSI-101-run-83-row-64 | George's d2,1,  (micro-m) | 0.25992561994041297 | um | BK64 | source_formula_cached_result |
| PSI-101-run-83-row-64 | MPASS 3/2 | 3.663184310123958 | Unknown（來源未提供／尚未核對） | BL64 | source_formula_cached_result |
| PSI-101-run-83-row-64 | Hatch Choate Sigma g | 1.9014741902301655 | dimensionless | BM64 | source_formula_cached_result |
| PSI-101-run-83-row-64 | Hatch Choate Dg | 0.11380087707932458 | Unknown（來源未提供／尚未核對） | BN64 | source_formula_cached_result |
| PSI-101-run-83-row-64 | CPC 100 nm cal, dilution corrected | 3535853.9755014894 | Unknown（來源未提供／尚未核對） | BO64 | source_formula_cached_result |
| PSI-101-run-83-row-64 | CPC 600 nm cal, dilution corrected | 3303545.048854555 | Unknown（來源未提供／尚未核對） | BP64 | source_formula_cached_result |
| PSI-101-run-83-row-64 | CPC 1200 nm cal, dilution corrected | 2901632.0622752355 | Unknown（來源未提供／尚未核對） | BQ64 | source_formula_cached_result |
| PSI-101-run-83-row-64 | Ion B Mment  mm/cm^3 | 494.67025905930427 | mm/cm^3 | BR64 | source_formula_cached_result |
| PSI-101-run-83-row-64 | Ion B X | 0.4684766492053628 | Unknown（來源未提供／尚未核對） | BS64 | source_formula_cached_result |
| PSI-101-run-83-row-64 | Dust Trak Cal Factor (Teom/Dusttrak) | 2.26 | Unknown（來源未提供／尚未核對） | BT64 | source_formula_cached_result |
| PSI-101-run-83-row-64 | MPASS Dilution factor | 1 | Unknown（來源未提供／尚未核對） | BU64 | source_formula_cached_result |
| PSI-101-run-83-row-64 | Dust Trak Dilution factor | 1 | Unknown（來源未提供／尚未核對） | BV64 | source_formula_cached_result |
| PSI-101-run-83-row-64 | Particle density g/cc | 2.2 | g/cm^3 | BW64 | source_formula_cached_result |
| PSI-101-run-83-row-64 | T ( C) - Eq. 2 of lrt | 532.3635398253948 | Unknown（來源未提供／尚未核對） | BZ64 | source_reported_value |
| PSI-101-run-83-row-64 | Mass Loss (mg) | 8.070000000000022 | mg | CA64 | source_reported_value |
| PSI-101-run-83-row-64 | Test Number |  36T | Unknown（來源未提供／尚未核對） | CB64 | source_reported_value |
| PSI-101-run-83-row-64 | GMT | 239 | Unknown（來源未提供／尚未核對） | CC64 | source_reported_value |
| PSI-101-run-83-row-64 | Yeild: Dust Trak mass/mass lostt | 0.028622857992564966 | Unknown（來源未提供／尚未核對） | CD64 | source_formula_cached_result |
| PSI-101-run-83-row-64 | run | 64 | Unknown（來源未提供／尚未核對） | CI64 | source_reported_value |
| PSI-101-run-83-row-64 | material | Teflon | Unknown（來源未提供／尚未核對） | CJ64 | source_reported_value |
| PSI-101-run-83-row-64 | AMD | 0.1399012126877059 | Unknown（來源未提供／尚未核對） | CK64 | source_reported_value |
| PSI-101-run-83-row-64 | mass1 caculated with dector 3 | 0.004724555418104501 | Unknown（來源未提供／尚未核對） | CL64 | source_reported_value |
| PSI-101-run-83-row-64 | mass2 both detectors | 0.01921082948521523 | Unknown（來源未提供／尚未核對） | CM64 | source_reported_value |
| PSI-101-run-83-row-64 | Unknown（來源未提供／尚未核對） | 0.8715998939041106 | Unknown（來源未提供／尚未核對） | CO64 | source_formula_cached_result |
| PSI-101-run-83-row-65 | Carousel | 4 | Unknown（來源未提供／尚未核對） | A65 | source_reported_value |
| PSI-101-run-83-row-65 | Sample Type | Teflon | Unknown（來源未提供／尚未核對） | B65 | source_reported_value |
| PSI-101-run-83-row-65 | Sample ID | T05 | Unknown（來源未提供／尚未核對） | C65 | source_reported_value |
| PSI-101-run-83-row-65 | Test ID Number | 36TA | Unknown（來源未提供／尚未核對） | D65 | source_reported_value |
| PSI-101-run-83-row-65 | Position in Carousel | 5 | Unknown（來源未提供／尚未核對） | E65 | source_reported_value |
| PSI-101-run-83-row-65 | SAME # | 83a | Unknown（來源未提供／尚未核對） | F65 | source_reported_value |
| PSI-101-run-83-row-65 | Description | aged | Unknown（來源未提供／尚未核對） | G65 | source_reported_value |
| PSI-101-run-83-row-65 | GMT | 239 | Unknown（來源未提供／尚未核對） | H65 | source_reported_value |
| PSI-101-run-83-row-65 | Date (EST) | 40417 | Unknown（來源未提供／尚未核對） | I65 | source_reported_value |
| PSI-101-run-83-row-65 | Inlet Velocity (cm/sec) | 8.1 | cm/s | K65 | source_reported_value |
| PSI-101-run-83-row-65 | Rt/R0 | 1.448 | dimensionless | L65 | source_reported_value |
| PSI-101-run-83-row-65 | Net Aging  Duration | 557.3333333333334 | Unknown（來源未提供／尚未核對） | R65 | source_reported_value |
| PSI-101-run-83-row-65 | Use STS Detector | n | Unknown（來源未提供／尚未核對） | U65 | source_reported_value |
| PSI-101-run-83-row-65 | Use Comm Diag A | y | Unknown（來源未提供／尚未核對） | V65 | source_reported_value |
| PSI-101-run-83-row-65 | Use Comm Diag B | y | Unknown（來源未提供／尚未核對） | W65 | source_reported_value |
| PSI-101-run-83-row-65 | Diluting A | n | Unknown（來源未提供／尚未核對） | X65 | source_reported_value |
| PSI-101-run-83-row-65 | Diluting B | n | Unknown（來源未提供／尚未核對） | Y65 | source_reported_value |
| PSI-101-run-83-row-65 | Cyclone Inlet on CDA (MPASS) | y | Unknown（來源未提供／尚未核對） | Z65 | source_reported_value |
| PSI-101-run-83-row-65 | Impactor Inlet on CDB | 10 | Unknown（來源未提供／尚未核對） | AA65 | source_reported_value |
| PSI-101-run-83-row-65 | Use P-Trak | y | Unknown（來源未提供／尚未核對） | AB65 | source_reported_value |
| PSI-101-run-83-row-65 | Aerosol Concentration To P-Trak | 0.0519567251427413 | Unknown（來源未提供／尚未核對） | AC65 | source_reported_value |
| PSI-101-run-83-row-65 | secondary agign thermal precip duration | 60 | Unknown（來源未提供／尚未核對） | AP65 | source_reported_value |
| PSI-101-run-83-row-65 | ISS Detector Scatter (volts) | 1.8084105000000001 | V | AR65 | source_reported_value |
| PSI-101-run-83-row-65 | STS Detector (volts) | 0 | V | AS65 | source_reported_value |
| PSI-101-run-83-row-65 | STS Detector offset (volts) | 0 | V | AT65 | source_reported_value |
| PSI-101-run-83-row-65 | Ion A (volts) Mpass_3rd | 0.1945191 | V | AU65 | source_reported_value |
| PSI-101-run-83-row-65 | Ion A offset V0 (volts) | 0.03163147000000001 | V | AV65 | source_reported_value |
| PSI-101-run-83-row-65 | Ion B (volts) | 6.2427220000000005 | V | AW65 | source_reported_value |
| PSI-101-run-83-row-65 | Ion B offset V0 (volts) | 4.7371219999999985 | V | AX65 | source_reported_value |
| PSI-101-run-83-row-65 | Ptrak (PT/cc) | 32650 | #/cm^3 | AY65 | source_reported_value |
| PSI-101-run-83-row-65 | DustTrak A (mg/m3) Mpass_2nd | 0.2760315 | mg/m^3 | AZ65 | source_reported_value |
| PSI-101-run-83-row-65 | DustTrak A (mg/m3) Mpass_2nd offset | 0.08198546 | mg/m^3 | BA65 | source_reported_value |
| PSI-101-run-83-row-65 | DustTrak B (mg/m3) | 15.891600000000002 | mg/m^3 | BB65 | source_reported_value |
| PSI-101-run-83-row-65 | Ion B Delta (volts) | 1.505600000000002 | V | BC65 | source_formula_cached_result |
| PSI-101-run-83-row-65 | M0 best Diameter (#/cm3) | 909242.929961684 | #/cm^3 | BD65 | source_formula_cached_result |
| PSI-101-run-83-row-65 | M1 (mm/cm3) | 306.4064378465123 | mm/cm^3 | BE65 | source_formula_cached_result |
| PSI-101-run-83-row-65 |  Mpass_3rd offset and dilution corrected | 0.16288763 | Unknown（來源未提供／尚未核對） | BF65 | source_formula_cached_result |
| PSI-101-run-83-row-65 | DustTrak A (mg/m3) Mpass_2nd  offset, dilution and Gain corrected | 0.048511509999999994 | mg/m^3 | BG65 | source_formula_cached_result |
| PSI-101-run-83-row-65 | DustTrak B calibratred and corrected for dilution (mg/m3) | 35.915016 | mg/m^3 | BH65 | source_formula_cached_result |
| PSI-101-run-83-row-65 | M1/M0 (micro-m)--AMD | 0.3369907290446838 | um | BI65 | source_formula_cached_result |
| PSI-101-run-83-row-65 | Diameter of Average mass (micro-m) | 0.32488147091855835 | um | BJ65 | source_formula_cached_result |
| PSI-101-run-83-row-65 | George's d2,1,  (micro-m) | 0.3189910055290903 | um | BK65 | source_formula_cached_result |
| PSI-101-run-83-row-65 | MPASS 3/2 | 3.357710984465337 | Unknown（來源未提供／尚未核對） | BL65 | source_formula_cached_result |
| PSI-101-run-83-row-65 | Hatch Choate Sigma g | #NUM! | dimensionless | BM65 | source_formula_cached_result |
| PSI-101-run-83-row-65 | Hatch Choate Dg | #NUM! | Unknown（來源未提供／尚未核對） | BN65 | source_formula_cached_result |
| PSI-101-run-83-row-65 | CPC 100 nm cal, dilution corrected | 909242.929961684 | Unknown（來源未提供／尚未核對） | BO65 | source_formula_cached_result |
| PSI-101-run-83-row-65 | CPC 600 nm cal, dilution corrected | 894789.5555825848 | Unknown（來源未提供／尚未核對） | BP65 | source_formula_cached_result |
| PSI-101-run-83-row-65 | CPC 1200 nm cal, dilution corrected | 836756.1154125928 | Unknown（來源未提供／尚未核對） | BQ65 | source_formula_cached_result |
| PSI-101-run-83-row-65 | Ion B Mment  mm/cm^3 | 306.4064378465123 | mm/cm^3 | BR65 | source_formula_cached_result |
| PSI-101-run-83-row-65 | Ion B X | 0.3341916008168343 | Unknown（來源未提供／尚未核對） | BS65 | source_formula_cached_result |
| PSI-101-run-83-row-65 | Dust Trak Cal Factor (Teom/Dusttrak) | 2.26 | Unknown（來源未提供／尚未核對） | BT65 | source_formula_cached_result |
| PSI-101-run-83-row-65 | MPASS Dilution factor | 1 | Unknown（來源未提供／尚未核對） | BU65 | source_formula_cached_result |
| PSI-101-run-83-row-65 | Dust Trak Dilution factor | 1 | Unknown（來源未提供／尚未核對） | BV65 | source_formula_cached_result |
| PSI-101-run-83-row-65 | Particle density g/cc | 2.2 | g/cm^3 | BW65 | source_formula_cached_result |
| PSI-101-run-83-row-65 | T ( C) - Eq. 2 of lrt | 532.3635398253948 | Unknown（來源未提供／尚未核對） | BZ65 | source_reported_value |
| PSI-101-run-83-row-65 | Mass Loss (mg) | 8.070000000000022 | mg | CA65 | source_formula_cached_result |
| PSI-101-run-83-row-65 | Yeild: Dust Trak mass/mass lostt | 0.02670261412639398 | Unknown（來源未提供／尚未核對） | CD65 | source_formula_cached_result |
| PSI-101-run-83-row-65 | run | 65 | Unknown（來源未提供／尚未核對） | CI65 | source_reported_value |
| PSI-101-run-83-row-65 | material | Teflon | Unknown（來源未提供／尚未核對） | CJ65 | source_reported_value |
| PSI-101-run-83-row-65 | AMD | 0.3369907290446838 | Unknown（來源未提供／尚未核對） | CK65 | source_reported_value |
| PSI-101-run-83-row-65 | mass1 caculated with dector 3 | 0.004535362868834584 | Unknown（來源未提供／尚未核對） | CL65 | source_reported_value |
| PSI-101-run-83-row-65 | mass2 both detectors | 0.018996434874645505 | Unknown（來源未提供／尚未核對） | CM65 | source_reported_value |
| PSI-101-run-83-row-65 | Unknown（來源未提供／尚未核對） | 0.8373863029388888 | Unknown（來源未提供／尚未核對） | CO65 | source_formula_cached_result |


你提供的 Excel 對照見 [FACTOR_MAP.md](../FACTOR_MAP.md)。總表是欄位／因子索引，不能替代本試次的實測數值。無法逐欄匹配者保留 Unknown。

### 感測器狀態與執行分率

| 摘要記錄 | 分率角色 | run原值 | 感測器啟用旗標 |
| --- | --- | --- | --- |
| PSI-101-run-83-row-64 | first_or_primary_fraction | 83 | {"Use STS Detector": {"cell": "U64", "value": "n", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "132", "status": "valid", "raw_header": "Use STS Detector", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "U64"}, "evidence_role": "source_reported_value"}, "Use Comm Diag A": {"cell": "V64", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "132", "status": "valid", "raw_header": "Use Comm Diag A", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "V64"}, "evidence_role": "source_reported_value"}, "Use Comm Diag B": {"cell": "W64", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "132", "status": "valid", "raw_header": "Use Comm Diag B", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "W64"}, "evidence_role": "source_reported_value"}, "Use P-Trak": {"cell": "AB64", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "132", "status": "valid", "raw_header": "Use P-Trak", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "AB64"}, "evidence_role": "source_reported_value"}, "STSDetector": {"cell": "AH64", "value": "n", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "132", "status": "valid", "raw_header": "STSDetector", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "AH64"}, "evidence_role": "source_reported_value"}, "Comm Diag A": {"cell": "AI64", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "132", "status": "valid", "raw_header": "Comm Diag A", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "AI64"}, "evidence_role": "source_reported_value"}, "Comm Diag B": {"cell": "AJ64", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "132", "status": "valid", "raw_header": "Comm Diag B", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "AJ64"}, "evidence_role": "source_reported_value"}, "Ues PTrak": {"cell": "AM64", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "132", "status": "valid", "raw_header": "Ues PTrak", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "AM64"}, "evidence_role": "source_reported_value"}} |
| PSI-101-run-83-row-65 | aged_fraction | 83a | {"Use STS Detector": {"cell": "U65", "value": "n", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "292", "status": "valid", "raw_header": "Use STS Detector", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "U65"}, "evidence_role": "source_reported_value"}, "Use Comm Diag A": {"cell": "V65", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "2000", "status": "valid", "raw_header": "Use Comm Diag A", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "V65"}, "evidence_role": "source_reported_value"}, "Use Comm Diag B": {"cell": "W65", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "292", "status": "valid", "raw_header": "Use Comm Diag B", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "W65"}, "evidence_role": "source_reported_value"}, "Use P-Trak": {"cell": "AB65", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "292", "status": "valid", "raw_header": "Use P-Trak", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "AB65"}, "evidence_role": "source_reported_value"}} |


Unknown；此處沒有補入推測值。


## 多個結論與適用範圍

| 判讀 | 證據層次 | 共同與不同之處 |
| --- | --- | --- |
| 此身份分組含 2 筆來源摘要記錄；分率／執行身份仍以來源標籤與衝突表為準。 | 資料稽核結論 | 同 baseRun 不代表每筆都是獨立產煙事件。 |
| 可追到上表數值的欄位共有 144 項；單位未提供時不轉換、不補 0。 | 原始欄位／快取判讀 | 同名粒徑可能來自不同矩、密度與儀器量測範圍，必須先對定義。 |
| 本試次與出版品的逐列身份對應，以明列的 exact_trial_ids 為限；其他連結僅為 campaign context。 | 文獻連結邊界 | 共用研究、材料或儀器不足以認定使用同一數據。 |
| 矩反演／PSD重建若重用了原量測矩，只能視為計算診斷，不能再把它當獨立預測成功。 | 物理／識別限制 | 需要未參與反演的尺寸分布、儀器響應或另一事件才能驗證外推。 |

Unknown；此處沒有補入推測值。


## 公式結果與實驗值的視覺化工具

程式名稱：`tools/smoke_evidence/physics.py`、`tools/smoke_evidence/viewer.js`；入口 `viewer.html`。

[開啟此試次的矩與來源快取比較](<../viewer/viewer.html?trial=PSI-101-run-83&view=moments>) · [檢查時間訊號／感測器狀態](<../viewer/viewer.html?trial=PSI-101-run-83&view=traces>)

展示狀態必須區分來源計算重現、同源反演重建、條件診斷、作者模擬與獨立預測。缺單位、越域或未使用的實驗目標不足時，該比較顯示 Unknown／Invalid，而非補出曲線。詳細公式見 [MODELS.md](../MODELS.md)。

### 本試次已執行的固定公式結果

| 來源記錄 | 輸出量 | 公式值 | 來源快取 | 公式減快取 | 比較角色 | 整體資格狀態 |
| --- | --- | --- | --- | --- | --- | --- |
| PSI-101-run-83-row-64 | d_count_um | 0.1399012126877059 | 0.1399012126877059 | 0.0 | same_source_reconstruction | unknown |
| PSI-101-run-83-row-64 | dm_um | 0.21143321745634563 | 0.2114332174563457 | -5.551115123125783e-17 | same_source_reconstruction | unknown |
| PSI-101-run-83-row-65 | d_count_um | 0.3369907290446838 | 0.3369907290446838 | 0.0 | same_source_reconstruction | invalid |
| PSI-101-run-83-row-65 | dm_um | 0.32488147091855835 | 0.32488147091855835 | 0.0 | same_source_reconstruction | invalid |


上述差值僅檢查已知公式與來源快取的數值重現，不是量測誤差、消防安全誤差或獨立模型預測分數。密度／校正等來源假設與各輸出的可計算性須保留；整體資格 Unknown 不會被改成安全 Pass。

- {"record_id": "PSI-101-run-83-row-64", "equation_ids": ["SMOKE-MOMENT-RATIOS", "SMOKE-LOGNORMAL-INVERSE"], "eligible_role": "same_source_equation_diagnostic_only", "raw_inversion_validation": false, "independent_validation_target": false}
- {"record_id": "PSI-101-run-83-row-65", "equation_ids": ["SMOKE-MOMENT-RATIOS", "SMOKE-LOGNORMAL-INVERSE"], "eligible_role": "same_source_equation_diagnostic_only", "raw_inversion_validation": false, "independent_validation_target": false}


## 消防 insight 與下一驗證

- **預防**：材料標籤與熱史可用來設計過熱煙情境；不能從煙粒徑單獨判定材料不會燃燒。
- **偵測**：必須同時保存材料、流動、老化、儀器校正／量測範圍及供電。斷電的 alarm 0 不是無煙；飽和限制幅度量化，但不自動否定已啟用警報事件。
- **撲滅／抑制後監測**：煙霧與訊號可能隨輸運／老化改變；本試次不是滅火劑噴放試驗，不能給出劑量、再燃機率或安全重啟時間。

上述是依量測定義提出的研究需求。具體產品構想、地球差異與驗證缺口見 [跨資料集整合](../SMOKE_SYNTHESIS.md)，不是已核准操作程序。

### 已知與未知

- Actual independent smoke-generation count is not inferred from fraction rows.
- Ambient oxygen composition, chamber temperature and absolute pressure are not supplied by these summary headers.
- Absence of a mapped telemetry file does not establish no data exist.


## 原始來源與再現定位

| 本機原始檔 | 資料角色 | 身份連結依據與資格 | SHA256 |
| --- | --- | --- | --- |
| [PSI-101-87164b7dc9168a42](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/01_實驗資料/第一批下載/PSI-101_SAME-R/Experimental table/PSI-101_Experimental table_SAME-R.csv>) | Experimental table | method=\["experimental table SAME Test# literal identifier"\]; status=\["source_identity_confirmed"\] | 87164b7dc9168a4273c159f7a9f23699afbd06ad97b77974377e79b9bf8a3bef |
| [PSI-101-6d3a539ccf425b1f](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/01_實驗資料/第一批下載/PSI-101_SAME-R/Analyzed Data/PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx>) | Analyzed Data | method=\["canonical summary row SAME R Results!64", "canonical summary row SAME R Results!65"\]; status=\["source_identity_confirmed", "source_identity_confirmed"\] | 6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218 |
| [PSI-101-e93299abe9d5956d](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/01_實驗資料/第一批下載/PSI-101_SAME-R/Analyzed Data/PSI-101_Analyzed Data_2010_239_17_teflon_run83.xls>) | Analyzed Data | method=\["literal filename run/test token"\]; status=\["filename_candidate_not_fully_content_joined"\] | e93299abe9d5956dc1f49444f6189007d9a21cd380da60d207db40461f53d9be |
| [PSI-101-ded55f1fea4645d4](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/簡報與海報/補下載/PSI-101/Raw Data/233a6237bcfb9ac8_PSI-101_Raw Data_83 postage Teflon 36T.pptx>) | Raw Data | method=\["literal filename run/test token"\]; status=\["filename_candidate_not_fully_content_joined"\] | ded55f1fea4645d455f8e79159792ea1a9fe565f8f96199fa90fecab3b798966 |


結構化完整記錄：`qa/trial_records.json` 的 `PSI-101-run-83`。原始資料只讀；本 Markdown 不改寫來源公式、快取或身份衝突。
