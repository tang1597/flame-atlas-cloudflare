# PSI-101-run-82 煙霧資料與研究判讀

本卡的單位是來源身份分組的一個試次。新鮮／老化分率、重複排序視圖及感測器時間樣本不自動算成新的火災。

## 身份與資料範圍

| 研究 | 來源身份 | 材料標籤 | 日期原值 | 摘要觀測列數 | 可連結檔案數 |
| --- | --- | --- | --- | --- | --- |
| PSI-101 | canonical_summary_group_not_independent_execution_count | \[{"raw": "Lampwick", "canonical_family": "Lampwick", "source_locator": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "B62"}}\] | \[{"date_value": 40416, "date_cell": "I62", "gmt_value": 239, "gmt_cell": "H62", "source_sheet": "SAME R Results", "date_encoding": "Excel serial when numeric; date-year comes from source style/context, not imputed from GMT"}, {"date_value": 40417, "date_cell": "I63", "gmt_value": 239, "gmt_cell": "H63", "source_sheet": "SAME R Results", "date_encoding": "Excel serial when numeric; date-year comes from source style/context, not imputed from GMT"}\] | 2 | 6 |

- {"type": "fraction_date_difference", "source_date_values": [40416, 40417], "resolution": "Source dates retained per fraction; not silently merged or interpreted as separate smoke generations."}


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


[開啟矩公式與TEM實驗方法對照](<../viewer/viewer.html?trial=PSI-101-run-82&view=methods>)。TEM是獨立的量測技術，但這裡使用相同飛行樣本；校正／密度／選模的保留樣本獨立性未證實，不能稱為獨立預測驗證。完整血緣及印列差異見 [PUBLICATION_DATA_BINDINGS.md](../PUBLICATION_DATA_BINDINGS.md)。

## 使用的資料部分與參數因子

下列快取值依原欄位保留。來源計算量、量測輸入、設定與狀態旗標分列；來源公式未被修正或重新擬合。

