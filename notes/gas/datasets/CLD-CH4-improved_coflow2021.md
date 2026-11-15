# CLD CH4 improved_coflow2021

小資料集 ID：`CLD-CH4-improved_coflow2021`

## 資料身份與範圍

| 項目 | 內容 |
| --- | --- |
| 原始 NASA PSI investigation | [PSI-21](https://psi.nasa.gov/physci/repo/data/investigations/PSI-21) |
| 相關PSI索引（不是原始資料） | 尚未取得／不適用 |
| 材料／配方 | fuel_family: CH4；diluent: N2；composition: per-run diluentvaries; rawbottle andreportedspecieskeptseparate |
| 幾何 | shape: concentric coflow burner；hardware_variant: improved_coflow2021；run_matched_dimensions: not inserted from generic ACME capability range |
| 實驗模式 | gravity: ISS microgravity；configuration: normal coflow；matched_ground_paper_cases: separate source panels, not all daily rows |
| 證據角色 | gaseous_flame_experiment |
| 環境 | gravity: 尚未確認；mode: gravity: ISS microgravity；configuration: normal coflow；matched_ground_paper_cases: separate source panels, not all daily rows |
| 資料粒度／共享試片 | Per-row source values retained; summary/day/variant rows are not promoted to independent burns. |
| 可用數值 | source_conditions_available_target_join_and_complete_chemistry_transport_closure_not_established |

## 1. 文獻結果與視覺化程式

### CLD-F01　Matched ground and microgravity soot fields differ

**873c31d3e4dd62e0_CLD_Flame_final_report_20220330**

來源以複製飛行硬體和匹配冷流流速作地面／微重力對照；40 cm/s下的乙烯40／60／80／100%案例，其光學反算soot與溫度場對稀釋及重力呈不同變化。

- 證據身份：source_matched_hardware_comparison。
- 文獻定位：GA-5054384d478c: physical29–30,Figs11–12。
- 使用數據部分：source_id: GA-5054384d478c；locator: physical29–30,Figs11–12；role: Sourceanalysisorboundedliteraturecontext;notindependentraw。
- 本組適用層級：related_other_fuel_groundpair；Exactpanel/CSVburnIDsnotfullyjoined.。
- 使用／控制因子：factor_and_role: fuelandcoflowexitvelocities40cm/s:coldflowmatchedcontrols；source_refs: source_id: GA-5054384d478c；locator: physical29–30,Figs11–12；factor_and_role: ethylene40/60/80/100%:composition；source_refs: source_id: GA-5054384d478c；locator: physical29–30,Figs11–12；factor_and_role: 1g/ISS:environment；source_refs: source_id: GA-5054384d478c；locator: physical29–30,Figs11–12；factor_and_role: soottemperature(K):pyrometryoutput；source_refs: source_id: GA-5054384d478c；locator: physical29–30,Figs11–12；factor_and_role: sootvolumefraction:opticalinverseoutput；source_refs: source_id: GA-5054384d478c；locator: physical29–30,Figs11–12。
- 來源限制：Reported soot volume fractions require optical/calibration assumptions and are not smoke-detector alarm counts.；These40cm/s panel results must not be attached to every daily index row or a different coflow design.。
- 搜尋句（改寫）：The report compares copied flight hardware and matched cold-flow fuel/coflow velocities. At40cm/s, ethylene cases are40/60/80/100% fuel, with source-derived soot distributions and temperature fields changing differently with dilution under microgravity and1g.。
- 來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/實驗附帶文件/補下載/PSI-21/Raw Data/873c31d3e4dd62e0_CLD_Flame_final_report_20220330.pdf>)
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/實驗附帶文件/補下載/PSI-21/Raw Data/873c31d3e4dd62e0_CLD_Flame_final_report_20220330.pdf>)

### CLD-F02　Dilute methane and ethylene can survive beyond ground dilution limits in the source apparatus

**0d356388b102bc5d_2021 Tinajero & Long Dilution Limits of Coflow Laminar Methane and Ethylene Flames in Microgravity ....pdf**

2021簡報報告微重力下稀釋與穩定範圍擴展；指定乙烯例在燃料／共流匹配的50／40／30 cm/s下，來源端點分別為11／12／10% C2H4。

