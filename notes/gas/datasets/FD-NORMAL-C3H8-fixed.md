# FlameDesign C3H8 Normal fixed

小資料集 ID：`FD-NORMAL-C3H8-fixed`

## 資料身份與範圍

| 項目 | 內容 |
| --- | --- |
| 原始 NASA PSI investigation | [PSI-10](https://psi.nasa.gov/physci/repo/data/investigations/PSI-10) |
| 相關PSI索引（不是原始資料） | 尚未取得／不適用 |
| 材料／配方 | fuel_family: C3H8；diluent: N2；stream_basis: source mole fractions; inverse fuel identification comes from source report, not a blankFuelCSV cell |
| 幾何 | shape: porous spherical burner；nominal_diameter_mm: 6.35；diameter_source: source_id: GA-1d64b7f42f07；locator: physical24 footnote,0.25inch sphere |
| 實驗模式 | flame_configuration: normal；gravity: ISS microgravity；control: fixed |
| 證據角色 | gaseous_flame_experiment |
| 環境 | gravity: 尚未確認；mode: flame_configuration: normal；gravity: ISS microgravity；control: fixed |
| 資料粒度／共享試片 | Per-row source values retained; summary/day/variant rows are not promoted to independent burns. |
| 可用數值 | source_conditions_available_target_join_and_complete_chemistry_transport_closure_not_established |

## 1. 文獻結果與視覺化程式

### FD-F01　Small long-lived spherical flames and large radiative extinction are distinct outcomes

**PSI-10_Reports_FinalRpt_ACMEFlameDesign**

ISS來源區分受燃燒器升溫限制的小型長時火焰，以及向外成長後輻射熄滅的火焰。排程或燃燒器溫度停止條件，不是自然熄滅端點。

- 證據身份：source_observation_and_author_model_interpretation。
- 文獻定位：GA-1d64b7f42f07: physical25–26。
- 使用數據部分：source_id: GA-1d64b7f42f07；locator: physical25–26；role: Sourceanalysisorboundedliteraturecontext;notindependentraw。
- 本組適用層級：context_selected_source_family；Publication examples do not establish every indexed row outcome.。
- 使用／控制因子：factor_and_role: fuel/oxidizer mixture(molefraction):controlled/sourceestimated；source_refs: source_id: GA-1d64b7f42f07；locator: physical25–26；factor_and_role: reactantmassflow(mg/s):input；source_refs: source_id: GA-1d64b7f42f07；locator: physical25–26；factor_and_role: flameradius/extension:sourceanalyzedoutput；source_refs: source_id: GA-1d64b7f42f07；locator: physical25–26；factor_and_role: burnertemperaturelimit:operationalcensoring；source_refs: source_id: GA-1d64b7f42f07；locator: physical25–26。
- 來源限制：Source selected conditions, not a universal critical flame diameter; no arbitrary-material safety approval.。
- 搜尋句（改寫）：The source ISS results distinguish long-lived small flames limited by burner heating from outwardly growing flames that extinguish radiatively. A scheduled or burner-temperature cutoff is not a spontaneous extinction endpoint.。
- 來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/研究報告與書章/第一批下載/PSI-10_ACME_Flame Design/Reports/PSI-10_Reports_FinalRpt_ACMEFlameDesign.pdf>)
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/研究報告與書章/第一批下載/PSI-10_ACME_Flame Design/Reports/PSI-10_Reports_FinalRpt_ACMEFlameDesign.pdf>)

### FD-F02　A1bar ethylene extinction relation has a narrow source domain

**PSI-10_Reports_FinalRpt_ACMEFlameDesign**

指定1 bar乙烯normal／inverse子集報告1130 K臨界條件，且燃料／氧為基準的火焰面質量通量不同。不能用可見焰徑或燃燒器面積替代來源反算的峰溫位置與反應面。

