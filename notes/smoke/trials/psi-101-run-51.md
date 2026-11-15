# PSI-101-run-51 煙霧資料與研究判讀

本卡的單位是來源身份分組的一個試次。新鮮／老化分率、重複排序視圖及感測器時間樣本不自動算成新的火災。

## 身份與資料範圍

| 研究 | 來源身份 | 材料標籤 | 日期原值 | 摘要觀測列數 | 可連結檔案數 |
| --- | --- | --- | --- | --- | --- |
| PSI-101 | canonical_summary_group_not_independent_execution_count | \[{"raw": "Kapton", "canonical_family": "Kapton", "source_locator": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "B6"}}\] | \[{"date_value": 40380.333333333336, "date_cell": "I6", "gmt_value": "202 12:00", "gmt_cell": "H6", "source_sheet": "SAME R Results", "date_encoding": "Excel serial when numeric; date-year comes from source style/context, not imputed from GMT"}, {"date_value": 40381.333333333336, "date_cell": "I7", "gmt_value": "203 12:00", "gmt_cell": "H7", "source_sheet": "SAME R Results", "date_encoding": "Excel serial when numeric; date-year comes from source style/context, not imputed from GMT"}\] | 2 | 5 |

- {"type": "fraction_date_difference", "source_date_values": [40380.333333333336, 40381.333333333336], "resolution": "Source dates retained per fraction; not silently merged or interpreted as separate smoke generations."}


其中 3 個檔案連結只屬檔名候選。未核對檔案內部身份／日期者，不當成已確認的本試次原始量測；下方來源表保留 method 與 status。

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


[開啟矩公式與TEM實驗方法對照](<../viewer/viewer.html?trial=PSI-101-run-51&view=methods>)。TEM是獨立的量測技術，但這裡使用相同飛行樣本；校正／密度／選模的保留樣本獨立性未證實，不能稱為獨立預測驗證。完整血緣及印列差異見 [PUBLICATION_DATA_BINDINGS.md](../PUBLICATION_DATA_BINDINGS.md)。

## 使用的資料部分與參數因子

下列快取值依原欄位保留。來源計算量、量測輸入、設定與狀態旗標分列；來源公式未被修正或重新擬合。