- 證據身份：source_selected_observations。
- 文獻定位：JET-1f53e7554a76: physical14 dilution-limit summary;physical16 conclusions。
- 使用數據部分：source_id: GA-1f53e7554a76；locator: physical14 dilution-limit summary;physical16 conclusions；role: Sourceanalysisorboundedliteraturecontext;notindependentraw。
- 本組適用層級：context_selected_dilution_panels；Slideselectedmatchedconditions,notallrowlimits.。
- 使用／控制因子：factor_and_role: fuelandcoflow50/40/30cm/s:matchedcontrols；source_refs: source_id: GA-1f53e7554a76；locator: physical14 dilution-limit summary;physical16 conclusions；factor_and_role: sourceethylene11/12/10%:dilutionendpoints；source_refs: source_id: GA-1f53e7554a76；locator: physical14 dilution-limit summary;physical16 conclusions；factor_and_role: CH*/PMT/opticalflameappearance:sourceobservables；source_refs: source_id: GA-1f53e7554a76；locator: physical14 dilution-limit summary;physical16 conclusions。
- 來源限制：Flow ramp history and extinction detection matter. These are selected plotted conditions, not a general safe fuel-concentration range or all rows in the CSV.；The18-page source is a presentation, not a new independent journal cohort.。
- 搜尋句（改寫）：The2021 slide summary reports expanded dilution limits/stability in microgravity; its ethylene example at matched fuel/coflow50/40/30cm/s gives source endpoints of11/12/10% C2H4 respectively.。
- 來源：[開啟檔案](<D:/NASA hackathon/supplement_20261113/01_PSI/PSI-21/Raw Data/0d356388b102bc5d_2021 Tinajero & Long Dilution Limits of Coflow Laminar Methane and Ethylene Flames in Microgravity ....pdf>)
- 本機來源：[開啟檔案](<D:/NASA hackathon/supplement_20261113/01_PSI/PSI-21/Raw Data/0d356388b102bc5d_2021 Tinajero & Long Dilution Limits of Coflow Laminar Methane and Ethylene Flames in Microgravity ....pdf>)

### CLD-F03　Dilution tables are daily summaries and some bottle labels are corrupt

**PSI-21_Experimental table_CLD Flame.csv**

CSV連號CH5…CH14／C2H5…與報告Table1的逐TestDay甲烷／乙烯瓶標不同；側表保留兩種原文並按日期連結，不改原CSV。

- 證據身份：source_quality_and_identity_crosswalk。
- 文獻定位：DATA-21_Experimental table_CLD Flame: TestType/TestDay/FuelBottle columns; GA-5054384d478c: physical23–24,Table1。
- 使用數據部分：source_id: DATA-21_Experimental table_CLD Flame；locator: TestType/TestDay/FuelBottle columns；role: Rawconditions/sourceclassifiedrecords；source_id: GA-5054384d478c；locator: physical23–24,Table1；role: Sourceanalysisorboundedliteraturecontext;notindependentraw。
- 本組適用層級：direct_day_identity_crosswalk；ExactTestDayboundsourceTable1crosswalk.。
- 使用／控制因子：factor_and_role: TestDay:identity；source_refs: source_id: DATA-21_Experimental table_CLD Flame；locator: TestType/TestDay/FuelBottle columns；source_id: GA-5054384d478c；locator: physical23–24,Table1；factor_and_role: FuelBottle:rawcorruptlabel；source_refs: source_id: DATA-21_Experimental table_CLD Flame；locator: TestType/TestDay/FuelBottle columns；source_id: GA-5054384d478c；locator: physical23–24,Table1；factor_and_role: source-reportedfuelidentity:Table1sidecar；source_refs: source_id: DATA-21_Experimental table_CLD Flame；locator: TestType/TestDay/FuelBottle columns；source_id: GA-5054384d478c；locator: physical23–24,Table1；factor_and_role: MFCslpmN2fullscale:controllerdesignationnotactualflow；source_refs: source_id: DATA-21_Experimental table_CLD Flame；locator: TestType/TestDay/FuelBottle columns；source_id: GA-5054384d478c；locator: physical23–24,Table1。
- 來源限制：MFC values identify controller range on an N2 basis, not actual fuel flow.；Minimum listed concentration may not have been reached before extinction. Daily count is not a per-burn condition table.。
- 搜尋句（改寫）：The local CSV has sequentialCH5…CH14/C2H5… labels, while the reportTable1 gives methane/ethylene bottles for the corresponding TestDays. A sidecar preserves both strings and binds the reported species by day; no original is repaired.。
- 來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/01_實驗資料/第一批下載/PSI-21_ACME CLD Flame/Experimental table/PSI-21_Experimental table_CLD Flame.csv>)
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/01_實驗資料/第一批下載/PSI-21_ACME CLD Flame/Experimental table/PSI-21_Experimental table_CLD Flame.csv>)

