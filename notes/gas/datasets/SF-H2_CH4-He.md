# s-Flame H2_CH4 He

小資料集 ID：`SF-H2_CH4-He`

## 資料身份與範圍

| 項目 | 內容 |
| --- | --- |
| 原始 NASA PSI investigation | [PSI-23](https://psi.nasa.gov/physci/repo/data/investigations/PSI-23) |
| 相關PSI索引（不是原始資料） | 尚未取得／不適用 |
| 材料／配方 | fuel_family: H2_CH4；diluent_family: He；composition: Sourcebottleidentitypluspublishedselecteddeliveredmixtures;runmatchedfractionnotinferred |
| 幾何 | shape: porous spherical burner；exact_diameter_per_trial: 尚未確認；guard: Generichardware6.35–12.7mmcapabilitynotassignedtoalldayrows |
| 實驗模式 | gravity: ISS microgravity；configuration: normal spherical diffusion；flow_history: constant and rampvariantsneedfullasrun |
| 證據角色 | gaseous_flame_experiment |
| 環境 | gravity: 尚未確認；mode: gravity: ISS microgravity；configuration: normal spherical diffusion；flow_history: constant and rampvariantsneedfullasrun |
| 資料粒度／共享試片 | Per-row source values retained; summary/day/variant rows are not promoted to independent burns. |
| 可用數值 | source_conditions_available_target_join_and_complete_chemistry_transport_closure_not_established |

## 1. 文獻結果與視覺化程式

### SF-F01　Flow reduction and flow increase can approach different extinction branches

**PSI-23_Reports_s_Flame_final_report_20210729**

氮稀釋乙烯來源在20–30% C2H4、3 cc/s附近操作，降流在1 cc/s前熄滅，升流在8 cc/s前輻射熄滅。19256影像損失與20029重複／補充保留原身份。

- 證據身份：source_selected_operational_observations。
- 文獻定位：GA-2056f8f85291: physical26–27,TestDays19254/19256/20029。
- 使用數據部分：source_id: GA-2056f8f85291；locator: physical26–27,TestDays19254/19256/20029；role: Sourceanalysisorboundedliteraturecontext;notindependentraw。
- 本組適用層級：related_other_composition；19254/19256/20029sourceselectedobservationsnotallrows.。
- 使用／控制因子：factor_and_role: C2H4/N2molefractions:mixture；source_refs: source_id: GA-2056f8f85291；locator: physical26–27,TestDays19254/19256/20029；factor_and_role: 3cc/sandflowramps:sourcecontrols；source_refs: source_id: GA-2056f8f85291；locator: physical26–27,TestDays19254/19256/20029；factor_and_role: radiative/kineticendpoint:authorclassification；source_refs: source_id: GA-2056f8f85291；locator: physical26–27,TestDays19254/19256/20029；factor_and_role: 19256/20029:imaginglossandrepeatcontext；source_refs: source_id: GA-2056f8f85291；locator: physical26–27,TestDays19254/19256/20029。
- 來源限制：Example mixture/flow statements are not exact per-burn thresholds or universal ventilation rules.；Do not label an instrumental cutoff or lost image as physical flame extinction.。
- 搜尋句（改寫）：For nitrogen-diluted ethylene, the report describes20–30%C2H4 at3cc/s with ramp-down extinction before1cc/s and ramp-up radiative extinction before8cc/s. TestDay19256 imagery loss and repeat/augmentation on20029 are preserved.。
- 來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/研究報告與書章/第一批下載/PSI-23_ACME s-Flame/Reports/PSI-23_Reports_s_Flame_final_report_20210729.pdf>)
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/研究報告與書章/第一批下載/PSI-23_ACME s-Flame/Reports/PSI-23_Reports_s_Flame_final_report_20210729.pdf>)

### SF-F02　Helium changes ignition and endpoint access, not merely a dilution percentage

**PSI-23_Reports_s_Flame_final_report_20210729**

He在燃料／氧化劑側會改變來源點火與熄滅行為，部分動力學界限仍未定。有些火焰達燃燒器溫度或時間上限，不能當成自然熄滅。

