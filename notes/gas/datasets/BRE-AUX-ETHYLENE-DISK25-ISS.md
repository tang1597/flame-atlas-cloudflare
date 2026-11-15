# Auxiliary BRE: ethylene/N2 family on nominal25mm disk

小資料集 ID：`BRE-AUX-ETHYLENE-DISK25-ISS`

## 資料身份與範圍

| 項目 | 內容 |
| --- | --- |
| 原始 NASA PSI investigation | [PSI-20](https://psi.nasa.gov/physci/repo/data/investigations/PSI-20) |
| 相關PSI索引（不是原始資料） | 尚未取得／不適用 |
| 材料／配方 | delivered_gas_family: ethylene/N2 family；condensed_material: emulated only; exact target identity requires matched properties；bottle_is_not_final_stream: True |
| 幾何 | shape: flat porous circular burner；summary_nominal_diameter_mm: 25；actual_hardware_and_gas_correction: Requires per-run source definition. |
| 實驗模式 | gravity: ISS microgravity；mode: gas-fed material-flammability emulation in nominally quiescent chamber |
| 證據角色 | gas_fueled_material_flammability_emulator_auxiliary |
| 環境 | gravity: 尚未確認；mode: gravity: ISS microgravity；mode: gas-fed material-flammability emulation in nominally quiescent chamber |
| 資料粒度／共享試片 | Per-row source values retained; summary/day/variant rows are not promoted to independent burns. |
| 可用數值 | source_conditions_available_target_join_and_complete_chemistry_transport_closure_not_established |

## 1. 文獻結果與視覺化程式

### BRE-F01　The material is emulated; the delivered fuel is gaseous

**PSI-20_Science Documents_BRE_data_interpretation_20220804**

BRE將氣體燃料／惰性混合物送過多孔圓盤，以材料性質與熱回授關係模擬凝聚燃料，並非實際固體試片。

- 證據身份：official_source_and_experiment_definition。
- 文獻定位：GA-6187d07f3add: physical3–6; WEB-NASA-BRE: Science Objectives and Experiment Description。
- 使用數據部分：source_id: GA-6187d07f3add；locator: physical3–6；role: Sourceanalysisorboundedliteraturecontext;notindependentraw；source_id: WEB-NASA-BRE；locator: Science Objectives and Experiment Description；role: Sourceanalysisorboundedliteraturecontext;notindependentraw。
- 本組適用層級：experiment_definition；No source result is transferred to unmatched50mm/methane cases.。
- 使用／控制因子：factor_and_role: fuel/diluentcomposition:source-specificinput；source_refs: source_id: GA-6187d07f3add；locator: physical3–6；source_id: WEB-NASA-BRE；locator: Science Objectives and Experiment Description；factor_and_role: burnergeometry/ambientstate/flow:source-specificconditions；source_refs: source_id: GA-6187d07f3add；locator: physical3–6；source_id: WEB-NASA-BRE；locator: Science Objectives and Experiment Description；factor_and_role: thermalfeedback/calorimetry/flameendpoint:keepmeasured/computed/operationalrolesseparate；source_refs: source_id: GA-6187d07f3add；locator: physical3–6；source_id: WEB-NASA-BRE；locator: Science Objectives and Experiment Description。
- 來源限制：Do not relabel an ethylene/N2 flame as an actual PMMA, polyethylene or liquid pool trial.；A fuel-bottle label is not necessarily the delivered fuel/inert mixture after control-system dilution.；BRE is not a leak, valve-isolation or flashback data set.。
- 搜尋句（改寫）：BRE supplies gaseous fuel/inert mixtures through a porous disk and seeks to emulate condensed-fuel burning through material-property and heat-feedback relations.。
- 來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/其他研究文件_正文類型待確認/第一批下載/PSI-20_ACME BRE/Science Documents/PSI-20_Science Documents_BRE_data_interpretation_20220804.pdf>)
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/其他研究文件_正文類型待確認/第一批下載/PSI-20_ACME BRE/Science Documents/PSI-20_Science Documents_BRE_data_interpretation_20220804.pdf>)