| 來源記錄 | 欄位／因子 | 原始值或快取 | 單位 | 儲存格／來源定位 | 量的角色 |
| --- | --- | --- | --- | --- | --- |
| PSI-101-run-51-row-6 | Carousel | 1 | Unknown（來源未提供／尚未核對） | A6 | source_reported_value |
| PSI-101-run-51-row-6 | Sample Type | Kapton | Unknown（來源未提供／尚未核對） | B6 | source_reported_value |
| PSI-101-run-51-row-6 | Sample ID | K01 | Unknown（來源未提供／尚未核對） | C6 | source_reported_value |
| PSI-101-run-51-row-6 | Test ID Number | 4K | Unknown（來源未提供／尚未核對） | D6 | source_reported_value |
| PSI-101-run-51-row-6 | Position in Carousel | 4 | Unknown（來源未提供／尚未核對） | E6 | source_reported_value |
| PSI-101-run-51-row-6 | SAME # | 51 | Unknown（來源未提供／尚未核對） | F6 | source_reported_value |
| PSI-101-run-51-row-6 | Description | Baseline new formula | Unknown（來源未提供／尚未核對） | G6 | source_reported_value |
| PSI-101-run-51-row-6 | GMT | 202 12:00 | Unknown（來源未提供／尚未核對） | H6 | source_reported_value |
| PSI-101-run-51-row-6 | Date (EST) | 40380.333333333336 | Unknown（來源未提供／尚未核對） | I6 | source_reported_value |
| PSI-101-run-51-row-6 | Inlet Velocity (cm/sec) | 8.1 | cm/s | K6 | source_reported_value |
| PSI-101-run-51-row-6 | Rt/R0 | 1.38 | dimensionless | L6 | source_reported_value |
| PSI-101-run-51-row-6 | Duration (sec) | 60 | s | M6 | source_reported_value |
| PSI-101-run-51-row-6 | Primary Aging Duration (sec) | 11 | s | N6 | source_reported_value |
| PSI-101-run-51-row-6 | Primary Mixing Duration (sec) | 8 | s | O6 | source_reported_value |
| PSI-101-run-51-row-6 | PreAge Thermal Precipitator | n | Unknown（來源未提供／尚未核對） | P6 | source_reported_value |
| PSI-101-run-51-row-6 | Net Aging  Duration | 38.142857142857146 | Unknown（來源未提供／尚未核對） | R6 | source_reported_value |
| PSI-101-run-51-row-6 | Primary Aging Therm Precip | y | Unknown（來源未提供／尚未核對） | S6 | source_reported_value |
| PSI-101-run-51-row-6 | Primary Aging Therm Precip Duration | ? | Unknown（來源未提供／尚未核對） | T6 | source_reported_value |
| PSI-101-run-51-row-6 | Use STS Detector | n | Unknown（來源未提供／尚未核對） | U6 | source_reported_value |
| PSI-101-run-51-row-6 | Use Comm Diag A | y | Unknown（來源未提供／尚未核對） | V6 | source_reported_value |
| PSI-101-run-51-row-6 | Use Comm Diag B | y | Unknown（來源未提供／尚未核對） | W6 | source_reported_value |
| PSI-101-run-51-row-6 | Diluting A | n | Unknown（來源未提供／尚未核對） | X6 | source_reported_value |
| PSI-101-run-51-row-6 | Diluting B | n | Unknown（來源未提供／尚未核對） | Y6 | source_reported_value |
| PSI-101-run-51-row-6 | Cyclone Inlet on CDA (MPASS) | y | Unknown（來源未提供／尚未核對） | Z6 | source_reported_value |
| PSI-101-run-51-row-6 | Impactor Inlet on CDB | 10 | Unknown（來源未提供／尚未核對） | AA6 | source_reported_value |
| PSI-101-run-51-row-6 | Use P-Trak | y | Unknown（來源未提供／尚未核對） | AB6 | source_reported_value |
| PSI-101-run-51-row-6 | Aerosol Concentration To P-Trak | 0.03852706928546 | Unknown（來源未提供／尚未核對） | AC6 | source_reported_value |
| PSI-101-run-51-row-6 | Secondary Aging Duration (sec) | 180 | s | AF6 | source_reported_value |
| PSI-101-run-51-row-6 | Secondary Mixing Duration (sec) | 0 | s | AG6 | source_reported_value |
| PSI-101-run-51-row-6 | STSDetector | n | Unknown（來源未提供／尚未核對） | AH6 | source_reported_value |
| PSI-101-run-51-row-6 | Comm Diag A | y | Unknown（來源未提供／尚未核對） | AI6 | source_reported_value |
| PSI-101-run-51-row-6 | Comm Diag B | y | Unknown（來源未提供／尚未核對） | AJ6 | source_reported_value |
| PSI-101-run-51-row-6 | Diluting A | n | Unknown（來源未提供／尚未核對） | AK6 | source_reported_value |
| PSI-101-run-51-row-6 | Diluting B | n | Unknown（來源未提供／尚未核對） | AL6 | source_reported_value |
| PSI-101-run-51-row-6 | Ues PTrak | y | Unknown（來源未提供／尚未核對） | AM6 | source_reported_value |
| PSI-101-run-51-row-6 | Aerosol Concentration To P-Trak | 0.03852706928546 | Unknown（來源未提供／尚未核對） | AN6 | source_formula_cached_result |
| PSI-101-run-51-row-6 | secondary agign thermal precip duration | 0 | Unknown（來源未提供／尚未核對） | AP6 | source_reported_value |
| PSI-101-run-51-row-6 | ISS Detector Scatter (volts) | 0.4175567 | V | AR6 | source_reported_value |
| PSI-101-run-51-row-6 | STS Detector (volts) | 0 | V | AS6 | source_reported_value |
| PSI-101-run-51-row-6 | STS Detector offset (volts) | 0 | V | AT6 | source_reported_value |
| PSI-101-run-51-row-6 | Ion A (volts) Mpass_3rd | 0.05915832000000001 | V | AU6 | source_reported_value |
| PSI-101-run-51-row-6 | Ion A offset V0 (volts) | 0.025772090000000004 | V | AV6 | source_reported_value |
| PSI-101-run-51-row-6 | Ion B (volts) | 5.28331 | V | AW6 | source_reported_value |
| PSI-101-run-51-row-6 | Ion B offset V0 (volts) | 4.6949 | V | AX6 | source_reported_value |
| PSI-101-run-51-row-6 | Ptrak (PT/cc) | 47624.95 | #/cm^3 | AY6 | source_reported_value |
| PSI-101-run-51-row-6 | DustTrak A (mg/m3) Mpass_2nd | 0.12976084999999998 | mg/m^3 | AZ6 | source_reported_value |
| PSI-101-run-51-row-6 | DustTrak A (mg/m3) Mpass_2nd offset | 0.0788160368573038 | mg/m^3 | BA6 | source_reported_value |
| PSI-101-run-51-row-6 | DustTrak B (mg/m3) | 2.76215 | mg/m^3 | BB6 | source_reported_value |
| PSI-101-run-51-row-6 | Ion B Delta (volts) | 0.5884100000000005 | V | BC6 | source_formula_cached_result |
| PSI-101-run-51-row-6 | M0 best Diameter (#/cm3) | 1825597.0139817814 | #/cm^3 | BD6 | source_formula_cached_result |
| PSI-101-run-51-row-6 | M1 (mm/cm3) | 102.91459773449184 | mm/cm^3 | BE6 | source_formula_cached_result |
| PSI-101-run-51-row-6 |  Mpass_3rd offset and dilution corrected | 0.03338623 | Unknown（來源未提供／尚未核對） | BF6 | source_formula_cached_result |
| PSI-101-run-51-row-6 | DustTrak A (mg/m3) Mpass_2nd  offset, dilution and Gain corrected | 0.012736203285674045 | mg/m^3 | BG6 | source_formula_cached_result |
| PSI-101-run-51-row-6 | DustTrak B calibratred and corrected for dilution (mg/m3) | 1.2429675 | mg/m^3 | BH6 | source_formula_cached_result |
| PSI-101-run-51-row-6 | M1/M0 (micro-m)--AMD | 0.0563731190105457 | um | BI6 | source_formula_cached_result |
| PSI-101-run-51-row-6 | Diameter of Average mass (micro-m) | 0.09710821323096017 | um | BJ6 | source_formula_cached_result |
| PSI-101-run-51-row-6 | George's d2,1,  (micro-m) | 0.12745236917509437 | um | BK6 | source_formula_cached_result |
| PSI-101-run-51-row-6 | MPASS 3/2 | 2.621364409089917 | Unknown（來源未提供／尚未核對） | BL6 | source_formula_cached_result |
| PSI-101-run-51-row-6 | Hatch Choate Sigma g | 2.090599137468832 | dimensionless | BM6 | source_formula_cached_result |
| PSI-101-run-51-row-6 | Hatch Choate Dg | 0.04295167596178432 | Unknown（來源未提供／尚未核對） | BN6 | source_formula_cached_result |
| PSI-101-run-51-row-6 | CPC 100 nm cal, dilution corrected | 1825597.0139817814 | Unknown（來源未提供／尚未核對） | BO6 | source_formula_cached_result |
| PSI-101-run-51-row-6 | CPC 600 nm cal, dilution corrected | 1797165.735135109 | Unknown（來源未提供／尚未核對） | BP6 | source_formula_cached_result |
| PSI-101-run-51-row-6 | CPC 1200 nm cal, dilution corrected | 1664496.7968457509 | Unknown（來源未提供／尚未核對） | BQ6 | source_formula_cached_result |
| PSI-101-run-51-row-6 | Ion B Mment  mm/cm^3 | 102.91459773449184 | mm/cm^3 | BR6 | source_formula_cached_result |
| PSI-101-run-51-row-6 | Ion B X | 0.13060685430169594 | Unknown（來源未提供／尚未核對） | BS6 | source_formula_cached_result |
| PSI-101-run-51-row-6 | Dust Trak Cal Factor (Teom/Dusttrak) | 0.45 | Unknown（來源未提供／尚未核對） | BT6 | source_formula_cached_result |
| PSI-101-run-51-row-6 | MPASS Dilution factor | 1 | Unknown（來源未提供／尚未核對） | BU6 | source_formula_cached_result |
| PSI-101-run-51-row-6 | Dust Trak Dilution factor | 1 | Unknown（來源未提供／尚未核對） | BV6 | source_formula_cached_result |
| PSI-101-run-51-row-6 | Particle density g/cc | 1.42 | g/cm^3 | BW6 | source_formula_cached_result |
| PSI-101-run-51-row-6 | T ( C) - Eq. 2 of lrt | 419.9282463017443 | Unknown（來源未提供／尚未核對） | BZ6 | source_reported_value |
| PSI-101-run-51-row-6 | run | 6 | Unknown（來源未提供／尚未核對） | CI6 | source_reported_value |
| PSI-101-run-51-row-6 | material | Kapton | Unknown（來源未提供／尚未核對） | CJ6 | source_reported_value |
| PSI-101-run-51-row-6 | AMD | 0.0563731190105457 | Unknown（來源未提供／尚未核對） | CK6 | source_reported_value |
| PSI-101-run-51-row-6 | mass1 caculated with dector 3 | 0.026860098916504257 | Unknown（來源未提供／尚未核對） | CL6 | source_reported_value |
| PSI-101-run-51-row-6 | mass2 both detectors | 0.028993357454059898 | Unknown（來源未提供／尚未核對） | CM6 | source_reported_value |
| PSI-101-run-51-row-6 | Unknown（來源未提供／尚未核對） | 0.5643539235056033 | Unknown（來源未提供／尚未核對） | CO6 | source_formula_cached_result |
| PSI-101-run-51-row-7 | Carousel | 1 | Unknown（來源未提供／尚未核對） | A7 | source_reported_value |
| PSI-101-run-51-row-7 | Sample Type | Kapton | Unknown（來源未提供／尚未核對） | B7 | source_reported_value |
| PSI-101-run-51-row-7 | Sample ID | K02 | Unknown（來源未提供／尚未核對） | C7 | source_reported_value |
| PSI-101-run-51-row-7 | Test ID Number | 4K | Unknown（來源未提供／尚未核對） | D7 | source_reported_value |
| PSI-101-run-51-row-7 | Position in Carousel | 4 | Unknown（來源未提供／尚未核對） | E7 | source_reported_value |
| PSI-101-run-51-row-7 | SAME # | 51a | Unknown（來源未提供／尚未核對） | F7 | source_reported_value |
| PSI-101-run-51-row-7 | Description | Baseline new formula | Unknown（來源未提供／尚未核對） | G7 | source_reported_value |
| PSI-101-run-51-row-7 | GMT | 203 12:00 | Unknown（來源未提供／尚未核對） | H7 | source_reported_value |
| PSI-101-run-51-row-7 | Date (EST) | 40381.333333333336 | Unknown（來源未提供／尚未核對） | I7 | source_reported_value |
| PSI-101-run-51-row-7 | Inlet Velocity (cm/sec) | 8.1 | cm/s | K7 | source_reported_value |
| PSI-101-run-51-row-7 | Rt/R0 | 1.38 | dimensionless | L7 | source_reported_value |
| PSI-101-run-51-row-7 | Duration (sec) | 60 | s | M7 | source_reported_value |
| PSI-101-run-51-row-7 | Net Aging  Duration | 261.14285714285717 | Unknown（來源未提供／尚未核對） | R7 | source_reported_value |
| PSI-101-run-51-row-7 | Use STS Detector | n | Unknown（來源未提供／尚未核對） | U7 | source_reported_value |
| PSI-101-run-51-row-7 | Use Comm Diag A | y | Unknown（來源未提供／尚未核對） | V7 | source_reported_value |
| PSI-101-run-51-row-7 | Use Comm Diag B | y | Unknown（來源未提供／尚未核對） | W7 | source_reported_value |
| PSI-101-run-51-row-7 | Diluting A | n | Unknown（來源未提供／尚未核對） | X7 | source_reported_value |
| PSI-101-run-51-row-7 | Diluting B | n | Unknown（來源未提供／尚未核對） | Y7 | source_reported_value |
| PSI-101-run-51-row-7 | Cyclone Inlet on CDA (MPASS) | y | Unknown（來源未提供／尚未核對） | Z7 | source_reported_value |
| PSI-101-run-51-row-7 | Impactor Inlet on CDB | 10 | Unknown（來源未提供／尚未核對） | AA7 | source_reported_value |
| PSI-101-run-51-row-7 | Use P-Trak | y | Unknown（來源未提供／尚未核對） | AB7 | source_reported_value |
| PSI-101-run-51-row-7 | Aerosol Concentration To P-Trak | 0.03852706928546 | Unknown（來源未提供／尚未核對） | AC7 | source_reported_value |
| PSI-101-run-51-row-7 | ISS Detector Scatter (volts) | 0.40887450000000003 | V | AR7 | source_reported_value |
| PSI-101-run-51-row-7 | STS Detector (volts) | 0 | V | AS7 | source_reported_value |
| PSI-101-run-51-row-7 | STS Detector offset (volts) | 0 | V | AT7 | source_reported_value |
| PSI-101-run-51-row-7 | Ion A (volts) Mpass_3rd | 0.05145264000000001 | V | AU7 | source_reported_value |
| PSI-101-run-51-row-7 | Ion A offset V0 (volts) | 0.0301056 | V | AV7 | source_reported_value |
| PSI-101-run-51-row-7 | Ion B (volts) | 5.093612499999999 | V | AW7 | source_reported_value |
| PSI-101-run-51-row-7 | Ion B offset V0 (volts) | 4.679275 | V | AX7 | source_reported_value |
| PSI-101-run-51-row-7 | Ptrak (PT/cc) | 28390 | #/cm^3 | AY7 | source_reported_value |
| PSI-101-run-51-row-7 | DustTrak A (mg/m3) Mpass_2nd | 0.12408455 | mg/m^3 | AZ7 | source_reported_value |
| PSI-101-run-51-row-7 | DustTrak A (mg/m3) Mpass_2nd offset | 0.090270985 | mg/m^3 | BA7 | source_reported_value |
| PSI-101-run-51-row-7 | DustTrak B (mg/m3) | 2.6983499999999996 | mg/m^3 | BB7 | source_reported_value |
| PSI-101-run-51-row-7 | Ion B Delta (volts) | 0.41433749999999936 | V | BC7 | source_formula_cached_result |
| PSI-101-run-51-row-7 | M0 best Diameter (#/cm3) | 1059919.9201329139 | #/cm^3 | BD7 | source_formula_cached_result |
| PSI-101-run-51-row-7 | M1 (mm/cm3) | 70.81926663871712 | mm/cm^3 | BE7 | source_formula_cached_result |
| PSI-101-run-51-row-7 |  Mpass_3rd offset and dilution corrected | 0.021347040000000008 | Unknown（來源未提供／尚未核對） | BF7 | source_formula_cached_result |
| PSI-101-run-51-row-7 | DustTrak A (mg/m3) Mpass_2nd  offset, dilution and Gain corrected | 0.008453391250000001 | mg/m^3 | BG7 | source_formula_cached_result |
| PSI-101-run-51-row-7 | DustTrak B calibratred and corrected for dilution (mg/m3) | 1.2142574999999998 | mg/m^3 | BH7 | source_formula_cached_result |
| PSI-101-run-51-row-7 | M1/M0 (micro-m)--AMD | 0.0668156766313406 | um | BI7 | source_formula_cached_result |
| PSI-101-run-51-row-7 | Diameter of Average mass (micro-m) | 0.11550042736986271 | um | BJ7 | source_formula_cached_result |
| PSI-101-run-51-row-7 | George's d2,1,  (micro-m) | 0.15185748443649788 | um | BK7 | source_formula_cached_result |
| PSI-101-run-51-row-7 | MPASS 3/2 | 2.5252634556575155 | Unknown（來源未提供／尚未核對） | BL7 | source_formula_cached_result |
| PSI-101-run-51-row-7 | Hatch Choate Sigma g | 2.0955623370880416 | dimensionless | BM7 | source_formula_cached_result |
| PSI-101-run-51-row-7 | Hatch Choate Dg | 0.05081895854236607 | Unknown（來源未提供／尚未核對） | BN7 | source_formula_cached_result |
| PSI-101-run-51-row-7 | CPC 100 nm cal, dilution corrected | 1059919.9201329139 | Unknown（來源未提供／尚未核對） | BO7 | source_formula_cached_result |
| PSI-101-run-51-row-7 | CPC 600 nm cal, dilution corrected | 1042971.5767444789 | Unknown（來源未提供／尚未核對） | BP7 | source_formula_cached_result |
| PSI-101-run-51-row-7 | CPC 1200 nm cal, dilution corrected | 978059.4215667731 | Unknown（來源未提供／尚未核對） | BQ7 | source_formula_cached_result |
| PSI-101-run-51-row-7 | Ion B Mment  mm/cm^3 | 70.81926663871712 | mm/cm^3 | BR7 | source_formula_cached_result |
| PSI-101-run-51-row-7 | Ion B X | 0.09196872502885539 | Unknown（來源未提供／尚未核對） | BS7 | source_formula_cached_result |
| PSI-101-run-51-row-7 | Dust Trak Cal Factor (Teom/Dusttrak) | 0.45 | Unknown（來源未提供／尚未核對） | BT7 | source_formula_cached_result |
| PSI-101-run-51-row-7 | MPASS Dilution factor | 1 | Unknown（來源未提供／尚未核對） | BU7 | source_formula_cached_result |
| PSI-101-run-51-row-7 | Dust Trak Dilution factor | 1 | Unknown（來源未提供／尚未核對） | BV7 | source_formula_cached_result |
| PSI-101-run-51-row-7 | Particle density g/cc | 1.42 | g/cm^3 | BW7 | source_formula_cached_result |
| PSI-101-run-51-row-7 | T ( C) - Eq. 2 of lrt | 419.9282463017443 | Unknown（來源未提供／尚未核對） | BZ7 | source_reported_value |
| PSI-101-run-51-row-7 | run | 7 | Unknown（來源未提供／尚未核對） | CI7 | source_reported_value |
| PSI-101-run-51-row-7 | material | Kapton | Unknown（來源未提供／尚未核對） | CJ7 | source_reported_value |
| PSI-101-run-51-row-7 | AMD | 0.0668156766313406 | Unknown（來源未提供／尚未核對） | CK7 | source_reported_value |
| PSI-101-run-51-row-7 | mass1 caculated with dector 3 | 0.017580323778111324 | Unknown（來源未提供／尚未核對） | CL7 | source_reported_value |
| PSI-101-run-51-row-7 | mass2 both detectors | 0.034853850095922234 | Unknown（來源未提供／尚未核對） | CM7 | source_reported_value |
| PSI-101-run-51-row-7 | Unknown（來源未提供／尚未核對） | 0.4148871661395801 | Unknown（來源未提供／尚未核對） | CO7 | source_formula_cached_result |


你提供的 Excel 對照見 [FACTOR_MAP.md](../FACTOR_MAP.md)。總表是欄位／因子索引，不能替代本試次的實測數值。無法逐欄匹配者保留 Unknown。

### 感測器狀態與執行分率

| 摘要記錄 | 分率角色 | run原值 | 感測器啟用旗標 |
| --- | --- | --- | --- |
| PSI-101-run-51-row-6 | first_or_primary_fraction | 51 | {"Use STS Detector": {"cell": "U6", "value": "n", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "95", "status": "valid", "raw_header": "Use STS Detector", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "U6"}, "evidence_role": "source_reported_value"}, "Use Comm Diag A": {"cell": "V6", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "95", "status": "valid", "raw_header": "Use Comm Diag A", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "V6"}, "evidence_role": "source_reported_value"}, "Use Comm Diag B": {"cell": "W6", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "95", "status": "valid", "raw_header": "Use Comm Diag B", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "W6"}, "evidence_role": "source_reported_value"}, "Use P-Trak": {"cell": "AB6", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "93", "status": "valid", "raw_header": "Use P-Trak", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "AB6"}, "evidence_role": "source_reported_value"}, "STSDetector": {"cell": "AH6", "value": "n", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "97", "status": "valid", "raw_header": "STSDetector", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "AH6"}, "evidence_role": "source_reported_value"}, "Comm Diag A": {"cell": "AI6", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "97", "status": "valid", "raw_header": "Comm Diag A", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "AI6"}, "evidence_role": "source_reported_value"}, "Comm Diag B": {"cell": "AJ6", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "97", "status": "valid", "raw_header": "Comm Diag B", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "AJ6"}, "evidence_role": "source_reported_value"}, "Ues PTrak": {"cell": "AM6", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "97", "status": "valid", "raw_header": "Ues PTrak", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "AM6"}, "evidence_role": "source_reported_value"}} |
| PSI-101-run-51-row-7 | aged_fraction | 51a | {"Use STS Detector": {"cell": "U7", "value": "n", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "95", "status": "valid", "raw_header": "Use STS Detector", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "U7"}, "evidence_role": "source_reported_value"}, "Use Comm Diag A": {"cell": "V7", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "95", "status": "valid", "raw_header": "Use Comm Diag A", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "V7"}, "evidence_role": "source_reported_value"}, "Use Comm Diag B": {"cell": "W7", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "95", "status": "valid", "raw_header": "Use Comm Diag B", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "W7"}, "evidence_role": "source_reported_value"}, "Use P-Trak": {"cell": "AB7", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "93", "status": "valid", "raw_header": "Use P-Trak", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "AB7"}, "evidence_role": "source_reported_value"}} |


