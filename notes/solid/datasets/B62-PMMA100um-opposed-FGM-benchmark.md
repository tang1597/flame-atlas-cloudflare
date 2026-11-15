# PSI62：100µmPMMA published-data模型比較

小資料集 ID：`B62-PMMA100um-opposed-FGM-benchmark`

## 資料身份與範圍

| 項目 | 內容 |
| --- | --- |
| NASA investigation | [PSI-62](https://psi.nasa.gov/physci/repo/data/investigations/PSI-62) |
| 材料／配方 | PMMA |
| 幾何 | 2cmwide100µmflatfilm |
| 實驗模式 | opposedspread: publishedNASAbenchmark, notnewflightdataset |
| 證據角色 | 既有固體資料再分析 |
| 環境 | ISS 微重力／來源指定的地面比較；逐次氣氛與流況不由材料名補值 |
| 資料粒度／共享試片 | 0 筆來源紀錄；獨立燃燒次數未自動確認；a/b、重複sample與階段保持原身份。 |
| 可用數值 | source_bound_observations_available |

## 1. 文獻結果與視覺化程式

### B62-BENCHMARK　B62-BENCHMARK

**Radiative flamelet generated manifolds for solid fuel flame spread in microgravity**

CR-FGM論文直接重用2cm寬100µm PMMA、20.6%O2的BASS延燒點，比對detailed2D及既有model；reference43可追到2017三regime論文，不是新flight實驗。

- 證據身份：direct_reanalysis_of_published_experiment。
- 文獻定位：bass-dffd07436b12: physicalpp10-12Sec2.6/Fig8; reference43physicalp28。
- 使用數據部分：literature_locator: physicalpp10-12Sec2.6/Fig8; reference43physicalp28；trial_binding: DirectFig8reuseofBASSIIpublicationRef43; individualrawBtrialbindingunknown；scope: 逐次索引為可用候選紀錄，不代表文獻使用其全部列。。
- 本組適用層級：同一BASS薄PMMA benchmark再分析／模型計算，非新增飛行量測。。
- 使用／控制因子：fuel_thickness_um: 100；width_cm: 2；farfield_O2_percent: 20.6。
- 來源限制：精確B-prefix rawtrialjoin未提供；Fig8有實驗波動範圍而非新置信區間。。
- 搜尋句（改寫）：CR-FGM論文直接重用2cm寬100µm PMMA、20.6%O2的BASS延燒點，比對detailed2D及既有model；reference43可追到2017三regime論文，不是新flight實驗。。
- 來源：https://doi.org/10.1016/j.combustflame.2023.112939
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/02_論文全文/01_期刊論文與作者稿/Radiative flamelet generated manifolds for solid fuel flame spread in microgravity (2023)__dffd07436b.pdf>)

### B62-MISMATCH　B62-MISMATCH

**Radiative flamelet generated manifolds for solid fuel flame spread in microgravity**

作者說model幾乎各case都過預測，kineticregime尤其明顯；transport與未解fullmomentum被列為可能原因，不當已證因果。

- 證據身份：source_model_vs_experiment_comparison。
- 文獻定位：bass-dffd07436b12: physicalp12Sec2.6/Fig8。
- 使用數據部分：literature_locator: physicalp12Sec2.6/Fig8；trial_binding: DirectFig8reuseofBASSIIpublicationRef43; individualrawBtrialbindingunknown；scope: 逐次索引為可用候選紀錄，不代表文獻使用其全部列。。
- 本組適用層級：同一BASS薄PMMA benchmark再分析／模型計算，非新增飛行量測。。
- 使用／控制因子：。
- 來源限制：未數位化Fig8，不另計R²或宣告達驗證門檻。。
- 搜尋句（改寫）：作者說model幾乎各case都過預測，kineticregime尤其明顯；transport與未解fullmomentum被列為可能原因，不當已證因果。。
- 來源：https://doi.org/10.1016/j.combustflame.2023.112939
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/02_論文全文/01_期刊論文與作者稿/Radiative flamelet generated manifolds for solid fuel flame spread in microgravity (2023)__dffd07436b.pdf>)

### B62-FGM-APRIORI　B62-FGM-APRIORI

**Radiative flamelet generated manifolds for solid fuel flame spread in microgravity**

CR-FGM對2D化學態的a-priori比較屬simulation-to-manifold，不等於所有空間點均有實驗溫度或species真值。

- 證據身份：source_model_to_model_comparison。
- 文獻定位：bass-dffd07436b12: physicalpp15-24Sections3/4。
- 使用數據部分：literature_locator: physicalpp15-24Sections3/4；trial_binding: DirectFig8reuseofBASSIIpublicationRef43; individualrawBtrialbindingunknown；scope: 逐次索引為可用候選紀錄，不代表文獻使用其全部列。。
- 本組適用層級：同一BASS薄PMMA benchmark再分析／模型計算，非新增飛行量測。。
- 使用／控制因子：。
- 來源限制：沒有找到可直接執行的作者solver/manifoldtables/codeexport。。
- 搜尋句（改寫）：CR-FGM對2D化學態的a-priori比較屬simulation-to-manifold，不等於所有空間點均有實驗溫度或species真值。。
- 來源：https://doi.org/10.1016/j.combustflame.2023.112939
- 本機來源：[開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/NASA_同事分享包_20261114/02_論文全文/01_期刊論文與作者稿/Radiative flamelet generated manifolds for solid fuel flame spread in microgravity (2023)__dffd07436b.pdf>)