| 來源記錄 | 欄位／因子 | 原始值或快取 | 單位 | 儲存格／來源定位 | 量的角色 |
| --- | --- | --- | --- | --- | --- |
| PSI-101-run-82-row-62 | Carousel | 4 | Unknown（來源未提供／尚未核對） | A62 | source_reported_value |
| PSI-101-run-82-row-62 | Sample Type | Lampwick | Unknown（來源未提供／尚未核對） | B62 | source_reported_value |
| PSI-101-run-82-row-62 | Sample ID | L17 | Unknown（來源未提供／尚未核對） | C62 | source_reported_value |
| PSI-101-run-82-row-62 | Test ID Number | 35 L | Unknown（來源未提供／尚未核對） | D62 | source_reported_value |
| PSI-101-run-82-row-62 | Position in Carousel | 2 | Unknown（來源未提供／尚未核對） | E62 | source_reported_value |
| PSI-101-run-82-row-62 | SAME # | 82 | Unknown（來源未提供／尚未核對） | F62 | source_reported_value |
| PSI-101-run-82-row-62 | Description | Mid temp aging | Unknown（來源未提供／尚未核對） | G62 | source_reported_value |
| PSI-101-run-82-row-62 | GMT | 239 | Unknown（來源未提供／尚未核對） | H62 | source_reported_value |
| PSI-101-run-82-row-62 | Date (EST) | 40416 | Unknown（來源未提供／尚未核對） | I62 | source_reported_value |
| PSI-101-run-82-row-62 | Inlet Velocity (cm/sec) | 8.1 | cm/s | K62 | source_reported_value |
| PSI-101-run-82-row-62 | Rt/R0 | 1.265 | dimensionless | L62 | source_reported_value |
| PSI-101-run-82-row-62 | Duration (sec) | 60 | s | M62 | source_reported_value |
| PSI-101-run-82-row-62 | Primary Aging Duration (sec) | 11 | s | N62 | source_reported_value |
| PSI-101-run-82-row-62 | Primary Mixing Duration (sec) | 8 | s | O62 | source_reported_value |
| PSI-101-run-82-row-62 | PreAge Thermal Precipitator | n | Unknown（來源未提供／尚未核對） | P62 | source_reported_value |
| PSI-101-run-82-row-62 | PreAge Thermal Precipitator Duration | n | Unknown（來源未提供／尚未核對） | Q62 | source_reported_value |
| PSI-101-run-82-row-62 | Net Aging  Duration | 39 | Unknown（來源未提供／尚未核對） | R62 | source_reported_value |
| PSI-101-run-82-row-62 | Primary Aging Therm Precip | y | Unknown（來源未提供／尚未核對） | S62 | source_reported_value |
| PSI-101-run-82-row-62 | Primary Aging Therm Precip Duration | 90 | Unknown（來源未提供／尚未核對） | T62 | source_reported_value |
| PSI-101-run-82-row-62 | Use STS Detector | n | Unknown（來源未提供／尚未核對） | U62 | source_reported_value |
| PSI-101-run-82-row-62 | Use Comm Diag A | y | Unknown（來源未提供／尚未核對） | V62 | source_reported_value |
| PSI-101-run-82-row-62 | Use Comm Diag B | y | Unknown（來源未提供／尚未核對） | W62 | source_reported_value |
| PSI-101-run-82-row-62 | Diluting A | n | Unknown（來源未提供／尚未核對） | X62 | source_reported_value |
| PSI-101-run-82-row-62 | Diluting B | y | Unknown（來源未提供／尚未核對） | Y62 | source_reported_value |
| PSI-101-run-82-row-62 | Cyclone Inlet on CDA (MPASS) | y | Unknown（來源未提供／尚未核對） | Z62 | source_reported_value |
| PSI-101-run-82-row-62 | Impactor Inlet on CDB | 10 | Unknown（來源未提供／尚未核對） | AA62 | source_reported_value |
| PSI-101-run-82-row-62 | Use P-Trak | y | Unknown（來源未提供／尚未核對） | AB62 | source_reported_value |
| PSI-101-run-82-row-62 | Aerosol Concentration To P-Trak | 0.03852706928546 | Unknown（來源未提供／尚未核對） | AC62 | source_reported_value |
| PSI-101-run-82-row-62 | Secondary Diagnostics Volume %  | 58 | % | AE62 | source_reported_value |
| PSI-101-run-82-row-62 | Secondary Aging Duration (sec) | 480 | s | AF62 | source_reported_value |
| PSI-101-run-82-row-62 | Secondary Mixing Duration (sec) | 0 | s | AG62 | source_reported_value |
| PSI-101-run-82-row-62 | STSDetector | n | Unknown（來源未提供／尚未核對） | AH62 | source_reported_value |
| PSI-101-run-82-row-62 | Comm Diag A | y | Unknown（來源未提供／尚未核對） | AI62 | source_reported_value |
| PSI-101-run-82-row-62 | Comm Diag B | y | Unknown（來源未提供／尚未核對） | AJ62 | source_reported_value |
| PSI-101-run-82-row-62 | Diluting A | n | Unknown（來源未提供／尚未核對） | AK62 | source_reported_value |
| PSI-101-run-82-row-62 | Diluting B | y | Unknown（來源未提供／尚未核對） | AL62 | source_reported_value |
| PSI-101-run-82-row-62 | Ues PTrak | y | Unknown（來源未提供／尚未核對） | AM62 | source_reported_value |
| PSI-101-run-82-row-62 | Aerosol Concentration To P-Trak | 0.03852706928546 | Unknown（來源未提供／尚未核對） | AN62 | source_formula_cached_result |
| PSI-101-run-82-row-62 | ISS Detector Scatter (volts) | 6.2503665 | V | AR62 | source_reported_value |
| PSI-101-run-82-row-62 | STS Detector (volts) | 0 | V | AS62 | source_reported_value |
| PSI-101-run-82-row-62 | STS Detector offset (volts) | 0 | V | AT62 | source_reported_value |
| PSI-101-run-82-row-62 | Ion A (volts) Mpass_3rd | 2.6140444999999994 | V | AU62 | source_reported_value |
| PSI-101-run-82-row-62 | Ion A offset V0 (volts) | 0.026229855000000003 | V | AV62 | source_reported_value |
| PSI-101-run-82-row-62 | Ion B (volts) | 6.784058 | V | AW62 | source_reported_value |
| PSI-101-run-82-row-62 | Ion B offset V0 (volts) | 4.7105095 | V | AX62 | source_reported_value |
| PSI-101-run-82-row-62 | Ptrak (PT/cc) | 85905 | #/cm^3 | AY62 | source_reported_value |
| PSI-101-run-82-row-62 | DustTrak A (mg/m3) Mpass_2nd | 2.3956139999999997 | mg/m^3 | AZ62 | source_reported_value |
| PSI-101-run-82-row-62 | DustTrak A (mg/m3) Mpass_2nd offset | 0.08052063999999999 | mg/m^3 | BA62 | source_reported_value |
| PSI-101-run-82-row-62 | DustTrak B (mg/m3) | 60.405999999999985 | mg/m^3 | BB62 | source_reported_value |
| PSI-101-run-82-row-62 | Ion B Delta (volts) | 2.0735485000000002 | V | BC62 | source_formula_cached_result |
| PSI-101-run-82-row-62 | M0 best Diameter (#/cm3) | 3463686.403480526 | #/cm^3 | BD62 | source_formula_cached_result |
| PSI-101-run-82-row-62 | M1 (mm/cm3) | 481.1580592236563 | mm/cm^3 | BE62 | source_formula_cached_result |
| PSI-101-run-82-row-62 |  Mpass_3rd offset and dilution corrected | 2.5878146449999995 | Unknown（來源未提供／尚未核對） | BF62 | source_formula_cached_result |
| PSI-101-run-82-row-62 | DustTrak A (mg/m3) Mpass_2nd  offset, dilution and Gain corrected | 0.5787733399999999 | mg/m^3 | BG62 | source_formula_cached_result |
| PSI-101-run-82-row-62 | DustTrak B calibratred and corrected for dilution (mg/m3) | 44.1112730601966 | mg/m^3 | BH62 | source_formula_cached_result |
| PSI-101-run-82-row-62 | M1/M0 (micro-m)--AMD | 0.13891501803978532 | um | BI62 | source_formula_cached_result |
| PSI-101-run-82-row-62 | Diameter of Average mass (micro-m) | 0.28973711732419516 | um | BJ62 | source_formula_cached_result |
| PSI-101-run-82-row-62 | George's d2,1,  (micro-m) | 0.4184384671617851 | um | BK62 | source_formula_cached_result |
| PSI-101-run-82-row-62 | MPASS 3/2 | 4.471205679584343 | Unknown（來源未提供／尚未核對） | BL62 | source_formula_cached_result |
| PSI-101-run-82-row-62 | Hatch Choate Sigma g | 2.356992697809274 | dimensionless | BM62 | source_formula_cached_result |
| PSI-101-run-82-row-62 | Hatch Choate Dg | 0.09618818545266336 | Unknown（來源未提供／尚未核對） | BN62 | source_formula_cached_result |
| PSI-101-run-82-row-62 | CPC 100 nm cal, dilution corrected | 3463686.403480526 | Unknown（來源未提供／尚未核對） | BO62 | source_formula_cached_result |
| PSI-101-run-82-row-62 | CPC 600 nm cal, dilution corrected | 3412402.5909133023 | Unknown（來源未提供／尚未核對） | BP62 | source_formula_cached_result |
| PSI-101-run-82-row-62 | CPC 1200 nm cal, dilution corrected | 3087742.6113980534 | Unknown（來源未提供／尚未核對） | BQ62 | source_formula_cached_result |
| PSI-101-run-82-row-62 | Ion B Mment  mm/cm^3 | 481.1580592236563 | mm/cm^3 | BR62 | source_formula_cached_result |
| PSI-101-run-82-row-62 | Ion B X | 0.46025670336500046 | Unknown（來源未提供／尚未核對） | BS62 | source_formula_cached_result |
| PSI-101-run-82-row-62 | Dust Trak Cal Factor (Teom/Dusttrak) | 0.28 | Unknown（來源未提供／尚未核對） | BT62 | source_formula_cached_result |
| PSI-101-run-82-row-62 | MPASS Dilution factor | 1 | Unknown（來源未提供／尚未核對） | BU62 | source_formula_cached_result |
| PSI-101-run-82-row-62 | Dust Trak Dilution factor | 2.608023390545204 | Unknown（來源未提供／尚未核對） | BV62 | source_formula_cached_result |
| PSI-101-run-82-row-62 | Particle density g/cc | 1 | g/cm^3 | BW62 | source_formula_cached_result |
| PSI-101-run-82-row-62 | Dilution ratio for Mpass, total flow 1.68576 LPM | 2.6205217898830857 | Unknown（來源未提供／尚未核對） | BX62 | source_reported_value |
| PSI-101-run-82-row-62 | Dilution ratio for DustTrak B, total flow 1.69076 LPM | 2.608023390545204 | Unknown（來源未提供／尚未核對） | BY62 | source_reported_value |
| PSI-101-run-82-row-62 | T ( C) - Eq. 2 of lrt | 282.5836772631244 | Unknown（來源未提供／尚未核對） | BZ62 | source_reported_value |
| PSI-101-run-82-row-62 | Mass Loss (mg) | 1.583333333333381 | mg | CA62 | source_reported_value |
| PSI-101-run-82-row-62 | Test Number |  35L | Unknown（來源未提供／尚未核對） | CB62 | source_reported_value |
| PSI-101-run-82-row-62 | GMT | 239 | Unknown（來源未提供／尚未核對） | CC62 | source_reported_value |
| PSI-101-run-82-row-62 | Yeild: Dust Trak mass/mass lostt | 0.16715850843863472 | Unknown（來源未提供／尚未核對） | CD62 | source_formula_cached_result |
| PSI-101-run-82-row-62 | run | 62 | Unknown（來源未提供／尚未核對） | CI62 | source_reported_value |
| PSI-101-run-82-row-62 | material | Lampwick | Unknown（來源未提供／尚未核對） | CJ62 | source_reported_value |
| PSI-101-run-82-row-62 | AMD | 0.13891501803978532 | Unknown（來源未提供／尚未核對） | CK62 | source_reported_value |
| PSI-101-run-82-row-62 | mass1 caculated with dector 3 | 0.0586656078020811 | Unknown（來源未提供／尚未核對） | CL62 | source_reported_value |
| PSI-101-run-82-row-62 | mass2 both detectors | 0.029331836379530463 | Unknown（來源未提供／尚未核對） | CM62 | source_reported_value |
| PSI-101-run-82-row-62 | Unknown（來源未提供／尚未核對） | 0.989965796297653 | Unknown（來源未提供／尚未核對） | CO62 | source_formula_cached_result |
| PSI-101-run-82-row-63 | Carousel | 4 | Unknown（來源未提供／尚未核對） | A63 | source_reported_value |
| PSI-101-run-82-row-63 | Sample Type | Lampwick | Unknown（來源未提供／尚未核對） | B63 | source_reported_value |
| PSI-101-run-82-row-63 | Sample ID | L17 | Unknown（來源未提供／尚未核對） | C63 | source_reported_value |
| PSI-101-run-82-row-63 | Test ID Number | 35LA | Unknown（來源未提供／尚未核對） | D63 | source_reported_value |
| PSI-101-run-82-row-63 | Position in Carousel | 2 | Unknown（來源未提供／尚未核對） | E63 | source_reported_value |
| PSI-101-run-82-row-63 | SAME # | 82a | Unknown（來源未提供／尚未核對） | F63 | source_reported_value |
| PSI-101-run-82-row-63 | Description | aged | Unknown（來源未提供／尚未核對） | G63 | source_reported_value |
| PSI-101-run-82-row-63 | GMT | 239 | Unknown（來源未提供／尚未核對） | H63 | source_reported_value |
| PSI-101-run-82-row-63 | Date (EST) | 40417 | Unknown（來源未提供／尚未核對） | I63 | source_reported_value |
| PSI-101-run-82-row-63 | Inlet Velocity (cm/sec) | 8.1 | cm/s | K63 | source_reported_value |
| PSI-101-run-82-row-63 | Rt/R0 | 1.265 | dimensionless | L63 | source_reported_value |
| PSI-101-run-82-row-63 | Net Aging  Duration | 579.3333333333334 | Unknown（來源未提供／尚未核對） | R63 | source_reported_value |
| PSI-101-run-82-row-63 | Use STS Detector | n | Unknown（來源未提供／尚未核對） | U63 | source_reported_value |
| PSI-101-run-82-row-63 | Use Comm Diag A | y | Unknown（來源未提供／尚未核對） | V63 | source_reported_value |
| PSI-101-run-82-row-63 | Use Comm Diag B | y | Unknown（來源未提供／尚未核對） | W63 | source_reported_value |
| PSI-101-run-82-row-63 | Diluting A | n | Unknown（來源未提供／尚未核對） | X63 | source_reported_value |
| PSI-101-run-82-row-63 | Diluting B | y | Unknown（來源未提供／尚未核對） | Y63 | source_reported_value |
| PSI-101-run-82-row-63 | Cyclone Inlet on CDA (MPASS) | y | Unknown（來源未提供／尚未核對） | Z63 | source_reported_value |
| PSI-101-run-82-row-63 | Impactor Inlet on CDB | 10 | Unknown（來源未提供／尚未核對） | AA63 | source_reported_value |
| PSI-101-run-82-row-63 | Use P-Trak | y | Unknown（來源未提供／尚未核對） | AB63 | source_reported_value |
| PSI-101-run-82-row-63 | Aerosol Concentration To P-Trak | 0.03852706928546 | Unknown（來源未提供／尚未核對） | AC63 | source_reported_value |
| PSI-101-run-82-row-63 | secondary agign thermal precip duration | 90 | Unknown（來源未提供／尚未核對） | AP63 | source_reported_value |
| PSI-101-run-82-row-63 | ISS Detector Scatter (volts) | 6.253204500000001 | V | AR63 | source_reported_value |
| PSI-101-run-82-row-63 | STS Detector (volts) | 0 | V | AS63 | source_reported_value |
| PSI-101-run-82-row-63 | STS Detector offset (volts) | 0 | V | AT63 | source_reported_value |
| PSI-101-run-82-row-63 | Ion A (volts) Mpass_3rd | 2.4960774999999997 | V | AU63 | source_reported_value |
| PSI-101-run-82-row-63 | Ion A offset V0 (volts) | 0.08370973000000001 | V | AV63 | source_reported_value |
| PSI-101-run-82-row-63 | Ion B (volts) | 6.268324999999999 | V | AW63 | source_reported_value |
| PSI-101-run-82-row-63 | Ion B offset V0 (volts) | 4.7524560000000005 | V | AX63 | source_reported_value |
| PSI-101-run-82-row-63 | Ptrak (PT/cc) | 35625 | #/cm^3 | AY63 | source_reported_value |
| PSI-101-run-82-row-63 | DustTrak A (mg/m3) Mpass_2nd | 2.2586815000000002 | mg/m^3 | AZ63 | source_reported_value |
| PSI-101-run-82-row-63 | DustTrak A (mg/m3) Mpass_2nd offset | 0.13061530000000002 | mg/m^3 | BA63 | source_reported_value |
| PSI-101-run-82-row-63 | DustTrak B (mg/m3) | 55.973349999999996 | mg/m^3 | BB63 | source_reported_value |
| PSI-101-run-82-row-63 | Ion B Delta (volts) | 1.5158689999999986 | V | BC63 | source_formula_cached_result |
| PSI-101-run-82-row-63 | M0 best Diameter (#/cm3) | 1343413.4028339714 | #/cm^3 | BD63 | source_formula_cached_result |
| PSI-101-run-82-row-63 | M1 (mm/cm3) | 309.1324727835684 | mm/cm^3 | BE63 | source_formula_cached_result |
| PSI-101-run-82-row-63 |  Mpass_3rd offset and dilution corrected | 2.41236777 | Unknown（來源未提供／尚未核對） | BF63 | source_formula_cached_result |
| PSI-101-run-82-row-63 | DustTrak A (mg/m3) Mpass_2nd  offset, dilution and Gain corrected | 0.53201655 | mg/m^3 | BG63 | source_formula_cached_result |
| PSI-101-run-82-row-63 | DustTrak B calibratred and corrected for dilution (mg/m3) | 40.26461338111957 | mg/m^3 | BH63 | source_formula_cached_result |
| PSI-101-run-82-row-63 | M1/M0 (micro-m)--AMD | 0.2301097131615957 | um | BI63 | source_formula_cached_result |
| PSI-101-run-82-row-63 | Diameter of Average mass (micro-m) | 0.3853941144913613 | um | BJ63 | source_formula_cached_result |
| PSI-101-run-82-row-63 | George's d2,1,  (micro-m) | 0.49875830643636493 | um | BK63 | source_formula_cached_result |
| PSI-101-run-82-row-63 | MPASS 3/2 | 4.534384823178902 | Unknown（來源未提供／尚未核對） | BL63 | source_formula_cached_result |
| PSI-101-run-82-row-63 | Hatch Choate Sigma g | 2.0505944091004547 | dimensionless | BM63 | source_formula_cached_result |
| PSI-101-run-82-row-63 | Hatch Choate Dg | 0.17780742294482293 | Unknown（來源未提供／尚未核對） | BN63 | source_formula_cached_result |
| PSI-101-run-82-row-63 | CPC 100 nm cal, dilution corrected | 1343413.4028339714 | Unknown（來源未提供／尚未核對） | BO63 | source_formula_cached_result |
| PSI-101-run-82-row-63 | CPC 600 nm cal, dilution corrected | 1322145.8884552114 | Unknown（來源未提供／尚未核對） | BP63 | source_formula_cached_result |
| PSI-101-run-82-row-63 | CPC 1200 nm cal, dilution corrected | 1234001.2881006338 | Unknown（來源未提供／尚未核對） | BQ63 | source_formula_cached_result |
| PSI-101-run-82-row-63 | Ion B Mment  mm/cm^3 | 309.1324727835684 | mm/cm^3 | BR63 | source_formula_cached_result |
| PSI-101-run-82-row-63 | Ion B X | 0.336470966882713 | Unknown（來源未提供／尚未核對） | BS63 | source_formula_cached_result |
| PSI-101-run-82-row-63 | Dust Trak Cal Factor (Teom/Dusttrak) | 0.28 | Unknown（來源未提供／尚未核對） | BT63 | source_formula_cached_result |
| PSI-101-run-82-row-63 | MPASS Dilution factor | 1 | Unknown（來源未提供／尚未核對） | BU63 | source_formula_cached_result |
| PSI-101-run-82-row-63 | Dust Trak Dilution factor | 2.569118886878409 | Unknown（來源未提供／尚未核對） | BV63 | source_formula_cached_result |
| PSI-101-run-82-row-63 | Particle density g/cc | 1 | g/cm^3 | BW63 | source_formula_cached_result |
| PSI-101-run-82-row-63 | Dilution ratio for Mpass, total flow 1.68576 LPM | 2.5811315764252223 | Unknown（來源未提供／尚未核對） | BX63 | source_reported_value |
| PSI-101-run-82-row-63 | Dilution ratio for DustTrak B, total flow 1.69076 LPM | 2.569118886878409 | Unknown（來源未提供／尚未核對） | BY63 | source_reported_value |
| PSI-101-run-82-row-63 | T ( C) - Eq. 2 of lrt | 282.5836772631244 | Unknown（來源未提供／尚未核對） | BZ63 | source_reported_value |
| PSI-101-run-82-row-63 | Mass Loss (mg) | 1.583333333333381 | mg | CA63 | source_formula_cached_result |
| PSI-101-run-82-row-63 | Yeild: Dust Trak mass/mass lostt | 0.15258169281265901 | Unknown（來源未提供／尚未核對） | CD63 | source_formula_cached_result |
| PSI-101-run-82-row-63 | run | 63 | Unknown（來源未提供／尚未核對） | CI63 | source_reported_value |
| PSI-101-run-82-row-63 | material | Lampwick | Unknown（來源未提供／尚未核對） | CJ63 | source_reported_value |
| PSI-101-run-82-row-63 | AMD | 0.2301097131615957 | Unknown（來源未提供／尚未核對） | CK63 | source_reported_value |
| PSI-101-run-82-row-63 | mass1 caculated with dector 3 | 0.05991285070009341 | Unknown（來源未提供／尚未核對） | CL63 | source_reported_value |
| PSI-101-run-82-row-63 | mass2 both detectors | 0.029507601227128227 | Unknown（來源未提供／尚未核對） | CM63 | source_reported_value |
| PSI-101-run-82-row-63 | Unknown（來源未提供／尚未核對） | 0.9664634892145777 | Unknown（來源未提供／尚未核對） | CO63 | source_formula_cached_result |


你提供的 Excel 對照見 [FACTOR_MAP.md](../FACTOR_MAP.md)。總表是欄位／因子索引，不能替代本試次的實測數值。無法逐欄匹配者保留 Unknown。

### 感測器狀態與執行分率

| 摘要記錄 | 分率角色 | run原值 | 感測器啟用旗標 |
| --- | --- | --- | --- |
| PSI-101-run-82-row-62 | first_or_primary_fraction | 82 | {"Use STS Detector": {"cell": "U62", "value": "n", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "132", "status": "valid", "raw_header": "Use STS Detector", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "U62"}, "evidence_role": "source_reported_value"}, "Use Comm Diag A": {"cell": "V62", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "132", "status": "valid", "raw_header": "Use Comm Diag A", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "V62"}, "evidence_role": "source_reported_value"}, "Use Comm Diag B": {"cell": "W62", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "132", "status": "valid", "raw_header": "Use Comm Diag B", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "W62"}, "evidence_role": "source_reported_value"}, "Use P-Trak": {"cell": "AB62", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "132", "status": "valid", "raw_header": "Use P-Trak", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "AB62"}, "evidence_role": "source_reported_value"}, "STSDetector": {"cell": "AH62", "value": "n", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "132", "status": "valid", "raw_header": "STSDetector", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "AH62"}, "evidence_role": "source_reported_value"}, "Comm Diag A": {"cell": "AI62", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "132", "status": "valid", "raw_header": "Comm Diag A", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "AI62"}, "evidence_role": "source_reported_value"}, "Comm Diag B": {"cell": "AJ62", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "132", "status": "valid", "raw_header": "Comm Diag B", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "AJ62"}, "evidence_role": "source_reported_value"}, "Ues PTrak": {"cell": "AM62", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "132", "status": "valid", "raw_header": "Ues PTrak", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "AM62"}, "evidence_role": "source_reported_value"}} |
| PSI-101-run-82-row-63 | aged_fraction | 82a | {"Use STS Detector": {"cell": "U63", "value": "n", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "306", "status": "valid", "raw_header": "Use STS Detector", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "U63"}, "evidence_role": "source_reported_value"}, "Use Comm Diag A": {"cell": "V63", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "306", "status": "valid", "raw_header": "Use Comm Diag A", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "V63"}, "evidence_role": "source_reported_value"}, "Use Comm Diag B": {"cell": "W63", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "306", "status": "valid", "raw_header": "Use Comm Diag B", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "W63"}, "evidence_role": "source_reported_value"}, "Use P-Trak": {"cell": "AB63", "value": "y", "formula": null, "raw_xml_formula": null, "formula_attributes": null, "type": "s", "style_id": "306", "status": "valid", "raw_header": "Use P-Trak", "unit": null, "source_ref": {"file_id": "PSI-101-6d3a539ccf425b1f", "path": "C:\\Users\\User\\Documents\\ChatGPT\\Nasa Hackathon\\NASA_同事分享包_20261114\\01_實驗資料\\第一批下載\\PSI-101_SAME-R\\Analyzed Data\\PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx", "sha256": "6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218", "sheet": "SAME R Results", "cell": "AB63"}, "evidence_role": "source_reported_value"}} |


