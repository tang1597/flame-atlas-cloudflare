# PSI-101-run-94 煙霧資料與研究判讀

本卡的單位是來源身份分組的一個試次。新鮮／老化分率、重複排序視圖及感測器時間樣本不自動算成新的火災。

## 身份與資料範圍

| 研究 | 來源身份 | 材料標籤 | 日期原值 | 摘要觀測列數 | 可連結檔案數 |
| --- | --- | --- | --- | --- | --- |
| PSI-101 | canonical_summary_group_not_independent_execution_count | \[{"raw": "Kapton", "canonical_family": "Kapton", "source_locator": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "B83"}}\] | \[{"date_value": 40428.354166666664, "date_cell": "I83", "gmt_value": 250, "gmt_cell": "H83", "source_sheet": "SAME R Results", "date_encoding": "Excel serial when numeric; date-year comes from source style/context, not imputed from GMT"}, {"date_value": 40428.354166666664, "date_cell": "I84", "gmt_value": 250, "gmt_cell": "H84", "source_sheet": "SAME R Results", "date_encoding": "Excel serial when numeric; date-year comes from source style/context, not imputed from GMT"}\] | 2 | 6 |

目前身份分組未記錄衝突；這不代表所有外部出版品都已逐列對上。

其中 3 個檔案連結只屬檔名候選。未核對檔案內部身份／日期者，不當成已確認的本試次原始量測；下方來源表保留 method 與 status。

## 文獻研究結果與本試次的關係

精確對上本試次摘要身份的已核對文獻數：1。這是出版表格與目前摘要資料的對照，不代表原始感測器／TEM影像也已對上。下表其餘項目是同研究的背景或方法脈絡，不能據此宣稱作者使用了本試次所有列。

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

| 出版定位 | 對應摘要列 | TEM粒子數 | 矩方法尺寸／σ | TEM尺寸／σ |
| --- | --- | --- | --- | --- |
| {"physical_page": 26, "table": "1", "table_row_ordinal": 3, "printed_manuscript_page": 26, "method": "pypdf text plus visual rendering of actual Table1"} | {"trial_id": "PSI-101-run-94", "study_id": "PSI-101", "campaign": "SAME-R", "record_id": "PSI-101-run-94-row-84", "canonical_json_pointer": "/trial_records/46/observations/1", "sheet": "SAME R Results", "row": 84, "run_label_raw": "94a", "fraction_role": "aged_fraction", "sample_id": "K11", "test_id": "47KA", "source_workbook_sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218"} | 1353 | {"diameter_of_average_mass_um": 0.176, "count_mean_diameter_um": 0.136, "geometric_mean_diameter_um": 0.119, "geometric_standard_deviation": 1.67} | {"diameter_of_average_mass_um": 0.159, "count_mean_diameter_um": 0.12, "geometric_mean_diameter_um": 0.103, "geometric_standard_deviation": 1.72} |


[開啟矩公式與TEM實驗方法對照](<../viewer/viewer.html?trial=PSI-101-run-94&view=methods>)。TEM是獨立的量測技術，但這裡使用相同飛行樣本；校正／密度／選模的保留樣本獨立性未證實，不能稱為獨立預測驗證。完整血緣及印列差異見 [PUBLICATION_DATA_BINDINGS.md](../PUBLICATION_DATA_BINDINGS.md)。

## 使用的資料部分與參數因子

下列快取值依原欄位保留。來源計算量、量測輸入、設定與狀態旗標分列；來源公式未被修正或重新擬合。