- 證據身份：source_experiment_plus_transient_model。
- 文獻定位：GA-1d64b7f42f07: physical25–26; PUB-FD-CRITICAL2023: primary publisher abstract。
- 使用數據部分：source_id: GA-1d64b7f42f07；locator: physical25–26；role: Sourceanalysisorboundedliteraturecontext;notindependentraw；source_id: PUB-FD-CRITICAL2023；locator: primary publisher abstract；role: Sourceanalysisorboundedliteraturecontext;notindependentraw。
- 本組適用層級：context_not_same_fuel_or_ramp；Exact paper-to-CSV subset remains unjoined;1130Knot assignedtoallrows.。
- 使用／控制因子：factor_and_role: ambientpressure1bar:sourcepapersubset；source_refs: source_id: GA-1d64b7f42f07；locator: physical25–26；source_id: PUB-FD-CRITICAL2023；locator: primary publisher abstract；factor_and_role: ethyleneandO2streamfractions:inputs；source_refs: source_id: GA-1d64b7f42f07；locator: physical25–26；source_id: PUB-FD-CRITICAL2023；locator: primary publisher abstract；factor_and_role: peaktemperature1130K:sourceexperimental/modelinterpretation；source_refs: source_id: GA-1d64b7f42f07；locator: physical25–26；source_id: PUB-FD-CRITICAL2023；locator: primary publisher abstract；factor_and_role: flamesurfacereactantmassflux(g/m²s):sourceinferredcriterion；source_refs: source_id: GA-1d64b7f42f07；locator: physical25–26；source_id: PUB-FD-CRITICAL2023；locator: primary publisher abstract。
- 來源限制：1130K is not an ignition temperature or a safety threshold for propane, all pressures, crew atmospheres or arbitrary geometry.；Exact publication-to-CSV trial membership is not fully joined; property/model role and experimental thermometry must be distinguished.。
- 搜尋句（改寫）：A published normal/inverse ethylene1bar subset reports a critical1130K and different fuel-based/oxygen-based flame-surface mass fluxes. Its inferred peak-temperature radius and source-specific chemistry must not be replaced with visible diameter or burner area.。
- 來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/研究報告與書章/第一批下載/PSI-10_ACME_Flame Design/Reports/PSI-10_Reports_FinalRpt_ACMEFlameDesign.pdf>)
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/研究報告與書章/第一批下載/PSI-10_ACME_Flame Design/Reports/PSI-10_Reports_FinalRpt_ACMEFlameDesign.pdf>)

- 共同來源：**Critical temperature and reactant mass flux for radiative extinction of ethylene microgravity spherical diffusion flames at 1 bar**；primary publisher abstract；[來源](<https://doi.org/10.1016/j.proci.2022.07.043>)

### FD-F03　Stream assignment is essential to composition and pressure comparisons

**PSI-10_Experimental table_Flame Design_Normal Flame.csv**

normal為燃料從多孔球流向外側氧化劑，inverse則相反。原表含RAMPED時變控制及計算的Zst／Tad，與量測量分開。

- 證據身份：source_data_structure_and_bookkeeping。
- 文獻定位：DATA-10_Experimental table_Flame Design_Normal Flame: Fuel/Test/Xfuel/meanZst/Tad columns; DATA-10_Experimental table_Flame Design_Inverse Flame: FlameType/Test/XO2/ambientXC2H4 columns; GA-e783fc0da3d3: physical8,Eqs1.1–1.2。
- 使用數據部分：source_id: DATA-10_Experimental table_Flame Design_Normal Flame；locator: Fuel/Test/Xfuel/meanZst/Tad columns；role: Rawconditions/sourceclassifiedrecords；source_id: DATA-10_Experimental table_Flame Design_Inverse Flame；locator: FlameType/Test/XO2/ambientXC2H4 columns；role: Rawconditions/sourceclassifiedrecords；source_id: GA-e783fc0da3d3；locator: physical8,Eqs1.1–1.2；role: Sourceanalysisorboundedliteraturecontext;notindependentraw。
- 本組適用層級：direct_data_structure；This subgroup retains streamroles and originalRAMPED fields.。
- 使用／控制因子：factor_and_role: normal/inversestreamroles:configuration；source_refs: source_id: DATA-10_Experimental table_Flame Design_Normal Flame；locator: Fuel/Test/Xfuel/meanZst/Tad columns；source_id: DATA-10_Experimental table_Flame Design_Inverse Flame；locator: FlameType/Test/XO2/ambientXC2H4 columns；source_id: GA-e783fc0da3d3；locator: physical8,Eqs1.1–1.2；factor_and_role: Xfuel/XO2:molefractions；source_refs: source_id: DATA-10_Experimental table_Flame Design_Normal Flame；locator: Fuel/Test/Xfuel/meanZst/Tad columns；source_id: DATA-10_Experimental table_Flame Design_Inverse Flame；locator: FlameType/Test/XO2/ambientXC2H4 columns；source_id: GA-e783fc0da3d3；locator: physical8,Eqs1.1–1.2；factor_and_role: mO2/mfuel/mN2(mg/s):flow；source_refs: source_id: DATA-10_Experimental table_Flame Design_Normal Flame；locator: Fuel/Test/Xfuel/meanZst/Tad columns；source_id: DATA-10_Experimental table_Flame Design_Inverse Flame；locator: FlameType/Test/XO2/ambientXC2H4 columns；source_id: GA-e783fc0da3d3；locator: physical8,Eqs1.1–1.2；factor_and_role: Zst/Tad(K):computeddescriptors；source_refs: source_id: DATA-10_Experimental table_Flame Design_Normal Flame；locator: Fuel/Test/Xfuel/meanZst/Tad columns；source_id: DATA-10_Experimental table_Flame Design_Inverse Flame；locator: FlameType/Test/XO2/ambientXC2H4 columns；source_id: GA-e783fc0da3d3；locator: physical8,Eqs1.1–1.2；factor_and_role: RAMPED:timevaryingcontrol；source_refs: source_id: DATA-10_Experimental table_Flame Design_Normal Flame；locator: Fuel/Test/Xfuel/meanZst/Tad columns；source_id: DATA-10_Experimental table_Flame Design_Inverse Flame；locator: FlameType/Test/XO2/ambientXC2H4 columns；source_id: GA-e783fc0da3d3；locator: physical8,Eqs1.1–1.2。
- 來源限制：Normal does not mean1g. Tad and Zst are computed descriptors, not measured flame temperature or predicted flame behavior.；RAMPED is a time-history requirement, not zero or a fixed input.。
- 搜尋句（改寫）：Normal means fuel exits the porous sphere into oxidizer; inverse means oxidizer exits into fuel. The source includes ramped cases and calculatedZst/Tad alongside measured or source-calculated conditions.。
- 來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/01_實驗資料/第一批下載/PSI-10_ACME_Flame Design/Experimental table/PSI-10_Experimental table_Flame Design_Normal Flame.csv>)
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/01_實驗資料/第一批下載/PSI-10_ACME_Flame Design/Experimental table/PSI-10_Experimental table_Flame Design_Normal Flame.csv>)