- {"execution_identity": "acquisition_segment_not_proven_independent_generation", "file_id": "PSI-101-03475608d80c6be6", "source_rows": 1586, "first_csv_row": 15, "last_csv_row": 1600, "first_time_string": "2010/239/16:35:10", "last_time_string": "2010/239/17:03:45", "state_values": {"TestRunning": ["0", "1"], "12VDCHeaterEnable": ["0", "1"], "HeatingInProgress": ["0", "1"], "PTrakState": ["0", "2", "3", "4", "5", "7"], "DustTrakAState": ["0", "2", "3", "4", "5", "6"], "DustTrakBState": ["0", "2", "3", "4", "5", "6"], "MixingFanPower": ["0", "1"], "PTrakPower": ["0", "1"], "DustTrakAPower": ["0", "1"], "DustTrakBPower": ["0", "1"], "STSDetectorPower": ["0"], "CarouselPower": ["0"], "STSDetectorSelfTest": ["0"], "STSDetectorAlarmReset": ["0", "1"], "STSDetectorAlarm": ["0"], "VideoPower": ["0", "1"], "CameraPower": ["0", "1"], "IlluminationLEDPower": ["0", "1"]}, "minus999_counts": {"PTrakMeasurement(PtPerCC)": 3}}


## 多個結論與適用範圍