| 來源記錄 | 欄位／因子 | 原始值或快取 | 單位 | 儲存格／來源定位 | 量的角色 |
| --- | --- | --- | --- | --- | --- |
| PSI-101-run-94-row-83 | Carousel | 8(4) | Unknown（來源未提供／尚未核對） | A83 | source_reported_value |
| PSI-101-run-94-row-83 | Sample Type | Kapton | Unknown（來源未提供／尚未核對） | B83 | source_reported_value |
| PSI-101-run-94-row-83 | Sample ID | K11 | Unknown（來源未提供／尚未核對） | C83 | source_reported_value |
| PSI-101-run-94-row-83 | Test ID Number | 47 K | Unknown（來源未提供／尚未核對） | D83 | source_reported_value |
| PSI-101-run-94-row-83 | SAME # | 94 | Unknown（來源未提供／尚未核對） | F83 | source_reported_value |
| PSI-101-run-94-row-83 | Description | Mid Temp aging run mid high | Unknown（來源未提供／尚未核對） | G83 | source_reported_value |
| PSI-101-run-94-row-83 | GMT | 250 | Unknown（來源未提供／尚未核對） | H83 | source_reported_value |
| PSI-101-run-94-row-83 | Date (EST) | 40428.354166666664 | Unknown（來源未提供／尚未核對） | I83 | source_reported_value |
| PSI-101-run-94-row-83 | Inlet Velocity (cm/sec) | 8.1 | cm/s | K83 | source_reported_value |
| PSI-101-run-94-row-83 | Rt/R0 | 1.45 | dimensionless | L83 | source_reported_value |
| PSI-101-run-94-row-83 | Duration (sec) | 60 | s | M83 | source_reported_value |
| PSI-101-run-94-row-83 | Primary Aging Duration (sec) | 11 | s | N83 | source_reported_value |
| PSI-101-run-94-row-83 | Primary Mixing Duration (sec) | 8 | s | O83 | source_reported_value |
| PSI-101-run-94-row-83 | PreAge Thermal Precipitator | n | Unknown（來源未提供／尚未核對） | P83 | source_reported_value |
| PSI-101-run-94-row-83 | Net Aging  Duration | 42.142857142857146 | Unknown（來源未提供／尚未核對） | R83 | source_reported_value |
| PSI-101-run-94-row-83 | Primary Aging Therm Precip | y | Unknown（來源未提供／尚未核對） | S83 | source_reported_value |
| PSI-101-run-94-row-83 | Primary Aging Therm Precip Duration | 60 | Unknown（來源未提供／尚未核對） | T83 | source_reported_value |
| PSI-101-run-94-row-83 | Use STS Detector | n | Unknown（來源未提供／尚未核對） | U83 | source_reported_value |
| PSI-101-run-94-row-83 | Use Comm Diag A | y | Unknown（來源未提供／尚未核對） | V83 | source_reported_value |
| PSI-101-run-94-row-83 | Use Comm Diag B | y | Unknown（來源未提供／尚未核對） | W83 | source_reported_value |
| PSI-101-run-94-row-83 | Diluting A | n | Unknown（來源未提供／尚未核對） | X83 | source_reported_value |
| PSI-101-run-94-row-83 | Diluting B | n | Unknown（來源未提供／尚未核對） | Y83 | source_reported_value |
| PSI-101-run-94-row-83 | Cyclone Inlet on CDA (MPASS) | y | Unknown（來源未提供／尚未核對） | Z83 | source_reported_value |
| PSI-101-run-94-row-83 | Impactor Inlet on CDB | 10 | Unknown（來源未提供／尚未核對） | AA83 | source_reported_value |
| PSI-101-run-94-row-83 | Use P-Trak | y | Unknown（來源未提供／尚未核對） | AB83 | source_reported_value |
| PSI-101-run-94-row-83 | Aerosol Concentration To P-Trak | 0.03852706928546 | Unknown（來源未提供／尚未核對） | AC83 | source_reported_value |
| PSI-101-run-94-row-83 | Secondary Diagnostics Volume %  | 58 | % | AE83 | source_reported_value |
| PSI-101-run-94-row-83 | Secondary Aging Duration (sec) | 480 | s | AF83 | source_reported_value |
| PSI-101-run-94-row-83 | Secondary Mixing Duration (sec) | 0 | s | AG83 | source_reported_value |
| PSI-101-run-94-row-83 | STSDetector | n | Unknown（來源未提供／尚未核對） | AH83 | source_reported_value |
| PSI-101-run-94-row-83 | Comm Diag A | y | Unknown（來源未提供／尚未核對） | AI83 | source_reported_value |
| PSI-101-run-94-row-83 | Comm Diag B | y | Unknown（來源未提供／尚未核對） | AJ83 | source_reported_value |
| PSI-101-run-94-row-83 | Diluting A | n | Unknown（來源未提供／尚未核對） | AK83 | source_reported_value |
| PSI-101-run-94-row-83 | Diluting B | n | Unknown（來源未提供／尚未核對） | AL83 | source_reported_value |
| PSI-101-run-94-row-83 | Ues PTrak | y | Unknown（來源未提供／尚未核對） | AM83 | source_reported_value |
| PSI-101-run-94-row-83 | Aerosol Concentration To P-Trak | 0.03852706928546 | Unknown（來源未提供／尚未核對） | AN83 | source_formula_cached_result |
| PSI-101-run-94-row-83 | ISS Detector Scatter (volts) | 0.7454529000000002 | V | AR83 | source_reported_value |
| PSI-101-run-94-row-83 | STS Detector (volts) | 0 | V | AS83 | source_reported_value |
| PSI-101-run-94-row-83 | STS Detector offset (volts) | 0 | V | AT83 | source_reported_value |
| PSI-101-run-94-row-83 | Ion A (volts) Mpass_3rd | 0.10324098999999998 | V | AU83 | source_reported_value |
| PSI-101-run-94-row-83 | Ion A offset V0 (volts) | 0.028869634999999998 | V | AV83 | source_reported_value |
| PSI-101-run-94-row-83 | Ion B (volts) | 6.0749664999999995 | V | AW83 | source_reported_value |
| PSI-101-run-94-row-83 | Ion B offset V0 (volts) | 4.6810754999999995 | V | AX83 | source_reported_value |
| PSI-101-run-94-row-83 | Ptrak (PT/cc) | 75855 | #/cm^3 | AY83 | source_reported_value |
| PSI-101-run-94-row-83 | DustTrak A (mg/m3) Mpass_2nd | 0.18572995000000003 | mg/m^3 | AZ83 | source_reported_value |
| PSI-101-run-94-row-83 | DustTrak A (mg/m3) Mpass_2nd offset | 0.081817625 | mg/m^3 | BA83 | source_reported_value |
| PSI-101-run-94-row-83 | DustTrak B (mg/m3) | 7.88 | mg/m^3 | BB83 | source_reported_value |
| PSI-101-run-94-row-83 | Ion B Delta (volts) | 1.393891 | V | BC83 | source_formula_cached_result |
| PSI-101-run-94-row-83 | M0 best Diameter (#/cm3) | 3018896.381352701 | #/cm^3 | BD83 | source_formula_cached_result |
| PSI-101-run-94-row-83 | M1 (mm/cm3) | 277.55824331110045 | mm/cm^3 | BE83 | source_formula_cached_result |
| PSI-101-run-94-row-83 |  Mpass_3rd offset and dilution corrected | 0.07437135499999997 | Unknown（來源未提供／尚未核對） | BF83 | source_formula_cached_result |
| PSI-101-run-94-row-83 | DustTrak A (mg/m3) Mpass_2nd  offset, dilution and Gain corrected | 0.025978081250000007 | mg/m^3 | BG83 | source_formula_cached_result |
| PSI-101-run-94-row-83 | DustTrak B calibratred and corrected for dilution (mg/m3) | 3.546 | mg/m^3 | BH83 | source_formula_cached_result |
| PSI-101-run-94-row-83 | M1/M0 (micro-m)--AMD | 0.0919403014378164 | um | BI83 | source_formula_cached_result |
| PSI-101-run-94-row-83 | Diameter of Average mass (micro-m) | 0.11646654330236111 | um | BJ83 | source_formula_cached_result |
| PSI-101-run-94-row-83 | George's d2,1,  (micro-m) | 0.13108373797981254 | um | BK83 | source_formula_cached_result |
| PSI-101-run-94-row-83 | MPASS 3/2 | 2.8628501960667303 | Unknown（來源未提供／尚未核對） | BL83 | source_formula_cached_result |
| PSI-101-run-94-row-83 | Hatch Choate Sigma g | 1.6262491679176359 | dimensionless | BM83 | source_formula_cached_result |
| PSI-101-run-94-row-83 | Hatch Choate Dg | 0.08168800542053994 | Unknown（來源未提供／尚未核對） | BN83 | source_formula_cached_result |
| PSI-101-run-94-row-83 | CPC 100 nm cal, dilution corrected | 3018896.381352701 | Unknown（來源未提供／尚未核對） | BO83 | source_formula_cached_result |
| PSI-101-run-94-row-83 | CPC 600 nm cal, dilution corrected | 2973612.2465260113 | Unknown（來源未提供／尚未核對） | BP83 | source_formula_cached_result |
| PSI-101-run-94-row-83 | CPC 1200 nm cal, dilution corrected | 2706721.3379854904 | Unknown（來源未提供／尚未核對） | BQ83 | source_formula_cached_result |
| PSI-101-run-94-row-83 | Ion B Mment  mm/cm^3 | 277.55824331110045 | mm/cm^3 | BR83 | source_formula_cached_result |
| PSI-101-run-94-row-83 | Ion B X | 0.30939603125277454 | Unknown（來源未提供／尚未核對） | BS83 | source_formula_cached_result |
| PSI-101-run-94-row-83 | Dust Trak Cal Factor (Teom/Dusttrak) | 0.45 | Unknown（來源未提供／尚未核對） | BT83 | source_formula_cached_result |
| PSI-101-run-94-row-83 | MPASS Dilution factor | 1 | Unknown（來源未提供／尚未核對） | BU83 | source_formula_cached_result |
| PSI-101-run-94-row-83 | Dust Trak Dilution factor | 1 | Unknown（來源未提供／尚未核對） | BV83 | source_formula_cached_result |
| PSI-101-run-94-row-83 | Particle density g/cc | 1.42 | g/cm^3 | BW83 | source_formula_cached_result |
| PSI-101-run-94-row-83 | T ( C) - Eq. 2 of lrt | 527.3436756384525 | Unknown（來源未提供／尚未核對） | BZ83 | source_reported_value |
| PSI-101-run-94-row-83 | Mass Loss (mg) | 0.5700000000000705 | mg | CA83 | source_reported_value |
| PSI-101-run-94-row-83 | Test Number |  47K | Unknown（來源未提供／尚未核對） | CB83 | source_reported_value |
| PSI-101-run-94-row-83 | GMT | 250 | Unknown（來源未提供／尚未核對） | CC83 | source_reported_value |
| PSI-101-run-94-row-83 | Yeild: Dust Trak mass/mass lostt | 0.03732631578946907 | Unknown（來源未提供／尚未核對） | CD83 | source_formula_cached_result |
| PSI-101-run-94-row-83 | run | 83 | Unknown（來源未提供／尚未核對） | CI83 | source_reported_value |
| PSI-101-run-94-row-83 | material | Kapton | Unknown（來源未提供／尚未核對） | CJ83 | source_reported_value |
| PSI-101-run-94-row-83 | AMD | 0.0919403014378164 | Unknown（來源未提供／尚未核對） | CK83 | source_reported_value |
| PSI-101-run-94-row-83 | mass1 caculated with dector 3 | 0.02097330936266215 | Unknown（來源未提供／尚未核對） | CL83 | source_reported_value |
| PSI-101-run-94-row-83 | mass2 both detectors | 0.03703332939225097 | Unknown（來源未提供／尚未核對） | CM83 | source_reported_value |
| PSI-101-run-94-row-83 | Unknown（來源未提供／尚未核對） | 0.7203665423975496 | Unknown（來源未提供／尚未核對） | CO83 | source_formula_cached_result |
| PSI-101-run-94-row-84 | Carousel | 8(4) | Unknown（來源未提供／尚未核對） | A84 | source_reported_value |
| PSI-101-run-94-row-84 | Sample Type | Kapton | Unknown（來源未提供／尚未核對） | B84 | source_reported_value |
| PSI-101-run-94-row-84 | Sample ID | K11 | Unknown（來源未提供／尚未核對） | C84 | source_formula_cached_result |
| PSI-101-run-94-row-84 | Test ID Number | 47KA | Unknown（來源未提供／尚未核對） | D84 | source_reported_value |
| PSI-101-run-94-row-84 | SAME # | 94a | Unknown（來源未提供／尚未核對） | F84 | source_reported_value |
| PSI-101-run-94-row-84 | Description | aged | Unknown（來源未提供／尚未核對） | G84 | source_reported_value |
| PSI-101-run-94-row-84 | GMT | 250 | Unknown（來源未提供／尚未核對） | H84 | source_reported_value |
| PSI-101-run-94-row-84 | Date (EST) | 40428.354166666664 | Unknown（來源未提供／尚未核對） | I84 | source_reported_value |
| PSI-101-run-94-row-84 | Inlet Velocity (cm/sec) | 8.1 | cm/s | K84 | source_reported_value |
| PSI-101-run-94-row-84 | Rt/R0 | 1.45 | dimensionless | L84 | source_reported_value |
| PSI-101-run-94-row-84 | Net Aging  Duration | 567.4285714285714 | Unknown（來源未提供／尚未核對） | R84 | source_reported_value |
| PSI-101-run-94-row-84 | Use STS Detector | n | Unknown（來源未提供／尚未核對） | U84 | source_reported_value |
| PSI-101-run-94-row-84 | Use Comm Diag A | y | Unknown（來源未提供／尚未核對） | V84 | source_reported_value |
| PSI-101-run-94-row-84 | Use Comm Diag B | y | Unknown（來源未提供／尚未核對） | W84 | source_reported_value |
| PSI-101-run-94-row-84 | Diluting A | n | Unknown（來源未提供／尚未核對） | X84 | source_reported_value |
| PSI-101-run-94-row-84 | Diluting B | n | Unknown（來源未提供／尚未核對） | Y84 | source_reported_value |
| PSI-101-run-94-row-84 | Cyclone Inlet on CDA (MPASS) | y | Unknown（來源未提供／尚未核對） | Z84 | source_reported_value |
| PSI-101-run-94-row-84 | Impactor Inlet on CDB | 10 | Unknown（來源未提供／尚未核對） | AA84 | source_reported_value |
| PSI-101-run-94-row-84 | Use P-Trak | y | Unknown（來源未提供／尚未核對） | AB84 | source_reported_value |
| PSI-101-run-94-row-84 | Aerosol Concentration To P-Trak | 0.03852706928546 | Unknown（來源未提供／尚未核對） | AC84 | source_reported_value |
| PSI-101-run-94-row-84 | secondary agign thermal precip duration | 60 | Unknown（來源未提供／尚未核對） | AP84 | source_reported_value |
| PSI-101-run-94-row-84 | ISS Detector Scatter (volts) | 0.8422851999999998 | V | AR84 | source_reported_value |
| PSI-101-run-94-row-84 | STS Detector (volts) | 0 | V | AS84 | source_reported_value |
| PSI-101-run-94-row-84 | STS Detector offset (volts) | 0 | V | AT84 | source_reported_value |
| PSI-101-run-94-row-84 | Ion A (volts) Mpass_3rd | 0.11454768499999998 | V | AU84 | source_reported_value |
| PSI-101-run-94-row-84 | Ion A offset V0 (volts) | 0.027988971428571426 | V | AV84 | source_reported_value |
| PSI-101-run-94-row-84 | Ion B (volts) | 5.540847999999999 | V | AW84 | source_reported_value |
| PSI-101-run-94-row-84 | Ion B offset V0 (volts) | 4.68276238095238 | V | AX84 | source_reported_value |
| PSI-101-run-94-row-84 | Ptrak (PT/cc) | 30740 | #/cm^3 | AY84 | source_reported_value |
| PSI-101-run-94-row-84 | DustTrak A (mg/m3) Mpass_2nd | 0.21058654999999998 | mg/m^3 | AZ84 | source_reported_value |
| PSI-101-run-94-row-84 | DustTrak A (mg/m3) Mpass_2nd offset | 0.07963634285714286 | mg/m^3 | BA84 | source_reported_value |
| PSI-101-run-94-row-84 | DustTrak B (mg/m3) | 10.39685 | mg/m^3 | BB84 | source_reported_value |
| PSI-101-run-94-row-84 | Ion B Delta (volts) | 0.8580856190476185 | V | BC84 | source_formula_cached_result |
| PSI-101-run-94-row-84 | M0 best Diameter (#/cm3) | 1151405.4928839717 | #/cm^3 | BD84 | source_formula_cached_result |
| PSI-101-run-94-row-84 | M1 (mm/cm3) | 156.01798358413714 | mm/cm^3 | BE84 | source_formula_cached_result |
| PSI-101-run-94-row-84 |  Mpass_3rd offset and dilution corrected | 0.08655871357142855 | Unknown（來源未提供／尚未核對） | BF84 | source_formula_cached_result |
| PSI-101-run-94-row-84 | DustTrak A (mg/m3) Mpass_2nd  offset, dilution and Gain corrected | 0.03273755178571428 | mg/m^3 | BG84 | source_formula_cached_result |
| PSI-101-run-94-row-84 | DustTrak B calibratred and corrected for dilution (mg/m3) | 4.6785825 | mg/m^3 | BH84 | source_formula_cached_result |
| PSI-101-run-94-row-84 | M1/M0 (micro-m)--AMD | 0.13550220539017285 | um | BI84 | source_formula_cached_result |
| PSI-101-run-94-row-84 | Diameter of Average mass (micro-m) | 0.1761433869212854 | um | BJ84 | source_formula_cached_result |
| PSI-101-run-94-row-84 | George's d2,1,  (micro-m) | 0.2008289567990138 | um | BK84 | source_formula_cached_result |
| PSI-101-run-94-row-84 | MPASS 3/2 | 2.6440191416268415 | Unknown（來源未提供／尚未核對） | BL84 | source_formula_cached_result |
| PSI-101-run-94-row-84 | Hatch Choate Sigma g | 1.6688963150865648 | dimensionless | BM84 | source_formula_cached_result |
| PSI-101-run-94-row-84 | Hatch Choate Dg | 0.118846493917783 | Unknown（來源未提供／尚未核對） | BN84 | source_formula_cached_result |
| PSI-101-run-94-row-84 | CPC 100 nm cal, dilution corrected | 1151405.4928839717 | Unknown（來源未提供／尚未核對） | BO84 | source_formula_cached_result |
| PSI-101-run-94-row-84 | CPC 600 nm cal, dilution corrected | 1133054.2397751133 | Unknown（來源未提供／尚未核對） | BP84 | source_formula_cached_result |
| PSI-101-run-94-row-84 | CPC 1200 nm cal, dilution corrected | 1060893.9210288024 | Unknown（來源未提供／尚未核對） | BQ84 | source_formula_cached_result |
| PSI-101-run-94-row-84 | Ion B Mment  mm/cm^3 | 156.01798358413714 | mm/cm^3 | BR84 | source_formula_cached_result |
| PSI-101-run-94-row-84 | Ion B X | 0.1904655995400023 | Unknown（來源未提供／尚未核對） | BS84 | source_formula_cached_result |
| PSI-101-run-94-row-84 | Dust Trak Cal Factor (Teom/Dusttrak) | 0.45 | Unknown（來源未提供／尚未核對） | BT84 | source_formula_cached_result |
| PSI-101-run-94-row-84 | MPASS Dilution factor | 1 | Unknown（來源未提供／尚未核對） | BU84 | source_formula_cached_result |
| PSI-101-run-94-row-84 | Dust Trak Dilution factor | 1 | Unknown（來源未提供／尚未核對） | BV84 | source_formula_cached_result |
| PSI-101-run-94-row-84 | Particle density g/cc | 1.42 | g/cm^3 | BW84 | source_formula_cached_result |
| PSI-101-run-94-row-84 | T ( C) - Eq. 2 of lrt | 527.3436756384525 | Unknown（來源未提供／尚未核對） | BZ84 | source_reported_value |
| PSI-101-run-94-row-84 | Mass Loss (mg) | 0.5700000000000705 | mg | CA84 | source_formula_cached_result |
| PSI-101-run-94-row-84 | Yeild: Dust Trak mass/mass lostt | 0.04924823684209918 | Unknown（來源未提供／尚未核對） | CD84 | source_formula_cached_result |
| PSI-101-run-94-row-84 | run | 84 | Unknown（來源未提供／尚未核對） | CI84 | source_reported_value |
| PSI-101-run-94-row-84 | material | Kapton | Unknown（來源未提供／尚未核對） | CJ84 | source_reported_value |
| PSI-101-run-94-row-84 | AMD | 0.13550220539017285 | Unknown（來源未提供／尚未核對） | CK84 | source_reported_value |
| PSI-101-run-94-row-84 | mass1 caculated with dector 3 | 0.018501055302846226 | Unknown（來源未提供／尚未核對） | CL84 | source_reported_value |
| PSI-101-run-94-row-84 | mass2 both detectors | 0.03580410777383729 | Unknown（來源未提供／尚未核對） | CM84 | source_reported_value |
| PSI-101-run-94-row-84 | Unknown（來源未提供／尚未核對） | 0.7556565946437815 | Unknown（來源未提供／尚未核對） | CO84 | source_formula_cached_result |


你提供的 Excel 對照見 [FACTOR_MAP.md](../FACTOR_MAP.md)。總表是欄位／因子索引，不能替代本試次的實測數值。無法逐欄匹配者保留 Unknown。

### 感測器狀態與執行分率

| 摘要記錄 | 分率角色 | run原值 | 感測器啟用旗標 |
| --- | --- | --- | --- |
| PSI-101-run-94-row-83 | first_or_primary_fraction | 94 | {"Use STS Detector": {"cell": "U83", "value": "n", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "132", "status": "valid", "raw_header": "Use STS Detector", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "U83"}, "evidence_role": "source_reported_value"}, "Use Comm Diag A": {"cell": "V83", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "132", "status": "valid", "raw_header": "Use Comm Diag A", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "V83"}, "evidence_role": "source_reported_value"}, "Use Comm Diag B": {"cell": "W83", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "132", "status": "valid", "raw_header": "Use Comm Diag B", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "W83"}, "evidence_role": "source_reported_value"}, "Use P-Trak": {"cell": "AB83", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "132", "status": "valid", "raw_header": "Use P-Trak", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "AB83"}, "evidence_role": "source_reported_value"}, "STSDetector": {"cell": "AH83", "value": "n", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "132", "status": "valid", "raw_header": "STSDetector", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "AH83"}, "evidence_role": "source_reported_value"}, "Comm Diag A": {"cell": "AI83", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "132", "status": "valid", "raw_header": "Comm Diag A", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "AI83"}, "evidence_role": "source_reported_value"}, "Comm Diag B": {"cell": "AJ83", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "132", "status": "valid", "raw_header": "Comm Diag B", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "AJ83"}, "evidence_role": "source_reported_value"}, "Ues PTrak": {"cell": "AM83", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "132", "status": "valid", "raw_header": "Ues PTrak", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "AM83"}, "evidence_role": "source_reported_value"}} |
| PSI-101-run-94-row-84 | aged_fraction | 94a | {"Use STS Detector": {"cell": "U84", "value": "n", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "132", "status": "valid", "raw_header": "Use STS Detector", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "U84"}, "evidence_role": "source_reported_value"}, "Use Comm Diag A": {"cell": "V84", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "132", "status": "valid", "raw_header": "Use Comm Diag A", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "V84"}, "evidence_role": "source_reported_value"}, "Use Comm Diag B": {"cell": "W84", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "132", "status": "valid", "raw_header": "Use Comm Diag B", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "W84"}, "evidence_role": "source_reported_value"}, "Use P-Trak": {"cell": "AB84", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "132", "status": "valid", "raw_header": "Use P-Trak", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "AB84"}, "evidence_role": "source_reported_value"}} |