- 共同來源：**PSI-10_Experimental table_Flame Design_Inverse Flame.csv**；FlameType/Test/XO2/ambientXC2H4 columns；[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/01_實驗資料/第一批下載/PSI-10_ACME_Flame Design/Experimental table/PSI-10_Experimental table_Flame Design_Inverse Flame.csv>)

- 共同來源：**PSI-10_Science Documents_SRD_ACMEFlameDesign**；physical8,Eqs1.1–1.2；[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/其他研究文件_正文類型待確認/第一批下載/PSI-10_ACME_Flame Design/Science Documents/PSI-10_Science Documents_SRD_ACMEFlameDesign.pdf>)

| Model ID | 公式／預測量 | 展示程式 | 數值比較與限制 |
| --- | --- | --- | --- |
| READINESS-PSI-10 | 原文方程／模型參見MODEL_INVENTORY；本次尚未閉合；FlameDesign spherical flames (inputs missing) | 未實作 · 尚未取得本機檔案 | 未執行／缺閉合輸入；來源就緒度盤點，不是數值預測；R²（模型全群）=N/A；尚未取得／不適用；Related Earth Roper jets are available separately; they do not close the actual spherical flame experiment.；Case-matched sphere geometry, reaction/transport/radiation closure and original measured geometry targets |

| 可開啟的圖／工具 | 身份與用途 |
| --- | --- |
| [開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/gas_combustion_evidence_20261115/models/comparison.html>) | 選正確架構；缺資料的研究僅顯示就緒度，不畫假預測 |

## 2. 使用資料與參數總表的因子對照

