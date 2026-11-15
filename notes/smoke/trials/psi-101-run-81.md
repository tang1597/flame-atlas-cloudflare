# PSI-101-run-81 煙霧資料與研究判讀

本卡的單位是來源身份分組的一個試次。新鮮／老化分率、重複排序視圖及感測器時間樣本不自動算成新的火災。

## 身份與資料範圍

| 研究 | 來源身份 | 材料標籤 | 日期原值 | 摘要觀測列數 | 可連結檔案數 |
| --- | --- | --- | --- | --- | --- |
| PSI-101 | canonical_summary_group_not_independent_execution_count | \[{"raw": "Teflon", "canonical_family": "Teflon", "source_locator": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "B60"}}\] | \[{"date_value": 40416, "date_cell": "I60", "gmt_value": 239, "gmt_cell": "H60", "source_sheet": "SAME R Results", "date_encoding": "Excel serial when numeric; date-year comes from source style/context, not imputed from GMT"}, {"date_value": 40417, "date_cell": "I61", "gmt_value": 239, "gmt_cell": "H61", "source_sheet": "SAME R Results", "date_encoding": "Excel serial when numeric; date-year comes from source style/context, not imputed from GMT"}\] | 2 | 4 |

- {"type": "fraction_date_difference", "source_date_values": [40416, 40417], "resolution": "Source dates retained per fraction; not silently merged or interpreted as separate smoke generations."}


其中 1 個檔案連結只屬檔名候選。未核對檔案內部身份／日期者，不當成已確認的本試次原始量測；下方來源表保留 method 與 status。

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


[開啟矩公式與TEM實驗方法對照](<../viewer/viewer.html?trial=PSI-101-run-81&view=methods>)。TEM是獨立的量測技術，但這裡使用相同飛行樣本；校正／密度／選模的保留樣本獨立性未證實，不能稱為獨立預測驗證。完整血緣及印列差異見 [PUBLICATION_DATA_BINDINGS.md](../PUBLICATION_DATA_BINDINGS.md)。

## 使用的資料部分與參數因子

下列快取值依原欄位保留。來源計算量、量測輸入、設定與狀態旗標分列；來源公式未被修正或重新擬合。

