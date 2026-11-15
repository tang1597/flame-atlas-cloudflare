# E-FIELD 100% CH4 coflow negative

小資料集 ID：`EF-100_CH4-coflow-negative`

## 資料身份與範圍

| 項目 | 內容 |
| --- | --- |
| 原始 NASA PSI investigation | [PSI-22](https://psi.nasa.gov/physci/repo/data/investigations/PSI-22) |
| 相關PSI索引（不是原始資料） | 尚未取得／不適用 |
| 材料／配方 | stock_bottle: 100% CH4；delivered_fraction: sourceFuelConc plus runMFC dilution, not bottlealone |
| 幾何 | shape: coflow burner and electrode mesh；source_case_gap_cm: 尚未確認；gap_guard: 3.5cm onlyNovember2019pureCH4gascases; other3.7/5cmreferencesnotpooled |
| 實驗模式 | gravity: ISS microgravity；field_mesh_polarity: negative |
| 證據角色 | gaseous_flame_experiment |
| 環境 | gravity: 尚未確認；mode: gravity: ISS microgravity；field_mesh_polarity: negative |
| 資料粒度／共享試片 | Per-row source values retained; summary/day/variant rows are not promoted to independent burns. |
| 可用數值 | source_conditions_available_target_join_and_complete_chemistry_transport_closure_not_established |

## 1. 文獻結果與視覺化程式

### EF-F01　Electric forcing changes I–V response and flame appearance in named ISS cases

**PSI-22_Presentations_Chien et al 2019 Microgravity Experiments Examining Electric Field Effects**

2019年11月來源明列純甲烷ISS試次18282B1／18282D1／18312B1／18312D1，比較19／24 cm/s下電場極性與火焰影像。

- 證據身份：source_case_bound_measurement_display。
- 文獻定位：GA-cf8e18a80996: physical13 case table;physical15–21 current/photo panels。
- 使用數據部分：source_id: GA-cf8e18a80996；locator: physical13 case table;physical15–21 current/photo panels；role: Sourceanalysisorboundedliteraturecontext;notindependentraw。
- 本組適用層級：context_other_case_or_composition；Onlyfourp13pureCH4gasjetcasesdirectlybind.。
- 使用／控制因子：factor_and_role: 19/24cm/s:fuelexitvelocity；source_refs: source_id: GA-cf8e18a80996；locator: physical13 case table;physical15–21 current/photo panels；factor_and_role: CH4=100%:sourcecases；source_refs: source_id: GA-cf8e18a80996；locator: physical13 case table;physical15–21 current/photo panels；factor_and_role: meshgap3.5cm:geometry；source_refs: source_id: GA-cf8e18a80996；locator: physical13 case table;physical15–21 current/photo panels；factor_and_role: fieldpolarity/voltagestaircase:input；source_refs: source_id: GA-cf8e18a80996；locator: physical13 case table;physical15–21 current/photo panels；factor_and_role: currentµAandflamephotos:outputs；source_refs: source_id: GA-cf8e18a80996；locator: physical13 case table;physical15–21 current/photo panels。
- 來源限制：The19cm/s cases are ISS, not an unidentified ground comparator.；A nominalE=V/H descriptor does not close ion wind, local oxygen transport, flame shape or equivalent gravity.。
- 搜尋句（改寫）：The November2019 source identifies pure-methane gas-jet ISS cases18282B1/18282D1/18312B1/18312D1 and compares field polarity and flame images at19/24cm/s.。
- 來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/簡報與海報/第一批下載/PSI-22_ACME E-FIELD Flames/Presentations/PSI-22_Presentations_Chien et al 2019 Microgravity Experiments Examining Electric Field Effects.pdf>)
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/簡報與海報/第一批下載/PSI-22_ACME E-FIELD Flames/Presentations/PSI-22_Presentations_Chien et al 2019 Microgravity Experiments Examining Electric Field Effects.pdf>)

