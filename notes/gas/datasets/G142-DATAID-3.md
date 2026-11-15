# Ground counterflow source bundle 3

小資料集 ID：`G142-DATAID-3`

## 資料身份與範圍

| 項目 | 內容 |
| --- | --- |
| 原始 NASA PSI investigation | [PSI-142](https://psi.nasa.gov/physci/repo/data/investigations/PSI-142) |
| 相關PSI索引（不是原始資料） | 尚未取得／不適用 |
| 材料／配方 | fuel_identity: source-specific,notfullyboundfromindex；source_description: CFE and HFE Predicted vs Measured  |
| 幾何 | shape: counterfloworothergroundsourceapparatus;notasphere；exactgeometry: requirespairedpaper |
| 實驗模式 | gravity: Earthlab/sourcecalculation；flame_mode: premixed/nonpremixedandassistancemustbecheckedperoriginalpaper |
| 證據角色 | related_ground_counterflow_or_diagnostic_data_bundle |
| 環境 | gravity: 尚未確認；mode: gravity: Earthlab/sourcecalculation；flame_mode: premixed/nonpremixedandassistancemustbecheckedperoriginalpaper |
| 資料粒度／共享試片 | Per-row source values retained; summary/day/variant rows are not promoted to independent burns. |
| 可用數值 | original_numeric_sheets_present_identity_and_model_closure_not_fullyverified |

## 1. 文獻結果與視覺化程式

### G142-F01　CSV and workbook disagree on ozone/mode indexing

**PSI-142_Experimental table_Data Summary Table.csv**

原CSV與原Excel對Data ID1／2的臭氧敘述正好相反；ID3／4的模式與觀測量也待核。原數字工作表存在，但不默修臭氧或火焰模式再歸因。

- 證據身份：source_quality_conflict。
- 文獻定位：DATA-142_Experimental table_Data Summary Table: rows2–5; DATA-142-WORKBOOK: data summary!B4:E8;dataID1–8 sheets。
- 使用數據部分：source_id: DATA-142_Experimental table_Data Summary Table；locator: rows2–5；role: Rawconditions/sourceclassifiedrecords；source_id: DATA-142-WORKBOOK；locator: data summary!B4:E8;dataID1–8 sheets；role: Rawconditions/sourceclassifiedrecords。
- 本組適用層級：direct_source_identity_conflict；Donottransferozone/modefromadjacentdatasetIDs.。
- 使用／控制因子：factor_and_role: DataID/DOI/FigureID:bundleidentity；source_refs: source_id: DATA-142_Experimental table_Data Summary Table；locator: rows2–5；source_id: DATA-142-WORKBOOK；locator: data summary!B4:E8;dataID1–8 sheets；factor_and_role: with/noozone:conflictingindexlabel；source_refs: source_id: DATA-142_Experimental table_Data Summary Table；locator: rows2–5；source_id: DATA-142-WORKBOOK；locator: data summary!B4:E8;dataID1–8 sheets；factor_and_role: Yf/strain(1/s):numericdatasheetvariables；source_refs: source_id: DATA-142_Experimental table_Data Summary Table；locator: rows2–5；source_id: DATA-142-WORKBOOK；locator: data summary!B4:E8;dataID1–8 sheets；factor_and_role: PLIFa.u./distancecm/thermometryK:distinctobservables；source_refs: source_id: DATA-142_Experimental table_Data Summary Table；locator: rows2–5；source_id: DATA-142-WORKBOOK；locator: data summary!B4:E8;dataID1–8 sheets。
- 來源限制：DataID is a figure/data bundle, not an independentexperiment.；Do not pool premixed and nonpremixed limits or assign ozone direction before primaryFigure4/5mapping is reconciled.。
- 搜尋句（改寫）：DataID1/2 ozone descriptions are reversed between originalCSV and workbookdata-summaryE4/E5; ID3/4also requiremode/observable checks. Numeric worksheets exist, but no ozone or flame-mode correction is silently applied.。
- 來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/01_實驗資料/第一批下載/PSI-142_research/Experimental table/PSI-142_Experimental table_Data Summary Table.csv>)
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/01_實驗資料/第一批下載/PSI-142_research/Experimental table/PSI-142_Experimental table_Data Summary Table.csv>)