| 判讀 | 證據層次 | 共同與不同之處 |
| --- | --- | --- |
| 此身份分組含 2 筆來源摘要記錄；分率／執行身份仍以來源標籤與衝突表為準。 | 資料稽核結論 | 同 baseRun 不代表每筆都是獨立產煙事件。 |
| 可追到上表數值的欄位共有 148 項；單位未提供時不轉換、不補 0。 | 原始欄位／快取判讀 | 同名粒徑可能來自不同矩、密度與儀器量測範圍，必須先對定義。 |
| 本試次與出版品的逐列身份對應，以明列的 exact_trial_ids 為限；其他連結僅為 campaign context。 | 文獻連結邊界 | 共用研究、材料或儀器不足以認定使用同一數據。 |
| 矩反演／PSD重建若重用了原量測矩，只能視為計算診斷，不能再把它當獨立預測成功。 | 物理／識別限制 | 需要未參與反演的尺寸分布、儀器響應或另一事件才能驗證外推。 |

Unknown；此處沒有補入推測值。


## 公式結果與實驗值的視覺化工具

程式名稱：`tools/smoke_evidence/physics.py`、`tools/smoke_evidence/viewer.js`；入口 `viewer.html`。

[開啟此試次的矩與來源快取比較](<../viewer/viewer.html?trial=PSI-101-run-82&view=moments>) · [檢查時間訊號／感測器狀態](<../viewer/viewer.html?trial=PSI-101-run-82&view=traces>)