- 證據身份：source_observation_with_provisional_author_interpretation。
- 文獻定位：GA-2056f8f85291: physical27–30。
- 使用數據部分：source_id: GA-2056f8f85291；locator: physical27–30；role: Sourceanalysisorboundedliteraturecontext;notindependentraw。
- 本組適用層級：context_selected_He_operating_cases；Authorprovisionalmechanismsandcutoffspreserved.。
- 使用／控制因子：factor_and_role: He/N2:diluentandtransportrole；source_refs: source_id: GA-2056f8f85291；locator: physical27–30；factor_and_role: fuelblendandO2mixtures:input；source_refs: source_id: GA-2056f8f85291；locator: physical27–30；factor_and_role: burnertemperaturelimit/timeout:operationalendpoint；source_refs: source_id: GA-2056f8f85291；locator: physical27–30；factor_and_role: brightness/flash/extinction:opticalobservationsnotuniquemechanism；source_refs: source_id: GA-2056f8f85291；locator: physical27–30。
- 來源限制：He is not an interchangeableN2 replacement with unchanged transport.；Some mechanisms and transientflash interpretations remain preliminary; the reportdoes not supply a universal control threshold.。
- 搜尋句（改寫）：The source describes He fuel/oxidizer cases with shifted ignition/extinction behavior and still-inconclusive kinetic limits. Some flames lasted to burner-temperature limits or timeout rather than naturally extinguishing.。
- 來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/研究報告與書章/第一批下載/PSI-23_ACME s-Flame/Reports/PSI-23_Reports_s_Flame_final_report_20210729.pdf>)
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/研究報告與書章/第一批下載/PSI-23_ACME s-Flame/Reports/PSI-23_Reports_s_Flame_final_report_20210729.pdf>)

### SF-F03　Bottle labels, actual diluted streams and gas sampling are distinct

**PSI-23_Reports_s_Flame_final_report_20210729**

瓶內純H2不等於實際送出的H2／N2或He混合物；報告Table1與26–28段需共同讀。艙內GC在攪拌測試前後／中間取樣，不是火焰內局部物種場。

- 證據身份：source_data_scope。
- 文獻定位：GA-2056f8f85291: physical22,24,26–28; GA-f4ae0b6ffb4c: physical1–2。
- 使用數據部分：source_id: GA-2056f8f85291；locator: physical22,24,26–28；role: Sourceanalysisorboundedliteraturecontext;notindependentraw；source_id: GA-f4ae0b6ffb4c；locator: physical1–2；role: Sourceanalysisorboundedliteraturecontext;notindependentraw。
- 本組適用層級：direct_source_data_roles；No bottle/drift/GCsamplereinterpretation.。
- 使用／控制因子：factor_and_role: TestDay:sourceidentity；source_refs: source_id: GA-2056f8f85291；locator: physical22,24,26–28；source_id: GA-f4ae0b6ffb4c；locator: physical1–2；factor_and_role: stockbottleandactualdilution:separateroles；source_refs: source_id: GA-2056f8f85291；locator: physical22,24,26–28；source_id: GA-f4ae0b6ffb4c；locator: physical1–2；factor_and_role: chamberGCsampling:averaged/stirredgasspecies；source_refs: source_id: GA-2056f8f85291；locator: physical22,24,26–28；source_id: GA-f4ae0b6ffb4c；locator: physical1–2；factor_and_role: fullTestIDvariants:notautomaticallyreplicates；source_refs: source_id: GA-2056f8f85291；locator: physical22,24,26–28；source_id: GA-f4ae0b6ffb4c；locator: physical1–2。
- 來源限制：Trailing ID variants are not necessarily independent replicates.；RawN3…N6 strings are retained; the sourceTable1N2 crosswalk is separate.；Flame luminosity is not necessarily flame strength; no automatic brightness-only safety test.。
- 搜尋句（改寫）：Table1daily bottle/atmosphere values and paragraphs26–28 give different roles: pure stockH2 may be delivered as dilutedH2/N2 orHe mixtures, and chamberGC sampling is before/between/after stirred tests rather than local in-flame profiles.。
- 來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/研究報告與書章/第一批下載/PSI-23_ACME s-Flame/Reports/PSI-23_Reports_s_Flame_final_report_20210729.pdf>)
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/研究報告與書章/第一批下載/PSI-23_ACME s-Flame/Reports/PSI-23_Reports_s_Flame_final_report_20210729.pdf>)

- 共同來源：**PSI-23_Science Documents_ACME s-Flame DoD**；physical1–2；[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/其他研究文件_正文類型待確認/第一批下載/PSI-23_ACME s-Flame/Science Documents/PSI-23_Science Documents_ACME s-Flame DoD.pdf>)

| Model ID | 公式／預測量 | 展示程式 | 數值比較與限制 |
| --- | --- | --- | --- |
| READINESS-PSI-23 | 原文方程／模型參見MODEL_INVENTORY；本次尚未閉合；s-Flame (inputs missing) | 未實作 · 尚未取得本機檔案 | 未執行／缺閉合輸入；來源就緒度盤點，不是數值預測；R²（模型全群）=N/A；尚未取得／不適用；Published moving-front conservation equations require full closure; measured front speed cannot become an independent predictor of itself.；Chemistry, transport, radiation, initial/boundary fields and independent front history |