- {"execution_identity": "acquisition_segment_not_proven_independent_generation", "file_id": "PSI-101-8a986805a5df0a2a", "source_rows": 1520, "first_csv_row": 5, "last_csv_row": 1524, "first_time_string": "2010/250/13:32:02", "last_time_string": "2010/250/13:59:31", "state_values": {"TestRunning": ["0", "1"], "12VDCHeaterEnable": ["0", "1"], "HeatingInProgress": ["0", "1"], "PTrakState": ["0", "2", "3", "4", "5", "7"], "DustTrakAState": ["0", "2", "3", "4", "5", "6", "8"], "DustTrakBState": ["0", "2", "3", "4", "5", "6", "8"], "MixingFanPower": ["0", "1"], "PTrakPower": ["0", "1"], "DustTrakAPower": ["0", "1"], "DustTrakBPower": ["0", "1"], "STSDetectorPower": ["0"], "CarouselPower": ["0"], "STSDetectorSelfTest": ["0"], "STSDetectorAlarmReset": ["0", "1"], "STSDetectorAlarm": ["0"], "VideoPower": ["0", "1"], "CameraPower": ["0", "1"], "IlluminationLEDPower": ["0", "1"]}, "minus999_counts": {"PTrakMeasurement(PtPerCC)": 2}}