- 共同來源：**6dbe702e6abad060_PSI-142_Analyzed Data_PSI data summary Princeton with links.xlsx**；data summary!B4:E8;dataID1–8 sheets；[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/01_實驗資料/補下載/PSI-142/Analyzed Data/6dbe702e6abad060_PSI-142_Analyzed Data_PSI data summary Princeton with links.xlsx>)

尚未取得可逐項對照的紀錄。

## 2. 使用資料與參數總表的因子對照

| 總表原分類 | 來源身份 | 原欄名單位 | 原欄名例 | 總表定位 |
| --- | --- | --- | --- | --- |
| 其他氣體組成／濃度 | 地面實驗／模擬來源，須按資料區分 | 未由欄名確認 | cool diffusion flame extinction limits, no ozone；cool diffusion flame extinction limits, with ozone；hot diffusion flame extinction limits, no ozone；Xf = 0.1；Xf = 0.042；Xf = 0.009；Xf | '物理參數'!A464:K464 |
| 尺寸／幾何 | 地面實驗／模擬來源，須按資料區分 | cm | distance [cm]；location [cm]；distance[cm] | '物理參數'!A465:K465 |
| 溫度 | 地面實驗／模擬來源，須按資料區分 | K | temperature [K] | '物理參數'!A466:K466 |

以上是該 investigation 的欄位盤點；個別結論實際使用的因子以第1節與下列補充為準。

| 本組實際因子 | 總表定位／未列欄位 | 文獻中的用途 |
| --- | --- | --- |
| G142-F01 / DataID/DOI/FigureID:bundleidentity | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| G142-F01 / with/noozone:conflictingindexlabel | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| G142-F01 / Yf/strain(1/s):numericdatasheetvariables | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| G142-F01 / PLIFa.u./distancecm/thermometryK:distinctobservables | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |

尚未取得可逐項對照的紀錄。

## 3. 共用資料的多項結論比較

| 結論／文獻 | 資料重疊身份 | 共同處 | 不同處／不能合併之處 |
| --- | --- | --- | --- |
| GA-4e2c7ec880ee；GA-006c9492c99d；GA-22df3ad78b88 | related_model_different_architecture | Literaturefixedformscaninformboundedphysicalcomparisons. | Wangjet,Markandiskandearlierspheredropareseparatehardware/campaigns,notPSI10/20ISSgroundtruth. |

## 4. 消防洞見

| 類別 | 對應證據 | 數據支持的判斷 | 策略／產品構想 | 待驗證 |
| --- | --- | --- | --- | --- |
| 預防 | 尚未取得／不適用 | 尚未建立本組可直接支持此消防用途的完整量測鏈。 | 先補本組對應的物理端點與資料配對，再設計策略測試。 | 相關系列與方法限制只能提供研究脈絡，不能代替本組產品或操作效能驗證。 |
| 偵測 | 尚未取得／不適用 | 尚未建立本組可直接支持此消防用途的完整量測鏈。 | 先補本組對應的物理端點與資料配對，再設計策略測試。 | 相關系列與方法限制只能提供研究脈絡，不能代替本組產品或操作效能驗證。 |
| 撲滅／抑制 | 尚未取得／不適用 | 尚未建立本組可直接支持此消防用途的完整量測鏈。 | 先補本組對應的物理端點與資料配對，再設計策略測試。 | 相關系列與方法限制只能提供研究脈絡，不能代替本組產品或操作效能驗證。 |

## 逐次索引

| 原始檔／資料位置 | Trial／Run／列 | 共享身份與保留事項 |
| --- | --- | --- |
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-142_research\Experimental table\PSI-142_Experimental table_Data Summary Table.csv | trial_id: 3；csv_row_including_header: 4；record_kind: figure_data_bundle_index_not_independenttrial；missing_values_preserved: True；independent_burn_status: not_established_from_summary_or_name | raw_parameters_as_stored: Data ID: 3；Data Description: CFE and HFE Predicted vs Measured ；Reference Publication Link: http://dx.doi.org/10.1016/j.combustflame.2017.01.028；Figure ID in Reference: 7；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |

## 缺件與適用範圍

- 目前不足兩項可適用的來源結論；尚未完成多結論比較，不以研究目的湊數。
- Numericworkbookexists,butpaperfigure/fuel/modeandunitsrequirefurtherexactmatchingbeforeaquantitativemodelcase.