- 共同來源：**Burning Rate Emulator**；Science Objectives and Experiment Description；[來源](<https://science.nasa.gov/biological-physical/investigations/bre/>)

### BRE-F02　Operation, ignition and analyzed-paper cohorts have different denominators

**PSI-20_Science Documents_BRE_data_interpretation_20220804**

兩輪ISS總點火群、早期成功點火分析群及後期擴大分析群互相重疊，不能當獨立重複或共用同一分母。

- 證據身份：source_scope_comparison。
- 文獻定位：GA-6187d07f3add: physical3–6/Table1; PUB-BRE2021RESULTS: primary publisher abstract; PUB-BRE2023STEADY: primary publisher abstract and experimental sections。
- 使用數據部分：source_id: GA-6187d07f3add；locator: physical3–6/Table1；role: Sourceanalysisorboundedliteraturecontext;notindependentraw；source_id: PUB-BRE2021RESULTS；locator: primary publisher abstract；role: Sourceanalysisorboundedliteraturecontext;notindependentraw；source_id: PUB-BRE2023STEADY；locator: primary publisher abstract and experimental sections；role: Sourceanalysisorboundedliteraturecontext;notindependentraw。
- 本組適用層級：campaign_context；No source result is transferred to unmatched50mm/methane cases.。
- 使用／控制因子：factor_and_role: fuel/diluentcomposition:source-specificinput；source_refs: source_id: GA-6187d07f3add；locator: physical3–6/Table1；source_id: PUB-BRE2021RESULTS；locator: primary publisher abstract；source_id: PUB-BRE2023STEADY；locator: primary publisher abstract and experimental sections；factor_and_role: burnergeometry/ambientstate/flow:source-specificconditions；source_refs: source_id: GA-6187d07f3add；locator: physical3–6/Table1；source_id: PUB-BRE2021RESULTS；locator: primary publisher abstract；source_id: PUB-BRE2023STEADY；locator: primary publisher abstract and experimental sections；factor_and_role: thermalfeedback/calorimetry/flameendpoint:keepmeasured/computed/operationalrolesseparate；source_refs: source_id: GA-6187d07f3add；locator: physical3–6/Table1；source_id: PUB-BRE2021RESULTS；locator: primary publisher abstract；source_id: PUB-BRE2023STEADY；locator: primary publisher abstract and experimental sections。
- 來源限制：Do not add194,59 and103 as independent burns.；Day rows and nested oxygen lists do not identify a complete Cartesian design or per-trial pressure.。
- 搜尋句（改寫）：The source guide reports two ISS rounds and an overall ignited-flame count; the earlier results paper analyzed a selected successful-ignition cohort and a later paper expanded the analysis. These are overlapping selections, not independent repeats.。
- 來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/其他研究文件_正文類型待確認/第一批下載/PSI-20_ACME BRE/Science Documents/PSI-20_Science Documents_BRE_data_interpretation_20220804.pdf>)
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/其他研究文件_正文類型待確認/第一批下載/PSI-20_ACME BRE/Science Documents/PSI-20_Science Documents_BRE_data_interpretation_20220804.pdf>)

