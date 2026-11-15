# Auxiliary BRE: methane family on nominal25mm disk

小資料集 ID：`BRE-AUX-METHANE-DISK25-ISS`

## 資料身份與範圍

| 項目 | 內容 |
| --- | --- |
| NASA investigation | [PSI-20](https://psi.nasa.gov/physci/repo/data/investigations/PSI-20) |
| 材料／配方 | delivered_gas_family: methane family；condensed_material: emulated only; exact target identity requires matched properties；bottle_is_not_final_stream: True |
| 幾何 | shape: flat porous circular burner；summary_nominal_diameter_mm: 25；actual_hardware_and_gas_correction: Requires per-run source definition. |
| 實驗模式 | gravity: ISS microgravity；mode: gas-fed material-flammability emulation in nominally quiescent chamber |
| 證據角色 | 氣體燃料的材料模擬器（輔助） |
| 環境 | gravity: ISS microgravity；mode: gas-fed material-flammability emulation in nominally quiescent chamber |
| 資料粒度／共享試片 | Requires exact trial and measurement/operation history; no values manufactured from summary lists. |
| 可用數值 | summary_and_source_analyzed_results_with_source_specific_raw_channels_not_complete_forward_closure |

## 1. 文獻結果與視覺化程式

### BRE-F01　The material is emulated; the delivered fuel is gaseous

**PSI-20_Science Documents_BRE_data_interpretation_20220804**

BRE 將氣體燃料／惰性混合氣送過多孔圓盤，以材料性質與熱回授關係模擬凝聚態燃料；它不是實際 PMMA 或 SIBAL 固體試片。

- 證據身份：official_source_and_experiment_definition。
- 文獻定位：SB-6187d07f3add: physical3–6; WEB-NASA-BRE: Science Objectives and Experiment Description。
- 使用數據部分：physical3–6；Science Objectives and Experiment Description。
- 本組適用層級：experiment_definition_not_empirical_subgroup_result；Official definition applies to all emulator groups; do not count it as a new material-burning result.。
- 使用／控制因子：氣體／惰性混合物、多孔盤、熱回授與材料模擬定義。
- 來源限制：Do not relabel an ethylene/N2 flame as an actual PMMA, polyethylene or liquid pool trial.；A fuel-bottle label is not necessarily the delivered fuel/inert mixture after control-system dilution.；BRE is not a leak, valve-isolation or flashback data set.。
- 搜尋句（改寫）：BRE supplies gaseous fuel/inert mixtures through a porous disk and seeks to emulate condensed-fuel burning through material-property and heat-feedback relations.。
- 來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/其他研究文件_正文類型待確認/第一批下載/PSI-20_ACME BRE/Science Documents/PSI-20_Science Documents_BRE_data_interpretation_20220804.pdf>)
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/其他研究文件_正文類型待確認/第一批下載/PSI-20_ACME BRE/Science Documents/PSI-20_Science Documents_BRE_data_interpretation_20220804.pdf>)

- 共同來源：**Burning Rate Emulator (BRE) — NASA Science**；Science Objectives and Experiment Description；https://science.nasa.gov/biological-physical/investigations/bre/

### BRE-F02　Operation, ignition and analyzed-paper cohorts have different denominators

**PSI-20_Science Documents_BRE_data_interpretation_20220804**

來源有不同飛行輪次與成功點火樣本選擇，較早及較晚論文使用重疊的分析群；新增論文不等於新增獨立實驗。

- 證據身份：source_scope_comparison。
- 文獻定位：SB-6187d07f3add: physical3–6/Table1; PUB-BRE2021RESULTS: primary publisher abstract; PUB-BRE2023STEADY: primary publisher abstract and experimental sections。
- 使用數據部分：physical3–6/Table1；primary publisher abstract；primary publisher abstract and experimental sections。
- 本組適用層級：campaign_cohort_context；194ignited overall is not59/103analyzed. Exact publication/run membership has not been fully reconstructed; preserve scope instead of assigning every cohort to methane or50mm.。
- 使用／控制因子：各論文樣本群；run交集未逐筆重建。
- 來源限制：Do not add194,59 and103 as independent burns.；Day rows and nested oxygen lists do not identify a complete Cartesian design or per-trial pressure.。
- 搜尋句（改寫）：The source guide reports two ISS rounds and an overall ignited-flame count; the earlier results paper analyzed a selected successful-ignition cohort and a later paper expanded the analysis. These are overlapping selections, not independent repeats.。
- 來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/其他研究文件_正文類型待確認/第一批下載/PSI-20_ACME BRE/Science Documents/PSI-20_Science Documents_BRE_data_interpretation_20220804.pdf>)
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/其他研究文件_正文類型待確認/第一批下載/PSI-20_ACME BRE/Science Documents/PSI-20_Science Documents_BRE_data_interpretation_20220804.pdf>)