### EF-F02　Different burner configurations and sign conventions prevent blind curve pooling

**PSI-22_Presentations_Tinajero et al 2016 characterizing i-v curves for non-premixed methane flames**

地面甲烷有不同網格間距與電極配置，2011落塔又採正網格E=V/d慣例。選定電場下外形或焰底相近，不能證明完整輸運或重力等價。

- 證據身份：related_ground_drop_measurement_and_author_inference。
- 文獻定位：GA-71132d684969: physical4–6,8–9,13–15; GA-3f8c275b6c39: physical2–6,Figs3–7。
- 使用數據部分：source_id: GA-71132d684969；locator: physical4–6,8–9,13–15；role: Sourceanalysisorboundedliteraturecontext;notindependentraw；source_id: GA-3f8c275b6c39；locator: physical2–6,Figs3–7；role: Sourceanalysisorboundedliteraturecontext;notindependentraw。
- 本組適用層級：related_ground_drop_context；Groundmesh/signconventionsandgravityregimesremainseparate.。
- 使用／控制因子：factor_and_role: ground/dropgravity:environment；source_refs: source_id: GA-71132d684969；locator: physical4–6,8–9,13–15；source_id: GA-3f8c275b6c39；locator: physical2–6,Figs3–7；factor_and_role: meshgapandburnerID/OD:geometry；source_refs: source_id: GA-71132d684969；locator: physical4–6,8–9,13–15；source_id: GA-3f8c275b6c39；locator: physical2–6,Figs3–7；factor_and_role: nominalE=V/dor−ΔV/H:sourceconvention；source_refs: source_id: GA-71132d684969；locator: physical4–6,8–9,13–15；source_id: GA-3f8c275b6c39；locator: physical2–6,Figs3–7；factor_and_role: I-Vandcylindricalarea/base:measured/image-reducedoutputs；source_refs: source_id: GA-71132d684969；locator: physical4–6,8–9,13–15；source_id: GA-3f8c275b6c39；locator: physical2–6,Figs3–7。
- 來源限制：Ground/drop studies are not independent ISS repeats; current standard deviations are not replicate confidence intervals.；Electric field is not measured lunar/Martian gravity. Never relabel a field setting as actual partialg.。
- 搜尋句（改寫）：Ground methane data use different mesh gaps/configurations, and the2011 drop source has a positive-meshE=V/d convention. Similar area/base location at a selected field does not establish complete transport or gravity equivalence.。
- 來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/簡報與海報/第一批下載/PSI-22_ACME E-FIELD Flames/Presentations/PSI-22_Presentations_Tinajero et al 2016 characterizing i-v curves for non-premixed methane flames.pdf>)
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/簡報與海報/第一批下載/PSI-22_ACME E-FIELD Flames/Presentations/PSI-22_Presentations_Tinajero et al 2016 characterizing i-v curves for non-premixed methane flames.pdf>)

- 共同來源：**PSI-22_Presentations_Swenson et al 2011 Electric field induced convection in microgravity combustion**；physical2–6,Figs3–7；[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/簡報與海報/第一批下載/PSI-22_ACME E-FIELD Flames/Presentations/PSI-22_Presentations_Swenson et al 2011 Electric field induced convection in microgravity combustion.pdf>)

### EF-F03　Daily table duplicates and continuation rows are not new tests

**PSI-22_Experimental table_ACME E-FIELD Flames.csv**

E-FIELD表含21個TestDay列、18319重複日摘要及11列無身份續列。續列濃度保留，但不向前填成某次燃燒。