## 多個結論與適用範圍

| 判讀 | 證據層次 | 共同與不同之處 |
| --- | --- | --- |
| 此身份分組含 2 筆來源摘要記錄；分率／執行身份仍以來源標籤與衝突表為準。 | 資料稽核結論 | 同 baseRun 不代表每筆都是獨立產煙事件。 |
| 可追到上表數值的欄位共有 141 項；單位未提供時不轉換、不補 0。 | 原始欄位／快取判讀 | 同名粒徑可能來自不同矩、密度與儀器量測範圍，必須先對定義。 |
| 本試次與出版品的逐列身份對應，以明列的 exact_trial_ids 為限；其他連結僅為 campaign context。 | 文獻連結邊界 | 共用研究、材料或儀器不足以認定使用同一數據。 |
| 矩反演／PSD重建若重用了原量測矩，只能視為計算診斷，不能再把它當獨立預測成功。 | 物理／識別限制 | 需要未參與反演的尺寸分布、儀器響應或另一事件才能驗證外推。 |

Unknown；此處沒有補入推測值。


## 公式結果與實驗值的視覺化工具

程式名稱：`tools/smoke_evidence/physics.py`、`tools/smoke_evidence/viewer.js`；入口 `viewer.html`。

[開啟此試次的矩與來源快取比較](<../viewer/viewer.html?trial=PSI-101-run-94&view=moments>) · [檢查時間訊號／感測器狀態](<../viewer/viewer.html?trial=PSI-101-run-94&view=traces>)

