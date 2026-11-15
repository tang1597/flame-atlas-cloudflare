# BRE NASA67 source short-drop example

小資料集 ID：`BRE-GROUND-DROP-NASA67`

## 資料身份與範圍

| 項目 | 內容 |
| --- | --- |
| 原始 NASA PSI investigation | 尚未取得／不適用 |
| 相關PSI索引（不是原始資料） | PSI-20 |
| 材料／配方 | fuel: C2H4；ambient_XO2: 0.26 |
| 幾何 | shape: flat porous disk；diameter_mm: 25 |
| 實驗模式 | gravity: ground5.18sdropmicrogravity；role: sourceAppendixC.2fixedexample |
| 證據角色 | related_ground_drop_model_not_ISS_validation |
| 環境 | gravity: 尚未確認；mode: gravity: ground5.18sdropmicrogravity；role: sourceAppendixC.2fixedexample |
| 資料粒度／共享試片 | Per-row source values retained; summary/day/variant rows are not promoted to independent burns. |
| 可用數值 | fixed_source_formula_available_independent_validation_blocked_by_target_alignment |

## 1. 文獻結果與視覺化程式

### DROP-F01　BRE NASA67 is a short-drop fixed-source example with conflicting comparators

**Development and analysis of a Burning Rate Emulator (BRE) for study in microgravity**

Markan2018 Appendix C.2的NASA67對到Table3.2 Test6：25 mm平盤、C2H4、XO2=0.26、0.81 atm、3.46 g/m²s。表中焰尖21.7 mm與Fig5.13約5秒的25–27 mm讀值分開保留，不挑較接近模型的值。

- 證據身份：related_ground_drop_source_equation_replay。
- 文獻定位：GA-006c9492c99d: physical54–55 opticaltip;61Table3.2;121Table5.1;125Fig5.13;139–142AppendixC.2。
- 使用數據部分：source_id: GA-006c9492c99d；locator: physical54–55 opticaltip;61Table3.2;121Table5.1;125Fig5.13;139–142AppendixC.2；role: Sourceanalysisorboundedliteraturecontext;notindependentraw。
- 本組適用層級：direct_source_example_with_unresolved_targets；NotISSPSI20raw;sourceequationreplayandopticaltargetsremainseparate.。
- 使用／控制因子：factor_and_role: 25mmdisk:geometry；source_refs: source_id: GA-006c9492c99d；locator: physical54–55 opticaltip;61Table3.2;121Table5.1;125Fig5.13;139–142AppendixC.2；factor_and_role: C2H4/XO2.26/p.81atm/mflux3.46g m−2s−1:sourcecase；source_refs: source_id: GA-006c9492c99d；locator: physical54–55 opticaltip;61Table3.2;121Table5.1;125Fig5.13;139–142AppendixC.2；factor_and_role: k/cp/rhoandfactor2M:fixedauthorclosure；source_refs: source_id: GA-006c9492c99d；locator: physical54–55 opticaltip;61Table3.2;121Table5.1;125Fig5.13;139–142AppendixC.2；factor_and_role: 5sheight:flamesheetprediction；source_refs: source_id: GA-006c9492c99d；locator: physical54–55 opticaltip;61Table3.2;121Table5.1;125Fig5.13;139–142AppendixC.2；factor_and_role: opticaltip21.7vs25–27mm:unresolvedsourcecomparators；source_refs: source_id: GA-006c9492c99d；locator: physical54–55 opticaltip;61Table3.2;121Table5.1;125Fig5.13;139–142AppendixC.2。
- 來源限制：Not an ISSPSI20raw trial; the supportingNASA67identifieris an oldergrounddrop test.；Modelstoichiometricflamesheet and highestopticaltip are differentobservables; R2N/A for this source example.；Exactfactor2M,k/cp/rho and pressure-as-metadata retained, not fit or repaired.。
- 搜尋句（改寫）：The2018dissertationAppendixC.2linksNASA67toTable3.2Test6:25mmflatdisk,C2H4,XO2.26,p.81atm,mflux3.46g/m²s. OpticaltipTable3.2says21.7mm; Fig5.13readoutnear5s is approximately25–27mm. Both remain, without choosing the closer one.。
- 來源：[來源](<https://drum.lib.umd.edu/bitstreams/6cb996b9-06ae-4413-9051-d65eec4a1637/download>)
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/earth_space_transfer_20261114/phase7/role_D/assets/Markan2018_dissertation.pdf>)