- 證據身份：source_data_structure。
- 文獻定位：DATA-22_Experimental table_ACME E-FIELD Flames: physicalCSVrows2–33。
- 使用數據部分：source_id: DATA-22_Experimental table_ACME E-FIELD Flames；locator: physicalCSVrows2–33；role: Rawconditions/sourceclassifiedrecords。
- 本組適用層級：direct_data_structure；Dayduplicates/continuationsretained.。
- 使用／控制因子：factor_and_role: TestDay:dayidentity；source_refs: source_id: DATA-22_Experimental table_ACME E-FIELD Flames；locator: physicalCSVrows2–33；factor_and_role: FuelConc:day/continuationmetadata；source_refs: source_id: DATA-22_Experimental table_ACME E-FIELD Flames；locator: physicalCSVrows2–33；factor_and_role: FlamesIgnited:sourceaggregatenotindependentrow；source_refs: source_id: DATA-22_Experimental table_ACME E-FIELD Flames；locator: physicalCSVrows2–33；factor_and_role: duplicate18319:identityconstraint；source_refs: source_id: DATA-22_Experimental table_ACME E-FIELD Flames；locator: physicalCSVrows2–33。
- 來源限制：Do not sum duplicated day counts or label32rows as32independent fires.；A bottle recipe is not necessarily the delivered diluted mixture.。
- 搜尋句（改寫）：The E-FIELD table has21rows with TestDay, duplicate18319 day-summary entries and11blank-identity continuation rows. A fuel concentration on a continuation row is retained but is not assigned a burn ID by forward fill.。
- 來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/01_實驗資料/第一批下載/PSI-22_ACME E-FIELD Flames/Experimental table/PSI-22_Experimental table_ACME E-FIELD Flames.csv>)
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/01_實驗資料/第一批下載/PSI-22_ACME E-FIELD Flames/Experimental table/PSI-22_Experimental table_ACME E-FIELD Flames.csv>)

| Model ID | 公式／預測量 | 展示程式 | 數值比較與限制 |
| --- | --- | --- | --- |
| READINESS-PSI-22 | 原文方程／模型參見MODEL_INVENTORY；本次尚未閉合；E-FIELD Flames (inputs missing) | 未實作 · 尚未取得本機檔案 | 未執行／缺閉合輸入；來源就緒度盤點，不是數值預測；R²（模型全群）=N/A；尚未取得／不適用；Nominal E-field descriptors and observations do not constitute a closed flame-shape or suppression predictor.；Local field/charge/flow/chemical and thermal closure with paired measured flame response |

| 可開啟的圖／工具 | 身份與用途 |
| --- | --- |
| [開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/gas_combustion_evidence_20261115/models/comparison.html>) | 選正確架構；缺資料的研究僅顯示就緒度，不畫假預測 |

## 2. 使用資料與參數總表的因子對照