Unknown；此處沒有補入推測值。


## 多個結論與適用範圍

| 判讀 | 證據層次 | 共同與不同之處 |
| --- | --- | --- |
| 此身份分組含 2 筆來源摘要記錄；分率／執行身份仍以來源標籤與衝突表為準。 | 資料稽核結論 | 同 baseRun 不代表每筆都是獨立產煙事件。 |
| 可追到上表數值的欄位共有 137 項；單位未提供時不轉換、不補 0。 | 原始欄位／快取判讀 | 同名粒徑可能來自不同矩、密度與儀器量測範圍，必須先對定義。 |
| 本試次與出版品的逐列身份對應，以明列的 exact_trial_ids 為限；其他連結僅為 campaign context。 | 文獻連結邊界 | 共用研究、材料或儀器不足以認定使用同一數據。 |
| 矩反演／PSD重建若重用了原量測矩，只能視為計算診斷，不能再把它當獨立預測成功。 | 物理／識別限制 | 需要未參與反演的尺寸分布、儀器響應或另一事件才能驗證外推。 |

Unknown；此處沒有補入推測值。


## 公式結果與實驗值的視覺化工具

程式名稱：`tools/smoke_evidence/physics.py`、`tools/smoke_evidence/viewer.js`；入口 `viewer.html`。