- 共同來源：**Burning in microgravity: Experimental results and analysis**；primary publisher abstract；https://doi.org/10.1016/j.combustflame.2021.01.035

- 共同來源：**Demonstrating steady burning for small flat materials in microgravity in a quiescent ambient**；primary publisher abstract and experimental sections；https://doi.org/10.1016/j.proci.2022.08.107

### BRE-F03　Fuel termination and self-extinction are distinct endpoints

**PSI-20_Reports_Dissertation-PD-revised_**

BRE 有自然熄滅與操作燃料終止等不同端點；19070C1 的 fuel-off 命令不能代替實測流量歸零或化學熄滅時刻。

- 證據身份：source_event_and_analyzed_result。
- 文獻定位：SB-2ada277f4acc: physical32/Table3.1 and110–111/Table6.1; SB-6187d07f3add: test-log/trace guidance; PUB-BRE2023STEADY: primary publisher abstract。
- 使用數據部分：physical32/Table3.1 and110–111/Table6.1；test-log/trace guidance；primary publisher abstract。
- 本組適用層級：endpoint_definition_context；The explicit120s FT/19070C1 record is25mm ethylene/N2; it is not a measured50mm or methane endpoint. FT is operation termination, not self-extinction.。
- 使用／控制因子：19070C1燃料終止命令；實際零流量與熄焰時刻未取得。
- 來源限制：FT is not a spontaneous extinction label or measured material burn-out time.；Commanded flow, measured MFC response and actual burner-boundary delivery remain distinct.。
- 搜尋句（改寫）：Some source flames self-extinguished; others reached the operational fuel-termination endpoint. The selected19070C1 record contains a fuel-off command, not a newly verified physical-flow-off or chemical-extinction time.。
- 來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/研究報告與書章/第一批下載/PSI-20_ACME BRE/Reports/PSI-20_Reports_Dissertation-PD-revised_.pdf>)
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/研究報告與書章/第一批下載/PSI-20_ACME BRE/Reports/PSI-20_Reports_Dissertation-PD-revised_.pdf>)

- 共同來源：**PSI-20_Science Documents_BRE_data_interpretation_20220804**；test-log/trace guidance；[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/其他研究文件_正文類型待確認/第一批下載/PSI-20_ACME BRE/Science Documents/PSI-20_Science Documents_BRE_data_interpretation_20220804.pdf>)

- 共同來源：**Demonstrating steady burning for small flat materials in microgravity in a quiescent ambient**；primary publisher abstract；https://doi.org/10.1016/j.proci.2022.08.107

### BRE-F04　Heat-flux steadiness is not shape steadiness

**A Burning Rate Emulator (BRE) for study of condensed fuel burning in microgravity**

短落塔 BRE 中火焰仍成長，而熱回授接近較慢變化的端點；作者限制準穩態假設並要求較長時間試驗。

- 證據身份：source_measurement_plus_model_interpretation。
- 文獻定位：SB-c613c4770ad7: physical8–10, Figs7–13。
- 使用數據部分：physical8–10, Figs7–13。
- 本組適用層級：related_ground_drop_architecture_context；Markan short-drop results, not any listed long-duration ISS trial. Do not assign its quasi-steady limit or flame-growth observation as a new result for all ISS groups.。
- 使用／控制因子：短落塔時間、火焰成長與熱回授，非長時ISS試驗。
- 來源限制：Short-drop data are not orbital ISS steady-state measurements.；A source-selected isotherm and radiation-free ellipsoidal theory do not independently validate a full flame contour.。
- 搜尋句（改寫）：Short-drop BRE flames continued growing while heat feedback approached a slower-changing endpoint; the source explicitly limits quasi-steady assumptions and calls for longer-duration tests.。
- 來源：https://doi.org/10.1016/j.combustflame.2018.01.044
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/earth_space_transfer_20261114/phase7/role_D/assets/Markan2018_BRE_microgravity.pdf>)

