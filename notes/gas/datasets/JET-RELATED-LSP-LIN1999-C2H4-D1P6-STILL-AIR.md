# Lin1999 C2H4, 1.6mm, nonbuoyant still-air jet (related source, not SPICE)

小資料集 ID：`JET-RELATED-LSP-LIN1999-C2H4-D1P6-STILL-AIR`

## 資料身份與範圍

| 項目 | 內容 |
| --- | --- |
| 原始 NASA PSI investigation | 尚未取得／不適用 |
| 相關PSI索引（不是原始資料） | PSI-107 |
| 材料／配方 | components_mole_fraction: C2H4: 1.0 |
| 幾何 | fuel_nozzle_inner_diameter_mm: 1.6；chamber_diameter_mm: 400；chamber_maximum_length_mm: 740 |
| 實驗模式 | steady_nonpremixed_nonbuoyant_jet_in_still_closed_chamber_air; near_smoke_point_not_all_at_endpoint |
| 證據角色 | 相關歷史NASA飛行試驗，非PSI原始資料 |
| 環境 | gravity: Space Shuttle orbital microgravity；mode: steady_nonpremixed_nonbuoyant_jet_in_still_closed_chamber_air; near_smoke_point_not_all_at_endpoint |
| 資料粒度／共享試片 | 原始試次／操作／圖上量測的身份見逐次索引，未預設互相一對一。 |
| 可用數值 | published_numeric_length_and_maximum_diameter_available; not_original_frame_data_or_direct_PSI_raw |

## 1. 文獻結果與視覺化程式

### JET-RELATED-LSP-LIN1999-C2H4-D1P6-STILL-AIR-TABLE　JET-RELATED-LSP-LIN1999-C2H4-D1P6-STILL-AIR-TABLE

**Shapes of nonbuoyant round luminous hydrocarbon/air laminar jet diffusion flames**

Table1 reports 10 genuine TestIDs with pressure, flow, luminous length and maximum full luminous diameter for this fuel/nozzle. These are published reduced measurements, not digitized curve coordinates or a new fit.

- 證據身份：original_published_numeric_processed_experimental_table。
- 文獻定位：JET-1f06a8313d4b: physical_pdf_pages: 4；5；table: 1。
- 使用數據部分：source_id: JET-1f06a8313d4b；physical_pdf_page: 5；table: 1；original_test_ids: 01E*；03E*；01E；02E；03E；04E；14E；15E；16E；17E。
- 本組適用層級：僅本項來源指定案例；逐次配對以data_used為準。
- 使用／控制因子：semantic_key: fuel_nozzle_inner_diameter；source_raw_name: d；unit: mm；value_or_range: 1.6；source_ref: source_id: JET-1f06a8313d4b；physical_pdf_pages: 4；5；table: 1；workbook_mapping_status: not_a_core_PSI_workbook_row；semantic_key: ambient_pressure；source_raw_name: p；unit: kPa；value_or_range: 35；100；source_ref: source_id: JET-1f06a8313d4b；physical_pdf_pages: 4；5；table: 1；workbook_mapping_status: not_a_core_PSI_workbook_row；semantic_key: luminous_flame_length；source_raw_name: Lf；unit: mm；value_or_range: 14.7；63.0；source_ref: source_id: JET-1f06a8313d4b；physical_pdf_pages: 4；5；table: 1；workbook_mapping_status: not_a_core_PSI_workbook_row；semantic_key: maximum_luminous_diameter；source_raw_name: wMAX；unit: mm；value_or_range: 11.5；14.7；source_ref: source_id: JET-1f06a8313d4b；physical_pdf_pages: 4；5；table: 1；workbook_mapping_status: not_a_core_PSI_workbook_row。
- 來源限制：wMAX is diameter, not radius. t_ch is kinematically derived, not a separate measured residence-time field.；No raw-image-to-table reprocessing or new R² was done by this source audit.。
- 搜尋句（改寫）：Table1 reports 10 genuine TestIDs with pressure, flow, luminous length and maximum full luminous diameter for this fuel/nozzle. These are published reduced measurements, not digitized curve coordinates or a new fit.。
- 來源：[來源](<https://ntrs.nasa.gov/api/citations/20000030674/downloads/20000030674.pdf>)
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/02_論文全文/02_會議論文與預印本/Shapes of nonbuoyant round luminous hydrocarbon_air laminar jet diffusion flames__1f06a8313d.pdf>)

### JET-RELATED-LSP-LIN1999-C2H4-D1P6-STILL-AIR-ENDPOINT　JET-RELATED-LSP-LIN1999-C2H4-D1P6-STILL-AIR-ENDPOINT

