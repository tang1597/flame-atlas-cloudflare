# CFI-G Normal propane

小資料集 ID：`CFIG-NORMAL-propane`

## 資料身份與範圍

| 項目 | 內容 |
| --- | --- |
| 原始 NASA PSI investigation | [PSI-159](https://psi.nasa.gov/physci/repo/data/investigations/PSI-159) |
| 相關PSI索引（不是原始資料） | 尚未取得／不適用 |
| 材料／配方 | source_fuel_label: propane；fuel_role: burnerstream；diluent: N2；inverse_source_fraction_fields: Xf before/after belongtoambientfuel;XO2belongstoburner |
| 幾何 | shape: porous spherical burner；nominal_diameter_mm: 6.35；source_scope: CFIGsourcehardware;notdropletdiameter；source_ref: source_id: GA-f6cce7cc08ca；locator: physical8 actualburnerslimitedto6.35mm;physical14/17size reference |
| 實驗模式 | gravity: ISS microgravity；configuration: normal；cool_flame: state/outcometag,notassumedforallrows |
| 證據角色 | gaseous_flame_experiment |
| 環境 | gravity: 尚未確認；mode: gravity: ISS microgravity；configuration: normal；cool_flame: state/outcometag,notassumedforallrows |
| 資料粒度／共享試片 | Per-row source values retained; summary/day/variant rows are not promoted to independent burns. |
| 可用數值 | source_conditions_available_target_join_and_complete_chemistry_transport_closure_not_established |

## 1. 文獻結果與視覺化程式

### CG-F01　Source flags identify a specific normal n-butane cool-flame series

**PSI-159_Experimental table_CFI-G_Normal Flames.csv**

normal表7列有yes、PCI-A…G冷焰旗標，都在30% butane組；論文／報告的n-butane案例為2 bar、環境XO2約0.39，不能延伸到所有燃料、inverse或壓力。

- 證據身份：source_classified_records_and_published_observation。
- 文獻定位：DATA-159_Experimental table_CFI-G_Normal Flames: rows160–163,165,169–170; GA-f6cce7cc08ca: physical23 first abstract; PUB-CFIG-KIM2023: primary publisher abstract。
- 使用數據部分：source_id: DATA-159_Experimental table_CFI-G_Normal Flames；locator: rows160–163,165,169–170；role: Rawconditions/sourceclassifiedrecords；source_id: GA-f6cce7cc08ca；locator: physical23 first abstract；role: Sourceanalysisorboundedliteraturecontext;notindependentraw；source_id: PUB-CFIG-KIM2023；locator: primary publisher abstract；role: Sourceanalysisorboundedliteraturecontext;notindependentraw。
- 本組適用層級：context_other_normalbutaneseries；Onlysevenflaggedrowsin30%butanenormal;repeattransitionsnotnewindependentburns.。
- 使用／控制因子：factor_and_role: 30%butanenormal:sourcefuelseries；source_refs: source_id: DATA-159_Experimental table_CFI-G_Normal Flames；locator: rows160–163,165,169–170；source_id: GA-f6cce7cc08ca；locator: physical23 first abstract；source_id: PUB-CFIG-KIM2023；locator: primary publisher abstract；factor_and_role: 2bar/ambientXO2≈.39:publishedcoolflameconditions；source_refs: source_id: DATA-159_Experimental table_CFI-G_Normal Flames；locator: rows160–163,165,169–170；source_id: GA-f6cce7cc08ca；locator: physical23 first abstract；source_id: PUB-CFIG-KIM2023；locator: primary publisher abstract；factor_and_role: coolflagPCI-A…G:sourceoutcome；source_refs: source_id: DATA-159_Experimental table_CFI-G_Normal Flames；locator: rows160–163,165,169–170；source_id: GA-f6cce7cc08ca；locator: physical23 first abstract；source_id: PUB-CFIG-KIM2023；locator: primary publisher abstract；factor_and_role: 21291C1multipletransitions:stagecount；source_refs: source_id: DATA-159_Experimental table_CFI-G_Normal Flames；locator: rows160–163,165,169–170；source_id: GA-f6cce7cc08ca；locator: physical23 first abstract；source_id: PUB-CFIG-KIM2023；locator: primary publisher abstract；factor_and_role: burntime:recorddurationnotcoolduration；source_refs: source_id: DATA-159_Experimental table_CFI-G_Normal Flames；locator: rows160–163,165,169–170；source_id: GA-f6cce7cc08ca；locator: physical23 first abstract；source_id: PUB-CFIG-KIM2023；locator: primary publisher abstract。
- 來源限制：Seven flagged rows are not seven independent cool-flame events:21291C1 reportsfivehot-to-cool transitions.；Burn time is the source record duration, not separately measured cold-flame duration.。
- 搜尋句（改寫）：Seven normal-table records carryyes,PCI-A…G cool-flame flags, all under30%butane. The report/paper describes normal n-butane at2bar and ambientXO2≈.39; this is not proof of cool flames for every ethane,propane,inverse or pressure condition.。
- 來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/01_實驗資料/第一批下載/PSI-159_ACME CFI-G/Experimental table/PSI-159_Experimental table_CFI-G_Normal Flames.csv>)
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/01_實驗資料/第一批下載/PSI-159_ACME CFI-G/Experimental table/PSI-159_Experimental table_CFI-G_Normal Flames.csv>)