| 可開啟的圖／工具 | 身份與用途 |
| --- | --- |
| [開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/gas_combustion_evidence_20261115/models/comparison.html>) | 選正確架構；缺資料的研究僅顯示就緒度，不畫假預測 |

## 2. 使用資料與參數總表的因子對照

| 總表原分類 | 來源身份 | 原欄名單位 | 原欄名例 | 總表定位 |
| --- | --- | --- | --- | --- |
| 光電／離子偵測訊號 | 儀器原始訊號 | 未由欄名確認 | IonCurrent；PMT1；PMT2；PMT3 | '物理參數'!A125:K125 |
| 光電／離子偵測訊號 | 儀器設定／控制參數 | 未由欄名確認 | PMT 1 Gain；PMT 2 Gain；PMT 3 Gain | '物理參數'!A126:K126 |
| 其他氣體組成／濃度 | 條件或分析量 | 未由欄名確認 | Atmosphere*；Dilution of fuel and inert | '物理參數'!A127:K127 |
| 影像／光譜設定 | 儀器設定或影像座標 | 未由欄名確認 | ACME Camera；Intensified Camera；filterNumber；2009-01-01 001 00:00:36:075~ipsug.Halcon~CameraB2020::CameraB2020(int；QObject*) "CIR_5_CAMERA_4/configFile" i32MaxExposure = 61052；2009-01-01 001 00:00:45:249~ipsug.Halcon~CameraB2020::CameraB2020(int；2009-01-01 001 00:00:33:250~ipsug.Halcon~CameraB2020::CameraB2020(int；2009-01-01 001 00:00:40:956~ipsug.Halcon~CameraB2020::CameraB2020(int；2009-01-01 001 00:00:31:484~ipsug.Halcon~CameraB2020::CameraB2020(int；2009-01-01 001 00:00:33:735~ipsug.Halcon~CameraB2020::CameraB2020(int；其餘見原始欄位 | '物理參數'!A128:K128 |
| 流速／通風 | 量測或設定 | 未由欄名確認 | Ramp to final velocity | '物理參數'!A129:K129 |
| 溫度 | 量測或設定 | C | 2019-09-13 256 17:25:57:028~acme~Copyright (C) 2002-13；2007-01-01 001 00:00:28:117~acme~Copyright (C) 2002-13；2007-01-01 001 01:41:36:042~acme~Copyright (C) 2002-13；2007-01-01 001 00:00:28:014~acme~Copyright (C) 2002-13；2019-09-13 256 14:17:24:932~acme~Copyright (C) 2002-13；2007-01-01 001 00:00:28:073~acme~Copyright (C) 2002-13；2007-01-01 001 00:00:27:775~acme~Copyright (C) 2002-13；2007-01-01 001 00:00:27:760~acme~Copyright (C) 2002-13；2007-01-01 001 00:45:31:931~acme~Copyright (C) 2002-13；2007-01-01 001 00:00:28:062~acme~Copyright (C) 2002-13；其餘見原始欄位 | '物理參數'!A130:K130 |
| 溫度 | 量測或設定 | 未由欄名確認 | Thermocouple；TC200A；TC200B | '物理參數'!A131:K131 |
| 熱通量／輻射 | 量測通道或來源分析量 | 未由欄名確認 | Radiometer；Radiometer+60；Radiometer+60CJ；Radiometer+30；Radiometer+30CJ；RadiometerCenter；RadiometerCenterCJ；Radiometer-30；Radiometer-30CJ；Radiometer-60；其餘見原始欄位 | '物理參數'!A132:K132 |
| 硬體電壓／電流／功率 | 原始訊號或狀態 | uV | microvolts_(uV) | '物理參數'!A133:K133 |
| 電場電壓／電流 | 儀器設定／控制參數 | 未由欄名確認 | EfieldSetpointOut | '物理參數'!A134:K134 |
| 電場電壓／電流 | 量測或設定 | 未由欄名確認 | EField；EFieldPol；EfieldVoltage；efieldConfig；efieldPolarity | '物理參數'!A135:K135 |
| 體積流量／MFC | 儀器設定／控制參數 | V | MFCA1Setpoint(V)；MFCA2Setpoint(V)；MFCA3Setpoint(V) | '物理參數'!A136:K136 |
| 體積流量／MFC | 儀器設定／控制參數 | 未由欄名確認 | MFCA1 Full Scale；MFCA2 Full Scale；MFCA3 Full Scale | '物理參數'!A137:K137 |
| 體積流量／MFC | 量測或設定 | 未由欄名確認 | MFCA1 Gas；MFCA2 Gas；MFCA3 Gas；MFCA1StaticMixerFlow；MFCA2BypassFlow；MFCA3FuelFlow；MFCs on for priming；MFCs off；mfc1GasType；mfc2GasType；其餘見原始欄位 | '物理參數'!A138:K138 |

以上是該 investigation 的欄位盤點；個別結論實際使用的因子以第1節與下列補充為準。

| 本組實際因子 | 總表定位／未列欄位 | 文獻中的用途 |
| --- | --- | --- |
| SF-F01 / C2H4/N2molefractions:mixture | '物理參數'!G127 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| SF-F01 / 3cc/sandflowramps:sourcecontrols | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| SF-F01 / radiative/kineticendpoint:authorclassification | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| SF-F01 / 19256/20029:imaginglossandrepeatcontext | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| SF-F02 / He/N2:diluentandtransportrole | '物理參數'!G127 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| SF-F02 / fuelblendandO2mixtures:input | '物理參數'!G127 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| SF-F02 / burnertemperaturelimit/timeout:operationalendpoint | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| SF-F02 / brightness/flash/extinction:opticalobservationsnotuniquemechanism | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| SF-F03 / TestDay:sourceidentity | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| SF-F03 / stockbottleandactualdilution:separateroles | '物理參數'!G127 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| SF-F03 / chamberGCsampling:averaged/stirredgasspecies | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| SF-F03 / fullTestIDvariants:notautomaticallyreplicates | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |

尚未取得可逐項對照的紀錄。

## 3. 共用資料的多項結論比較

| 結論／文獻 | 資料重疊身份 | 共同處 | 不同處／不能合併之處 |
| --- | --- | --- | --- |
| GA-2056f8f85291；GA-f4ae0b6ffb4c；GA-6686f5f2038e | report_appendix_overlap | FinalreportAppendixDrepeats30dayoperatingreport. | Objectives/earlymechanisminterpretations/notreconstructedperrunclosure;do notsumversions. |

## 4. 消防洞見

| 類別 | 對應證據 | 數據支持的判斷 | 策略／產品構想 | 待驗證 |
| --- | --- | --- | --- | --- |
| 預防 | 尚未取得／不適用 | 尚未建立本組可直接支持此消防用途的完整量測鏈。 | 先補本組對應的物理端點與資料配對，再設計策略測試。 | 相關系列與方法限制只能提供研究脈絡，不能代替本組產品或操作效能驗證。 |
| 偵測 | 尚未取得／不適用 | 尚未建立本組可直接支持此消防用途的完整量測鏈。 | 先補本組對應的物理端點與資料配對，再設計策略測試。 | 相關系列與方法限制只能提供研究脈絡，不能代替本組產品或操作效能驗證。 |
| 撲滅／抑制 | 尚未取得／不適用 | 尚未建立本組可直接支持此消防用途的完整量測鏈。 | 先補本組對應的物理端點與資料配對，再設計策略測試。 | 相關系列與方法限制只能提供研究脈絡，不能代替本組產品或操作效能驗證。 |

## 逐次索引

| 原始檔／資料位置 | Trial／Run／列 | 共享身份與保留事項 |
| --- | --- | --- |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-23_ACME s-Flame\Experimental table\PSI-23_Experimental table_ACME s-Flame.csv | trial_id: 20132；csv_row_including_header: 11；record_kind: operation_day_summary_not_individual_trial；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Test Type: First round of tests with nitrogen-diluted fuel and oxygen；Test Day*: 20132；Year: 2020；Month: May；Date: 11；Atmosphere*: ~21% O2 with He；Fuel Bottle: 25% H2, 20% CH4, with He；Flames Ignited*: 7；Notes: 尚未取得／不適用；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-23_ACME s-Flame\Experimental table\PSI-23_Experimental table_ACME s-Flame.csv | trial_id: 20136；csv_row_including_header: 12；record_kind: operation_day_summary_not_individual_trial；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Test Type: Second round of tests with helium-diluted fuel and oxygen；Test Day*: 20136；Year: 2020；Month: May；Date: 15；Atmosphere*: ~21% O2 with He；Fuel Bottle: 20% H2, 25% CH4, with He；Flames Ignited*: 11；Notes: 尚未取得／不適用；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-23_ACME s-Flame\Experimental table\PSI-23_Experimental table_ACME s-Flame.csv | trial_id: 20142；csv_row_including_header: 13；record_kind: operation_day_summary_not_individual_trial；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Test Type: Second round of tests with helium-diluted fuel and oxygen；Test Day*: 20142；Year: 2020；Month: May；Date: 21；Atmosphere*: ~30% O2 with He；Fuel Bottle: 30% H2, 15% CH4, with He；Flames Ignited*: 17；Notes: 尚未取得／不適用；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |

## 缺件與適用範圍

- Exact measuredg, per-runburnerdiameter andcompleteboundary/chemistryfilesnotclosed.