**Shapes of nonbuoyant round luminous hydrocarbon/air laminar jet diffusion flames**

Only original Tests01E*,03E*,01E were soot-emitting during shape observations; other flames contained soot without emitting it. The idealized contour law has opened-tip limitations and is not an extinction or smoke-emission law.

- 證據身份：source_observed_flame_state_and_model_limit。
- 文獻定位：JET-1f06a8313d4b: physical_pdf_pages: 5；6；13；table: 1；figure: 6–8；equation: 3。
- 使用數據部分：source_id: JET-1f06a8313d4b；physical_pdf_page: 5；table: 1；original_test_ids: 01E*；03E*；01E；02E；03E；04E；14E；15E；16E；17E。
- 本組適用層級：僅本項來源指定案例；逐次配對以data_used為準。
- 使用／控制因子：semantic_key: soot_emission_state；source_raw_name: Table1 footnotea；unit: source categorical state；value_or_range: 01E*: True；03E*: True；01E: True；02E: False；03E: False；04E: False；14E: False；15E: False；16E: False；17E: False；source_ref: source_id: JET-1f06a8313d4b；physical_pdf_pages: 5；13；locator: Table1 footnotea; Flame shapes discussion；workbook_mapping_status: not_a_core_PSI_workbook_row。
- 來源限制：Still-air shuttle apparatus differs from forced coflow SPICE; do not insert Uair=0 into SPICE Eq7.；Visible soot-containing and soot-emitting labels are not calibrated alarm or occupational exposure limits.。
- 搜尋句（改寫）：Only original Tests01E*,03E*,01E were soot-emitting during shape observations; other flames contained soot without emitting it. The idealized contour law has opened-tip limitations and is not an extinction or smoke-emission law.。
- 來源：[來源](<https://ntrs.nasa.gov/api/citations/20000030674/downloads/20000030674.pdf>)
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/02_論文全文/02_會議論文與預印本/Shapes of nonbuoyant round luminous hydrocarbon_air laminar jet diffusion flames__1f06a8313d.pdf>)

| Model ID | 公式／預測量 | 展示程式 | 數值比較與限制 |
| --- | --- | --- | --- |
| SHUTTLE-STILLAIR-IDEAL-WIDTH | w_max * Z_st / d = 9/16; therefore w_max = (9/16) * d / Z_st. d and w_max in mm. Inputs use source Table1 nozzle diameter and stoichiometric mixture fraction only. Luminous length, mass flow and pressure are not predictors in this ideal width law.；Maximum FULL luminous flame diameter (mm), compared with ideal flame-sheet maximum diameter; not radius or full contour | producer.py · [開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/tools/gas_evidence/models/producer.py>) | runnable；same_source_reproduction；R²（模型全群）=0.5064696499327288；模型每個燃料×噴口群只給常數寬度，無法描述實測群內變化；分組負R²完整保留在工具與MODEL_INVENTORY。；Equal species diffusivities, constant properties, negligible radiation and ideal nonbuoyant boundary-layer approximation. The original source states these assumptions cannot all be satisfied by practical laminar flames.；Source Z_st describes the source burner fluid/ambient composition; it is not a material constant transferable to arbitrary oxygen fraction or habitat atmosphere.；The model predicts one constant diameter per fuel/nozzle cohort, while the observed luminous diameter varies across source pressure and flow conditions. Cohort scores retain this failure.；No new luminous-width calibration is made. The source empirical width factors are not used. A theoretical stoichiometric sheet is not a directly measured luminous chemical boundary.；Original published numeric table is available; original image frames and per-point uncertainty are not supplied. This comparison is not an independent held-out campaign or a full-shape validation.；Source Table1 Test17E velocity1690mm/s conflicts with body range1630mm/s; both are preserved in the source ledger and this velocity is unused by Eq3.；related_NASA_shuttle_flight_still_air_not_SPICE_or_SLICE_raw_campaign；Fixed ideal source width law versus original published processed numeric luminous-width table; no newly estimated coefficient |

| 可開啟的圖／工具 | 身份與用途 |
| --- | --- |
| [開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/gas_combustion_evidence_20261115/models/shuttle_still_air_width_comparison.png>) | 21筆歷史NASA飛行論文表值；固定理想式與發光最大直徑的比較，不是SPICE共流資料 |
| [開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/gas_combustion_evidence_20261115/models/comparison.html>) | 選正確架構；缺資料的研究僅顯示就緒度，不畫假預測 |

## 2. 使用資料與參數總表的因子對照