- 共同來源：**PSI-159_Reports_FinalRpt_ACME.CFI-G**；physical23 first abstract；[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/研究報告與書章/第一批下載/PSI-159_ACME CFI-G/Reports/PSI-159_Reports_FinalRpt_ACME.CFI-G.pdf>)

- 共同來源：**Spherical gas-fueled cool diffusion flames**；primary publisher abstract；[來源](<https://doi.org/10.1016/j.proci.2022.07.015>)

### CG-F02　The operational record distinguishes failed ignition, physical extinction and cutoff imperfectly

**PSI-159_Experimental table_CFI-G_Normal Flames.csv**

inverse CSV有1015實體資料列，但僅154列具Test；與179列normal合計333個具名紀錄。空列、公式／錯誤及操作備註保留，不能當333個已確認獨立火災。

- 證據身份：source_data_structure_and_label_conflict。
- 文獻定位：DATA-159_Experimental table_CFI-G_Normal Flames: Test/Hotignition/endcondition/Comments;21088C1 row4; DATA-159_Experimental table_CFI-G_Inverse Flames: Test column and blank tail rows。
- 使用數據部分：source_id: DATA-159_Experimental table_CFI-G_Normal Flames；locator: Test/Hotignition/endcondition/Comments;21088C1 row4；role: Rawconditions/sourceclassifiedrecords；source_id: DATA-159_Experimental table_CFI-G_Inverse Flames；locator: Test column and blank tail rows；role: Rawconditions/sourceclassifiedrecords。
- 本組適用層級：direct_source_records_and_endpoint_checks；Rawlabel/commentconflicts,blanksandFTpreserved.。
- 使用／控制因子：factor_and_role: Test:rowidentity；source_refs: source_id: DATA-159_Experimental table_CFI-G_Normal Flames；locator: Test/Hotignition/endcondition/Comments;21088C1 row4；source_id: DATA-159_Experimental table_CFI-G_Inverse Flames；locator: Test column and blank tail rows；factor_and_role: Hotignition:sourceoutcome；source_refs: source_id: DATA-159_Experimental table_CFI-G_Normal Flames；locator: Test/Hotignition/endcondition/Comments;21088C1 row4；source_id: DATA-159_Experimental table_CFI-G_Inverse Flames；locator: Test column and blank tail rows；factor_and_role: SE/FT:sourceendpointlabel；source_refs: source_id: DATA-159_Experimental table_CFI-G_Normal Flames；locator: Test/Hotignition/endcondition/Comments;21088C1 row4；source_id: DATA-159_Experimental table_CFI-G_Inverse Flames；locator: Test column and blank tail rows；factor_and_role: burnerTlimit:operationalcomment；source_refs: source_id: DATA-159_Experimental table_CFI-G_Normal Flames；locator: Test/Hotignition/endcondition/Comments;21088C1 row4；source_id: DATA-159_Experimental table_CFI-G_Inverse Flames；locator: Test column and blank tail rows；factor_and_role: blank/#VALUE!:unknownnotzero；source_refs: source_id: DATA-159_Experimental table_CFI-G_Normal Flames；locator: Test/Hotignition/endcondition/Comments;21088C1 row4；source_id: DATA-159_Experimental table_CFI-G_Inverse Flames；locator: Test column and blank tail rows。
- 來源限制：333rows is not333independent ignitions; preserve duplicate fullIDs, stages and multiple transitions.；Never infer physical extinction fromFT, a temperature limit or a missing signal.。
- 搜尋句（改寫）：The inverseCSV has1015physical data rows but only154namedTest records; with179normal records the pair has333named rows. Blank/formula/error cells and operational notes are kept. For example21088C1hasSE plus hitburnerTlimit in comments.。
- 來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/01_實驗資料/第一批下載/PSI-159_ACME CFI-G/Experimental table/PSI-159_Experimental table_CFI-G_Normal Flames.csv>)
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/01_實驗資料/第一批下載/PSI-159_ACME CFI-G/Experimental table/PSI-159_Experimental table_CFI-G_Normal Flames.csv>)

- 共同來源：**PSI-159_Experimental table_CFI-G_Inverse Flames.csv**；Test column and blank tail rows；[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/01_實驗資料/第一批下載/PSI-159_ACME CFI-G/Experimental table/PSI-159_Experimental table_CFI-G_Inverse Flames.csv>)