| 來源記錄 | 欄位／因子 | 原始值或快取 | 單位 | 儲存格／來源定位 | 量的角色 |
| --- | --- | --- | --- | --- | --- |
| PSI-101-run-81-row-60 | Carousel | 4 | Unknown（來源未提供／尚未核對） | A60 | source_reported_value |
| PSI-101-run-81-row-60 | Sample Type | Teflon | Unknown（來源未提供／尚未核對） | B60 | source_reported_value |
| PSI-101-run-81-row-60 | Sample ID | T06 | Unknown（來源未提供／尚未核對） | C60 | source_reported_value |
| PSI-101-run-81-row-60 | Test ID Number | 34 T | Unknown（來源未提供／尚未核對） | D60 | source_reported_value |
| PSI-101-run-81-row-60 | Position in Carousel | 6 | Unknown（來源未提供／尚未核對） | E60 | source_reported_value |
| PSI-101-run-81-row-60 | SAME # | 81 | Unknown（來源未提供／尚未核對） | F60 | source_reported_value |
| PSI-101-run-81-row-60 | Description | High temp  aging | Unknown（來源未提供／尚未核對） | G60 | source_reported_value |
| PSI-101-run-81-row-60 | GMT | 239 | Unknown（來源未提供／尚未核對） | H60 | source_reported_value |
| PSI-101-run-81-row-60 | Date (EST) | 40416 | Unknown（來源未提供／尚未核對） | I60 | source_reported_value |
| PSI-101-run-81-row-60 | Inlet Velocity (cm/sec) | 8.1 | cm/s | K60 | source_reported_value |
| PSI-101-run-81-row-60 | Rt/R0 | 1.45 | dimensionless | L60 | source_reported_value |
| PSI-101-run-81-row-60 | Duration (sec) | 60 | s | M60 | source_reported_value |
| PSI-101-run-81-row-60 | Primary Aging Duration (sec) | 11 | s | N60 | source_reported_value |
| PSI-101-run-81-row-60 | Primary Mixing Duration (sec) | 8 | s | O60 | source_reported_value |
| PSI-101-run-81-row-60 | PreAge Thermal Precipitator | n | Unknown（來源未提供／尚未核對） | P60 | source_reported_value |
| PSI-101-run-81-row-60 | PreAge Thermal Precipitator Duration | n | Unknown（來源未提供／尚未核對） | Q60 | source_reported_value |
| PSI-101-run-81-row-60 | Net Aging  Duration | 30.166666666666668 | Unknown（來源未提供／尚未核對） | R60 | source_reported_value |
| PSI-101-run-81-row-60 | Primary Aging Therm Precip | y | Unknown（來源未提供／尚未核對） | S60 | source_reported_value |
| PSI-101-run-81-row-60 | Primary Aging Therm Precip Duration | 45 | Unknown（來源未提供／尚未核對） | T60 | source_reported_value |
| PSI-101-run-81-row-60 | Use STS Detector | n | Unknown（來源未提供／尚未核對） | U60 | source_reported_value |
| PSI-101-run-81-row-60 | Use Comm Diag A | y | Unknown（來源未提供／尚未核對） | V60 | source_reported_value |
| PSI-101-run-81-row-60 | Use Comm Diag B | y | Unknown（來源未提供／尚未核對） | W60 | source_reported_value |
| PSI-101-run-81-row-60 | Diluting A | n | Unknown（來源未提供／尚未核對） | X60 | source_reported_value |
| PSI-101-run-81-row-60 | Diluting B | n | Unknown（來源未提供／尚未核對） | Y60 | source_reported_value |
| PSI-101-run-81-row-60 | Cyclone Inlet on CDA (MPASS) | y | Unknown（來源未提供／尚未核對） | Z60 | source_reported_value |
| PSI-101-run-81-row-60 | Impactor Inlet on CDB | 10 | Unknown（來源未提供／尚未核對） | AA60 | source_reported_value |
| PSI-101-run-81-row-60 | Use P-Trak | y | Unknown（來源未提供／尚未核對） | AB60 | source_reported_value |
| PSI-101-run-81-row-60 | Aerosol Concentration To P-Trak | 0.0519567251427413 | Unknown（來源未提供／尚未核對） | AC60 | source_reported_value |
| PSI-101-run-81-row-60 | Secondary Diagnostics Volume %  | 58 | % | AE60 | source_reported_value |
| PSI-101-run-81-row-60 | Secondary Aging Duration (sec) | 480 | s | AF60 | source_reported_value |
| PSI-101-run-81-row-60 | Secondary Mixing Duration (sec) | 0 | s | AG60 | source_reported_value |
| PSI-101-run-81-row-60 | STSDetector | n | Unknown（來源未提供／尚未核對） | AH60 | source_reported_value |
| PSI-101-run-81-row-60 | Comm Diag A | y | Unknown（來源未提供／尚未核對） | AI60 | source_reported_value |
| PSI-101-run-81-row-60 | Comm Diag B | y | Unknown（來源未提供／尚未核對） | AJ60 | source_reported_value |
| PSI-101-run-81-row-60 | Diluting A | n | Unknown（來源未提供／尚未核對） | AK60 | source_reported_value |
| PSI-101-run-81-row-60 | Diluting B | n | Unknown（來源未提供／尚未核對） | AL60 | source_reported_value |
| PSI-101-run-81-row-60 | Ues PTrak | y | Unknown（來源未提供／尚未核對） | AM60 | source_reported_value |
| PSI-101-run-81-row-60 | Aerosol Concentration To P-Trak | 0.0519567251427413 | Unknown（來源未提供／尚未核對） | AN60 | source_formula_cached_result |
| PSI-101-run-81-row-60 | ISS Detector Scatter (volts) | 2.1625675000000006 | V | AR60 | source_reported_value |
| PSI-101-run-81-row-60 | STS Detector (volts) | 0 | V | AS60 | source_reported_value |
| PSI-101-run-81-row-60 | STS Detector offset (volts) | 0 | V | AT60 | source_reported_value |
| PSI-101-run-81-row-60 | Ion A (volts) Mpass_3rd | 0.25022875 | V | AU60 | source_reported_value |
| PSI-101-run-81-row-60 | Ion A offset V0 (volts) | 0.026962295000000004 | V | AV60 | source_reported_value |
| PSI-101-run-81-row-60 | Ion B (volts) | 6.977615 | V | AW60 | source_reported_value |
| PSI-101-run-81-row-60 | Ion B offset V0 (volts) | 4.716292999999999 | V | AX60 | source_reported_value |
| PSI-101-run-81-row-60 | Ptrak (PT/cc) | 88505 | #/cm^3 | AY60 | source_reported_value |
| PSI-101-run-81-row-60 | DustTrak A (mg/m3) Mpass_2nd | 0.33628839999999993 | mg/m^3 | AZ60 | source_reported_value |
| PSI-101-run-81-row-60 | DustTrak A (mg/m3) Mpass_2nd offset | 0.08174134499999999 | mg/m^3 | BA60 | source_reported_value |
| PSI-101-run-81-row-60 | DustTrak B (mg/m3) | 21.487300000000005 | mg/m^3 | BB60 | source_reported_value |
| PSI-101-run-81-row-60 | Ion B Delta (volts) | 2.2613220000000007 | V | BC60 | source_formula_cached_result |
| PSI-101-run-81-row-60 | M0 best Diameter (#/cm3) | 2654993.7023748658 | #/cm^3 | BD60 | source_formula_cached_result |
| PSI-101-run-81-row-60 | M1 (mm/cm3) | 553.24833622877 | mm/cm^3 | BE60 | source_formula_cached_result |
| PSI-101-run-81-row-60 |  Mpass_3rd offset and dilution corrected | 0.223266455 | Unknown（來源未提供／尚未核對） | BF60 | source_formula_cached_result |
| PSI-101-run-81-row-60 | DustTrak A (mg/m3) Mpass_2nd  offset, dilution and Gain corrected | 0.06363676374999999 | mg/m^3 | BG60 | source_formula_cached_result |
| PSI-101-run-81-row-60 | DustTrak B calibratred and corrected for dilution (mg/m3) | 48.56129800000001 | mg/m^3 | BH60 | source_formula_cached_result |
| PSI-101-run-81-row-60 | M1/M0 (micro-m)--AMD | 0.20838028193207944 | um | BI60 | source_formula_cached_result |
| PSI-101-run-81-row-60 | Diameter of Average mass (micro-m) | 0.2513439847697668 | um | BJ60 | source_formula_cached_result |
| PSI-101-run-81-row-60 | George's d2,1,  (micro-m) | 0.2760415347905845 | um | BK60 | source_formula_cached_result |
| PSI-101-run-81-row-60 | MPASS 3/2 | 3.508450804901279 | Unknown（來源未提供／尚未核對） | BL60 | source_formula_cached_result |
| PSI-101-run-81-row-60 | Hatch Choate Sigma g | 1.541820614289457 | dimensionless | BM60 | source_formula_cached_result |
| PSI-101-run-81-row-60 | Hatch Choate Dg | 0.18973641212359585 | Unknown（來源未提供／尚未核對） | BN60 | source_formula_cached_result |
| PSI-101-run-81-row-60 | CPC 100 nm cal, dilution corrected | 2654993.7023748658 | Unknown（來源未提供／尚未核對） | BO60 | source_formula_cached_result |
| PSI-101-run-81-row-60 | CPC 600 nm cal, dilution corrected | 2615814.6549193626 | Unknown（來源未提供／尚未核對） | BP60 | source_formula_cached_result |
| PSI-101-run-81-row-60 | CPC 1200 nm cal, dilution corrected | 2363356.797174021 | Unknown（來源未提供／尚未核對） | BQ60 | source_formula_cached_result |
| PSI-101-run-81-row-60 | Ion B Mment  mm/cm^3 | 553.24833622877 | mm/cm^3 | BR60 | source_formula_cached_result |
| PSI-101-run-81-row-60 | Ion B X | 0.5019359850839031 | Unknown（來源未提供／尚未核對） | BS60 | source_formula_cached_result |
| PSI-101-run-81-row-60 | Dust Trak Cal Factor (Teom/Dusttrak) | 2.26 | Unknown（來源未提供／尚未核對） | BT60 | source_formula_cached_result |
| PSI-101-run-81-row-60 | MPASS Dilution factor | 1 | Unknown（來源未提供／尚未核對） | BU60 | source_formula_cached_result |
| PSI-101-run-81-row-60 | Dust Trak Dilution factor | 1 | Unknown（來源未提供／尚未核對） | BV60 | source_formula_cached_result |
| PSI-101-run-81-row-60 | Particle density g/cc | 2.2 | g/cm^3 | BW60 | source_formula_cached_result |
| PSI-101-run-81-row-60 | T ( C) - Eq. 2 of lrt | 538.4309629381966 | Unknown（來源未提供／尚未核對） | BZ60 | source_reported_value |
| PSI-101-run-81-row-60 | Mass Loss (mg) | 9.71333333333324 | mg | CA60 | source_reported_value |
| PSI-101-run-81-row-60 | Test Number |  34T | Unknown（來源未提供／尚未核對） | CB60 | source_reported_value |
| PSI-101-run-81-row-60 | GMT | 239 | Unknown（來源未提供／尚未核對） | CC60 | source_reported_value |
| PSI-101-run-81-row-60 | Yeild: Dust Trak mass/mass lostt | 0.029996683733699677 | Unknown（來源未提供／尚未核對） | CD60 | source_formula_cached_result |
| PSI-101-run-81-row-60 | run | 60 | Unknown（來源未提供／尚未核對） | CI60 | source_reported_value |
| PSI-101-run-81-row-60 | material | Teflon | Unknown（來源未提供／尚未核對） | CJ60 | source_reported_value |
| PSI-101-run-81-row-60 | AMD | 0.20838028193207944 | Unknown（來源未提供／尚未核對） | CK60 | source_reported_value |
| PSI-101-run-81-row-60 | mass1 caculated with dector 3 | 0.004597621237389494 | Unknown（來源未提供／尚未核對） | CL60 | source_reported_value |
| PSI-101-run-81-row-60 | mass2 both detectors | 0.018992864421797373 | Unknown（來源未提供／尚未核對） | CM60 | source_reported_value |
| PSI-101-run-81-row-60 | Unknown（來源未提供／尚未核對） | 0.8922494117882137 | Unknown（來源未提供／尚未核對） | CO60 | source_formula_cached_result |
| PSI-101-run-81-row-61 | Carousel | 4 | Unknown（來源未提供／尚未核對） | A61 | source_reported_value |
| PSI-101-run-81-row-61 | Sample Type | Teflon | Unknown（來源未提供／尚未核對） | B61 | source_reported_value |
| PSI-101-run-81-row-61 | Sample ID | T06 | Unknown（來源未提供／尚未核對） | C61 | source_reported_value |
| PSI-101-run-81-row-61 | Test ID Number | 34TA | Unknown（來源未提供／尚未核對） | D61 | source_reported_value |
| PSI-101-run-81-row-61 | Position in Carousel | 6 | Unknown（來源未提供／尚未核對） | E61 | source_reported_value |
| PSI-101-run-81-row-61 | SAME # | 81a | Unknown（來源未提供／尚未核對） | F61 | source_reported_value |
| PSI-101-run-81-row-61 | Description | aged | Unknown（來源未提供／尚未核對） | G61 | source_reported_value |
| PSI-101-run-81-row-61 | GMT | 239 | Unknown（來源未提供／尚未核對） | H61 | source_reported_value |
| PSI-101-run-81-row-61 | Date (EST) | 40417 | Unknown（來源未提供／尚未核對） | I61 | source_reported_value |
| PSI-101-run-81-row-61 | Inlet Velocity (cm/sec) | 8.1 | cm/s | K61 | source_reported_value |
| PSI-101-run-81-row-61 | Rt/R0 | 1.45 | dimensionless | L61 | source_reported_value |
| PSI-101-run-81-row-61 | Net Aging  Duration | 559 | Unknown（來源未提供／尚未核對） | R61 | source_reported_value |
| PSI-101-run-81-row-61 | Use STS Detector | n | Unknown（來源未提供／尚未核對） | U61 | source_reported_value |
| PSI-101-run-81-row-61 | Use Comm Diag A | y | Unknown（來源未提供／尚未核對） | V61 | source_reported_value |
| PSI-101-run-81-row-61 | Use Comm Diag B | y | Unknown（來源未提供／尚未核對） | W61 | source_reported_value |
| PSI-101-run-81-row-61 | Diluting A | n | Unknown（來源未提供／尚未核對） | X61 | source_reported_value |
| PSI-101-run-81-row-61 | Diluting B | n | Unknown（來源未提供／尚未核對） | Y61 | source_reported_value |
| PSI-101-run-81-row-61 | Cyclone Inlet on CDA (MPASS) | y | Unknown（來源未提供／尚未核對） | Z61 | source_reported_value |
| PSI-101-run-81-row-61 | Impactor Inlet on CDB | 10 | Unknown（來源未提供／尚未核對） | AA61 | source_reported_value |
| PSI-101-run-81-row-61 | Use P-Trak | y | Unknown（來源未提供／尚未核對） | AB61 | source_reported_value |
| PSI-101-run-81-row-61 | Aerosol Concentration To P-Trak | 0.0519567251427413 | Unknown（來源未提供／尚未核對） | AC61 | source_reported_value |
| PSI-101-run-81-row-61 | secondary agign thermal precip duration | 45 | Unknown（來源未提供／尚未核對） | AP61 | source_reported_value |
| PSI-101-run-81-row-61 | ISS Detector Scatter (volts) | 2.1021720000000004 | V | AR61 | source_reported_value |
| PSI-101-run-81-row-61 | STS Detector (volts) | 0 | V | AS61 | source_reported_value |
| PSI-101-run-81-row-61 | STS Detector offset (volts) | 0 | V | AT61 | source_reported_value |
| PSI-101-run-81-row-61 | Ion A (volts) Mpass_3rd | 0.23783875000000002 | V | AU61 | source_reported_value |
| PSI-101-run-81-row-61 | Ion A offset V0 (volts) | 0.029037475 | V | AV61 | source_reported_value |
| PSI-101-run-81-row-61 | Ion B (volts) | 6.401839999999998 | V | AW61 | source_reported_value |
| PSI-101-run-81-row-61 | Ion B offset V0 (volts) | 4.722350499999999 | V | AX61 | source_reported_value |
| PSI-101-run-81-row-61 | Ptrak (PT/cc) | 33040 | #/cm^3 | AY61 | source_reported_value |
| PSI-101-run-81-row-61 | DustTrak A (mg/m3) Mpass_2nd | 0.33061215 | mg/m^3 | AZ61 | source_reported_value |
| PSI-101-run-81-row-61 | DustTrak A (mg/m3) Mpass_2nd offset | 0.08517456500000001 | mg/m^3 | BA61 | source_reported_value |
| PSI-101-run-81-row-61 | DustTrak B (mg/m3) | 19.779400000000003 | mg/m^3 | BB61 | source_reported_value |
| PSI-101-run-81-row-61 | Ion B Delta (volts) | 1.679489499999999 | V | BC61 | source_formula_cached_result |
| PSI-101-run-81-row-61 | M0 best Diameter (#/cm3) | 920599.7311915328 | #/cm^3 | BD61 | source_formula_cached_result |
| PSI-101-run-81-row-61 | M1 (mm/cm3) | 354.42148985691654 | mm/cm^3 | BE61 | source_formula_cached_result |
| PSI-101-run-81-row-61 |  Mpass_3rd offset and dilution corrected | 0.208801275 | Unknown（來源未提供／尚未核對） | BF61 | source_formula_cached_result |
| PSI-101-run-81-row-61 | DustTrak A (mg/m3) Mpass_2nd  offset, dilution and Gain corrected | 0.061359396249999996 | mg/m^3 | BG61 | source_formula_cached_result |
| PSI-101-run-81-row-61 | DustTrak B calibratred and corrected for dilution (mg/m3) | 44.701444 | mg/m^3 | BH61 | source_formula_cached_result |
| PSI-101-run-81-row-61 | M1/M0 (micro-m)--AMD | 0.38498978203935447 | um | BI61 | source_formula_cached_result |
| PSI-101-run-81-row-61 | Diameter of Average mass (micro-m) | 0.3480244869065179 | um | BJ61 | source_formula_cached_result |
| PSI-101-run-81-row-61 | George's d2,1,  (micro-m) | 0.3308949211021129 | um | BK61 | source_formula_cached_result |
| PSI-101-run-81-row-61 | MPASS 3/2 | 3.4029225800930205 | Unknown（來源未提供／尚未核對） | BL61 | source_formula_cached_result |
| PSI-101-run-81-row-61 | Hatch Choate Sigma g | #NUM! | dimensionless | BM61 | source_formula_cached_result |
| PSI-101-run-81-row-61 | Hatch Choate Dg | #NUM! | Unknown（來源未提供／尚未核對） | BN61 | source_formula_cached_result |
| PSI-101-run-81-row-61 | CPC 100 nm cal, dilution corrected | 920599.7311915328 | Unknown（來源未提供／尚未核對） | BO61 | source_formula_cached_result |
| PSI-101-run-81-row-61 | CPC 600 nm cal, dilution corrected | 905973.7131368486 | Unknown（來源未提供／尚未核對） | BP61 | source_formula_cached_result |
| PSI-101-run-81-row-61 | CPC 1200 nm cal, dilution corrected | 846999.064685048 | Unknown（來源未提供／尚未核對） | BQ61 | source_formula_cached_result |
| PSI-101-run-81-row-61 | Ion B Mment  mm/cm^3 | 354.42148985691654 | mm/cm^3 | BR61 | source_formula_cached_result |
| PSI-101-run-81-row-61 | Ion B X | 0.37278911036136 | Unknown（來源未提供／尚未核對） | BS61 | source_formula_cached_result |
| PSI-101-run-81-row-61 | Dust Trak Cal Factor (Teom/Dusttrak) | 2.26 | Unknown（來源未提供／尚未核對） | BT61 | source_formula_cached_result |
| PSI-101-run-81-row-61 | MPASS Dilution factor | 1 | Unknown（來源未提供／尚未核對） | BU61 | source_formula_cached_result |
| PSI-101-run-81-row-61 | Dust Trak Dilution factor | 1 | Unknown（來源未提供／尚未核對） | BV61 | source_formula_cached_result |
| PSI-101-run-81-row-61 | Particle density g/cc | 2.2 | g/cm^3 | BW61 | source_formula_cached_result |
| PSI-101-run-81-row-61 | T ( C) - Eq. 2 of lrt | 538.4309629381966 | Unknown（來源未提供／尚未核對） | BZ61 | source_reported_value |
| PSI-101-run-81-row-61 | Mass Loss (mg) | 9.71333333333324 | mg | CA61 | source_formula_cached_result |
| PSI-101-run-81-row-61 | Yeild: Dust Trak mass/mass lostt | 0.02761242251201125 | Unknown（來源未提供／尚未核對） | CD61 | source_formula_cached_result |
| PSI-101-run-81-row-61 | run | 61 | Unknown（來源未提供／尚未核對） | CI61 | source_reported_value |
| PSI-101-run-81-row-61 | material | Teflon | Unknown（來源未提供／尚未核對） | CJ61 | source_reported_value |
| PSI-101-run-81-row-61 | AMD | 0.38498978203935447 | Unknown（來源未提供／尚未核對） | CK61 | source_reported_value |
| PSI-101-run-81-row-61 | mass1 caculated with dector 3 | 0.004671018569333017 | Unknown（來源未提供／尚未核對） | CL61 | source_reported_value |
| PSI-101-run-81-row-61 | mass2 both detectors | 0.01939356764411986 | Unknown（來源未提供／尚未核對） | CM61 | source_reported_value |
| PSI-101-run-81-row-61 | Unknown（來源未提供／尚未核對） | 0.8779110847160103 | Unknown（來源未提供／尚未核對） | CO61 | source_formula_cached_result |


你提供的 Excel 對照見 [FACTOR_MAP.md](../FACTOR_MAP.md)。總表是欄位／因子索引，不能替代本試次的實測數值。無法逐欄匹配者保留 Unknown。

### 感測器狀態與執行分率

| 摘要記錄 | 分率角色 | run原值 | 感測器啟用旗標 |
| --- | --- | --- | --- |
| PSI-101-run-81-row-60 | first_or_primary_fraction | 81 | {"Use STS Detector": {"cell": "U60", "value": "n", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "132", "status": "valid", "raw_header": "Use STS Detector", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "U60"}, "evidence_role": "source_reported_value"}, "Use Comm Diag A": {"cell": "V60", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "132", "status": "valid", "raw_header": "Use Comm Diag A", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "V60"}, "evidence_role": "source_reported_value"}, "Use Comm Diag B": {"cell": "W60", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "132", "status": "valid", "raw_header": "Use Comm Diag B", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "W60"}, "evidence_role": "source_reported_value"}, "Use P-Trak": {"cell": "AB60", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "132", "status": "valid", "raw_header": "Use P-Trak", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "AB60"}, "evidence_role": "source_reported_value"}, "STSDetector": {"cell": "AH60", "value": "n", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "132", "status": "valid", "raw_header": "STSDetector", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "AH60"}, "evidence_role": "source_reported_value"}, "Comm Diag A": {"cell": "AI60", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "132", "status": "valid", "raw_header": "Comm Diag A", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "AI60"}, "evidence_role": "source_reported_value"}, "Comm Diag B": {"cell": "AJ60", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "132", "status": "valid", "raw_header": "Comm Diag B", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "AJ60"}, "evidence_role": "source_reported_value"}, "Ues PTrak": {"cell": "AM60", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "132", "status": "valid", "raw_header": "Ues PTrak", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "AM60"}, "evidence_role": "source_reported_value"}} |
| PSI-101-run-81-row-61 | aged_fraction | 81a | {"Use STS Detector": {"cell": "U61", "value": "n", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "306", "status": "valid", "raw_header": "Use STS Detector", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "U61"}, "evidence_role": "source_reported_value"}, "Use Comm Diag A": {"cell": "V61", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "1999", "status": "valid", "raw_header": "Use Comm Diag A", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "V61"}, "evidence_role": "source_reported_value"}, "Use Comm Diag B": {"cell": "W61", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "306", "status": "valid", "raw_header": "Use Comm Diag B", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "W61"}, "evidence_role": "source_reported_value"}, "Use P-Trak": {"cell": "AB61", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "306", "status": "valid", "raw_header": "Use P-Trak", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "AB61"}, "evidence_role": "source_reported_value"}} |


