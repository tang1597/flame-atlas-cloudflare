# Earlier spherical ethylene/propane short-drop campaign

小資料集 ID：`SPHERICAL-PREISS-2007-DROP`

## 資料身份與範圍

| 項目 | 內容 |
| --- | --- |
| 原始 NASA PSI investigation | 尚未取得／不適用 |
| 相關PSI索引（不是原始資料） | PSI-10 |
| 材料／配方 | fuel_family: C2H4；C3H8；diluent: N2 |
| 幾何 | shape: poroussphericalburner；diameter_per_case: 尚未確認 |
| 實驗模式 | gravity: ground2.2sdropmicrogravity；configuration: normalandinverseinoriginalpaper |
| 證據角色 | related_older_spherical_ground_drop_campaign |
| 環境 | gravity: 尚未確認；mode: gravity: ground2.2sdropmicrogravity；configuration: normalandinverseinoriginalpaper |
| 資料粒度／共享試片 | Per-row source values retained; summary/day/variant rows are not promoted to independent burns. |
| 可用數值 | sourcepaperobservations_available_pointwise_original_target_join_missing |

## 1. 文獻結果與視覺化程式

### SPHERE-F01　Earlier spherical drop results have limited duration and selected extinction conditions

**Radiative extinction of gaseous spherical diffusion flames in microgravity__22df3ad78b**

2007會議稿的normal／inverse乙烯／丙烷在0.98 bar，刻意選在2.2秒內熄滅。這是相關短落塔前期證據，不是長時ACME飛行重複。

- 證據身份：related_older_microgravity_campaign。
- 文獻定位：GA-22df3ad78b88: physical1 abstract。
- 使用數據部分：source_id: GA-22df3ad78b88；locator: physical1 abstract；role: Sourceanalysisorboundedliteraturecontext;notindependentraw。
- 本組適用層級：direct_related_campaign_abstract；NoexactISSrunjoinclaimed.。
- 使用／控制因子：factor_and_role: normal/inverseC2H4/C3H8:streamroles；source_refs: source_id: GA-22df3ad78b88；locator: physical1 abstract；factor_and_role: 0.98bar:pressure；source_refs: source_id: GA-22df3ad78b88；locator: physical1 abstract；factor_and_role: 2.2sdrop:duration；source_refs: source_id: GA-22df3ad78b88；locator: physical1 abstract；factor_and_role: temperature/radiativefraction:sourceexperimentandmodelroles；source_refs: source_id: GA-22df3ad78b88；locator: physical1 abstract。
- 來源限制：Conference manuscript edition is not automatically the later journal article.；Source model temperature/radiation interpretations do not establish the same mechanism for all ISS mixtures.。
- 搜尋句（改寫）：The2007conference manuscript reports normal/inverseethylene/propane at.98bar, deliberately chosen to extinguish within2.2s. These unsteady short-drop flames are related pre-ISS evidence, not a long-duration ACME replicate.。
- 來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/02_論文全文/02_會議論文與預印本/Radiative extinction of gaseous spherical diffusion flames in microgravity__22df3ad78b.pdf>)
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/02_論文全文/02_會議論文與預印本/Radiative extinction of gaseous spherical diffusion flames in microgravity__22df3ad78b.pdf>)

尚未取得可逐項對照的紀錄。

## 2. 使用資料與參數總表的因子對照

尚未取得可逐項對照的紀錄。

以上是該 investigation 的欄位盤點；個別結論實際使用的因子以第1節與下列補充為準。

| 本組實際因子 | 總表定位／未列欄位 | 文獻中的用途 |
| --- | --- | --- |
| SPHERE-F01 / normal/inverseC2H4/C3H8:streamroles | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| SPHERE-F01 / 0.98bar:pressure | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| SPHERE-F01 / 2.2sdrop:duration | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |
| SPHERE-F01 / temperature/radiativefraction:sourceexperimentandmodelroles | 總表未明確列出同一量或角色；須由本項文獻定位／原資料補齊 | 不以相近名稱、點火位置、Tad或感測器增益替代。 |

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

尚未取得可逐項對照的紀錄。

## 缺件與適用範圍

- 目前不足兩項可適用的來源結論；尚未完成多結論比較，不以研究目的湊數。