### BRE-F05　Heat of gasification can be a reconstructed effective quantity

**Emulation of condensed fuel flames with gaseous fuels supplied through a porous copper calorimeter**

以淨熱回授除以指定質量通量反算的有效氣化熱，再帶回同一式重建熱通量，是來源量的重建，不構成獨立預測。

- 證據身份：source_equation_identity。
- 文獻定位：SB-52b0b7aaa14e: physical5–6, Eqs14–19; SB-2ada277f4acc: material emulation and heat-flux analysis chapters。
- 使用數據部分：physical5–6, Eqs14–19；material emulation and heat-flux analysis chapters。
- 本組適用層級：model_identity_constraint_not_new_prediction；qnet/m effective gasification identity is a mathematical/source-analysis limitation; it is not three independent validated material predictions.。
- 使用／控制因子：指定質量通量、反算有效氣化熱及淨熱回授；同量代數重建。
- 來源限制：The input stream's heat of combustion, inferredL, surface state and smoke point require consistent mixture bases.；A fitted effective property is not an independently measured material intrinsic constant.。
- 搜尋句（改寫）：The emulator commonly infers an effective heat of gasification from net heat feedback divided by prescribed mass flux; using the same quantities to reconstruct that heat flux is bookkeeping, not independent prediction.。
- 來源：https://doi.org/10.1002/fam.2896
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/earth_space_transfer_20261114/phase4_earth_experiment_search/role_D/assets/Auth2020_BRE_FAM.pdf>)

- 共同來源：**PSI-20_Reports_Dissertation-PD-revised_**；material emulation and heat-flux analysis chapters；[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/研究報告與書章/第一批下載/PSI-20_ACME BRE/Reports/PSI-20_Reports_Dissertation-PD-revised_.pdf>)

### BRE-F06　Calorimeter and local gauges require different corrections

**Emulation of condensed fuel flames with gaseous fuels supplied through a porous copper calorimeter**

局部熱流規與銅熱量計對應不同空間範圍的熱回授；支撐、桿件、感測器損失與飛行校正需要各自處理。

- 證據身份：source_instrument_model_and_calibration。
- 文獻定位：SB-52b0b7aaa14e: physical3–6, calorimeter energy balances; SB-22b0ccfa2c69: physical26–34 and82–85; SB-2ada277f4acc: physical76 and AppendixA。
- 使用數據部分：physical3–6, calorimeter energy balances；physical26–34 and82–85；physical76 and AppendixA。
- 本組適用層級：instrumentation_and_calibration_context；Preserve the spatial observable and actual hardware/calibration; no per-group flight calorimeter coefficients transferred here.。
- 使用／控制因子：局部熱流規／熱量計空間範圍、支撐損失與飛行校正。
- 來源限制：Ground BRE2 constants cannot be transferred unchanged to flight hardware.；Source-derived calorimeter flux is not independent direct heat flux; condensation/radial nonuniformity and correction assumptions need source-specific handling.。
- 搜尋句（改寫）：Local gauges and the copper calorimeter reconstruct different spatial heat-feedback quantities. Source work includes sensor/backing/rod losses, calibration and flight correction concerns.。
- 來源：https://doi.org/10.1002/fam.2896
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/earth_space_transfer_20261114/phase4_earth_experiment_search/role_D/assets/Auth2020_BRE_FAM.pdf>)

- 共同來源：**Auth2019_BRE_1g_thesis**；physical26–34 and82–85；[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/earth_space_transfer_20261114/phase4_earth_experiment_search/role_D/assets/Auth2019_BRE_1g_thesis.pdf>)

- 共同來源：**PSI-20_Reports_Dissertation-PD-revised_**；physical76 and AppendixA；[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/研究報告與書章/第一批下載/PSI-20_ACME BRE/Reports/PSI-20_Reports_Dissertation-PD-revised_.pdf>)

### BRE-F07　A computed temperature separator is not a measured ignition threshold

**Demonstrating steady burning for small flat materials in microgravity in a quiescent ambient**

較晚 BRE 分析以計算火焰溫度範圍區分來源中的自然熄滅與燃料終止，提出可燃性圖；這些計算量不等於獨立量測的材料燃燒界限。