[開啟此試次的矩與來源快取比較](<../viewer/viewer.html?trial=PSI-101-run-51&view=moments>) · [檢查時間訊號／感測器狀態](<../viewer/viewer.html?trial=PSI-101-run-51&view=traces>)

展示狀態必須區分來源計算重現、同源反演重建、條件診斷、作者模擬與獨立預測。缺單位、越域或未使用的實驗目標不足時，該比較顯示 Unknown／Invalid，而非補出曲線。詳細公式見 [MODELS.md](../MODELS.md)。

### 本試次已執行的固定公式結果

| 來源記錄 | 輸出量 | 公式值 | 來源快取 | 公式減快取 | 比較角色 | 整體資格狀態 |
| --- | --- | --- | --- | --- | --- | --- |
| PSI-101-run-51-row-6 | d_count_um | 0.0563731190105457 | 0.0563731190105457 | 0.0 | same_source_reconstruction | unknown |
| PSI-101-run-51-row-6 | dm_um | 0.09710821323096012 | 0.09710821323096017 | -4.163336342344337e-17 | same_source_reconstruction | unknown |
| PSI-101-run-51-row-7 | d_count_um | 0.0668156766313406 | 0.0668156766313406 | 0.0 | same_source_reconstruction | unknown |
| PSI-101-run-51-row-7 | dm_um | 0.11550042736986273 | 0.11550042736986271 | 1.3877787807814457e-17 | same_source_reconstruction | unknown |