| 總表原分類 | 來源身份 | 原欄名單位 | 原欄名例 | 總表定位 |
| --- | --- | --- | --- | --- |
| 光電／離子偵測訊號 | 儀器原始訊號 | 未由欄名確認 | IonCurrent；PMT1；PMT2；PMT3 | '物理參數'!A7:K7 |
| 光電／離子偵測訊號 | 儀器設定／控制參數 | 未由欄名確認 | PMT 1 Gain；PMT 2 Gain；PMT 3 Gain | '物理參數'!A8:K8 |
| 其他氣體組成／濃度 | 條件或分析量 | 未由欄名確認 | Xfuel；Nitrogen；Hydrogen / Helium (45/55)；Dilution of fuel and inert | '物理參數'!A9:K9 |
| 化學計量混合分率 | 計算／分析參數 | 未由欄名確認 | mean Zst；Stoichiometric Conversion Equation | '物理參數'!A10:K10 |
| 壓力 | 量測或設定 | atm | pinit (atm)；pfinal (atm)；pmean (atm) | '物理參數'!A11:K11 |
| 壓力 | 量測或設定 | psia | Pstart (psia)；Pend (psia)；Returns the delta pressure (psia) of the combustion chamber from event start to event end | '物理參數'!A12:K12 |
| 壓力 | 量測或設定 | 未由欄名確認 | Chamber Pressure | '物理參數'!A13:K13 |
| 密度 | 量測或來源分析量 | g/L | Density (g/L) | '物理參數'!A14:K14 |
| 密度 | 量測或來源分析量 | 未由欄名確認 | Density | '物理參數'!A15:K15 |
| 尺寸／幾何 | 儀器設定／控制參數 | 未由欄名確認 | TP_PARAMETER_IGNITER_IGNITION_POSITION_1；TP_PARAMETER_IGNITER_IGNITION_POSITION_2 | '物理參數'!A16:K16 |
| 影像／光譜設定 | 儀器設定或影像座標 | 未由欄名確認 | filterNumber；along with ACME & Intensified Camera Packages and Rack went Off Nominal. | '物理參數'!A17:K17 |
| 氧濃度 | 量測或條件值 | 未由欄名確認 | XO2；XO2 (init)；XO2 (final)；Oxygen；O2；Ethylene: C2H4 → - 3 O2 + 2 H2O + 2 CO2；Methane: CH4 → - 2 O2 + 2 H2O + CO2；Hydrogen: 2 H2 → - O2 + 2 H2O；PickOxygen；O2 Fill | '物理參數'!A18:K18 |
| 流速／通風 | 量測或設定 | 未由欄名確認 | Ramp to final velocity | '物理參數'!A19:K19 |
| 溫度 | 量測或設定 | C | 2019-07-26 207 11:53:01:582~acme~Copyright (C) 2002-13；2007-01-01 001 00:00:28:018~acme~Copyright (C) 2002-13；2019-04-26 116 00:45:53:031~acme~Copyright (C) 2002-13；2021-11-24 328 13:58:00:669~acme~Copyright (C) 2002-13；2019-05-30 150 22:48:25:031~acme~Copyright (C) 2002-13；2022-02-04 035 16:09:22:795~acme~Copyright (C) 2002-13；2007-01-01 001 00:00:28:116~acme~Copyright (C) 2002-13；2007-01-01 001 00:00:29:300~acme~Copyright (C) 2002-13；2007-01-01 001 00:00:28:514~acme~Copyright (C) 2002-13；2019-05-22 142 13:39:15:059~acme~Copyright (C) 2002-13；其餘見原始欄位 | '物理參數'!A20:K20 |
| 溫度 | 量測或設定 | Standard Liters - 0 DegC, 760 Torr | ACME MFCs (Standard Liters - 0 DegC, 760 Torr) | '物理參數'!A21:K21 |
| 溫度 | 量測或設定 | Standard Liters - 0 DegC, 760 torr | Start Mixture (Standard Liters - 0 DegC, 760 torr)；Event Delta (Standard Liters - 0 DegC, 760 torr)；Finish Mixture (Standard Liters - 0 DegC, 760 torr)；Recirculation Loop Contents (Standard Liters - 0 DegC, 760 torr) | '物理參數'!A22:K22 |
| 溫度 | 量測或設定 | 未由欄名確認 | Thermocouple；Chamber Temperature；FCU_MP_TM1；FCU_MP_TM2；FCU_MP_TM3；FCU_MP_TM4；TC200A；TC200B | '物理參數'!A23:K23 |
| 熱通量／輻射 | 儀器設定／控制參數 | 未由欄名確認 | Radiometer3+60LoGain；Radiometer3+60HiGain；Radiometer3+30LoGain；Radiometer3+30HiGain；Radiometer3-10LoGain；Radiometer3-10HiGain | '物理參數'!A24:K24 |
| 熱通量／輻射 | 量測通道或來源分析量 | 未由欄名確認 | Radiometer；RadiometerOffset；RadiometerOffsetCJ；Radiometer+60；Radiometer+60CJ；Radiometer+30；Radiometer+30CJ；RadiometerCenter；RadiometerCenterCJ；Radiometer-30；其餘見原始欄位 | '物理參數'!A25:K25 |
| 硬體電壓／電流／功率 | 原始訊號或狀態 | uV | microvolts_(uV) | '物理參數'!A26:K26 |
| 硬體電壓／電流／功率 | 原始訊號或狀態 | 未由欄名確認 | Archive numbers prior to power cycle；Archive numbers after power cycle | '物理參數'!A27:K27 |
| 絕熱溫度 | 計算／分析參數 | K | Tad (K) | '物理參數'!A28:K28 |
| 質量流率 | 量測或設定 | mg/s | mO2 (mg/s)；mN2 (mg/s)；mtot (mg/s)；mfuel (mg/s) | '物理參數'!A29:K29 |
| 電場電壓／電流 | 儀器設定／控制參數 | 未由欄名確認 | EfieldSetpointOut | '物理參數'!A30:K30 |
| 電場電壓／電流 | 量測或設定 | 未由欄名確認 | EField；EFieldPol；EfieldVoltage | '物理參數'!A31:K31 |
| 體積流量／MFC | 儀器設定／控制參數 | V | MFCA1Setpoint(V)；MFCA2Setpoint(V)；MFCA3Setpoint(V) | '物理參數'!A32:K32 |
| 體積流量／MFC | 儀器設定／控制參數 | 未由欄名確認 | MFCA1 Full Scale；MFCA2 Full Scale；MFCA3 Full Scale | '物理參數'!A33:K33 |
| 體積流量／MFC | 量測或設定 | 未由欄名確認 | MFCA1 Gas；MFCA2 Gas；MFCA3 Gas；MFCDiluent；MFCFuel；MFCN2；MFCO2；MFCA1StaticMixerFlow；MFCA2BypassFlow；MFCA3FuelFlow；其餘見原始欄位 | '物理參數'!A34:K34 |
| 點火功率／電壓／電流 | 儀器設定／控制參數 | 未由欄名確認 | TP_PARAMETER_IGNITER_WATTAGE；TP_PARAMETER_IGNITER_ON_TIME | '物理參數'!A35:K35 |
| 點火功率／電壓／電流 | 量測或設定 | ms | Igniter On Time (ms) | '物理參數'!A36:K36 |
| 點火功率／電壓／電流 | 量測或設定 | 未由欄名確認 | Igniter Wattage | '物理參數'!A37:K37 |