- 證據身份：source_model_interpretation_not_gas_thermometry。
- 文獻定位：PUB-BRE2023STEADY: primary publisher abstract/steadiness analysis; PUB-BRE2023MAP: primary publisher abstract。
- 使用數據部分：primary publisher abstract/steadiness analysis；primary publisher abstract。
- 本組適用層級：unmatched_source_cohort_context；Computed criticalT/flame-map results belong to published selected ethylene/N2 model cohorts. No exact local per-run mapping has been established for50mm/methane; not directly measured material ignition limits.。
- 使用／控制因子：選定乙烯/N2群之計算火焰溫度／可燃性圖，非實測材料界限。
- 來源限制：The critical temperature is model-derived and source-selected; do not present it as gas thermometry or a universal material ignition slider threshold.；No joint validation of arbitrary material, geometry, atmosphere and external heat flux follows.。
- 搜尋句（改寫）：Later BRE analyses use a calculated flame-temperature range to distinguish source self-extinguished and fuel-terminated conditions and propose flammability diagrams.。
- 來源：https://doi.org/10.1016/j.proci.2022.08.107
- 本機來源：尚未取得本機檔案

- 共同來源：**Flammability maps for microgravity burning of a small flat material in a quiescent ambient**；primary publisher abstract；https://doi.org/10.1016/j.combustflame.2023.112809

| Model ID | 公式／預測量 | 展示程式 | 數值比較與限制 |
| --- | --- | --- | --- |
| BRE-AUXILIARY-ONLY | BRE auxiliary material emulator；BRE auxiliary material emulator | reproduce_solid_models.py · [開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/solid_combustion_evidence_20261115/models/reproduce_solid_models.py>) | 目前未執行／尚未閉合；缺少完整輸入與對應目標；Exact matched geometry/flow/composition/pressure/property state；Calorimeter thermal/sensor definitions and material-boundary heat flux for transfer；Gas-emulator and calorimeter conventions require their own closure; command-off is not measured physical flow-off. No source constants are transferred to PMMA/SIBAL. |

## 2. 使用資料與參數總表的因子對照