### CG-F03　Inverse oxidizer concentration belongs to the burner stream

**PSI-159_Reports_FinalRpt_ACME.CFI-G**

inverse為O2／N2從球形燃燒器流入碳氫燃料／N2艙體；85%氧瓶標不是載人艙或該燃料艙的氧濃度。

- 證據身份：source_experiment_and_stream_definition。
- 文獻定位：GA-f6cce7cc08ca: physical22,Table2。
- 使用數據部分：source_id: GA-f6cce7cc08ca；locator: physical22,Table2；role: Sourceanalysisorboundedliteraturecontext;notindependentraw。
- 本組適用層級：context_inverse_stream_guard；85%burnerO2notcabinO2.。
- 使用／控制因子：factor_and_role: inverseO2/N2burnerstream:reactantinput；source_refs: source_id: GA-f6cce7cc08ca；locator: physical22,Table2；factor_and_role: 85%O2bottle:stocknotcabin；source_refs: source_id: GA-f6cce7cc08ca；locator: physical22,Table2；factor_and_role: hydrocarbon/N2chamber:ambientmixture；source_refs: source_id: GA-f6cce7cc08ca；locator: physical22,Table2；factor_and_role: burnertemperature:hardwareobservable；source_refs: source_id: GA-f6cce7cc08ca；locator: physical22,Table2。
- 來源限制：Normal/inverse are stream roles, not1g/microgravity labels.；Hotflamequenching is not evidence of complete chemical extinction in cases with low-temperature reactions.。
- 搜尋句（改寫）：The inverse experiment sendsO2/N2from the porous sphere into a hydrocarbon/N2chamber. The85%O2stock bottle inTable2is not the atmosphere of the habitable cabin or the fuel-filled chamber.。
- 來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/研究報告與書章/第一批下載/PSI-159_ACME CFI-G/Reports/PSI-159_Reports_FinalRpt_ACME.CFI-G.pdf>)
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/03_其他文件/研究報告與書章/第一批下載/PSI-159_ACME CFI-G/Reports/PSI-159_Reports_FinalRpt_ACME.CFI-G.pdf>)

| Model ID | 公式／預測量 | 展示程式 | 數值比較與限制 |
| --- | --- | --- | --- |
| READINESS-PSI-159 | 原文方程／模型參見MODEL_INVENTORY；本次尚未閉合；CFI-G (inputs missing) | 未實作 · 尚未取得本機檔案 | 未執行／缺閉合輸入；來源就緒度盤點，不是數值預測；R²（模型全群）=N/A；尚未取得／不適用；Event-timing recurrence or source descriptors do not establish a general continuous geometry or ignition/extinction predictor.；Case-linked original geometry/transition data and a complete fixed physical forward closure |

| 可開啟的圖／工具 | 身份與用途 |
| --- | --- |
| [開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/gas_combustion_evidence_20261115/models/comparison.html>) | 選正確架構；缺資料的研究僅顯示就緒度，不畫假預測 |

## 2. 使用資料與參數總表的因子對照