- {"execution_identity": "acquisition_segment_not_proven_independent_generation", "file_id": "PSI-101-3319d7ca308be9e7", "source_rows": 1265, "first_csv_row": 13, "last_csv_row": 1277, "first_time_string": "2010/239/16:05:31", "last_time_string": "2010/239/16:26:35", "state_values": {"TestRunning": ["0", "1"], "12VDCHeaterEnable": ["0", "1"], "HeatingInProgress": ["0", "1"], "PTrakState": ["0", "1", "2", "3", "4", "5", "7"], "DustTrakAState": ["0", "2", "3", "4", "5", "6"], "DustTrakBState": ["0", "2", "3", "4", "5", "6"], "MixingFanPower": ["0", "1"], "PTrakPower": ["0", "1"], "DustTrakAPower": ["0", "1"], "DustTrakBPower": ["0", "1"], "STSDetectorPower": ["0"], "CarouselPower": ["0"], "STSDetectorSelfTest": ["0"], "STSDetectorAlarmReset": ["0", "1"], "STSDetectorAlarm": ["0"], "VideoPower": ["0", "1"], "CameraPower": ["0", "1"], "IlluminationLEDPower": ["0", "1"]}, "minus999_counts": {}}


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

[開啟此試次的矩與來源快取比較](<../viewer/viewer.html?trial=PSI-101-run-81&view=moments>) · [檢查時間訊號／感測器狀態](<../viewer/viewer.html?trial=PSI-101-run-81&view=traces>)