以上是該 investigation 的欄位盤點；個別結論實際使用的因子以第1節與下列補充為準。

| 本組實際因子 | 總表定位／未列欄位 | 文獻中的用途 |
| --- | --- | --- |
| FD-F01 / fuel/oxidizer mixture(molefraction):controlled/sourceestimated | '物理參數'!G9 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| FD-F01 / reactantmassflow(mg/s):input | '物理參數'!G29 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| FD-F01 / flameradius/extension:sourceanalyzedoutput | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| FD-F01 / burnertemperaturelimit:operationalcensoring | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| FD-F02 / ambientpressure1bar:sourcepapersubset | '物理參數'!G11；'物理參數'!G12；'物理參數'!G13 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| FD-F02 / ethyleneandO2streamfractions:inputs | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| FD-F02 / peaktemperature1130K:sourceexperimental/modelinterpretation | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| FD-F02 / flamesurfacereactantmassflux(g/m²s):sourceinferredcriterion | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| FD-F03 / normal/inversestreamroles:configuration | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| FD-F03 / Xfuel/XO2:molefractions | '物理參數'!G18 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| FD-F03 / mO2/mfuel/mN2(mg/s):flow | '物理參數'!G29 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| FD-F03 / Zst/Tad(K):computeddescriptors | '物理參數'!G28 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| FD-F03 / RAMPED:timevaryingcontrol | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |

| 文獻因子／疑點 | 正確讀法或需補資料 |
| --- | --- |
| 流股與模式 | normal／inverse不是重力；氧化劑流與艙內氣氛分開；Tad與Zst為計算量。 |

## 3. 共用資料的多項結論比較

| 結論／文獻 | 資料重疊身份 | 共同處 | 不同處／不能合併之處 |
| --- | --- | --- | --- |
| GA-1d64b7f42f07；PUB-FD-CRITICAL2023；PUB-FD-STEADY2023 | overlapping_campaign_analysis | SourcepapersanalyzeFlameDesignsphericalflamesandadddifferentmodelquestions. | Criticalextinctionvsconditionsforsteadyexistence;exactrunintersectionunverified;notindependentreplication. |

## 4. 消防洞見

| 類別 | 對應證據 | 數據支持的判斷 | 策略／產品構想 | 待驗證 |
| --- | --- | --- | --- | --- |
| 預防 | FD-F03 | normal／inverse、燃料流／氧化劑流／艙內氣氛與Tad各有不同角色。 | 搜尋條件先確認氧濃度所在流股，再選近似火源與材料暴露資料。 | 同流股組成、P/T、幾何與實際局部反應條件。 |
| 偵測 | 尚未取得／不適用 | 尚未建立本組可直接支持此消防用途的完整量測鏈。 | 先補本組對應的物理端點與資料配對，再設計策略測試。 | 相關系列與方法限制只能提供研究脈絡，不能代替本組產品或操作效能驗證。 |
| 撲滅／抑制 | 尚未取得／不適用 | 尚未建立本組可直接支持此消防用途的完整量測鏈。 | 先補本組對應的物理端點與資料配對，再設計策略測試。 | 相關系列與方法限制只能提供研究脈絡，不能代替本組產品或操作效能驗證。 |

## 逐次索引