- 共同來源：**873c31d3e4dd62e0_CLD_Flame_final_report_20220330**；physical23–24,Table1；[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/實驗附帶文件/補下載/PSI-21/Raw Data/873c31d3e4dd62e0_CLD_Flame_final_report_20220330.pdf>)

| Model ID | 公式／預測量 | 展示程式 | 數值比較與限制 |
| --- | --- | --- | --- |
| READINESS-PSI-21 | 原文方程／模型參見MODEL_INVENTORY；本次尚未閉合；ACME CLD (inputs missing) | 未實作 · 尚未取得本機檔案 | 未執行／缺閉合輸入；來源就緒度盤點，不是數值預測；R²（模型全群）=N/A；尚未取得／不適用；No complete audited source-fixed scalar geometry comparison is presently joined.；Exact model/transport/chemistry version and compatible original flame target/case inputs |

| 可開啟的圖／工具 | 身份與用途 |
| --- | --- |
| [開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/gas_combustion_evidence_20261115/models/comparison.html>) | 選正確架構；缺資料的研究僅顯示就緒度，不畫假預測 |

## 2. 使用資料與參數總表的因子對照

| 總表原分類 | 來源身份 | 原欄名單位 | 原欄名例 | 總表定位 |
| --- | --- | --- | --- | --- |
| 光電／離子偵測訊號 | 儀器原始訊號 | 未由欄名確認 | IonCurrent；PMT1；PMT2；PMT3 | '物理參數'!A64:K64 |
| 光電／離子偵測訊號 | 儀器設定／控制參數 | 未由欄名確認 | PMT 1 Gain；PMT 2 Gain；PMT 3 Gain | '物理參數'!A65:K65 |
| 其他氣體組成／濃度 | 條件或分析量 | 未由欄名確認 | Fuel conc. Range；Nitrogen；Hydrogen / Helium (45/55)；Dilution of fuel and inert | '物理參數'!A66:K66 |
| 化學計量混合分率 | 計算／分析參數 | 未由欄名確認 | Stoichiometric Conversion Equation | '物理參數'!A67:K67 |
| 壓力 | 量測或設定 | PSIA | FCU_MP_PT1(PSIA)；FCU_MP_PT2(PSIA)；FCU_MP_PT3(PSIA)；FCU_MP_PT4(PSIA)；FCU_MP_PT5(PSIA)；FCU_MP_PT6(PSIA)；FCU_MP_PT7(PSIA)；FCU_MP_PT8(PSIA)；FCU_MP_PT9(PSIA)；FCU_MP_PT10(PSIA)；其餘見原始欄位 | '物理參數'!A68:K68 |
| 壓力 | 量測或設定 | psia | Pstart (psia)；Pend (psia)；Returns the delta pressure (psia) of the combustion chamber from event start to event end | '物理參數'!A69:K69 |
| 壓力 | 量測或設定 | 未由欄名確認 | Chamber Pressure | '物理參數'!A70:K70 |
| 密度 | 量測或來源分析量 | g/L | Density (g/L) | '物理參數'!A71:K71 |
| 密度 | 量測或來源分析量 | 未由欄名確認 | Density | '物理參數'!A72:K72 |
| 尺寸／幾何 | 儀器設定／控制參數 | 未由欄名確認 | TP_PARAMETER_IGNITER_IGNITION_POSITION_1；TP_PARAMETER_IGNITER_IGNITION_POSITION_2 | '物理參數'!A73:K73 |
| 尺寸／幾何 | 裝置或樣本條件 | N/A（來源未給物理單位） | IPSUG_CAMERA_3_ROI_WIDTH(N/A)；IPSUG_CAMERA_3_WIDTH(N/A)；ACME_COMMANDED_ZOOM_POSITION(N/A)；ACME_COMMANDED_IRIS_POSITION(N/A)；ACME_COMMANDED_FOCUS_POSITION(N/A)；ACME_COMMANDED_FILTER_POSITION(N/A) | '物理參數'!A74:K74 |
| 影像／光譜設定 | 儀器設定或影像座標 | Ins | 5:IPSUG_LV_ACTIVE_CAMERAS(Ins)；5:IPSUG_LV_LEFT_CAMERA(Ins)；5:IPSUG_LV_RIGHT_CAMERA(Ins)；5:IPSUG_CAMERA_1_PIXEL_FORMAT(Ins)；5:IPSUG_CAMERA_1_FRAME_RATE(Ins)；5:IPSUG_CAMERA_1_EXP_MODE(Ins)；5:IPSUG_CAMERA_1_AUTO_EXP(Ins)；5:IPSUG_CAMERA_1_MAN_EXP(Ins)；5:IPSUG_CAMERA_3_FRAME_RATE(Ins)；5:IPSUG_CAMERA_3_EXP_MODE(Ins)；其餘見原始欄位 | '物理參數'!A75:K75 |
| 影像／光譜設定 | 儀器設定或影像座標 | N/A（來源未給物理單位） | IPSUG_CAMERA_3_INFO(N/A)；IPSUG_CAMERA_3_POWERED(N/A)；IPSUG_CAMERA_3_CONNECTED(N/A)；IPSUG_CAMERA_3_RESETS(N/A)；IPSUG_CAMERA_3_LV_STAT(N/A)；IPSUG_CAMERA_3_LV_INTERVAL(N/A)；IPSUG_CAMERA_3_ARCHIVE_STAT(N/A)；IPSUG_CAMERA_3_ARCHIVE_NUM(N/A)；IPSUG_CAMERA_3_ARCHIVE_LOST(N/A)；IPSUG_CAMERA_3_PIXEL_FORMAT(N/A)；其餘見原始欄位 | '物理參數'!A76:K76 |
| 影像／光譜設定 | 儀器設定或影像座標 | 未由欄名確認 | filterNumber；useIntensifiedCamera | '物理參數'!A77:K77 |
| 影像／光譜設定 | 儀器設定／控制參數 | Ins | 5:IPSUG_CAMERA_1_GAIN_MODE(Ins)；5:IPSUG_CAMERA_1_AUTO_GAIN(Ins)；5:IPSUG_CAMERA_1_MAN_GAIN(Ins)；5:IPSUG_CAMERA_3_GAIN_MODE(Ins)；5:IPSUG_CAMERA_3_AUTO_GAIN(Ins)；5:IPSUG_CAMERA_3_MAN_GAIN(Ins) | '物理參數'!A78:K78 |
| 影像／光譜設定 | 儀器設定／控制參數 | N/A（來源未給物理單位） | IPSUG_CAMERA_3_GAIN_MODE(N/A)；IPSUG_CAMERA_3_AUTO_GAIN(N/A)；IPSUG_CAMERA_3_MAN_GAIN(N/A)；IPSUG_CAMERA_1_GAIN_MODE(N/A)；IPSUG_CAMERA_1_AUTO_GAIN(N/A)；IPSUG_CAMERA_1_MAN_GAIN(N/A) | '物理參數'!A79:K79 |
| 氧濃度 | 量測或條件值 | 未由欄名確認 | Oxygen；O2；Ethylene: C2H4 → - 3 O2 + 2 H2O + 2 CO2；Methane: CH4 → - 2 O2 + 2 H2O + CO2；Hydrogen: 2 H2 → - O2 + 2 H2O；PickOxygen；O2 Fill | '物理參數'!A80:K80 |
| 流速／通風 | 量測或設定 | 未由欄名確認 | Ramp to final velocity | '物理參數'!A81:K81 |
| 溫度 | 量測或設定 | C | 2018-01-03 003 22:16:19:624~acme~Copyright (C) 2002-13；2018-01-03 003 21:02:30:791~acme~Copyright (C) 2002-13；2018-01-03 003 21:44:33:670~acme~Copyright (C) 2002-13；2018-09-07 250 12:45:57:763~acme~Copyright (C) 2002-13；2018-01-03 003 13:05:26:624~acme~Copyright (C) 2002-13；2018-01-03 003 18:02:32:748~acme~Copyright (C) 2002-13；2018-01-03 003 20:02:26:007~acme~Copyright (C) 2002-13；2007-01-01 001 00:00:41:122~acme~Copyright (C) 2002-13；2007-01-01 001 00:00:26:102~acme~Copyright (C) 2002-13；2018-01-03 003 22:34:03:579~acme~Copyright (C) 2002-13；其餘見原始欄位 | '物理參數'!A82:K82 |
| 溫度 | 量測或設定 | Deg C | IPSUG_CAMERA_3_TEMP(Deg C)；FCU_MP_TM1(Deg C)；FCU_MP_TM2(Deg C)；FCU_MP_TM3(Deg C)；FCU_MP_TM4(Deg C) | '物理參數'!A83:K83 |
| 溫度 | 量測或設定 | Ins | FCU_MP_TM1(Ins)；FCU_MP_TM2(Ins)；FCU_MP_TM3(Ins)；FCU_MP_TM4(Ins) | '物理參數'!A84:K84 |
| 溫度 | 量測或設定 | Standard Liters - 0 DegC, 760 Torr | ACME MFCs (Standard Liters - 0 DegC, 760 Torr) | '物理參數'!A85:K85 |
| 溫度 | 量測或設定 | Standard Liters - 0 DegC, 760 torr | Start Mixture (Standard Liters - 0 DegC, 760 torr)；Event Delta (Standard Liters - 0 DegC, 760 torr)；Finish Mixture (Standard Liters - 0 DegC, 760 torr)；Recirculation Loop Contents (Standard Liters - 0 DegC, 760 torr) | '物理參數'!A86:K86 |
| 溫度 | 量測或設定 | 未由欄名確認 | Thermocouple；TC200A；TC200B；Chamber Temperature；FCU_MP_TM1；FCU_MP_TM2；FCU_MP_TM3；FCU_MP_TM4 | '物理參數'!A87:K87 |
| 熱通量／輻射 | 量測通道或來源分析量 | 未由欄名確認 | Radiometer；Radiometer+60；Radiometer+60CJ；Radiometer+30；Radiometer+30CJ；RadiometerCenter；RadiometerCenterCJ；Radiometer-30；Radiometer-30CJ；Radiometer-60；其餘見原始欄位 | '物理參數'!A88:K88 |
| 燃燒／點火／老化時間 | 時序或處理條件 | 未由欄名確認 | aveDuration | '物理參數'!A89:K89 |
| 硬體電壓／電流／功率 | 儀器設定／控制參數 | 未由欄名確認 | again and failed. Manually powered off PI Bus B | '物理參數'!A90:K90 |
| 硬體電壓／電流／功率 | 原始訊號或狀態 | Volts | IPSUG_SYSTEM_5V_POS(Volts)；IPSUG_SYSTEM_12V_POS(Volts) | '物理參數'!A91:K91 |
| 電場電壓／電流 | 儀器設定／控制參數 | 未由欄名確認 | EfieldSetpointOut | '物理參數'!A92:K92 |
| 電場電壓／電流 | 量測或設定 | 未由欄名確認 | EField；EFieldPol；EfieldVoltage | '物理參數'!A93:K93 |
| 體積流量／MFC | 儀器設定／控制參數 | V | MFCA1Setpoint(V)；MFCA2Setpoint(V)；MFCA3Setpoint(V) | '物理參數'!A94:K94 |
| 體積流量／MFC | 儀器設定／控制參數 | 未由欄名確認 | MFCA1 Full Scale；MFCA2 Full Scale；MFCA3 Full Scale | '物理參數'!A95:K95 |
| 體積流量／MFC | 量測或設定 | 未由欄名確認 | Fuel MFC；N2 MFC；MFCA1 Gas；MFCA2 Gas；MFCA3 Gas；MFCA1StaticMixerFlow；MFCA2BypassFlow；MFCA3FuelFlow；MFCDiluent；MFCFuel；其餘見原始欄位 | '物理參數'!A96:K96 |
| 點火功率／電壓／電流 | 儀器設定／控制參數 | 未由欄名確認 | TP_PARAMETER_IGNITER_WATTAGE；TP_PARAMETER_IGNITER_ON_TIME | '物理參數'!A97:K97 |
| 點火功率／電壓／電流 | 量測或設定 | ms | Igniter On Time (ms) | '物理參數'!A98:K98 |
| 點火功率／電壓／電流 | 量測或設定 | 未由欄名確認 | Igniter Wattage | '物理參數'!A99:K99 |