- 共同來源：**Burning in microgravity: Experimental results and analysis**；primary publisher abstract；[來源](<https://doi.org/10.1016/j.combustflame.2021.01.035>)

- 共同來源：**Demonstrating steady burning for small flat materials in microgravity in a quiescent ambient**；primary publisher abstract and experimental sections；[來源](<https://doi.org/10.1016/j.proci.2022.08.107>)

### BRE-F03　Fuel termination and self-extinction are distinct endpoints

**PSI-20_Reports_Dissertation-PD-revised_**

來源有自然熄滅與操作燃料終止；19070C1的fuel-off命令不是本次已驗證的實際零流量或化學熄滅時刻。

- 證據身份：source_event_and_analyzed_result。
- 文獻定位：GA-2ada277f4acc: physical32/Table3.1 and110–111/Table6.1; GA-6187d07f3add: test-log/trace guidance; PUB-BRE2023STEADY: primary publisher abstract。
- 使用數據部分：source_id: GA-2ada277f4acc；locator: physical32/Table3.1 and110–111/Table6.1；role: Sourceanalysisorboundedliteraturecontext;notindependentraw；source_id: GA-6187d07f3add；locator: test-log/trace guidance；role: Sourceanalysisorboundedliteraturecontext;notindependentraw；source_id: PUB-BRE2023STEADY；locator: primary publisher abstract；role: Sourceanalysisorboundedliteraturecontext;notindependentraw。
- 本組適用層級：direct_selected19070C1；No source result is transferred to unmatched50mm/methane cases.。
- 使用／控制因子：factor_and_role: fuel/diluentcomposition:source-specificinput；source_refs: source_id: GA-2ada277f4acc；locator: physical32/Table3.1 and110–111/Table6.1；source_id: GA-6187d07f3add；locator: test-log/trace guidance；source_id: PUB-BRE2023STEADY；locator: primary publisher abstract；factor_and_role: burnergeometry/ambientstate/flow:source-specificconditions；source_refs: source_id: GA-2ada277f4acc；locator: physical32/Table3.1 and110–111/Table6.1；source_id: GA-6187d07f3add；locator: test-log/trace guidance；source_id: PUB-BRE2023STEADY；locator: primary publisher abstract；factor_and_role: thermalfeedback/calorimetry/flameendpoint:keepmeasured/computed/operationalrolesseparate；source_refs: source_id: GA-2ada277f4acc；locator: physical32/Table3.1 and110–111/Table6.1；source_id: GA-6187d07f3add；locator: test-log/trace guidance；source_id: PUB-BRE2023STEADY；locator: primary publisher abstract。
- 來源限制：FT is not a spontaneous extinction label or measured material burn-out time.；Commanded flow, measured MFC response and actual burner-boundary delivery remain distinct.。
- 搜尋句（改寫）：Some source flames self-extinguished; others reached the operational fuel-termination endpoint. The selected19070C1 record contains a fuel-off command, not a newly verified physical-flow-off or chemical-extinction time.。
- 來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/研究報告與書章/第一批下載/PSI-20_ACME BRE/Reports/PSI-20_Reports_Dissertation-PD-revised_.pdf>)
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/研究報告與書章/第一批下載/PSI-20_ACME BRE/Reports/PSI-20_Reports_Dissertation-PD-revised_.pdf>)

- 共同來源：**PSI-20_Science Documents_BRE_data_interpretation_20220804**；test-log/trace guidance；[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/其他研究文件_正文類型待確認/第一批下載/PSI-20_ACME BRE/Science Documents/PSI-20_Science Documents_BRE_data_interpretation_20220804.pdf>)