| 原始檔／資料位置 | Trial／Run／列 | 共享身份與保留事項 |
| --- | --- | --- |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-10_ACME_Flame Design\Experimental table\PSI-10_Experimental table_Flame Design_Normal Flame.csv | trial_id: 21301A1；csv_row_including_header: 189；record_kind: source_named_record；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Flame Type: Normal；Day: 13；Fuel: C3H8；Test: 21301A1；Xfuel: 1；mfuel (mg/s): 1.2；mN2 (mg/s): 0；mtot (mg/s): 1.2；XO2 (init): 0.4；XO2 (final): 尚未取得／不適用；pinit (atm): 0.931972789；pfinal (atm): 尚未取得／不適用；pmean (atm): 尚未取得／不適用；mean Zst: 0.106461571；Tad (K): 2734.953406；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-10_ACME_Flame Design\Experimental table\PSI-10_Experimental table_Flame Design_Normal Flame.csv | trial_id: 21301A2；csv_row_including_header: 190；record_kind: source_named_record；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Flame Type: Normal；Day: 13；Fuel: C3H8；Test: 21301A2；Xfuel: 1；mfuel (mg/s): 1.2；mN2 (mg/s): 0；mtot (mg/s): 1.2；XO2 (init): 0.4；XO2 (final): 尚未取得／不適用；pinit (atm): 0.931972789；pfinal (atm): 尚未取得／不適用；pmean (atm): 尚未取得／不適用；mean Zst: 0.106461571；Tad (K): 2734.953406；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-10_ACME_Flame Design\Experimental table\PSI-10_Experimental table_Flame Design_Normal Flame.csv | trial_id: 21301A3；csv_row_including_header: 191；record_kind: source_named_record；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Flame Type: Normal；Day: 13；Fuel: C3H8；Test: 21301A3；Xfuel: 1；mfuel (mg/s): 1.75；mN2 (mg/s): 0；mtot (mg/s): 1.75；XO2 (init): 0.4；XO2 (final): 尚未取得／不適用；pinit (atm): 0.931972789；pfinal (atm): 尚未取得／不適用；pmean (atm): 尚未取得／不適用；mean Zst: 0.106461571；Tad (K): 2734.953406；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-10_ACME_Flame Design\Experimental table\PSI-10_Experimental table_Flame Design_Normal Flame.csv | trial_id: 21301A4；csv_row_including_header: 192；record_kind: source_named_record；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Flame Type: Normal；Day: 13；Fuel: C3H8；Test: 21301A4；Xfuel: 1；mfuel (mg/s): 1.6；mN2 (mg/s): 0；mtot (mg/s): 1.6；XO2 (init): 0.4；XO2 (final): 尚未取得／不適用；pinit (atm): 0.931972789；pfinal (atm): 尚未取得／不適用；pmean (atm): 尚未取得／不適用；mean Zst: 0.106461571；Tad (K): 2734.953406；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-10_ACME_Flame Design\Experimental table\PSI-10_Experimental table_Flame Design_Normal Flame.csv | trial_id: 21301A5；csv_row_including_header: 193；record_kind: source_named_record；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Flame Type: Normal；Day: 13；Fuel: C3H8；Test: 21301A5；Xfuel: 1；mfuel (mg/s): 1.1；mN2 (mg/s): 0；mtot (mg/s): 1.1；XO2 (init): 0.4；XO2 (final): 尚未取得／不適用；pinit (atm): 0.931972789；pfinal (atm): 尚未取得／不適用；pmean (atm): 尚未取得／不適用；mean Zst: 0.106461571；Tad (K): 2734.953406；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-10_ACME_Flame Design\Experimental table\PSI-10_Experimental table_Flame Design_Normal Flame.csv | trial_id: 21301A6；csv_row_including_header: 194；record_kind: source_named_record；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Flame Type: Normal；Day: 13；Fuel: C3H8；Test: 21301A6；Xfuel: 1；mfuel (mg/s): 1.05；mN2 (mg/s): 0；mtot (mg/s): 1.05；XO2 (init): 0.4；XO2 (final): 尚未取得／不適用；pinit (atm): 0.931972789；pfinal (atm): 尚未取得／不適用；pmean (atm): 尚未取得／不適用；mean Zst: 0.106461571；Tad (K): 2734.953406；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-10_ACME_Flame Design\Experimental table\PSI-10_Experimental table_Flame Design_Normal Flame.csv | trial_id: 21301C1；csv_row_including_header: 195；record_kind: source_named_record；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Flame Type: Normal；Day: 13；Fuel: C3H8；Test: 21301C1；Xfuel: 0.25；mfuel (mg/s): 1.05；mN2 (mg/s): 2.001192204；mtot (mg/s): 3.051192204；XO2 (init): 0.4；XO2 (final): 尚未取得／不適用；pinit (atm): 0.931972789；pfinal (atm): 尚未取得／不適用；pmean (atm): 尚未取得／不適用；mean Zst: 0.257182771；Tad (K): 2607.182737；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-10_ACME_Flame Design\Experimental table\PSI-10_Experimental table_Flame Design_Normal Flame.csv | trial_id: 21301C2；csv_row_including_header: 196；record_kind: source_named_record；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Flame Type: Normal；Day: 13；Fuel: C3H8；Test: 21301C2；Xfuel: 0.25；mfuel (mg/s): 1.05；mN2 (mg/s): 2.001192204；mtot (mg/s): 3.051192204；XO2 (init): 0.4；XO2 (final): 尚未取得／不適用；pinit (atm): 0.931972789；pfinal (atm): 尚未取得／不適用；pmean (atm): 尚未取得／不適用；mean Zst: 0.257182771；Tad (K): 2607.182737；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-10_ACME_Flame Design\Experimental table\PSI-10_Experimental table_Flame Design_Normal Flame.csv | trial_id: 21301D1；csv_row_including_header: 197；record_kind: source_named_record；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Flame Type: Normal；Day: 13；Fuel: C3H8；Test: 21301D1；Xfuel: 0.167；mfuel (mg/s): 1；mN2 (mg/s): 3.168887189；mtot (mg/s): 4.168887189；XO2 (init): 0.4；XO2 (final): 尚未取得／不適用；pinit (atm): 0.931972789；pfinal (atm): 尚未取得／不適用；pmean (atm): 尚未取得／不適用；mean Zst: 0.331866302；Tad (K): 2523.97951；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-10_ACME_Flame Design\Experimental table\PSI-10_Experimental table_Flame Design_Normal Flame.csv | trial_id: 21301D2；csv_row_including_header: 198；record_kind: source_named_record；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Flame Type: Normal；Day: 13；Fuel: C3H8；Test: 21301D2；Xfuel: 0.167；mfuel (mg/s): 1；mN2 (mg/s): 3.168887189；mtot (mg/s): 4.168887189；XO2 (init): 0.4；XO2 (final): 尚未取得／不適用；pinit (atm): 0.931972789；pfinal (atm): 尚未取得／不適用；pmean (atm): 尚未取得／不適用；mean Zst: 0.331866302；Tad (K): 2523.97951；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-10_ACME_Flame Design\Experimental table\PSI-10_Experimental table_Flame Design_Normal Flame.csv | trial_id: 21301A7；csv_row_including_header: 199；record_kind: source_named_record；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Flame Type: Normal；Day: 13；Fuel: C3H8；Test: 21301A7；Xfuel: 1；mfuel (mg/s): 1.2；mN2 (mg/s): 0；mtot (mg/s): 1.2；XO2 (init): 0.4；XO2 (final): 尚未取得／不適用；pinit (atm): 0.931972789；pfinal (atm): 尚未取得／不適用；pmean (atm): 尚未取得／不適用；mean Zst: 0.106461571；Tad (K): 2734.953406；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-10_ACME_Flame Design\Experimental table\PSI-10_Experimental table_Flame Design_Normal Flame.csv | trial_id: 21301A8；csv_row_including_header: 200；record_kind: source_named_record；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Flame Type: Normal；Day: 13；Fuel: C3H8；Test: 21301A8；Xfuel: 1；mfuel (mg/s): 1.3；mN2 (mg/s): 0；mtot (mg/s): 1.3；XO2 (init): 0.4；XO2 (final): 尚未取得／不適用；pinit (atm): 0.931972789；pfinal (atm): 尚未取得／不適用；pmean (atm): 尚未取得／不適用；mean Zst: 0.106461571；Tad (K): 2734.953406；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-10_ACME_Flame Design\Experimental table\PSI-10_Experimental table_Flame Design_Normal Flame.csv | trial_id: 21301A9；csv_row_including_header: 201；record_kind: source_named_record；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Flame Type: Normal；Day: 13；Fuel: C3H8；Test: 21301A9；Xfuel: 1；mfuel (mg/s): 1.45；mN2 (mg/s): 0；mtot (mg/s): 1.45；XO2 (init): 0.4；XO2 (final): 尚未取得／不適用；pinit (atm): 0.931972789；pfinal (atm): 尚未取得／不適用；pmean (atm): 尚未取得／不適用；mean Zst: 0.106461571；Tad (K): 2734.953406；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-10_ACME_Flame Design\Experimental table\PSI-10_Experimental table_Flame Design_Normal Flame.csv | trial_id: 21301H1；csv_row_including_header: 202；record_kind: source_named_record；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Flame Type: Normal；Day: 13；Fuel: C3H8；Test: 21301H1；Xfuel: 1；mfuel (mg/s): 1.4；mN2 (mg/s): 0；mtot (mg/s): 1.4；XO2 (init): 0.4；XO2 (final): 尚未取得／不適用；pinit (atm): 0.931972789；pfinal (atm): 尚未取得／不適用；pmean (atm): 尚未取得／不適用；mean Zst: 0.106461571；Tad (K): 2734.953406；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-10_ACME_Flame Design\Experimental table\PSI-10_Experimental table_Flame Design_Normal Flame.csv | trial_id: 21301H2；csv_row_including_header: 203；record_kind: source_named_record；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Flame Type: Normal；Day: 13；Fuel: C3H8；Test: 21301H2；Xfuel: 1；mfuel (mg/s): 0.95；mN2 (mg/s): 0；mtot (mg/s): 0.95；XO2 (init): 0.4；XO2 (final): 尚未取得／不適用；pinit (atm): 0.931972789；pfinal (atm): 尚未取得／不適用；pmean (atm): 尚未取得／不適用；mean Zst: 0.106461571；Tad (K): 2734.953406；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-10_ACME_Flame Design\Experimental table\PSI-10_Experimental table_Flame Design_Normal Flame.csv | trial_id: 21301H3；csv_row_including_header: 204；record_kind: source_named_record；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Flame Type: Normal；Day: 13；Fuel: C3H8；Test: 21301H3；Xfuel: 1；mfuel (mg/s): 1.05；mN2 (mg/s): 0；mtot (mg/s): 1.05；XO2 (init): 0.4；XO2 (final): 尚未取得／不適用；pinit (atm): 0.931972789；pfinal (atm): 尚未取得／不適用；pmean (atm): 尚未取得／不適用；mean Zst: 0.106461571；Tad (K): 2734.953406；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-10_ACME_Flame Design\Experimental table\PSI-10_Experimental table_Flame Design_Normal Flame.csv | trial_id: 21301J1；csv_row_including_header: 205；record_kind: source_named_record；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Flame Type: Normal；Day: 13；Fuel: C3H8；Test: 21301J1；Xfuel: 0.1；mfuel (mg/s): 0.55；mN2 (mg/s): 3.144730606；mtot (mg/s): 3.694730606；XO2 (init): 0.4；XO2 (final): 尚未取得／不適用；pinit (atm): 0.931972789；pfinal (atm): 尚未取得／不適用；pmean (atm): 尚未取得／不適用；mean Zst: 0.444563692；Tad (K): 2357.78851；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-10_ACME_Flame Design\Experimental table\PSI-10_Experimental table_Flame Design_Normal Flame.csv | trial_id: 21301J2；csv_row_including_header: 206；record_kind: source_named_record；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Flame Type: Normal；Day: 13；Fuel: C3H8；Test: 21301J2；Xfuel: 0.111；mfuel (mg/s): 0.6；mN2 (mg/s): 3.052869788；mtot (mg/s): 3.652869788；XO2 (init): 0.4；XO2 (final): 尚未取得／不適用；pinit (atm): 0.931972789；pfinal (atm): 尚未取得／不適用；pmean (atm): 尚未取得／不適用；mean Zst: 0.420415848；Tad (K): 2398.666876；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-10_ACME_Flame Design\Experimental table\PSI-10_Experimental table_Flame Design_Normal Flame.csv | trial_id: 21301J3；csv_row_including_header: 207；record_kind: source_named_record；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Flame Type: Normal；Day: 13；Fuel: C3H8；Test: 21301J3；Xfuel: 0.125；mfuel (mg/s): 0.65；mN2 (mg/s): 2.890610961；mtot (mg/s): 3.540610961；XO2 (init): 0.4；XO2 (final): 尚未取得／不適用；pinit (atm): 0.931972789；pfinal (atm): 尚未取得／不適用；pmean (atm): 尚未取得／不適用；mean Zst: 0.393571748；Tad (K): 2440.404887；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-10_ACME_Flame Design\Experimental table\PSI-10_Experimental table_Flame Design_Normal Flame.csv | trial_id: 21301J4；csv_row_including_header: 208；record_kind: source_named_record；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Flame Type: Normal；Day: 13；Fuel: C3H8；Test: 21301J4；Xfuel: 0.1；mfuel (mg/s): 0.65；mN2 (mg/s): 3.716499807；mtot (mg/s): 4.366499807；XO2 (init): 0.4；XO2 (final): 尚未取得／不適用；pinit (atm): 0.931972789；pfinal (atm): 尚未取得／不適用；pmean (atm): 尚未取得／不適用；mean Zst: 0.444563692；Tad (K): 2357.78851；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |

## 缺件與適用範圍

- 無新增缺件紀錄；不代表資料完整。