| 總表原分類 | 來源身份 | 原欄名單位 | 原欄名例 | 總表定位 |
| --- | --- | --- | --- | --- |
| 光電／離子偵測訊號 | 儀器原始訊號 | 未由欄名確認 | IonCurrent；PMT1；PMT2；PMT3 | '物理參數'!A38:K38 |
| 光電／離子偵測訊號 | 儀器設定／控制參數 | 未由欄名確認 | PMT 1 Gain；PMT 2 Gain；PMT 3 Gain | '物理參數'!A39:K39 |
| 其他氣體組成／濃度 | 條件或分析量 | 未由欄名確認 | Nitrogen；Hydrogen / Helium (45/55)；Dilution of fuel and inert | '物理參數'!A40:K40 |
| 化學計量混合分率 | 計算／分析參數 | 未由欄名確認 | Stoichiometric Conversion Equation | '物理參數'!A41:K41 |
| 壓力 | 量測或設定 | psia | Pstart (psia)；Pend (psia)；Returns the delta pressure (psia) of the combustion chamber from event start to event end | '物理參數'!A42:K42 |
| 壓力 | 量測或設定 | 未由欄名確認 | Chamber Pressure | '物理參數'!A43:K43 |
| 密度 | 量測或來源分析量 | g/L | Density (g/L) | '物理參數'!A44:K44 |
| 密度 | 量測或來源分析量 | 未由欄名確認 | Density | '物理參數'!A45:K45 |
| 尺寸／幾何 | 儀器設定／控制參數 | 未由欄名確認 | TP_PARAMETER_IGNITER_IGNITION_POSITION_1；TP_PARAMETER_IGNITER_IGNITION_POSITION_2 | '物理參數'!A46:K46 |
| 尺寸／幾何 | 裝置或樣本條件 | mm | Burner Size (mm) | '物理參數'!A47:K47 |
| 影像／光譜設定 | 儀器設定或影像座標 | 未由欄名確認 | filterNumber；missing Intensified Camera Image not downlinked | '物理參數'!A48:K48 |
| 氧濃度 | 量測或條件值 | percent | Oxygen Conc (percent) | '物理參數'!A49:K49 |
| 氧濃度 | 量測或條件值 | 未由欄名確認 | Oxygen；O2；Ethylene: C2H4 → - 3 O2 + 2 H2O + 2 CO2；Methane: CH4 → - 2 O2 + 2 H2O + CO2；Hydrogen: 2 H2 → - O2 + 2 H2O；PickOxygen；O2 Fill | '物理參數'!A50:K50 |
| 流速／通風 | 量測或設定 | 未由欄名確認 | Ramp to final velocity | '物理參數'!A51:K51 |
| 溫度 | 量測或設定 | Standard Liters - 0 DegC, 760 Torr | ACME MFCs (Standard Liters - 0 DegC, 760 Torr) | '物理參數'!A52:K52 |
| 溫度 | 量測或設定 | Standard Liters - 0 DegC, 760 torr | Start Mixture (Standard Liters - 0 DegC, 760 torr)；Event Delta (Standard Liters - 0 DegC, 760 torr)；Finish Mixture (Standard Liters - 0 DegC, 760 torr)；Recirculation Loop Contents (Standard Liters - 0 DegC, 760 torr) | '物理參數'!A53:K53 |
| 溫度 | 量測或設定 | 未由欄名確認 | Thermocouple；Chamber Temperature；FCU_MP_TM1；FCU_MP_TM2；FCU_MP_TM3；FCU_MP_TM4；TC200A；TC200B | '物理參數'!A54:K54 |
| 熱通量／輻射 | 量測通道或來源分析量 | 未由欄名確認 | Radiometer；Radiometer+60；Radiometer+60CJ；Radiometer+30；Radiometer+30CJ；RadiometerCenter；RadiometerCenterCJ；Radiometer-30；Radiometer-30CJ；Radiometer-60；其餘見原始欄位 | '物理參數'!A55:K55 |
| 電場電壓／電流 | 儀器設定／控制參數 | 未由欄名確認 | EfieldSetpointOut | '物理參數'!A56:K56 |
| 電場電壓／電流 | 量測或設定 | 未由欄名確認 | EField；EFieldPol；EfieldVoltage | '物理參數'!A57:K57 |
| 體積流量／MFC | 儀器設定／控制參數 | V | MFCA1Setpoint(V)；MFCA2Setpoint(V)；MFCA3Setpoint(V) | '物理參數'!A58:K58 |
| 體積流量／MFC | 儀器設定／控制參數 | 未由欄名確認 | MFCA1 Full Scale；MFCA2 Full Scale；MFCA3 Full Scale | '物理參數'!A59:K59 |
| 體積流量／MFC | 量測或設定 | 未由欄名確認 | MFCA1 Gas；MFCA2 Gas；MFCA3 Gas；MFCDiluent；MFCFuel；MFCN2；MFCO2；MFCA1StaticMixerFlow；MFCA2BypassFlow；MFCA3FuelFlow；其餘見原始欄位 | '物理參數'!A60:K60 |
| 點火功率／電壓／電流 | 儀器設定／控制參數 | 未由欄名確認 | TP_PARAMETER_IGNITER_WATTAGE；TP_PARAMETER_IGNITER_ON_TIME | '物理參數'!A61:K61 |
| 點火功率／電壓／電流 | 量測或設定 | ms | Igniter On Time (ms) | '物理參數'!A62:K62 |
| 點火功率／電壓／電流 | 量測或設定 | 未由欄名確認 | Igniter Wattage | '物理參數'!A63:K63 |

以上是該 investigation 的欄位盤點；個別結論實際使用的因子以第1節與下列補充為準。