| 總表原分類 | 來源身份 | 原欄名單位 | 原欄名例 | 總表定位 |
| --- | --- | --- | --- | --- |
| 光電／離子偵測訊號 | 儀器原始訊號 | 未由欄名確認 | IonCurrent；PMT1；PMT2；PMT3 | '物理參數'!A467:K467 |
| 光電／離子偵測訊號 | 儀器設定／控制參數 | 未由欄名確認 | PMT 1 Gain；PMT 2 Gain；PMT 3 Gain | '物理參數'!A468:K468 |
| 其他氣體組成／濃度 | 條件或分析量 | 未由欄名確認 | Xf；Xf before test；Xf after test；Nitrogen；Hydrogen / Helium (45/55)；Dilution of fuel and inert | '物理參數'!A469:K469 |
| 化學計量混合分率 | 計算／分析參數 | 未由欄名確認 | Zst；Stoichiometric Conversion Equation | '物理參數'!A470:K470 |
| 壓力 | 量測或設定 | bar | approx p (bar) | '物理參數'!A471:K471 |
| 壓力 | 量測或設定 | psia | Pstart (psia)；Pend (psia)；Returns the delta pressure (psia) of the combustion chamber from event start to event end | '物理參數'!A472:K472 |
| 壓力 | 量測或設定 | 未由欄名確認 | Chamber Pressure | '物理參數'!A473:K473 |
| 密度 | 量測或來源分析量 | g/L | Density (g/L) | '物理參數'!A474:K474 |
| 密度 | 量測或來源分析量 | 未由欄名確認 | Density | '物理參數'!A475:K475 |
| 尺寸／幾何 | 儀器設定／控制參數 | 未由欄名確認 | TP_PARAMETER_IGNITER_IGNITION_POSITION_1；TP_PARAMETER_IGNITER_IGNITION_POSITION_2 | '物理參數'!A476:K476 |
| 影像／光譜設定 | 儀器設定或影像座標 | 未由欄名確認 | Color；filterNumber | '物理參數'!A477:K477 |
| 氧濃度 | 量測或條件值 | mg/s | O2 flow rate (mg/s) | '物理參數'!A478:K478 |
| 氧濃度 | 量測或條件值 | 未由欄名確認 | XO2 before test；XO2 after test；XO2；Oxygen；O2；Ethylene: C2H4 → - 3 O2 + 2 H2O + 2 CO2；Methane: CH4 → - 2 O2 + 2 H2O + CO2；Hydrogen: 2 H2 → - O2 + 2 H2O；PickOxygen；O2 Fill | '物理參數'!A479:K479 |
| 流速／通風 | 量測或設定 | 未由欄名確認 | Ramp to final velocity | '物理參數'!A480:K480 |
| 液滴直徑／面積 | 影像／來源分析量 | 未由欄名確認 | sd0 IPSU1 fci files cannot be re-downlinked for this TP | '物理參數'!A481:K481 |
| 溫度 | 量測或設定 | C | Peak burner Temp (C)；2007-01-01 001 00:00:27:504~acme~Copyright (C) 2002-13；2007-01-01 001 00:00:28:187~acme~Copyright (C) 2002-13；2007-01-01 001 00:00:28:042~acme~Copyright (C) 2002-13；2007-01-01 001 00:00:41:182~acme~Copyright (C) 2002-13；2007-01-01 001 00:00:27:956~acme~Copyright (C) 2002-13；2007-01-01 001 00:00:27:818~acme~Copyright (C) 2002-13；2007-01-01 001 00:00:27:918~acme~Copyright (C) 2002-13；2007-01-01 001 00:00:29:293~acme~Copyright (C) 2002-13；2007-01-01 001 00:00:29:278~acme~Copyright (C) 2002-13；其餘見原始欄位 | '物理參數'!A482:K482 |
| 溫度 | 量測或設定 | K | Peak burner temp (K) | '物理參數'!A483:K483 |
| 溫度 | 量測或設定 | Standard Liters - 0 DegC, 760 Torr | ACME MFCs (Standard Liters - 0 DegC, 760 Torr) | '物理參數'!A484:K484 |
| 溫度 | 量測或設定 | Standard Liters - 0 DegC, 760 torr | Start Mixture (Standard Liters - 0 DegC, 760 torr)；Event Delta (Standard Liters - 0 DegC, 760 torr)；Finish Mixture (Standard Liters - 0 DegC, 760 torr)；Recirculation Loop Contents (Standard Liters - 0 DegC, 760 torr) | '物理參數'!A485:K485 |
| 溫度 | 量測或設定 | 未由欄名確認 | Thermocouple；Chamber Temperature；FCU_MP_TM1；FCU_MP_TM2；FCU_MP_TM3；FCU_MP_TM4；TC200A；TC200B | '物理參數'!A486:K486 |
| 熱通量／輻射 | 儀器設定／控制參數 | 未由欄名確認 | Radiometer3+60LoGain；Radiometer3+60HiGain；Radiometer3+30LoGain；Radiometer3+30HiGain；Radiometer3-10LoGain；Radiometer3-10HiGain | '物理參數'!A487:K487 |
| 熱通量／輻射 | 量測通道或來源分析量 | 未由欄名確認 | Radiometer；RadiometerOffset；RadiometerOffsetCJ | '物理參數'!A488:K488 |
| 燃燒率／燃燒常數 | 計算／分析參數 | mg/s | HC burnrate (mg/s) | '物理參數'!A489:K489 |
| 燃燒／點火／老化時間 | 時序或處理條件 | sec | burn time (sec) | '物理參數'!A490:K490 |
| 絕熱溫度 | 計算／分析參數 | K | Tad (K) | '物理參數'!A491:K491 |
| 質量流率 | 量測或設定 | mg/s | mHC (mg/s) | '物理參數'!A492:K492 |
| 電場電壓／電流 | 儀器設定／控制參數 | 未由欄名確認 | EfieldSetpointOut | '物理參數'!A493:K493 |
| 電場電壓／電流 | 量測或設定 | 未由欄名確認 | EField；EFieldPol；EfieldVoltage | '物理參數'!A494:K494 |
| 體積流量／MFC | 儀器設定／控制參數 | V | MFCA1Setpoint(V)；MFCA2Setpoint(V)；MFCA3Setpoint(V) | '物理參數'!A495:K495 |
| 體積流量／MFC | 儀器設定／控制參數 | 未由欄名確認 | MFCA1 Full Scale；MFCA2 Full Scale；MFCA3 Full Scale | '物理參數'!A496:K496 |
| 體積流量／MFC | 量測或設定 | 未由欄名確認 | MFCA1 Gas；MFCA2 Gas；MFCA3 Gas；MFCDiluent；MFCFuel；MFCN2；MFCO2；MFCA1StaticMixerFlow；MFCA2BypassFlow；MFCA3FuelFlow；其餘見原始欄位 | '物理參數'!A497:K497 |
| 點火功率／電壓／電流 | 儀器設定／控制參數 | 未由欄名確認 | TP_PARAMETER_IGNITER_WATTAGE；TP_PARAMETER_IGNITER_ON_TIME | '物理參數'!A498:K498 |
| 點火功率／電壓／電流 | 量測或設定 | ms | Igniter On Time (ms) | '物理參數'!A499:K499 |
| 點火功率／電壓／電流 | 量測或設定 | 未由欄名確認 | Igniter Wattage | '物理參數'!A500:K500 |