尚未取得可逐項對照的紀錄。

以上是該 investigation 的欄位盤點；個別結論實際使用的因子以第1節與下列補充為準。

| 本組實際因子 | 總表定位／未列欄位 | 文獻中的用途 |
| --- | --- | --- |
| JET-RELATED-LSP-LIN1999-C2H4-D1P6-STILL-AIR-TABLE / fuel_nozzle_inner_diameter | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| JET-RELATED-LSP-LIN1999-C2H4-D1P6-STILL-AIR-TABLE / ambient_pressure | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| JET-RELATED-LSP-LIN1999-C2H4-D1P6-STILL-AIR-TABLE / luminous_flame_length | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| JET-RELATED-LSP-LIN1999-C2H4-D1P6-STILL-AIR-TABLE / maximum_luminous_diameter | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| JET-RELATED-LSP-LIN1999-C2H4-D1P6-STILL-AIR-ENDPOINT / soot_emission_state | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |

尚未取得可逐項對照的紀錄。

## 3. 共用資料的多項結論比較

| 結論／文獻 | 資料重疊身份 | 共同處 | 不同處／不能合併之處 |
| --- | --- | --- | --- |
| JET-RELATED-LSP-LIN1999-C2H4-D1P6-STILL-AIR-TABLE；JET-RELATED-LSP-LIN1999-C2H4-D1P6-STILL-AIR-ENDPOINT | 來源系列；精確論文／試次交集仍以每項data_used為準 | 不把多份出版物當獨立實驗。 | 尚未取得完全同試次的多篇結論比較時保留缺口。 |

## 4. 消防洞見

| 類別 | 對應證據 | 數據支持的判斷 | 策略／產品構想 | 待驗證 |
| --- | --- | --- | --- | --- |
| 預防 | 尚未取得／不適用 | 尚未建立本組可直接支持此消防用途的完整量測鏈。 | 先補本組對應的物理端點與資料配對，再設計策略測試。 | 相關系列與方法限制只能提供研究脈絡，不能代替本組產品或操作效能驗證。 |
| 偵測 | 尚未取得／不適用 | 尚未建立本組可直接支持此消防用途的完整量測鏈。 | 先補本組對應的物理端點與資料配對，再設計策略測試。 | 相關系列與方法限制只能提供研究脈絡，不能代替本組產品或操作效能驗證。 |
| 撲滅／抑制 | 尚未取得／不適用 | 尚未建立本組可直接支持此消防用途的完整量測鏈。 | 先補本組對應的物理端點與資料配對，再設計策略測試。 | 相關系列與方法限制只能提供研究脈絡，不能代替本組產品或操作效能驗證。 |

## 逐次索引