| 總表原分類 | 來源身份 | 原欄名單位 | 原欄名例 | 總表定位 |
| --- | --- | --- | --- | --- |
| 光電／離子偵測訊號 | 儀器原始訊號 | 未由欄名確認 | IonCurrent；PMT1；PMT2；PMT3 | '物理參數'!A100:K100 |
| 光電／離子偵測訊號 | 儀器設定／控制參數 | 未由欄名確認 | PMT 1 Gain；PMT 2 Gain；PMT 3 Gain | '物理參數'!A101:K101 |
| 其他氣體組成／濃度 | 條件或分析量 | 未由欄名確認 | Fuel Conc；Dilution Gas Correction Factor；Dilution of fuel and inert | '物理參數'!A102:K102 |
| 壓力 | 量測或設定 | PSIA | FCU_MP_PT1(PSIA)；FCU_MP_PT2(PSIA)；FCU_MP_PT3(PSIA)；FCU_MP_PT4(PSIA)；FCU_MP_PT5(PSIA)；FCU_MP_PT6(PSIA)；FCU_MP_PT7(PSIA)；FCU_MP_PT8(PSIA)；FCU_MP_PT9(PSIA)；FCU_MP_PT10(PSIA)；其餘見原始欄位 | '物理參數'!A103:K103 |
| 壓力 | 量測或設定 | psia | PTA1 (psia)；PTA2 (psia)；PTA3 (psia) | '物理參數'!A104:K104 |
| 尺寸／幾何 | 裝置或樣本條件 | 未由欄名確認 | 10 mm position；Width；RegionWidth；ImageWidth | '物理參數'!A105:K105 |
| 影像／光譜設定 | 儀器設定或影像座標 | N/A（來源未給物理單位） | IPSUG_LV_ACTIVE_CAMERAS(N/A)；IPSUG_LV_LEFT_CAMERA(N/A)；IPSUG_LV_RIGHT_CAMERA(N/A)；IPSUG_CAMERA_1_PIXEL_FORMAT(N/A)；IPSUG_CAMERA_1_FRAME_RATE(N/A)；IPSUG_CAMERA_1_EXP_MODE(N/A)；IPSUG_CAMERA_1_AUTO_EXP(N/A)；IPSUG_CAMERA_1_MAN_EXP(N/A)；IPSUG_CAMERA_3_FRAME_RATE(N/A)；IPSUG_CAMERA_3_EXP_MODE(N/A)；其餘見原始欄位 | '物理參數'!A106:K106 |
| 影像／光譜設定 | 儀器設定或影像座標 | 未由欄名確認 | filterNumber；2018-04-23 113 14:20:06:142~ipsug.Halcon~CameraB2020::CameraB2020(int；QObject*) "CIR_5_CAMERA_4/configFile" i32MaxExposure = 61052；2009-01-01 001 00:00:48:415~ipsug.Halcon~CameraB2020::CameraB2020(int；2018-04-23 113 14:07:57:287~ipsug.Halcon~CameraB2020::CameraB2020(int；2018-04-23 113 13:27:33:425~ipsug.Halcon~"CIR_5_CAMERA_3" Registry QMap(("adaptor；gige-00")("color；2018-04-23 113 13:27:33:439~ipsug.Halcon~"CIR_5_CAMERA_4" Registry QMap(("ExposureManualMax；gige-01")("color；2018-04-23 113 13:27:33:439~ipsug.Halcon~CameraB2020::CameraB2020(QString；其餘見原始欄位 | '物理參數'!A107:K107 |
| 影像／光譜設定 | 儀器設定／控制參數 | N/A（來源未給物理單位） | IPSUG_CAMERA_1_GAIN_MODE(N/A)；IPSUG_CAMERA_1_AUTO_GAIN(N/A)；IPSUG_CAMERA_1_MAN_GAIN(N/A)；IPSUG_CAMERA_3_GAIN_MODE(N/A)；IPSUG_CAMERA_3_AUTO_GAIN(N/A)；IPSUG_CAMERA_3_MAN_GAIN(N/A) | '物理參數'!A108:K108 |
| 氧濃度 | 量測或條件值 | 未由欄名確認 | Oxygen/Nitrogen (21/79) | '物理參數'!A109:K109 |
| 流速／通風 | 量測或設定 | cm/s | Coflow Velocity (cm/s)；Inert Velocity (cm/s)；Fuel Velocity (cm/s)；Fuel + Inert Velocity (cm/s) | '物理參數'!A110:K110 |
| 流速／通風 | 量測或設定 | m2 | velocity-based Burner Areas (m2) | '物理參數'!A111:K111 |
| 流速／通風 | 量測或設定 | 未由欄名確認 | Convert From SLPM (N2) to velocity；Velocity cm/s；Convert from velocity to SLPM (N2)；velocity-based Experiments；Ramp to final velocity | '物理參數'!A112:K112 |
| 溫度 | 量測或設定 | C | Temperature [C]；2018-03-29 088 14:19:48:715~acme~Copyright (C) 2002-13；2018-04-23 113 12:57:59:623~acme~Copyright (C) 2002-13；2018-05-17 137 16:07:31:935~acme~Copyright (C) 2002-13；2018-04-02 092 17:27:56:761~acme~Copyright (C) 2002-13；2018-05-17 137 11:43:26:624~acme~Copyright (C) 2002-13；2018-04-02 092 12:12:30:493~acme~Copyright (C) 2002-13；2018-03-21 080 12:44:43:630~acme~Copyright (C) 2002-13；2018-10-12 285 11:48:54:622~acme~Copyright (C) 2002-13；2018-10-29 302 13:40:02:247~acme~Copyright (C) 2002-13；其餘見原始欄位 | '物理參數'!A113:K113 |
| 溫度 | 量測或設定 | Deg C | FCU_MP_TM1(Deg C)；FCU_MP_TM2(Deg C)；FCU_MP_TM3(Deg C)；FCU_MP_TM4(Deg C) | '物理參數'!A114:K114 |
| 溫度 | 量測或設定 | 未由欄名確認 | Thermocouple；TC200A；TC200B；Temperature C；Temperature Factor | '物理參數'!A115:K115 |
| 熱通量／輻射 | 量測通道或來源分析量 | 未由欄名確認 | Radiometer；Radiometer+60；Radiometer+60CJ；Radiometer+30；Radiometer+30CJ；RadiometerCenter；RadiometerCenterCJ；Radiometer-30；Radiometer-30CJ；Radiometer-60；其餘見原始欄位 | '物理參數'!A116:K116 |
| 硬體電壓／電流／功率 | 儀器設定／控制參數 | 未由欄名確認 | CurrentAutoGain | '物理參數'!A117:K117 |
| 硬體電壓／電流／功率 | 原始訊號或狀態 | Volts | IPSUG_SYSTEM_5V_POS(Volts)；IPSUG_SYSTEM_12V_POS(Volts) | '物理參數'!A118:K118 |
| 電場電壓／電流 | 儀器設定／控制參數 | 未由欄名確認 | EfieldSetpointOut | '物理參數'!A119:K119 |
| 電場電壓／電流 | 量測或設定 | 未由欄名確認 | Mesh Polarity；EField；EFieldPol；EfieldVoltage | '物理參數'!A120:K120 |
| 體積流量／MFC | 儀器設定／控制參數 | V | MFCA1Setpoint(V)；MFCA2Setpoint(V)；MFCA3Setpoint(V) | '物理參數'!A121:K121 |
| 體積流量／MFC | 儀器設定／控制參數 | 未由欄名確認 | MFCA1 Full Scale；MFCA2 Full Scale；MFCA3 Full Scale | '物理參數'!A122:K122 |
| 體積流量／MFC | 量測或設定 | SLPM | MFCA1 (SLPM)；MFCA2 (SLPM)；MFCA3 (SLPM) | '物理參數'!A123:K123 |
| 體積流量／MFC | 量測或設定 | 未由欄名確認 | MFCA1 Gas；MFCA2 Gas；MFCA3 Gas；Coflow/MFCA1；Coflow/MFCA1 Gas T ype；MFCA1StaticMixerFlow；MFCA2BypassFlow；MFCA3FuelFlow；MFCA1 Gas Type；MFCA1 Range；其餘見原始欄位 | '物理參數'!A124:K124 |

以上是該 investigation 的欄位盤點；個別結論實際使用的因子以第1節與下列補充為準。

| 本組實際因子 | 總表定位／未列欄位 | 文獻中的用途 |
| --- | --- | --- |
| EF-F01 / 19/24cm/s:fuelexitvelocity | '物理參數'!G110；'物理參數'!G111；'物理參數'!G112 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| EF-F01 / CH4=100%:sourcecases | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| EF-F01 / meshgap3.5cm:geometry | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| EF-F01 / fieldpolarity/voltagestaircase:input | '物理參數'!G119；'物理參數'!G120 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| EF-F01 / currentµAandflamephotos:outputs | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| EF-F02 / ground/dropgravity:environment | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| EF-F02 / meshgapandburnerID/OD:geometry | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| EF-F02 / nominalE=V/dor−ΔV/H:sourceconvention | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| EF-F02 / I-Vandcylindricalarea/base:measured/image-reducedoutputs | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| EF-F03 / TestDay:dayidentity | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| EF-F03 / FuelConc:day/continuationmetadata | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| EF-F03 / FlamesIgnited:sourceaggregatenotindependentrow | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| EF-F03 / duplicate18319:identityconstraint | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |

尚未取得可逐項對照的紀錄。

## 3. 共用資料的多項結論比較

| 結論／文獻 | 資料重疊身份 | 共同處 | 不同處／不能合併之處 |
| --- | --- | --- | --- |
| GA-3f8c275b6c39；GA-71132d684969；GA-6a720d52378b；GA-cf8e18a80996 | different_ground_drop_and_ISS_source_editions | Fieldpolarity/configurationaffectcurrentandappearance. | Flow/gap/sign/mixtureandgravitydifferencespreventblindcurvepooling;notpartialgdata. |

## 4. 消防洞見

| 類別 | 對應證據 | 數據支持的判斷 | 策略／產品構想 | 待驗證 |
| --- | --- | --- | --- | --- |
| 預防／抑制研究 | EF-F01；EF-F02 | 來源比較電場、極性與火焰影像；部分相似外形不證明完整部分重力或輸運等價。 | 以電場作可控輸運研究旋鈕，測同火源的熱／soot／穩定性變化，再評估消防用途。 | 完整反應與流場、設備限制及重複介入；既有影像比較不構成已驗證消防硬體。 |
| 預防 | 尚未取得／不適用 | 尚未建立本組可直接支持此消防用途的完整量測鏈。 | 先補本組對應的物理端點與資料配對，再設計策略測試。 | 相關系列與方法限制只能提供研究脈絡，不能代替本組產品或操作效能驗證。 |
| 偵測 | 尚未取得／不適用 | 尚未建立本組可直接支持此消防用途的完整量測鏈。 | 先補本組對應的物理端點與資料配對，再設計策略測試。 | 相關系列與方法限制只能提供研究脈絡，不能代替本組產品或操作效能驗證。 |
| 撲滅／抑制 | 尚未取得／不適用 | 尚未建立本組可直接支持此消防用途的完整量測鏈。 | 先補本組對應的物理端點與資料配對，再設計策略測試。 | 相關系列與方法限制只能提供研究脈絡，不能代替本組產品或操作效能驗證。 |

## 逐次索引

| 原始檔／資料位置 | Trial／Run／列 | 共享身份與保留事項 |
| --- | --- | --- |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-22_ACME E-FIELD Flames\Experimental table\PSI-22_Experimental table_ACME E-FIELD Flames.csv | trial_id: 18073；csv_row_including_header: 2；record_kind: operation_day_summary_not_individual_trial；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Test Type: First round of tests with coflow burner；Test Day: 18073；Year: 2018；Month: 3；Date: 14；Mesh Polarity: negative；Fuel Bottle: 100% CH4；Fuel Conc: 100%；Flames Ignited: 10；Notes: Test day is formatted YYDDD where YY identifies year and DDD identifies day of year (GMT). ；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-22_ACME E-FIELD Flames\Experimental table\PSI-22_Experimental table_ACME E-FIELD Flames.csv | trial_id: 18078；csv_row_including_header: 3；record_kind: operation_day_summary_not_individual_trial；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Test Type: First round of tests with coflow burner；Test Day: 18078；Year: 2018；Month: 3；Date: 19；Mesh Polarity: negative；Fuel Bottle: 100% CH4；Fuel Conc: 70%；Flames Ignited: 10；Notes: Mesh polarity refers to the polarity of the high-voltage power supply and the copper electrode relative to the burner. ；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |

## 缺件與適用範圍

- No numerical mapping from electricfield to actualpartialgravity.
- No complete ionic-current/charged-species/radiationclosure from condition summaries.
