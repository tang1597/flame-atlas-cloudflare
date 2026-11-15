# Wang2019 ground methane jet IDF

小資料集 ID：`WANG2019-GROUND-JET-IDF`

## 資料身份與範圍

| 項目 | 內容 |
| --- | --- |
| 原始 NASA PSI investigation | 尚未取得／不適用 |
| 相關PSI索引（不是原始資料） | PSI-10 |
| 材料／配方 | fuel: CH4；diluent: N2 |
| 幾何 | shape: verticalconcentriccoflowjet；inner_ID_mm: 2.9；outer_diameter_mm: 102；chimney_ID_mm: 100 |
| 實驗模式 | gravity: Earthlaboratory；configuration: IDF；experiment_pressure_bar: 1.01；ambient_temperature_C: 25 |
| 證據角色 | related_ground_model_not_flight_or_spherical_validation |
| 環境 | gravity: 尚未確認；mode: gravity: Earthlaboratory；configuration: IDF；experiment_pressure_bar: 1.01；ambient_temperature_C: 25 |
| 資料粒度／共享試片 | Per-row source values retained; summary/day/variant rows are not promoted to independent burns. |
| 可用數值 | fixed_original_formula_and_qualified_figure_proxy_available |

## 1. 文獻結果與視覺化程式

### GROUND-F01　Fixed Roper comparison is a ground jet example, not an ISS spherical validation

**Dilution effects on laminar jet diffusion flame lengths**

Wang2019為25°C、1.01 bar、2.9 mm內徑的地面垂直共流噴口。Roper固定常數沿用較早校準；287點的alpha=0.735為作者擬合，兩個既存圖上讀值另有光學端點歧義。它不是PSI10球形飛行試驗。

- 證據身份：related_ground_source_model_and_optical_comparison。
- 文獻定位：GA-4e2c7ec880ee: physical2–3,Eq1;physical4,Fig3;physical6。
- 使用數據部分：source_id: GA-4e2c7ec880ee；locator: physical2–3,Eq1;physical4,Fig3;physical6；role: Sourceanalysisorboundedliteraturecontext;notindependentraw。
- 本組適用層級：direct_ground_source_example_related_to_FlameDesign；Jet2.9mmnot6.35mmporoussphere;do notmergewithPSI10flightrecords.。
- 使用／控制因子：factor_and_role: 2.9mmjet:geometry；source_refs: source_id: GA-4e2c7ec880ee；locator: physical2–3,Eq1;physical4,Fig3;physical6；factor_and_role: CH4/O2/N2fractionsandcomponentflow:inputs；source_refs: source_id: GA-4e2c7ec880ee；locator: physical2–3,Eq1;physical4,Fig3;physical6；factor_and_role: Qat25C/1.01bar:ideal-gas-derivedflow；source_refs: source_id: GA-4e2c7ec880ee；locator: physical2–3,Eq1;physical4,Fig3;physical6；factor_and_role: D20mm²s/Tf1500K/T0293K:priorcalibratedconstants；source_refs: source_id: GA-4e2c7ec880ee；locator: physical2–3,Eq1;physical4,Fig3;physical6；factor_and_role: sourceFig3opticalclosure:lengthproxy；source_refs: source_id: GA-4e2c7ec880ee；locator: physical2–3,Eq1;physical4,Fig3;physical6。
- 來源限制：This apparatus is not PSI10poroussphere. Do not assign its predicted jet length to the sphere.；OriginalRoper Sc=Le=1/no axial diffusion/constant nearzoneproperties/equalreactantproductmoles assumptions retained.；Two sourcefigure proxies, not independent raw validation or a meaningfulR2 benchmark.。
- 搜尋句（改寫）：Wang2019uses a2.9mmID verticalcoflowjet/chimney with methane/propane at25°C/1.01bar. Eq1fixedD20mm²/s,Tf1500K,T0293K derives from older calibration. Current287pointalpha.735is source-fitted; the preserved twoFigure3readouts have optical-endpoint ambiguity.。
- 來源：[來源](<https://terpconnect.umd.edu/~pbs/2019%20Wang%20et%20al.%20PCI.pdf>)
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/earth_space_transfer_20261114/phase6_mass_balance_dynamic_20261114/role_D/psi10_case/Wang_2019_Dilution_flame_lengths.pdf>)

| Model ID | 公式／預測量 | 展示程式 | 數值比較與限制 |
| --- | --- | --- | --- |
| EARTH-ROPER-RELATED | L_mm=Q_total_mm3_s/[4*pi*D0_mm2_s*ln(1+1/S)]*(T0_legacy/Tf_characteristic)^exponent<br>Q uses source component mass flow, component mole fraction and actual ambient ideal-gas conversion.<br>NDF S=nu*X_CH4/X_O2; IDF S=X_O2/(nu*X_CH4).；Legacy-model stoichiometric length versus qualified optical closure proxy (mm) | producer.py · [開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/tools/gas_evidence/models/producer.py>) | runnable；fixed previously calibrated correlation compared with qualified source-figure optical proxies；R²（模型全群）=N/A；尚未取得／不適用；Legacy D0/T0/Tf parameters came from prior calibration, not independently measured flame temperature or pure first-principles constants.；The extended alpha model was calibrated on the current287cases and is not substituted.；Both author dashed annotation and restricted grayscale readout remain separate.；NDF has a stronger near-base grayscale feature; its closure ROI is not the global grayscale maximum. IDF has a broad plateau.；Reading bounds are not experimental confidence intervals; no favored endpoint or error gate is chosen.；These methane ground jets are related literature, not FlameDesign spherical burner flight records or Earth-to-space validation.；related_ground_coflow_jet_not_PSI10_spherical_or_ISS_measurement；fixed previously calibrated correlation compared with qualified source-figure optical proxies |

| 可開啟的圖／工具 | 身份與用途 |
| --- | --- |
| [開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/gas_combustion_evidence_20261115/models/earth_roper_related_comparison.png>) | 相關地面噴流，不能當PSI10球形ISS驗證 |
| [開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/gas_combustion_evidence_20261115/models/comparison.html>) | 選正確架構；缺資料的研究僅顯示就緒度，不畫假預測 |

## 2. 使用資料與參數總表的因子對照

尚未取得可逐項對照的紀錄。

以上是該 investigation 的欄位盤點；個別結論實際使用的因子以第1節與下列補充為準。

| 本組實際因子 | 總表定位／未列欄位 | 文獻中的用途 |
| --- | --- | --- |
| GROUND-F01 / 2.9mmjet:geometry | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| GROUND-F01 / CH4/O2/N2fractionsandcomponentflow:inputs | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| GROUND-F01 / Qat25C/1.01bar:ideal-gas-derivedflow | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| GROUND-F01 / D20mm²s/Tf1500K/T0293K:priorcalibratedconstants | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| GROUND-F01 / sourceFig3opticalclosure:lengthproxy | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |

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
| C:\Users\User\Documents\ChatGPT\Nasa Hackathon\output\earth_space_transfer_20261114\phase6_mass_balance_dynamic_20261114\role_D\psi10_case\Wang_2019_Dilution_flame_lengths.pdf | trial_id: Wang2019Fig3b；source_locator: physical4Fig3；record_kind: qualified_source_figure_optical_proxy_notoriginalraw | raw_parameters_as_stored: 尚未取得／不適用；source_identity: 原列／階段身份保留，未自動視為獨立燃燒。 |

## 缺件與適用範圍

- 目前不足兩項可適用的來源結論；尚未完成多結論比較，不以研究目的湊數。