以上是該 investigation 的欄位盤點；個別結論實際使用的因子以第1節與下列補充為準。

| 本組實際因子 | 總表定位／未列欄位 | 文獻中的用途 |
| --- | --- | --- |
| CLD-F01 / fuelandcoflowexitvelocities40cm/s:coldflowmatchedcontrols | '物理參數'!G81 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| CLD-F01 / ethylene40/60/80/100%:composition | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| CLD-F01 / 1g/ISS:environment | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| CLD-F01 / soottemperature(K):pyrometryoutput | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| CLD-F01 / sootvolumefraction:opticalinverseoutput | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| CLD-F02 / fuelandcoflow50/40/30cm/s:matchedcontrols | '物理參數'!G81 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| CLD-F02 / sourceethylene11/12/10%:dilutionendpoints | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| CLD-F02 / CH*/PMT/opticalflameappearance:sourceobservables | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| CLD-F03 / TestDay:identity | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| CLD-F03 / FuelBottle:rawcorruptlabel | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| CLD-F03 / source-reportedfuelidentity:Table1sidecar | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| CLD-F03 / MFCslpmN2fullscale:controllerdesignationnotactualflow | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |

尚未取得可逐項對照的紀錄。

## 3. 共用資料的多項結論比較

| 結論／文獻 | 資料重疊身份 | 共同處 | 不同處／不能合併之處 |
| --- | --- | --- | --- |
| GA-5054384d478c；GA-1f53e7554a76 | report_slides_shared_test_family_with_hardware_variants | Matchedgravitydilution/sootcomparisonsandimprovedcoflowarepartofsameproject. | Original/improvedcoflowandphotometryreductionsmuststayseparate;slidesarenotnewreplications. |