展示狀態必須區分來源計算重現、同源反演重建、條件診斷、作者模擬與獨立預測。缺單位、越域或未使用的實驗目標不足時，該比較顯示 Unknown／Invalid，而非補出曲線。詳細公式見 [MODELS.md](../MODELS.md)。

### 本試次已執行的固定公式結果

| 來源記錄 | 輸出量 | 公式值 | 來源快取 | 公式減快取 | 比較角色 | 整體資格狀態 |
| --- | --- | --- | --- | --- | --- | --- |
| PSI-101-run-94-row-83 | d_count_um | 0.0919403014378164 | 0.0919403014378164 | 0.0 | same_source_reconstruction | unknown |
| PSI-101-run-94-row-83 | dm_um | 0.11646654330236104 | 0.11646654330236111 | -6.938893903907228e-17 | same_source_reconstruction | unknown |
| PSI-101-run-94-row-84 | d_count_um | 0.13550220539017285 | 0.13550220539017285 | 0.0 | same_source_reconstruction | unknown |
| PSI-101-run-94-row-84 | dm_um | 0.17614338692128542 | 0.1761433869212854 | 2.7755575615628914e-17 | same_source_reconstruction | unknown |


上述差值僅檢查已知公式與來源快取的數值重現，不是量測誤差、消防安全誤差或獨立模型預測分數。密度／校正等來源假設與各輸出的可計算性須保留；整體資格 Unknown 不會被改成安全 Pass。