上述差值僅檢查已知公式與來源快取的數值重現，不是量測誤差、消防安全誤差或獨立模型預測分數。密度／校正等來源假設與各輸出的可計算性須保留；整體資格 Unknown 不會被改成安全 Pass。

- {"record_id": "PSI-101-run-51-row-6", "equation_ids": ["SMOKE-MOMENT-RATIOS", "SMOKE-LOGNORMAL-INVERSE"], "eligible_role": "same_source_equation_diagnostic_only", "raw_inversion_validation": false, "independent_validation_target": false}
- {"record_id": "PSI-101-run-51-row-7", "equation_ids": ["SMOKE-MOMENT-RATIOS", "SMOKE-LOGNORMAL-INVERSE"], "eligible_role": "same_source_equation_diagnostic_only", "raw_inversion_validation": false, "independent_validation_target": false}


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
| [PSI-101-6d3a539ccf425b1f](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/01_實驗資料/第一批下載/PSI-101_SAME-R/Analyzed Data/PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx>) | Analyzed Data | method=\["canonical summary row SAME R Results!6", "canonical summary row SAME R Results!7"\]; status=\["source_identity_confirmed", "source_identity_confirmed"\] | 6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218 |
| [PSI-101-f198083bd1ffefa5](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/簡報與海報/補下載/PSI-101/Raw Data/a57382999ff88c4c_PSI-101_Raw Data_51 - 4K Kapton.pptx>) | Raw Data | method=\["literal filename run/test token"\]; status=\["filename_candidate_not_fully_content_joined"\] | f198083bd1ffefa587bdd16e52693212b0991b93eae20ba5cf27960aa8f237b1 |
| [PSI-101-307b64db49c24e1a](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/實驗附帶文件/補下載/PSI-101/Raw Data/cc1bc73ed5bb1991_PSI-101_Raw Data_K01-4K images.pdf>) | Raw Data | method=\["literal unique sample-ID token also present in source summary"\]; status=\["filename_candidate_not_fully_content_joined"\] | 307b64db49c24e1af4dd62a3df7105f51b59be18c8f41ecc0e5db97c6344e6ed |
| [PSI-101-44cf3bb0662623f2](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/簡報與海報/補下載/PSI-101/Raw Data/90ff193361ae5c91_PSI-101_Raw Data_K01-4K images.pptx>) | Raw Data | method=\["literal unique sample-ID token also present in source summary"\]; status=\["filename_candidate_not_fully_content_joined"\] | 44cf3bb0662623f2c2c5debc90a3bcb41ec77f244302cd8ee471906946c84896 |


結構化完整記錄：`qa/trial_records.json` 的 `PSI-101-run-51`。原始資料只讀；本 Markdown 不改寫來源公式、快取或身份衝突。