## 4. 消防洞見

| 類別 | 對應證據 | 數據支持的判斷 | 策略／產品構想 | 待驗證 |
| --- | --- | --- | --- | --- |
| 預防 | 尚未取得／不適用 | 尚未建立本組可直接支持此消防用途的完整量測鏈。 | 先補本組對應的物理端點與資料配對，再設計策略測試。 | 相關系列與方法限制只能提供研究脈絡，不能代替本組產品或操作效能驗證。 |
| 偵測 | 尚未取得／不適用 | 尚未建立本組可直接支持此消防用途的完整量測鏈。 | 先補本組對應的物理端點與資料配對，再設計策略測試。 | 相關系列與方法限制只能提供研究脈絡，不能代替本組產品或操作效能驗證。 |
| 撲滅／抑制 | 尚未取得／不適用 | 尚未建立本組可直接支持此消防用途的完整量測鏈。 | 先補本組對應的物理端點與資料配對，再設計策略測試。 | 相關系列與方法限制只能提供研究脈絡，不能代替本組產品或操作效能驗證。 |

## 逐次索引

| 原始檔／資料位置 | Trial／Run／列 | 共享身份與保留事項 |
| --- | --- | --- |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-21_ACME CLD Flame\Experimental table\PSI-21_Experimental table_CLD Flame.csv | trial_id: 21050；csv_row_including_header: 32；record_kind: operation_day_summary_not_individual_trial；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name；reported_identity_sidecar: raw_bottle: 40% CH4；reported_fuel_species: CH4；source_id: GA-5054384d478c；locator: physical23–24,Table1,TestDay21050；canonical_role: source_reported_species_sidecar_not_repaired_original；exact_delivered_fraction: Use per-run MFC/gas correction; listed range is not an achieved per-burn input | raw_parameters_as_stored: Test Type: Improved coflow tests；Test Day: 21050；Fuel MFC: 0.2；N2 MFC: 0.2；Fuel Bottle: 40% CH4；Fuel conc. Range: 20%-40%；Flames ignited: 16；Notes: 尚未取得／不適用；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-21_ACME CLD Flame\Experimental table\PSI-21_Experimental table_CLD Flame.csv | trial_id: 21062；csv_row_including_header: 33；record_kind: operation_day_summary_not_individual_trial；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name；reported_identity_sidecar: raw_bottle: 40% CH5；reported_fuel_species: CH4；source_id: GA-5054384d478c；locator: physical23–24,Table1,TestDay21062；canonical_role: source_reported_species_sidecar_not_repaired_original；exact_delivered_fraction: Use per-run MFC/gas correction; listed range is not an achieved per-burn input | raw_parameters_as_stored: Test Type: Improved coflow tests；Test Day: 21062；Fuel MFC: 0.2；N2 MFC: 0.2；Fuel Bottle: 40% CH5；Fuel conc. Range: 30%-40%；Flames ignited: 11；Notes: 尚未取得／不適用；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |

## 缺件與適用範圍

- Controller fullscale in slpm/N2basis is not actual stream velocity or massflow.