| Model ID | 公式／預測量 | 展示程式 | 數值比較與限制 |
| --- | --- | --- | --- |
| SOLID-PMMA-THIN-THERMAL | Vf=(2.34e-8 m²/s)×F_adb/τ_half；F_adb=4.89；τ_half=t_full/2；BASS-II PMMA thin-sheet thermal limit | reproduce_solid_models.py · [開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/solid_combustion_evidence_20261115/models/reproduce_solid_models.py>) | runnable；固定原式前向比較（非獨立驗證）；Original numeric front-position/spread trajectories, exact trial IDs and per-point statistics；Case-specific proof of thermal-regime eligibility; low-flow radiation/high-flow kinetics are not modeled；F_adb and prefactor are fixed by source; no coefficient is estimated. Original numeric spread trajectories/trial IDs are missing. R2 N/A. |
| SOLID-PSI62-FGM-BLOCKED | PSI62 BASS flamelet/tomography model；PSI62 BASS flamelet/tomography model | reproduce_solid_models.py · [開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/solid_combustion_evidence_20261115/models/reproduce_solid_models.py>) | 目前未執行／尚未閉合；缺少完整輸入與對應目標；Exact solver/manifold version and chemistry/transport files；Matched simulation/experimental trial, fields and boundary conditions；No complete verified manifold, chemistry, transport, boundary bundle or compatible numeric target pair. A generic PDE is not a reproduced model. |

| 可開啟的圖／工具 | 身份與用途 |
| --- | --- |
| [開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/solid_combustion_evidence_20261115/models/comparison.html>) | 薄片熱控式與來源取點；PSI62僅共享benchmark參考，不是FGM重現 |
| [開啟檔案](<C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/solid_combustion_evidence_20261115/models/pmma_thin_model_vs_paper_observations.png>) | 固定物理公式與文獻圖上點比較 |

## 2. 使用資料與參數總表的因子對照

尚未取得可逐項對照的紀錄。

以上是該 investigation 的欄位盤點；個別結論實際使用的因子以第1節與下列補充為準。

| 本組實際因子 | 總表定位／未列欄位 | 文獻中的用途 |
| --- | --- | --- |
| 材料／配方／幾何 | '實驗總覽'!E14 | 文獻選樣身份；逐次厚度、支撐與歷史另由原文補齊 |
| 環境／流向／重力 | '實驗總覽'!F14 | 環境摘要，非本組全部逐次聯合條件 |
| 厚度、支撐、前緣位置／延燒速度與熱物性 | 需文獻／原始影像補欄位；本總表未提供全部閉合數值 | 選擇薄片／厚板／棒模型並核對同一observable |

| 文獻因子／疑點 | 正確讀法或需補資料 |
| --- | --- |
| 需補因子 | 燃料厚度/寬度/直徑、燒面/backing、模式、點火/預熱歷史需由原文/原始表逐項補；workbook不是完整聯合試驗條件。 |

## 3. 共用資料的多項結論比較

| 結論／文獻 | 資料重疊身份 | 共同處 | 不同處／不能合併之處 |
| --- | --- | --- | --- |
| B62-BENCHMARK；B62-MISMATCH；B62-FGM-APRIORI | 直接再用BASS/2017薄PMMA benchmark，不是新飛行試驗 | 同一延燒observable可用不同熱化學／傳輸模型比較。 | FGM作者指出速度過預測，尤其動力學區；manifold對詳細化學的比較是simulation-to-simulation，不能取代實驗真值。 |

## 4. 消防洞見

| 類別 | 對應證據 | 數據支持的判斷 | 策略／產品構想 | 待驗證 |
| --- | --- | --- | --- | --- |
| 預防 | B62-BENCHMARK；B62-MISMATCH | 來源包含不同受熱面／模型過預測或來源分析差異，不能以同材料名選任一預測器。 | 模型選擇先匹配幾何、受熱面、observable與試次身份。 | 補原始前緣軌跡及可執行原模型邊界條件，再作盲測。 |
| 偵測 | 尚未取得／不適用 | 尚未建立本組可直接支持此用途的數據結論。 | 先補對應資料與試次匹配，再決定可測試策略；此處是研究缺口。 | 需本組材料、幾何、操作歷史與對應端點的量測；相近系列不能代替。 |
| 撲滅／抑制 | 尚未取得／不適用 | 尚未建立本組可直接支持此用途的數據結論。 | 先補對應資料與試次匹配，再決定可測試策略；此處是研究缺口。 | 需本組材料、幾何、操作歷史與對應端點的量測；相近系列不能代替。 |

## 逐次索引

尚未取得可逐項對照的紀錄。

## 缺件與適用範圍

- PSI62下載目錄只有metadatazip；沒有可執行原作者solver/FGMtables。