展示狀態必須區分來源計算重現、同源反演重建、條件診斷、作者模擬與獨立預測。缺單位、越域或未使用的實驗目標不足時，該比較顯示 Unknown／Invalid，而非補出曲線。詳細公式見 [MODELS.md](../MODELS.md)。

### 本試次已執行的固定公式結果

| 來源記錄 | 輸出量 | 公式值 | 來源快取 | 公式減快取 | 比較角色 | 整體資格狀態 |
| --- | --- | --- | --- | --- | --- | --- |
| PSI-101-run-82-row-62 | d_count_um | 0.1389150180397853 | 0.13891501803978532 | -2.7755575615628914e-17 | same_source_reconstruction | unknown |
| PSI-101-run-82-row-62 | dm_um | 0.28973711732419516 | 0.28973711732419516 | 0.0 | same_source_reconstruction | unknown |
| PSI-101-run-82-row-63 | d_count_um | 0.23010971316159573 | 0.2301097131615957 | 2.7755575615628914e-17 | same_source_reconstruction | unknown |
| PSI-101-run-82-row-63 | dm_um | 0.38539411449136135 | 0.3853941144913613 | 5.551115123125783e-17 | same_source_reconstruction | unknown |


上述差值僅檢查已知公式與來源快取的數值重現，不是量測誤差、消防安全誤差或獨立模型預測分數。密度／校正等來源假設與各輸出的可計算性須保留；整體資格 Unknown 不會被改成安全 Pass。