- {"record_id": "PSI-101-run-94-row-83", "equation_ids": ["SMOKE-MOMENT-RATIOS", "SMOKE-LOGNORMAL-INVERSE"], "eligible_role": "same_source_equation_diagnostic_only", "raw_inversion_validation": false, "independent_validation_target": false}
- {"record_id": "PSI-101-run-94-row-84", "equation_ids": ["SMOKE-MOMENT-RATIOS", "SMOKE-LOGNORMAL-INVERSE"], "eligible_role": "same_source_equation_diagnostic_only", "raw_inversion_validation": false, "independent_validation_target": false}


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
| [PSI-101-8a986805a5df0a2a](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/01_實驗資料/第一批下載/PSI-101_SAME-R/Raw Data/PSI-101_Raw Data_HKPData_gmt250_3.csv>) | Raw Data | method=\["Original CSV TestNumber field; acquisition day/time retained"\]; status=\["source_identity_confirmed"\] | 8a986805a5df0a2a2c7e9db3a5bbd375501a76f8d4279c671721d6aa0a15087b |
| [PSI-101-8950c69bd71977e3](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/01_實驗資料/第一批下載/PSI-101_SAME-R/Analyzed Data/PSI-101_Analyzed Data_94 Kapton aged- results.xlsx>) | Analyzed Data | method=\["literal filename run/test token"\]; status=\["filename_candidate_not_fully_content_joined"\] | 8950c69bd71977e37e069288a16e4c94b63bb5ea64f22d0ebed38de81d5afba4 |
| [PSI-101-6d3a539ccf425b1f](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/01_實驗資料/第一批下載/PSI-101_SAME-R/Analyzed Data/PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx>) | Analyzed Data | method=\["canonical summary row SAME R Results!83", "canonical summary row SAME R Results!84"\]; status=\["source_identity_confirmed", "source_identity_confirmed"\] | 6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218 |
| [PSI-101-48a7bffcd47fc3cd](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/01_實驗資料/第一批下載/PSI-101_SAME-R/Analyzed Data/PSI-101_Analyzed Data_2010_250_13_kapton_run94.xls>) | Analyzed Data | method=\["literal filename run/test token"\]; status=\["filename_candidate_not_fully_content_joined"\] | 48a7bffcd47fc3cd51587454ad073417fc86a15dc839a65074d8ee16f0500e6e |
| [PSI-101-1e410a2ef34cfb97](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/簡報與海報/補下載/PSI-101/Raw Data/959399048c8190a6_PSI-101_Raw Data_94 postage 47k Kapton.pptx>) | Raw Data | method=\["literal filename run/test token"\]; status=\["filename_candidate_not_fully_content_joined"\] | 1e410a2ef34cfb97a0bcebb33149a8a5c9c5911ce0cc33e878a6d3a20bb7e53e |


結構化完整記錄：`qa/trial_records.json` 的 `PSI-101-run-94`。原始資料只讀；本 Markdown 不改寫來源公式、快取或身份衝突。