| 原始檔／資料位置 | Trial／Run／列 | 共享身份與保留事項 |
| --- | --- | --- |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\02_論文全文\02_會議論文與預印本\Shapes of nonbuoyant round luminous hydrocarbon_air laminar jet diffusion flames__1f06a8313d.pdf | original_test_id: 01E*；fuel: C2H4；nozzle_inner_diameter_mm: 1.6；stoichiometric_mixture_fraction: 0.0636；pressure_kPa: 100；fuel_mass_flow_mg_s: 1.84；source_mean_exit_velocity_mm_s: 820；source_Reynolds_number: 138；source_characteristic_residence_time_ms: 121；luminous_length_mm: 49.3；maximum_luminous_diameter_mm: 13.7；source_table_body_ordinal: 1；physical_pdf_page: 5；table: 1；source_record_locator: Table1 original Test 01E*；measurement_class: original_published_numeric_processed_experimental_table；soot_emitting_during_shape_observation: True；flight: STS-83；replicate_count: 尚未取得／不適用；source_coflow_mode: still air, no imposed coflow；uncertainty: 尚未取得／不適用 | raw_parameters_as_stored: 尚未取得／不適用；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\02_論文全文\02_會議論文與預印本\Shapes of nonbuoyant round luminous hydrocarbon_air laminar jet diffusion flames__1f06a8313d.pdf | original_test_id: 03E*；fuel: C2H4；nozzle_inner_diameter_mm: 1.6；stoichiometric_mixture_fraction: 0.0636；pressure_kPa: 50；fuel_mass_flow_mg_s: 1.84；source_mean_exit_velocity_mm_s: 1630；source_Reynolds_number: 138；source_characteristic_residence_time_ms: 77；luminous_length_mm: 63.0；maximum_luminous_diameter_mm: 14.2；source_table_body_ordinal: 2；physical_pdf_page: 5；table: 1；source_record_locator: Table1 original Test 03E*；measurement_class: original_published_numeric_processed_experimental_table；soot_emitting_during_shape_observation: True；flight: STS-83；replicate_count: 尚未取得／不適用；source_coflow_mode: still air, no imposed coflow；uncertainty: 尚未取得／不適用 | raw_parameters_as_stored: 尚未取得／不適用；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\02_論文全文\02_會議論文與預印本\Shapes of nonbuoyant round luminous hydrocarbon_air laminar jet diffusion flames__1f06a8313d.pdf | original_test_id: 01E；fuel: C2H4；nozzle_inner_diameter_mm: 1.6；stoichiometric_mixture_fraction: 0.0636；pressure_kPa: 100；fuel_mass_flow_mg_s: 0.71；source_mean_exit_velocity_mm_s: 320；source_Reynolds_number: 54；source_characteristic_residence_time_ms: 130；luminous_length_mm: 20.6；maximum_luminous_diameter_mm: 12.6；source_table_body_ordinal: 3；physical_pdf_page: 5；table: 1；source_record_locator: Table1 original Test 01E；measurement_class: original_published_numeric_processed_experimental_table；soot_emitting_during_shape_observation: True；flight: STS-94；replicate_count: 尚未取得／不適用；source_coflow_mode: still air, no imposed coflow；uncertainty: 尚未取得／不適用 | raw_parameters_as_stored: 尚未取得／不適用；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\02_論文全文\02_會議論文與預印本\Shapes of nonbuoyant round luminous hydrocarbon_air laminar jet diffusion flames__1f06a8313d.pdf | original_test_id: 02E；fuel: C2H4；nozzle_inner_diameter_mm: 1.6；stoichiometric_mixture_fraction: 0.0636；pressure_kPa: 50；fuel_mass_flow_mg_s: 0.76；source_mean_exit_velocity_mm_s: 670；source_Reynolds_number: 57；source_characteristic_residence_time_ms: 53；luminous_length_mm: 17.7；maximum_luminous_diameter_mm: 13.1；source_table_body_ordinal: 4；physical_pdf_page: 5；table: 1；source_record_locator: Table1 original Test 02E；measurement_class: original_published_numeric_processed_experimental_table；soot_emitting_during_shape_observation: False；flight: STS-94；replicate_count: 尚未取得／不適用；source_coflow_mode: still air, no imposed coflow；uncertainty: 尚未取得／不適用 | raw_parameters_as_stored: 尚未取得／不適用；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\02_論文全文\02_會議論文與預印本\Shapes of nonbuoyant round luminous hydrocarbon_air laminar jet diffusion flames__1f06a8313d.pdf | original_test_id: 03E；fuel: C2H4；nozzle_inner_diameter_mm: 1.6；stoichiometric_mixture_fraction: 0.0636；pressure_kPa: 50；fuel_mass_flow_mg_s: 1.29；source_mean_exit_velocity_mm_s: 1140；source_Reynolds_number: 97；source_characteristic_residence_time_ms: 64；luminous_length_mm: 36.5；maximum_luminous_diameter_mm: 13.8；source_table_body_ordinal: 5；physical_pdf_page: 5；table: 1；source_record_locator: Table1 original Test 03E；measurement_class: original_published_numeric_processed_experimental_table；soot_emitting_during_shape_observation: False；flight: STS-94；replicate_count: 尚未取得／不適用；source_coflow_mode: still air, no imposed coflow；uncertainty: 尚未取得／不適用 | raw_parameters_as_stored: 尚未取得／不適用；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\02_論文全文\02_會議論文與預印本\Shapes of nonbuoyant round luminous hydrocarbon_air laminar jet diffusion flames__1f06a8313d.pdf | original_test_id: 04E；fuel: C2H4；nozzle_inner_diameter_mm: 1.6；stoichiometric_mixture_fraction: 0.0636；pressure_kPa: 65；fuel_mass_flow_mg_s: 0.91；source_mean_exit_velocity_mm_s: 620；source_Reynolds_number: 68；source_characteristic_residence_time_ms: 86；luminous_length_mm: 26.5；maximum_luminous_diameter_mm: 13.1；source_table_body_ordinal: 6；physical_pdf_page: 5；table: 1；source_record_locator: Table1 original Test 04E；measurement_class: original_published_numeric_processed_experimental_table；soot_emitting_during_shape_observation: False；flight: STS-94；replicate_count: 尚未取得／不適用；source_coflow_mode: still air, no imposed coflow；uncertainty: 尚未取得／不適用 | raw_parameters_as_stored: 尚未取得／不適用；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\02_論文全文\02_會議論文與預印本\Shapes of nonbuoyant round luminous hydrocarbon_air laminar jet diffusion flames__1f06a8313d.pdf | original_test_id: 14E；fuel: C2H4；nozzle_inner_diameter_mm: 1.6；stoichiometric_mixture_fraction: 0.0636；pressure_kPa: 80；fuel_mass_flow_mg_s: 0.67；source_mean_exit_velocity_mm_s: 370；source_Reynolds_number: 50；source_characteristic_residence_time_ms: 97；luminous_length_mm: 18.0；maximum_luminous_diameter_mm: 12.9；source_table_body_ordinal: 7；physical_pdf_page: 5；table: 1；source_record_locator: Table1 original Test 14E；measurement_class: original_published_numeric_processed_experimental_table；soot_emitting_during_shape_observation: False；flight: STS-94；replicate_count: 尚未取得／不適用；source_coflow_mode: still air, no imposed coflow；uncertainty: 尚未取得／不適用 | raw_parameters_as_stored: 尚未取得／不適用；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\02_論文全文\02_會議論文與預印本\Shapes of nonbuoyant round luminous hydrocarbon_air laminar jet diffusion flames__1f06a8313d.pdf | original_test_id: 15E；fuel: C2H4；nozzle_inner_diameter_mm: 1.6；stoichiometric_mixture_fraction: 0.0636；pressure_kPa: 100；fuel_mass_flow_mg_s: 0.61；source_mean_exit_velocity_mm_s: 270；source_Reynolds_number: 46；source_characteristic_residence_time_ms: 109；luminous_length_mm: 14.7；maximum_luminous_diameter_mm: 11.5；source_table_body_ordinal: 8；physical_pdf_page: 5；table: 1；source_record_locator: Table1 original Test 15E；measurement_class: original_published_numeric_processed_experimental_table；soot_emitting_during_shape_observation: False；flight: STS-94；replicate_count: 尚未取得／不適用；source_coflow_mode: still air, no imposed coflow；uncertainty: 尚未取得／不適用 | raw_parameters_as_stored: 尚未取得／不適用；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\02_論文全文\02_會議論文與預印本\Shapes of nonbuoyant round luminous hydrocarbon_air laminar jet diffusion flames__1f06a8313d.pdf | original_test_id: 16E；fuel: C2H4；nozzle_inner_diameter_mm: 1.6；stoichiometric_mixture_fraction: 0.0636；pressure_kPa: 65；fuel_mass_flow_mg_s: 0.74；source_mean_exit_velocity_mm_s: 510；source_Reynolds_number: 56；source_characteristic_residence_time_ms: 75；luminous_length_mm: 19.0；maximum_luminous_diameter_mm: 13.4；source_table_body_ordinal: 9；physical_pdf_page: 5；table: 1；source_record_locator: Table1 original Test 16E；measurement_class: original_published_numeric_processed_experimental_table；soot_emitting_during_shape_observation: False；flight: STS-94；replicate_count: 尚未取得／不適用；source_coflow_mode: still air, no imposed coflow；uncertainty: 尚未取得／不適用 | raw_parameters_as_stored: 尚未取得／不適用；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\02_論文全文\02_會議論文與預印本\Shapes of nonbuoyant round luminous hydrocarbon_air laminar jet diffusion flames__1f06a8313d.pdf | original_test_id: 17E；fuel: C2H4；nozzle_inner_diameter_mm: 1.6；stoichiometric_mixture_fraction: 0.0636；pressure_kPa: 35；fuel_mass_flow_mg_s: 1.34；source_mean_exit_velocity_mm_s: 1690；source_Reynolds_number: 100；source_characteristic_residence_time_ms: 40；luminous_length_mm: 34.0；maximum_luminous_diameter_mm: 14.7；source_table_body_ordinal: 10；physical_pdf_page: 5；table: 1；source_record_locator: Table1 original Test 17E；measurement_class: original_published_numeric_processed_experimental_table；soot_emitting_during_shape_observation: False；flight: STS-94；replicate_count: 尚未取得／不適用；source_coflow_mode: still air, no imposed coflow；uncertainty: 尚未取得／不適用 | raw_parameters_as_stored: 尚未取得／不適用；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |

## 缺件與適用範圍

- No direct original PSI raw archive mapping established.
- Source Re in Table1 uses cold fuel viscosity; modified length-law Re needs a different property basis.
- No complete contour or raw frame uncertainty table is established here.
- Multiple pressures/flows and selected soot-emitting states do not isolate a nozzle-only causal effect.