| Model ID | 公式／預測量 | 展示程式 | 數值比較與限制 |
| --- | --- | --- | --- |
| BRE-MARKAN-C2-RELATED | D_model=k/(rho*cp); Pe=M_author/(4*pi*c*rho*D_model)<br>Z(xi,tau)=[1-exp(Pe*(atan(xi)-pi/2))]/[1-E0] * erfc((xi-xi0)/(2*sqrt(tau)))<br>Solve Z=Y_O2/(S*Y_F_b+Y_O2); height_mm=c*xi*1000<br>M_author includes the original factor2; thermal diffusivity is not inferred from target height.；Computed stoichiometric-sheet height compared descriptively with source visible-tip height (mm) | producer.py · [開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/tools/gas_evidence/models/producer.py>) | runnable；same-source fixed author numerical example with source-analyzed table and qualified figure comparators；R²（模型全群）=N/A；尚未取得／不適用；One fully specified same-source example, not an independently validated ISS flight architecture.；Source Table3.2 lists21.7mm; independent Fig5.13 readout is25-27mm. Neither comparator is selected based on closeness to the model.；Modeled stoichiometric sheet is not directly measured by the visible highest-tip method.；Model starts at the burner while the experiment was ignited under1g before release; no time shift is fitted.；Source script32C and tables32.9C remain distinct; fixed properties are not pressure-corrected.；The original factor2 model mass flow is not relabeled as measured single-face meter flow.；Eq5.90 heat-flux extension with these constants does not reproduce the source Fig5.11 flux curves; closure linkage remains unresolved.；related_ground_short_drop_BRE_program_not_PSI20_ISS_raw_trial；same-source fixed author numerical example with source-analyzed table and qualified figure comparators |

| 可開啟的圖／工具 | 身份與用途 |
| --- | --- |
| [開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/gas_combustion_evidence_20261115/models/bre_fixed_transient_comparison.png>) | 固定作者案例；火焰面與可見尖端分開；單例不計R² |
| [開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/gas_combustion_evidence_20261115/models/comparison.html>) | 選正確架構；缺資料的研究僅顯示就緒度，不畫假預測 |

## 2. 使用資料與參數總表的因子對照

尚未取得可逐項對照的紀錄。

以上是該 investigation 的欄位盤點；個別結論實際使用的因子以第1節與下列補充為準。

| 本組實際因子 | 總表定位／未列欄位 | 文獻中的用途 |
| --- | --- | --- |
| DROP-F01 / 25mmdisk:geometry | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| DROP-F01 / C2H4/XO2.26/p.81atm/mflux3.46g m−2s−1:sourcecase | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| DROP-F01 / k/cp/rhoandfactor2M:fixedauthorclosure | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| DROP-F01 / 5sheight:flamesheetprediction | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| DROP-F01 / opticaltip21.7vs25–27mm:unresolvedsourcecomparators | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |

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
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\output\earth_space_transfer_20261114\phase7\role_D\assets\Markan2018_dissertation.pdf | trial_id: NASA67 / Table3.2Test6 / Table5.1Test2；source_locator: physical61/121/139；record_kind: same_source_ground_drop_example | raw_parameters_as_stored: 尚未取得／不適用；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |

## 缺件與適用範圍

- 目前不足兩項可適用的來源結論；尚未完成多結論比較，不以研究目的湊數。
- 5smodel26.0523mmdoesnotresolveTable21.7vsFig25–27conflict.
- Predictedflamesheetisnotdirectmeasuredcontour.