展示狀態必須區分來源計算重現、同源反演重建、條件診斷、作者模擬與獨立預測。缺單位、越域或未使用的實驗目標不足時，該比較顯示 Unknown／Invalid，而非補出曲線。詳細公式見 [MODELS.md](../MODELS.md)。

### 本試次已執行的固定公式結果

| 來源記錄 | 輸出量 | 公式值 | 來源快取 | 公式減快取 | 比較角色 | 整體資格狀態 |
| --- | --- | --- | --- | --- | --- | --- |
| PSI-101-run-81-row-60 | d_count_um | 0.20838028193207944 | 0.20838028193207944 | 0.0 | same_source_reconstruction | unknown |
| PSI-101-run-81-row-60 | dm_um | 0.25134398476976677 | 0.2513439847697668 | -5.551115123125783e-17 | same_source_reconstruction | unknown |
| PSI-101-run-81-row-61 | d_count_um | 0.38498978203935447 | 0.38498978203935447 | 0.0 | same_source_reconstruction | invalid |
| PSI-101-run-81-row-61 | dm_um | 0.34802448690651777 | 0.3480244869065179 | -1.1102230246251565e-16 | same_source_reconstruction | invalid |


上述差值僅檢查已知公式與來源快取的數值重現，不是量測誤差、消防安全誤差或獨立模型預測分數。密度／校正等來源假設與各輸出的可計算性須保留；整體資格 Unknown 不會被改成安全 Pass。