以上是該 investigation 的欄位盤點；個別結論實際使用的因子以第1節與下列補充為準。

| 本組實際因子 | 總表定位／未列欄位 | 文獻中的用途 |
| --- | --- | --- |
| CG-F01 / 30%butanenormal:sourcefuelseries | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| CG-F01 / 2bar/ambientXO2≈.39:publishedcoolflameconditions | '物理參數'!G479 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| CG-F01 / coolflagPCI-A…G:sourceoutcome | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| CG-F01 / 21291C1multipletransitions:stagecount | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| CG-F01 / burntime:recorddurationnotcoolduration | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| CG-F02 / Test:rowidentity | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| CG-F02 / Hotignition:sourceoutcome | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| CG-F02 / SE/FT:sourceendpointlabel | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| CG-F02 / burnerTlimit:operationalcomment | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| CG-F02 / blank/#VALUE!:unknownnotzero | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| CG-F03 / inverseO2/N2burnerstream:reactantinput | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| CG-F03 / 85%O2bottle:stocknotcabin | '物理參數'!G469 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| CG-F03 / hydrocarbon/N2chamber:ambientmixture | '物理參數'!G469 | 文獻實際因子對應的原欄位類型；不是已完成各raw通道的試次／校準配對。 |
| CG-F03 / burnertemperature:hardwareobservable | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |

| 文獻因子／疑點 | 正確讀法或需補資料 |
| --- | --- |
| 流股與模式 | normal／inverse不是重力；氧化劑流與艙內氣氛分開；Tad與Zst為計算量。 |
| 總表類別疑點 | '物理參數'!G478是O2質量流率，不是氧百分比；G481的sd0日誌字串不能證明CFI-G為液滴試驗。 |

## 3. 共用資料的多項結論比較

| 結論／文獻 | 資料重疊身份 | 共同處 | 不同處／不能合併之處 |
| --- | --- | --- | --- |
| GA-f6cce7cc08ca；PUB-CFIG-KIM2023 | same_campaign_source_flags_and_publication | Publishedcoolflamepaperandfinalreportdescribeanarrowselectednormalbutaneseries. | CSV333namedrecordsincludeotherfuels/failures/FT,multipletransitionsandoperationalcutoffs. |

## 4. 消防洞見

| 類別 | 對應證據 | 數據支持的判斷 | 策略／產品構想 | 待驗證 |
| --- | --- | --- | --- | --- |
| 預防 | CG-F03 | normal／inverse、燃料流／氧化劑流／艙內氣氛與Tad各有不同角色。 | 搜尋條件先確認氧濃度所在流股，再選近似火源與材料暴露資料。 | 同流股組成、P/T、幾何與實際局部反應條件。 |
| 偵測 | 尚未取得／不適用 | 尚未建立本組可直接支持此消防用途的完整量測鏈。 | 先補本組對應的物理端點與資料配對，再設計策略測試。 | 相關系列與方法限制只能提供研究脈絡，不能代替本組產品或操作效能驗證。 |
| 撲滅／抑制 | 尚未取得／不適用 | 尚未建立本組可直接支持此消防用途的完整量測鏈。 | 先補本組對應的物理端點與資料配對，再設計策略測試。 | 相關系列與方法限制只能提供研究脈絡，不能代替本組產品或操作效能驗證。 |

## 逐次索引