| 本組實際因子 | 總表定位／未列欄位 | 文獻中的用途 |
| --- | --- | --- |
| 材料／配方／幾何 | '實驗總覽'!E19 | 文獻選樣身份；逐次厚度、支撐與歷史另由原文補齊 |
| 環境／流向／重力 | '實驗總覽'!F19 | 環境摘要，非本組全部逐次聯合條件 |
| 尺寸／幾何 / TP_PARAMETER_IGNITER_IGNITION_POSITION_1；TP_PARAMETER_IGNITER_IGNITION_POSITION_2 | '物理參數'!G46 | 是否為模型輸入、控制條件或量測輸出，依第1節文獻定位逐項核對 |
| 尺寸／幾何 / Burner Size (mm) | '物理參數'!G47 | 是否為模型輸入、控制條件或量測輸出，依第1節文獻定位逐項核對 |
| 氧濃度 / Oxygen Conc (percent) | '物理參數'!G49 | 是否為模型輸入、控制條件或量測輸出，依第1節文獻定位逐項核對 |
| 氧濃度 / Oxygen；O2；Ethylene: C2H4 → - 3 O2 + 2 H2O + 2 CO2；Methane: CH4 → - 2 O2 + 2 H2O + CO2；Hydrogen: 2 H2 → - O2 + 2 H2O；PickOxygen；O2 Fill | '物理參數'!G50 | 是否為模型輸入、控制條件或量測輸出，依第1節文獻定位逐項核對 |
| 流速／通風 / Ramp to final velocity | '物理參數'!G51 | 是否為模型輸入、控制條件或量測輸出，依第1節文獻定位逐項核對 |
| 溫度 / ACME MFCs (Standard Liters - 0 DegC, 760 Torr) | '物理參數'!G52 | 是否為模型輸入、控制條件或量測輸出，依第1節文獻定位逐項核對 |
| 溫度 / Start Mixture (Standard Liters - 0 DegC, 760 torr)；Event Delta (Standard Liters - 0 DegC, 760 torr)；Finish Mixture (Standard Liters - 0 DegC, 760 torr)；Recirculation Loop Contents (Standard Liters - 0 DegC, 760 torr) | '物理參數'!G53 | 是否為模型輸入、控制條件或量測輸出，依第1節文獻定位逐項核對 |
| 溫度 / Thermocouple；Chamber Temperature；FCU_MP_TM1；FCU_MP_TM2；FCU_MP_TM3；FCU_MP_TM4；TC200A；TC200B | '物理參數'!G54 | 是否為模型輸入、控制條件或量測輸出，依第1節文獻定位逐項核對 |
| 熱通量／輻射 / Radiometer；Radiometer+60；Radiometer+60CJ；Radiometer+30；Radiometer+30CJ；RadiometerCenter；RadiometerCenterCJ；Radiometer-30；Radiometer-30CJ；Radiometer-60；其餘見原始欄位 | '物理參數'!G55 | 是否為模型輸入、控制條件或量測輸出，依第1節文獻定位逐項核對 |

| 文獻因子／疑點 | 正確讀法或需補資料 |
| --- | --- |
| 物性／熱回授 | BRE是氣體材料模擬器；有效氣化熱、指定質量通量及熱量計校正各有身份。 |

## 3. 共用資料的多項結論比較

| 結論／文獻 | 資料重疊身份 | 共同處 | 不同處／不能合併之處 |
| --- | --- | --- | --- |
| SB-6187d07f3add；SB-2ada277f4acc；SB-c2f22c914b38；PUB-BRE2021RESULTS；PUB-BRE2023STEADY；PUB-BRE2023MAP | overlapping_campaigns_different_analysis_cohorts | Source papers analyze selected/expanded subsets of the two ISS rounds. | 194guide totalignited,59earlier-paper analyzed,103expanded analysis and49fuel-terminated have different denominators; not contradictory counts or independent cohorts. |

## 4. 消防洞見

| 類別 | 對應證據 | 數據支持的判斷 | 策略／產品構想 | 待驗證 |
| --- | --- | --- | --- | --- |
| 預防 | 尚未取得／不適用 | 輔助模擬器／方法限制；沒有本組實際固體試片的消防成效量測。 | 先補對應資料與試次匹配，再決定可測試策略；此處是研究缺口。 | 需本組材料、幾何、操作歷史與對應端點的量測；相近系列不能代替。 |
| 偵測 | 尚未取得／不適用 | 輔助模擬器／方法限制；沒有本組實際固體試片的消防成效量測。 | 先補對應資料與試次匹配，再決定可測試策略；此處是研究缺口。 | 需本組材料、幾何、操作歷史與對應端點的量測；相近系列不能代替。 |
| 撲滅／抑制 | 尚未取得／不適用 | 輔助模擬器／方法限制；沒有本組實際固體試片的消防成效量測。 | 先補對應資料與試次匹配，再決定可測試策略；此處是研究缺口。 | 需本組材料、幾何、操作歷史與對應端點的量測；相近系列不能代替。 |

## 逐次索引

尚未取得可逐項對照的紀錄。

## 缺件與適用範圍

- Auxiliary, not a genuine solid-fuel specimen dataset.
- Do not create a completeP/O2/fuel grid from operation-day lists.
- Raw3400%/2100% oxygen strings remain source-quality issues, not physical percentages.
- 尚未建立全火焰形狀／艙室安全的閉合預測。