- 共同來源：**Demonstrating steady burning for small flat materials in microgravity in a quiescent ambient**；primary publisher abstract；[來源](<https://doi.org/10.1016/j.proci.2022.08.107>)

### BRE-F04　Heat-flux steadiness is not shape steadiness

**A Burning Rate Emulator (BRE) for study of condensed fuel burning in microgravity**

短落塔中火焰仍成長，而熱回授進入較慢變化階段；作者限制準穩態假設並要求較長試驗。

- 證據身份：source_measurement_plus_model_interpretation。
- 文獻定位：GA-c613c4770ad7: physical8–10, Figs7–13。
- 使用數據部分：source_id: GA-c613c4770ad7；locator: physical8–10, Figs7–13；role: Sourceanalysisorboundedliteraturecontext;notindependentraw。
- 本組適用層級：related_ground_drop；No source result is transferred to unmatched50mm/methane cases.。
- 使用／控制因子：factor_and_role: fuel/diluentcomposition:source-specificinput；source_refs: source_id: GA-c613c4770ad7；locator: physical8–10, Figs7–13；factor_and_role: burnergeometry/ambientstate/flow:source-specificconditions；source_refs: source_id: GA-c613c4770ad7；locator: physical8–10, Figs7–13；factor_and_role: thermalfeedback/calorimetry/flameendpoint:keepmeasured/computed/operationalrolesseparate；source_refs: source_id: GA-c613c4770ad7；locator: physical8–10, Figs7–13。
- 來源限制：Short-drop data are not orbital ISS steady-state measurements.；A source-selected isotherm and radiation-free ellipsoidal theory do not independently validate a full flame contour.。
- 搜尋句（改寫）：Short-drop BRE flames continued growing while heat feedback approached a slower-changing endpoint; the source explicitly limits quasi-steady assumptions and calls for longer-duration tests.。
- 來源：[來源](<https://doi.org/10.1016/j.combustflame.2018.01.044>)
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/earth_space_transfer_20261114/phase7/role_D/assets/Markan2018_BRE_microgravity.pdf>)

### BRE-F05　Heat of gasification can be a reconstructed effective quantity

**Emulation of condensed fuel flames with gaseous fuels supplied through a porous copper calorimeter**

有效氣化熱由淨熱回授除以指定質量通量反算；同量再重建熱通量只是代數重建，不是獨立預測。

- 證據身份：source_equation_identity。
- 文獻定位：GA-52b0b7aaa14e: physical5–6, Eqs14–19; GA-2ada277f4acc: material emulation and heat-flux analysis chapters。
- 使用數據部分：source_id: GA-52b0b7aaa14e；locator: physical5–6, Eqs14–19；role: Sourceanalysisorboundedliteraturecontext;notindependentraw；source_id: GA-2ada277f4acc；locator: material emulation and heat-flux analysis chapters；role: Sourceanalysisorboundedliteraturecontext;notindependentraw。
- 本組適用層級：model_identity_not_independentprediction；No source result is transferred to unmatched50mm/methane cases.。
- 使用／控制因子：factor_and_role: fuel/diluentcomposition:source-specificinput；source_refs: source_id: GA-52b0b7aaa14e；locator: physical5–6, Eqs14–19；source_id: GA-2ada277f4acc；locator: material emulation and heat-flux analysis chapters；factor_and_role: burnergeometry/ambientstate/flow:source-specificconditions；source_refs: source_id: GA-52b0b7aaa14e；locator: physical5–6, Eqs14–19；source_id: GA-2ada277f4acc；locator: material emulation and heat-flux analysis chapters；factor_and_role: thermalfeedback/calorimetry/flameendpoint:keepmeasured/computed/operationalrolesseparate；source_refs: source_id: GA-52b0b7aaa14e；locator: physical5–6, Eqs14–19；source_id: GA-2ada277f4acc；locator: material emulation and heat-flux analysis chapters。
- 來源限制：The input stream's heat of combustion, inferredL, surface state and smoke point require consistent mixture bases.；A fitted effective property is not an independently measured material intrinsic constant.。
- 搜尋句（改寫）：The emulator commonly infers an effective heat of gasification from net heat feedback divided by prescribed mass flux; using the same quantities to reconstruct that heat flux is bookkeeping, not independent prediction.。
- 來源：[來源](<https://doi.org/10.1002/fam.2896>)
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/earth_space_transfer_20261114/phase4_earth_experiment_search/role_D/assets/Auth2020_BRE_FAM.pdf>)

- 共同來源：**PSI-20_Reports_Dissertation-PD-revised_**；material emulation and heat-flux analysis chapters；[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/研究報告與書章/第一批下載/PSI-20_ACME BRE/Reports/PSI-20_Reports_Dissertation-PD-revised_.pdf>)

### BRE-F06　Calorimeter and local gauges require different corrections

**Emulation of condensed fuel flames with gaseous fuels supplied through a porous copper calorimeter**

局部熱流規與銅熱量計對應不同空間熱回授，需分別處理支撐／桿件損失、校準及飛行修正。

- 證據身份：source_instrument_model_and_calibration。
- 文獻定位：GA-52b0b7aaa14e: physical3–6, calorimeter energy balances; GA-22b0ccfa2c69: physical26–34 and82–85; GA-2ada277f4acc: physical76 and AppendixA。
- 使用數據部分：source_id: GA-52b0b7aaa14e；locator: physical3–6, calorimeter energy balances；role: Sourceanalysisorboundedliteraturecontext;notindependentraw；source_id: GA-22b0ccfa2c69；locator: physical26–34 and82–85；role: Sourceanalysisorboundedliteraturecontext;notindependentraw；source_id: GA-2ada277f4acc；locator: physical76 and AppendixA；role: Sourceanalysisorboundedliteraturecontext;notindependentraw。
- 本組適用層級：calibration_context；No source result is transferred to unmatched50mm/methane cases.。
- 使用／控制因子：factor_and_role: fuel/diluentcomposition:source-specificinput；source_refs: source_id: GA-52b0b7aaa14e；locator: physical3–6, calorimeter energy balances；source_id: GA-22b0ccfa2c69；locator: physical26–34 and82–85；source_id: GA-2ada277f4acc；locator: physical76 and AppendixA；factor_and_role: burnergeometry/ambientstate/flow:source-specificconditions；source_refs: source_id: GA-52b0b7aaa14e；locator: physical3–6, calorimeter energy balances；source_id: GA-22b0ccfa2c69；locator: physical26–34 and82–85；source_id: GA-2ada277f4acc；locator: physical76 and AppendixA；factor_and_role: thermalfeedback/calorimetry/flameendpoint:keepmeasured/computed/operationalrolesseparate；source_refs: source_id: GA-52b0b7aaa14e；locator: physical3–6, calorimeter energy balances；source_id: GA-22b0ccfa2c69；locator: physical26–34 and82–85；source_id: GA-2ada277f4acc；locator: physical76 and AppendixA。
- 來源限制：Ground BRE2 constants cannot be transferred unchanged to flight hardware.；Source-derived calorimeter flux is not independent direct heat flux; condensation/radial nonuniformity and correction assumptions need source-specific handling.。
- 搜尋句（改寫）：Local gauges and the copper calorimeter reconstruct different spatial heat-feedback quantities. Source work includes sensor/backing/rod losses, calibration and flight correction concerns.。
- 來源：[來源](<https://doi.org/10.1002/fam.2896>)
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/earth_space_transfer_20261114/phase4_earth_experiment_search/role_D/assets/Auth2020_BRE_FAM.pdf>)

- 共同來源：**Auth2019_BRE_1g_thesis**；physical26–34 and82–85；[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/earth_space_transfer_20261114/phase4_earth_experiment_search/role_D/assets/Auth2019_BRE_1g_thesis.pdf>)

- 共同來源：**PSI-20_Reports_Dissertation-PD-revised_**；physical76 and AppendixA；[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/研究報告與書章/第一批下載/PSI-20_ACME BRE/Reports/PSI-20_Reports_Dissertation-PD-revised_.pdf>)

### BRE-F07　A computed temperature separator is not a measured ignition threshold

**Demonstrating steady burning for small flat materials in microgravity in a quiescent ambient**

後期BRE以計算火焰溫度區分來源自然熄滅與供料終止群，提出可燃性圖；不是直接量測的材料點燃界限。

- 證據身份：source_model_interpretation_not_gas_thermometry。
- 文獻定位：PUB-BRE2023STEADY: primary publisher abstract/steadiness analysis; PUB-BRE2023MAP: primary publisher abstract。
- 使用數據部分：source_id: PUB-BRE2023STEADY；locator: primary publisher abstract/steadiness analysis；role: Sourceanalysisorboundedliteraturecontext;notindependentraw；source_id: PUB-BRE2023MAP；locator: primary publisher abstract；role: Sourceanalysisorboundedliteraturecontext;notindependentraw。
- 本組適用層級：context_selected_ethylene_model_cohort；No source result is transferred to unmatched50mm/methane cases.。
- 使用／控制因子：factor_and_role: fuel/diluentcomposition:source-specificinput；source_refs: source_id: PUB-BRE2023STEADY；locator: primary publisher abstract/steadiness analysis；source_id: PUB-BRE2023MAP；locator: primary publisher abstract；factor_and_role: burnergeometry/ambientstate/flow:source-specificconditions；source_refs: source_id: PUB-BRE2023STEADY；locator: primary publisher abstract/steadiness analysis；source_id: PUB-BRE2023MAP；locator: primary publisher abstract；factor_and_role: thermalfeedback/calorimetry/flameendpoint:keepmeasured/computed/operationalrolesseparate；source_refs: source_id: PUB-BRE2023STEADY；locator: primary publisher abstract/steadiness analysis；source_id: PUB-BRE2023MAP；locator: primary publisher abstract。
- 來源限制：The critical temperature is model-derived and source-selected; do not present it as gas thermometry or a universal material ignition slider threshold.；No joint validation of arbitrary material, geometry, atmosphere and external heat flux follows.。
- 搜尋句（改寫）：Later BRE analyses use a calculated flame-temperature range to distinguish source self-extinguished and fuel-terminated conditions and propose flammability diagrams.。
- 來源：[來源](<https://doi.org/10.1016/j.proci.2022.08.107>)
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/gas_combustion_evidence_20261115/abstract_supplement/abstracts/ef381be11878b287.txt>)

- 共同來源：**Flammability maps for microgravity burning of a small flat material in a quiescent ambient**；primary publisher abstract；[來源](<https://doi.org/10.1016/j.combustflame.2023.112809>)

| Model ID | 公式／預測量 | 展示程式 | 數值比較與限制 |
| --- | --- | --- | --- |
| READINESS-PSI-20 | 原文方程／模型參見MODEL_INVENTORY；本次尚未閉合；BRE ISS flight cases (inputs missing) | 未實作 · 尚未取得本機檔案 | 未執行／缺閉合輸入；來源就緒度盤點，不是數值預測；R²（模型全群）=N/A；尚未取得／不適用；The ground-drop fixed example is separate from the flight raw-data comparison.；Matched flight geometry/flow/composition/property convention and original target trace |

| 可開啟的圖／工具 | 身份與用途 |
| --- | --- |
| [開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/gas_combustion_evidence_20261115/models/comparison.html>) | 選正確架構；缺資料的研究僅顯示就緒度，不畫假預測 |

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
| BRE-F01 / fuel/diluentcomposition:source-specificinput | '物理參數'!G40 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| BRE-F01 / burnergeometry/ambientstate/flow:source-specificconditions | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| BRE-F01 / thermalfeedback/calorimetry/flameendpoint:keepmeasured/computed/operationalrolesseparate | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| BRE-F02 / fuel/diluentcomposition:source-specificinput | '物理參數'!G40 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| BRE-F02 / burnergeometry/ambientstate/flow:source-specificconditions | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| BRE-F02 / thermalfeedback/calorimetry/flameendpoint:keepmeasured/computed/operationalrolesseparate | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| BRE-F03 / fuel/diluentcomposition:source-specificinput | '物理參數'!G40 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| BRE-F03 / burnergeometry/ambientstate/flow:source-specificconditions | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| BRE-F03 / thermalfeedback/calorimetry/flameendpoint:keepmeasured/computed/operationalrolesseparate | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| BRE-F04 / fuel/diluentcomposition:source-specificinput | '物理參數'!G40 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| BRE-F04 / burnergeometry/ambientstate/flow:source-specificconditions | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| BRE-F04 / thermalfeedback/calorimetry/flameendpoint:keepmeasured/computed/operationalrolesseparate | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| BRE-F05 / fuel/diluentcomposition:source-specificinput | '物理參數'!G40 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| BRE-F05 / burnergeometry/ambientstate/flow:source-specificconditions | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| BRE-F05 / thermalfeedback/calorimetry/flameendpoint:keepmeasured/computed/operationalrolesseparate | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| BRE-F06 / fuel/diluentcomposition:source-specificinput | '物理參數'!G40 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| BRE-F06 / burnergeometry/ambientstate/flow:source-specificconditions | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| BRE-F06 / thermalfeedback/calorimetry/flameendpoint:keepmeasured/computed/operationalrolesseparate | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| BRE-F07 / fuel/diluentcomposition:source-specificinput | '物理參數'!G40 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| BRE-F07 / burnergeometry/ambientstate/flow:source-specificconditions | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| BRE-F07 / thermalfeedback/calorimetry/flameendpoint:keepmeasured/computed/operationalrolesseparate | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |

尚未取得可逐項對照的紀錄。

## 3. 共用資料的多項結論比較

| 結論／文獻 | 資料重疊身份 | 共同處 | 不同處／不能合併之處 |
| --- | --- | --- | --- |
| BRE-F01；BRE-F02；BRE-F03；BRE-F04；BRE-F05；BRE-F06；BRE-F07 | 來源系列；精確論文／試次交集仍以每項data_used為準 | 不把多份出版物當獨立實驗。 | 尚未取得完全同試次的多篇結論比較時保留缺口。 |

## 4. 消防洞見

| 類別 | 對應證據 | 數據支持的判斷 | 策略／產品構想 | 待驗證 |
| --- | --- | --- | --- | --- |
| 預防 | 尚未取得／不適用 | 尚未建立本組可直接支持此消防用途的完整量測鏈。 | 先補本組對應的物理端點與資料配對，再設計策略測試。 | 相關系列與方法限制只能提供研究脈絡，不能代替本組產品或操作效能驗證。 |
| 偵測 | 尚未取得／不適用 | 尚未建立本組可直接支持此消防用途的完整量測鏈。 | 先補本組對應的物理端點與資料配對，再設計策略測試。 | 相關系列與方法限制只能提供研究脈絡，不能代替本組產品或操作效能驗證。 |
| 撲滅／抑制 | 尚未取得／不適用 | 尚未建立本組可直接支持此消防用途的完整量測鏈。 | 先補本組對應的物理端點與資料配對，再設計策略測試。 | 相關系列與方法限制只能提供研究脈絡，不能代替本組產品或操作效能驗證。 |

## 逐次索引

| 原始檔／資料位置 | Trial／Run／列 | 共享身份與保留事項 |
| --- | --- | --- |
| 尚未取得／不適用 | trial_id: 19070C1；source_ref: source_id: GA-2ada277f4acc；locator: physical111/Table6.1; alternate summary physical32/Table3.1；source_table_values: diameter_mm: 25；mass_flux_total_g_m2_s: 4.43；pressure_bar: 0.605；O2_mole_fraction_before_after: 0.342；0.331；heat_of_combustion_kJ_g: 23.6；duration_s: 120；end_condition: FT；flame_height_mm: 25.6；base_radius_mm: 20.4；alternate_summary_values: pressure_bar: 0.57；mass_flux_total_g_m2_s: 4.42；O2_mole_fraction: 0.34；interpretation: Versions preserved. Source chamber estimates and prescribed stream are distinct from direct ambient species measurements. FT means fuel termination, not self-extinction. | raw_parameters_as_stored: 尚未取得／不適用；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |

## 缺件與適用範圍

- Auxiliary, not a genuine solid-fuel specimen dataset.
- Do not create a completeP/O2/fuel grid from operation-day lists.
- Raw3400%/2100% oxygen strings remain source-quality issues, not physical percentages.