| 原始檔／資料位置 | Trial／Run／列 | 共享身份與保留事項 |
| --- | --- | --- |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-159_ACME CFI-G\Experimental table\PSI-159_Experimental table_CFI-G_Normal Flames.csv | trial_id: 21112A1；csv_row_including_header: 46；record_kind: source_named_record；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Flame Type: Normal；Day: 4；Fuel: propane；Test: 21112A1；Cool flame?: 尚未取得／不適用； XO2 before test: 0.3954；XO2  after test: 0.3940449；approx p (bar): 0.9443956；Xf: 1；mHC (mg/s): 0.8；TFP: No；Tad (K): 2729.986983；Zst: 0.105434724；Hot ignition: Yes；burn time (sec): 43；Self-ext or flow term: FT；Peak burner T (C ): 513.074689；Comments: 1 bottle 100% propane；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-159_ACME CFI-G\Experimental table\PSI-159_Experimental table_CFI-G_Normal Flames.csv | trial_id: 21112 A2；csv_row_including_header: 47；record_kind: source_named_record；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Flame Type: Normal；Day: 4；Fuel: propane；Test: 21112 A2；Cool flame?: 尚未取得／不適用； XO2 before test: 0.3940449；XO2  after test: 0.391274328；approx p (bar): 0.9443956；Xf: 1；mHC (mg/s): 1.6；TFP: No；Tad (K): 2728.07951；Zst: 0.105128534；Hot ignition: Yes；burn time (sec): 44；Self-ext or flow term: SE；Peak burner T (C ): 306.401465；Comments: 尚未取得／不適用；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-159_ACME CFI-G\Experimental table\PSI-159_Experimental table_CFI-G_Normal Flames.csv | trial_id: 21112 A3；csv_row_including_header: 48；record_kind: source_named_record；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Flame Type: Normal；Day: 4；Fuel: propane；Test: 21112 A3；Cool flame?: 尚未取得／不適用； XO2 before test: 0.391274328；XO2  after test: 0.386794842；approx p (bar): 0.9443956；Xf: 1；mHC (mg/s): 1.2；TFP: No；Tad (K): 2724.147584；Zst: 0.104501512；Hot ignition: Yes；burn time (sec): 95；Self-ext or flow term: SE；Peak burner T (C ): 423.011622；Comments: 尚未取得／不適用；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-159_ACME CFI-G\Experimental table\PSI-159_Experimental table_CFI-G_Normal Flames.csv | trial_id: 21112 A4；csv_row_including_header: 49；record_kind: source_named_record；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Flame Type: Normal；Day: 4；Fuel: propane；Test: 21112 A4；Cool flame?: 尚未取得／不適用； XO2 before test: 0.386794842；XO2  after test: 0.379543758；approx p (bar): 0.9443956；Xf: 1；mHC (mg/s): 1；TFP: No；Tad (K): 2717.697955；Zst: 0.103484882；Hot ignition: Yes；burn time (sec): 185；Self-ext or flow term: FT；Peak burner T (C ): 472.323053；Comments: 尚未取得／不適用；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-159_ACME CFI-G\Experimental table\PSI-159_Experimental table_CFI-G_Normal Flames.csv | trial_id: 21112 A5；csv_row_including_header: 50；record_kind: source_named_record；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Flame Type: Normal；Day: 4；Fuel: propane；Test: 21112 A5；Cool flame?: 尚未取得／不適用； XO2 before test: 0.379543758；XO2  after test: 0.377663625；approx p (bar): 0.9443956；Xf: 1；mHC (mg/s): 2；TFP: No；Tad (K): 2707.007929；Zst: 0.101831712；Hot ignition: Yes；burn time (sec): 24；Self-ext or flow term: SE；Peak burner T (C ): 201.343312；Comments: 尚未取得／不適用；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-159_ACME CFI-G\Experimental table\PSI-159_Experimental table_CFI-G_Normal Flames.csv | trial_id: 21112 C1；csv_row_including_header: 51；record_kind: source_named_record；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Flame Type: Normal；Day: 4；Fuel: propane；Test: 21112 C1；Cool flame?: 尚未取得／不適用； XO2 before test: 0.377663625；XO2  after test: 0.37709578；approx p (bar): 0.9443956；Xf: 1；mHC (mg/s): 0.5；TFP: No；Tad (K): 2704.18406；Zst: 0.101401536；Hot ignition: Yes；burn time (sec): 29；Self-ext or flow term: FT；Peak burner T (C ): 529.294181；Comments: 尚未取得／不適用；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-159_ACME CFI-G\Experimental table\PSI-159_Experimental table_CFI-G_Normal Flames.csv | trial_id: 21112 C2；csv_row_including_header: 52；record_kind: source_named_record；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Flame Type: Normal；Day: 4；Fuel: propane；Test: 21112 C2；Cool flame?: 尚未取得／不適用； XO2 before test: 0.37709578；XO2  after test: 0.376528047；approx p (bar): 0.9443956；Xf: 1；mHC (mg/s): 0.5；TFP: No；Tad (K): 2703.326866；Zst: 0.101271488；Hot ignition: Yes；burn time (sec): 29；Self-ext or flow term: FT；Peak burner T (C ): 529.870579；Comments: 尚未取得／不適用；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-159_ACME CFI-G\Experimental table\PSI-159_Experimental table_CFI-G_Normal Flames.csv | trial_id: 21112 A6；csv_row_including_header: 53；record_kind: source_named_record；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Flame Type: Normal；Day: 4；Fuel: propane；Test: 21112 A6；Cool flame?: 尚未取得／不適用； XO2 before test: 0.376528047；XO2  after test: 0.366422787；approx p (bar): 0.9443956；Xf: 1；mHC (mg/s): 1；TFP: No；Tad (K): 2702.467823；Zst: 0.101141409；Hot ignition: Yes；burn time (sec): 259；Self-ext or flow term: SE；Peak burner T (C ): 460.517765；Comments: 尚未取得／不適用；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-159_ACME CFI-G\Experimental table\PSI-159_Experimental table_CFI-G_Normal Flames.csv | trial_id: 21112 C3；csv_row_including_header: 54；record_kind: source_named_record；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Flame Type: Normal；Day: 4；Fuel: propane；Test: 21112 C3；Cool flame?: 尚未取得／不適用； XO2 before test: 0.366422787；XO2  after test: 0.366422787；approx p (bar): 0.9443956；Xf: 1；mHC (mg/s): 0.5；TFP: No；Tad (K): 2686.828847；Zst: 0.098816409；Hot ignition: No；burn time (sec): 0；Self-ext or flow term: -；Peak burner T (C ): -；Comments: 尚未取得／不適用；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-159_ACME CFI-G\Experimental table\PSI-159_Experimental table_CFI-G_Normal Flames.csv | trial_id: 21112 C4；csv_row_including_header: 55；record_kind: source_named_record；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Flame Type: Normal；Day: 4；Fuel: propane；Test: 21112 C4；Cool flame?: 尚未取得／不適用； XO2 before test: 0.366422787；XO2  after test: 0.366422787；approx p (bar): 0.9443956；Xf: 1；mHC (mg/s): 0.5；TFP: No；Tad (K): 2686.828847；Zst: 0.098816409；Hot ignition: No；burn time (sec): 0；Self-ext or flow term: -；Peak burner T (C ): -；Comments: 尚未取得／不適用；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-159_ACME CFI-G\Experimental table\PSI-159_Experimental table_CFI-G_Normal Flames.csv | trial_id: 21112 C5；csv_row_including_header: 56；record_kind: source_named_record；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Flame Type: Normal；Day: 4；Fuel: propane；Test: 21112 C5；Cool flame?: 尚未取得／不適用； XO2 before test: 0.366422787；XO2  after test: 0.366422787；approx p (bar): 0.9443956；Xf: 1；mHC (mg/s): 0.5；TFP: No；Tad (K): 2686.828847；Zst: 0.098816409；Hot ignition: No；burn time (sec): 0；Self-ext or flow term: -；Peak burner T (C ): -；Comments: 尚未取得／不適用；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-159_ACME CFI-G\Experimental table\PSI-159_Experimental table_CFI-G_Normal Flames.csv | trial_id: 21112 C6；csv_row_including_header: 57；record_kind: source_named_record；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Flame Type: Normal；Day: 4；Fuel: propane；Test: 21112 C6；Cool flame?: 尚未取得／不適用； XO2 before test: 0.366422787；XO2  after test: 0.366422787；approx p (bar): 0.9443956；Xf: 1；mHC (mg/s): 0.5；TFP: No；Tad (K): 2686.828847；Zst: 0.098816409；Hot ignition: No；burn time (sec): 0；Self-ext or flow term: -；Peak burner T (C ): -；Comments: 尚未取得／不適用；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-159_ACME CFI-G\Experimental table\PSI-159_Experimental table_CFI-G_Normal Flames.csv | trial_id: 21112 F1；csv_row_including_header: 58；record_kind: source_named_record；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Flame Type: Normal；Day: 4；Fuel: propane；Test: 21112 F1；Cool flame?: 尚未取得／不適用； XO2 before test: 0.2125；XO2  after test: 0.2125；approx p (bar): 1.0133；Xf: 1；mHC (mg/s): 1；TFP: No；Tad (K): 2275.686041；Zst: 0.060981864；Hot ignition: No；burn time (sec): 0；Self-ext or flow term: -；Peak burner T (C ): -；Comments: 尚未取得／不適用；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-159_ACME CFI-G\Experimental table\PSI-159_Experimental table_CFI-G_Normal Flames.csv | trial_id: 21112 F2；csv_row_including_header: 59；record_kind: source_named_record；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Flame Type: Normal；Day: 4；Fuel: propane；Test: 21112 F2；Cool flame?: 尚未取得／不適用； XO2 before test: 0.2125；XO2  after test: 0.212224743；approx p (bar): 1.0133；Xf: 1；mHC (mg/s): 1；TFP: No；Tad (K): 2275.686041；Zst: 0.060981864；Hot ignition: Yes；burn time (sec): 8；Self-ext or flow term: SE；Peak burner T (C ): 95.0990032；Comments: 尚未取得／不適用；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-159_ACME CFI-G\Experimental table\PSI-159_Experimental table_CFI-G_Normal Flames.csv | trial_id: 21112 F3；csv_row_including_header: 60；record_kind: source_named_record；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Flame Type: Normal；Day: 4；Fuel: propane；Test: 21112 F3；Cool flame?: 尚未取得／不適用； XO2 before test: 0.212224743；XO2  after test: 0.212004554；approx p (bar): 1.0133；Xf: 1；mHC (mg/s): 0.8；TFP: No；Tad (K): 2274.412146；Zst: 0.060909858；Hot ignition: Yes；burn time (sec): 8；Self-ext or flow term: SE；Peak burner T (C ): 105.264091；Comments: 尚未取得／不適用；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-159_ACME CFI-G\Experimental table\PSI-159_Experimental table_CFI-G_Normal Flames.csv | trial_id: 21112 F4；csv_row_including_header: 61；record_kind: source_named_record；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Flame Type: Normal；Day: 4；Fuel: propane；Test: 21112 F4；Cool flame?: 尚未取得／不適用； XO2 before test: 0.212004554；XO2  after test: 0.211798144；approx p (bar): 1.0133；Xf: 1；mHC (mg/s): 0.6；TFP: No；Tad (K): 2273.390966；Zst: 0.060852246；Hot ignition: Yes；burn time (sec): 10；Self-ext or flow term: SE；Peak burner T (C ): 136.737387；Comments: 尚未取得／不適用；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-159_ACME CFI-G\Experimental table\PSI-159_Experimental table_CFI-G_Normal Flames.csv | trial_id: 21112 F5；csv_row_including_header: 62；record_kind: source_named_record；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Flame Type: Normal；Day: 4；Fuel: propane；Test: 21112 F5；Cool flame?: 尚未取得／不適用； XO2 before test: 0.211798144；XO2  after test: 0.211798144；approx p (bar): 1.0133；Xf: 1；mHC (mg/s): 0.4；TFP: No；Tad (K): 2272.431946；Zst: 0.060798229；Hot ignition: No；burn time (sec): 0；Self-ext or flow term: -；Peak burner T (C ): -；Comments: 尚未取得／不適用；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-159_ACME CFI-G\Experimental table\PSI-159_Experimental table_CFI-G_Normal Flames.csv | trial_id: 21112 H1；csv_row_including_header: 63；record_kind: source_named_record；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Flame Type: Normal；Day: 4；Fuel: propane；Test: 21112 H1；Cool flame?: 尚未取得／不適用； XO2 before test: 0.211798144；XO2  after test: 0.211591749；approx p (bar): 1.0133；Xf: 1；mHC (mg/s): 0.5；TFP: No；Tad (K): 2272.431946；Zst: 0.060798229；Hot ignition: Yes；burn time (sec): 12；Self-ext or flow term: SE；Peak burner T (C ): 154.162132；Comments: 尚未取得／不適用；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-159_ACME CFI-G\Experimental table\PSI-159_Experimental table_CFI-G_Normal Flames.csv | trial_id: 21112 H2；csv_row_including_header: 64；record_kind: source_named_record；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Flame Type: Normal；Day: 4；Fuel: propane；Test: 21112 H2；Cool flame?: 尚未取得／不適用； XO2 before test: 0.211591749；XO2  after test: 0.211402567；approx p (bar): 1.0133；Xf: 1；mHC (mg/s): 0.5；TFP: No；Tad (K): 2271.471317；Zst: 0.060744207；Hot ignition: Yes；burn time (sec): 11；Self-ext or flow term: SE；Peak burner T (C ): 155.395419；Comments: 尚未取得／不適用；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-159_ACME CFI-G\Experimental table\PSI-159_Experimental table_CFI-G_Normal Flames.csv | trial_id: 21112 H3；csv_row_including_header: 65；record_kind: source_named_record；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Flame Type: Normal；Day: 4；Fuel: propane；Test: 21112 H3；Cool flame?: 尚未取得／不適用； XO2 before test: 0.211402567；XO2  after test: 0.211402567；approx p (bar): 1.0133；Xf: 1；mHC (mg/s): 0.5；TFP: No；Tad (K): 2270.589322；Zst: 0.060694682；Hot ignition: No；burn time (sec): 0；Self-ext or flow term: -；Peak burner T (C ): -；Comments: 尚未取得／不適用；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |

## 缺件與適用範圍

- Tad/Zstcalculated;peakburnerTisnotpeakflameT.
- Fulltimealignedflamegeometryandchemistrytargetjoinnotclosed.