- {"record_id": "PSI-101-run-82-row-62", "equation_ids": ["SMOKE-MOMENT-RATIOS", "SMOKE-LOGNORMAL-INVERSE"], "eligible_role": "same_source_equation_diagnostic_only", "raw_inversion_validation": false, "independent_validation_target": false}
- {"record_id": "PSI-101-run-82-row-63", "equation_ids": ["SMOKE-MOMENT-RATIOS", "SMOKE-LOGNORMAL-INVERSE"], "eligible_role": "same_source_equation_diagnostic_only", "raw_inversion_validation": false, "independent_validation_target": false}


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
| [PSI-101-03475608d80c6be6](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/01_實驗資料/第一批下載/PSI-101_SAME-R/Raw Data/PSI-101_Raw Data_HKPData_gmt239_5.csv>) | Raw Data | method=\["Original CSV TestNumber field; acquisition day/time retained"\]; status=\["source_identity_confirmed"\] | 03475608d80c6be69e33b0592191686f51c4b4d746b1d1a07c017cf0278da0ba |
| [PSI-101-6d3a539ccf425b1f](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/01_實驗資料/第一批下載/PSI-101_SAME-R/Analyzed Data/PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx>) | Analyzed Data | method=\["canonical summary row SAME R Results!62", "canonical summary row SAME R Results!63"\]; status=\["source_identity_confirmed", "source_identity_confirmed"\] | 6d3a539ccf425b1fa8edc19cc75d828f57d650c7ce734d4e7aa686fea9593218 |
| [PSI-101-95ed4293585a3068](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/01_實驗資料/第一批下載/PSI-101_SAME-R/Analyzed Data/PSI-101_Analyzed Data_2010_239_16_lampwick_run82.xls>) | Analyzed Data | method=\["literal filename run/test token"\]; status=\["filename_candidate_not_fully_content_joined"\] | 95ed4293585a30680c48f6d60b62617cbe1795fab7de81839036c4201d3f94ed |
| [PSI-101-e2f0d8c27a6b7b29](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/簡報與海報/補下載/PSI-101/Raw Data/455857a34149eeda_PSI-101_Raw Data_82 Preage 35 L Lampwick.pptx>) | Raw Data | method=\["literal filename run/test token"\]; status=\["filename_candidate_not_fully_content_joined"\] | e2f0d8c27a6b7b2993fdea5a686e701deebb08bb60f39170d1a0d615d483a926 |
| [PSI-101-4f754c5c1f3cf1c1](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/簡報與海報/補下載/PSI-101/Raw Data/295bcd8979e999ee_PSI-101_Raw Data_82 Postage 35L Lampwick.pptx>) | Raw Data | method=\["literal filename run/test token"\]; status=\["filename_candidate_not_fully_content_joined"\] | 4f754c5c1f3cf1c1d9bea89da90ada196188fb726fcb0a89599dac429a728b3c |


結構化完整記錄：`qa/trial_records.json` 的 `PSI-101-run-82`。原始資料只讀；本 Markdown 不改寫來源公式、快取或身份衝突。