- {"record_id": "PSI-101-run-81-row-60", "equation_ids": ["SMOKE-MOMENT-RATIOS", "SMOKE-LOGNORMAL-INVERSE"], "eligible_role": "same_source_equation_diagnostic_only", "raw_inversion_validation": false, "independent_validation_target": false}
- {"record_id": "PSI-101-run-81-row-61", "equation_ids": ["SMOKE-MOMENT-RATIOS", "SMOKE-LOGNORMAL-INVERSE"], "eligible_role": "same_source_equation_diagnostic_only", "raw_inversion_validation": false, "independent_validation_target": false}


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
| [PSI-101-3319d7ca308be9e7](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/01_實驗資料/第一批下載/PSI-101_SAME-R/Raw Data/PSI-101_Raw Data_HKPData_gmt239_4.csv>) | Raw Data | method=\["Original CSV TestNumber field; acquisition day/time retained"\]; status=\["source_identity_confirmed"\] | 3319d7ca308be9e7c3caa4393622bea086ba368f387a5ca5a5253033b7a47111 |
| [PSI-101-6d3a539ccf425b1f](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/01_實驗資料/第一批下載/PSI-101_SAME-R/Analyzed Data/PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx>) | Analyzed Data | method=\["canonical summary row SAME R Results!60", "canonical summary row SAME R Results!61"\]; status=\["source_identity_confirmed", "source_identity_confirmed"\] | 6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218 |
| [PSI-101-28c66a39a92da9e8](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/01_實驗資料/第一批下載/PSI-101_SAME-R/Analyzed Data/PSI-101_Analyzed Data_2010_239_16_teflon_run81.xls>) | Analyzed Data | method=\["literal filename run/test token"\]; status=\["filename_candidate_not_fully_content_joined"\] | 28c66a39a92da9e8111c814a4f9ca598f9f173f1f7008503ffd7d63da1e4c568 |


結構化完整記錄：`qa/trial_records.json` 的 `PSI-101-run-81`。原始資料只讀；本 Markdown 不改寫來源公式、快取或身份衝突。
