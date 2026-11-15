# PSI-117 / n-dodecane / PROCI_2023_C12_Extinction_Diameter_vs_pressure / Model

`PSI117-PROCI_2023_C12_Extinction_Diameter_vs_pressure-n-dodecane-Model`

## 資料身分與可追溯範圍

- 類別：source analyzed figure/curve block; simulation output；作者已計算的source numerical output，不是本輪forward或原始量測。
- 觀測單位是各曲線點／來源分析block，原始physical test-ID與獨立burn分母均Unknown；多個series不能加算成獨立試次。
- 本分支source series：`PSI117-PROCI_2023_C12_Extinction_Diameter_vs_pressure-Model_hot`, `PSI117-PROCI_2023_C12_Extinction_Diameter_vs_pressure-Model_cool`。
- **來源檔：** `C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\補下載\PSI-117\Analyzed Data\112192ecaa82caf6_PSI-117_Analyzed Data_PROCI_2023_C12_Extinction_Diameter_vs_pressure.csv`
- **SHA256：** `4ab6f8c19f40a3349096eab8bdceb0a62611020af15e63f816922b149cfa7001`
- **原始儲存／版本：** `supplement_20261113/01_PSI/PSI-117/Analyzed Data/112192ecaa82caf6_PSI-117_Analyzed Data_PROCI_2023_C12_Extinction_Diameter_vs_pressure.csv`；source identity=`psi:PSI-117|psi-data/PSI-117/Analyzed Data/PSI-117_Analyzed Data_PROCI_2023_C12_Extinction_Diameter_vs_pressure.csv|1`；version=`None`。
- **NASA／DOI：** https://psi-repo-prod.s3.amazonaws.com/psi-data/PSI-117/Analyzed%20Data/PSI-117_Analyzed%20Data_PROCI_2023_C12_Extinction_Diameter_vs_pressure.csv；DOI=此file registry未列；下方文獻ReadMe另列。
- ReadMe：`C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\補下載\PSI-117\Analyzed Data\72c51a58b2632547_PSI-117_Analyzed Data_ReadMe_List_of_Data.xlsx`；SHA256 `a84c138d22545ba9f59c4aa336710741dd48cf3c27823124ed04ac8f91a5f4a0`；`Sheet1!B10:K10`；對應https://doi.org/10.1016/j.proci.2022.07.094 / Fig. 7。
- ReadMe原值：fuel=n-dodecane；D0(mm)=4；P(atm)=0.5 - 3.0；XO2=0.21；XN2=0.79；第三物種=None。這是來源條件，不補成逐次實測。

## 文獻結果與視覺化程式

| 結論 ID | 文獻／頁或圖 | 結果與端點 | 使用的資料子集 | 公式／參數來源 | 展示程式 | 證據角色 |
|---|---|---|---|---|---|---|
| C01 | https://doi.org/10.1016/j.proci.2022.07.094；Fig. 7；CSV D/E rows 2–6 | Model_hot：raw numeric pairs=5；source pairs after point-specific censor=5；remaining source x=0.5–3 atm；remaining source y=3.43–3.94 mm | `PSI117-PROCI_2023_C12_Extinction_Diameter_vs_pressure-Model_hot`；censor/units見下方audit | 來源作者已計算output，不新fit | prepare_visualization.py → viewer.js；permission=`units_verified_comparative_not_exact_matched` | literature_model_generated；不是安全閾值或獨立驗證 |
| C02 | https://doi.org/10.1016/j.proci.2022.07.094；Fig. 7；CSV J/K rows 2–6 | Model_cool：raw numeric pairs=5；source pairs after point-specific censor=5；remaining source x=0.5–3 atm；remaining source y=0.03–1.19 mm | `PSI117-PROCI_2023_C12_Extinction_Diameter_vs_pressure-Model_cool`；censor/units見下方audit | 來源作者已計算output，不新fit | prepare_visualization.py → viewer.js；permission=`units_verified_comparative_not_exact_matched` | literature_model_generated；不是安全閾值或獨立驗證 |
| C03 | ReadMe file-specific row；原CSV各block | 同一表裡實驗與模型各自有x坐標；不同P／time row不作paired trial | 同table跨分支 | 不插值、不新fit、不拿K當分子D | prepare_visualization.py保留source axes | **comparison／identifiability限制，非物理結果** |
| C04 | 原欄定義／待綁primary方法 | 光學Df、D_OHm、D_Tmax、Tmax與Ddrop不是同一邊界／溫度角色 | 同table多quantity | Tmax是模型量時不叫thermometry；radiance W不當W/m² heatflux | 分量／分角色顯示 | **量測／模型定義，非新物理結果** |

### 真實程式與展示範圍

- [physics_models.py](</C:/Users/User/Documents/ChatGPT/Nasa Hackathon/research/liquid_combustion/physics_models.py>)：`d2_history`只用明示D0²/K做條件重建；`classical_burning_constant`需要匹配物性與氧質量分率；`cool_stage_rate`含effective NTC參數，不是測得火焰溫度。
- [prepare_visualization.py](</C:/Users/User/Documents/ChatGPT/Nasa Hackathon/research/liquid_combustion/prepare_visualization.py>)：保留各source block的x軸與實驗／來源模型角色；重播已發表數值，不是執行作者原solver。
- [web/viewer.js](</C:/Users/User/Documents/ChatGPT/Nasa Hackathon/research/liquid_combustion/web/viewer.js>)；入口 [http://127.0.0.1:8808/](http://127.0.0.1:8808/)。
- 目前入口有source case `PSI117-PROCI_2023_C12_Extinction_Diameter_vs_pressure`，請由case選單選取；不宣稱URL有未實作的case deep link。
- 本文件產出沒有fit/train、反推係數或重跑作者模型；輸入缺件時不生成理論數值。

### Series級單位與端點審核

[unit_audit.json](</C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/literature/unit_audit.json>)；SHA256 `d0804a6fd04a7847e3e55743968237a58e2dbcc31d24a68dc7ed0a7a2e422a45`；input fixture SHA=cff6dbbfd8b8f3313eed3f300416a61e33faebbbc0acda99e9faa68ff1655fd7。以下是獨立display overlay，不改原header／值。

| Series | raw units → display units | plot permission | quantity／source evidence |
|---|---|---|---|
| `PSI117-PROCI_2023_C12_Extinction_Diameter_vs_pressure-Model_hot` | atm / Unknown / 未核 → atm / mm | `units_verified_comparative_not_exact_matched` | liquid droplet diameter at hot/cool extinction, not flame-envelope diameter；source PSI117-EXTDECK2022 physical pages [15]；SHA 2fe2fc85aa8ee3ac99a07495d31c49704f32d42bb83ae2ba2481d47c14407c43 |

- 單位來源：`C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\03_其他文件\簡報與海報\第一批下載\PSI-117_research\Presentations\PSI-117_Presentations_Extinction_Characteristics_TFarouk.pdf`；SHA256 `2fe2fc85aa8ee3ac99a07495d31c49704f32d42bb83ae2ba2481d47c14407c43`；physical pages [15]。
| `PSI117-PROCI_2023_C12_Extinction_Diameter_vs_pressure-Model_cool` | atm / Unknown / 未核 → atm / mm | `units_verified_comparative_not_exact_matched` | liquid droplet diameter at hot/cool extinction, not flame-envelope diameter；source PSI117-EXTDECK2022 physical pages [15]；SHA 2fe2fc85aa8ee3ac99a07495d31c49704f32d42bb83ae2ba2481d47c14407c43 |

- 單位來源：`C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\03_其他文件\簡報與海報\第一批下載\PSI-117_research\Presentations\PSI-117_Presentations_Extinction_Characteristics_TFarouk.pdf`；SHA256 `2fe2fc85aa8ee3ac99a07495d31c49704f32d42bb83ae2ba2481d47c14407c43`；physical pages [15]。

- **Point note — Model_cool：** source cells `J6, K6`，x=3，raw y=0.03；actual archived Model_cool value is 0.03, not the Experiment_cool zero; do not apply experimental censor to this value。

- 只對明確source-confirmed的Experiment_cool G7/H7原始0套censor；Model_cool J6/K6=0.03保留，其餘zero沒有全域censor規則。
- Errorbar+／−欄的bound／offset意義與confidence level尚Unknown；不是獨立試次或已校準PI。

### 最終CFI／PSI117文獻binding（保留review程度）

專項receipt：[cfi_literature.json](</C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/literature/cfi_literature.json>)；SHA256 `87d764f52cb27ffea8c7889aa71746057f0cacbd1dfe8a82f72328f55135b403`。這些是文獻來源與適用範圍，未取得exact archived test mapping者不提升成same-data。

- **PSI117-EXT2023 — Extinction characteristics of isolated n-alkane fuel droplets during low temperature cool flame burning in air**；DOI/NTRS=10.1016/j.proci.2022.07.094；官方URL=https://www.sciencedirect.com/science/article/abs/pii/S1540748922001134。
  - review狀態=`primary_abstract_or_metadata_reviewed_fulltext_not_obtained`；physical pages=[]；edition SHA=None；local source `未取得local全文`。
  - dataset mapping=`ReadMe_tables_and_figures_only`；trial IDs=None。
- **PSI117-EXTDECK2022 — Extinction characteristics of isolated n-alkane fuel droplets during low temperature cool flame droplet burning in air**；DOI/NTRS=Unknown；官方URL=https://psi.nasa.gov/physci/repo/data/investigations/PSI-117。
  - review狀態=`18slide_text_and_p9_p15_axes_visually_verified`；physical pages=[1, 2, 7, 8, 9, 11, 15, 16]；edition SHA=2fe2fc85aa8ee3ac99a07495d31c49704f32d42bb83ae2ba2481d47c14407c43；local source `C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\03_其他文件\簡報與海報\第一批下載\PSI-117_research\Presentations\PSI-117_Presentations_Extinction_Characteristics_TFarouk.pdf`。
  - dataset mapping=`unknown`；trial IDs=None。
- 未取得全文者只依receipt明示的primary abstract／captions／metadata範圍；不把slide、conference與journal版混成同一edition。
- 沒有複製英文直接引句；維持既有quote ledger。

## 因子與試驗目的

本節引用使用者Excel `C:\Users\User\Downloads\NASA_實驗目的_燃料_環境_物理參數總表_20261114.xlsx`，SHA256 `fac357147ff98acf3a2f76b2ddd88d2fbab9a500159cc5ca360bb2d3a236dae1`。來源分類是前一輪表頭盤點，不能直接升格為逐次校準量測或科學因果角色；原公式/cache未重算。

| 因子 | Excel sheet／cell與原表欄 | 單位與定義 | 操縱／控制／應變／未確立 | 結論使用方式 |
|---|---|---|---|---|
| 壓力 | `物理參數!C454:I454`；G454=`Pressure`；原定位 `line 1, column 2` | E454=未由欄名確認；原分類D454=模擬／實驗並列表，須按欄位區分 | 環境初始／設定條件；原摘要之absolute ambient已核時才使用；單一欄名不能證明因果操縱。 | 僅供結論來源／條件核對；未建立數值trial join |
| 尺寸／幾何 | `物理參數!C455:I455`；G455=`Diameter(mm)；D (mm)；do (mm)`；原定位 `line 1, column 2` | E455=mm；原分類D455=模擬／實驗並列表，須按欄位區分 | 逐欄核對硬體、液滴、座標、指令的角色；不可generic diameter。 | 僅供結論來源／條件核對；未建立數值trial join |
| 氧濃度 | `物理參數!C456:I456`；G456=`XO2`；原定位 `Sheet1!R1C5` | E456=未由欄名確認；原分類D456=模擬／實驗並列表，須按欄位區分 | 初始氣氛或列舉配方選項；各物種basis/scope分開。 | 僅供結論來源／條件核對；未建立數值trial join |
| 液滴直徑／面積 | `物理參數!C457:I457`；G457=`d^2 (mm^2)`；原定位 `line 1, column 3` | E457=mm^2；原分類D457=模擬／實驗並列表，須按欄位區分 | D0是初始狀態；D(t)、熄滅D與影像面積是應變／來源影像分析；不是火焰尺寸。 | 僅供結論來源／條件核對；未建立數值trial join |
| 溫度 | `物理參數!C458:I458`；G458=`T_max(K)`；原定位 `line 1, column 4` | E458=K；原分類D458=模擬／實驗並列表，須按欄位區分 | 環境氣體、初始液體、火焰／表面、點火器與property reference分開；儀器時序不是溫度。 | 僅供結論來源／條件核對；未建立數值trial join |
| 火焰幾何／延燒 | `物理參數!C459:I459`；G459=`dflame (mm)；df (mm)；Dflame (mm)；Dflame(mm)`；原定位 `line 1, column 6` | E459=mm；原分類D459=模擬／實驗並列表，須按欄位區分 | 來源定義的光學或模型邊界應變；不等於液滴或熱通量。 | 僅供結論來源／條件核對；未建立數值trial join |
| 火焰幾何／延燒 | `物理參數!C460:I460`；G460=`D_OHm/D_drop；Dflame/Dodrop`；原定位 `line 1, column 6` | E460=未由欄名確認；原分類D460=模擬／實驗並列表，須按欄位區分 | 來源定義的光學或模型邊界應變；不等於液滴或熱通量。 | 僅供結論來源／條件核對；未建立數值trial join |
| 燃燒率／燃燒常數 | `物理參數!C461:I461`；G461=`kb (mm2/s)`；原定位 `line 1, column 7` | E461=mm2/s；原分類D461=模擬／實驗並列表，須按欄位區分 | 來源分析／擬合後的D²應變量；不是O2分子擴散係數或獨立輸入。 | 僅供結論來源／條件核對；未建立數值trial join |
| 燃燒率／燃燒常數 | `物理參數!C462:I462`；G462=`K(mm^2/sec)`；原定位 `line 1, column 3` | E462=mm^2/sec；原分類D462=模擬／實驗並列表，須按欄位區分 | 來源分析／擬合後的D²應變量；不是O2分子擴散係數或獨立輸入。 | 僅供結論來源／條件核對；未建立數值trial join |
| 燃燒率／燃燒常數 | `物理參數!C463:I463`；G463=`Kavg_CF`；原定位 `line 1, column 3` | E463=未由欄名確認；原分類D463=模擬／實驗並列表，須按欄位區分 | 來源分析／擬合後的D²應變量；不是O2分子擴散係數或獨立輸入。 | 僅供結論來源／條件核對；未建立數值trial join |

- 每列原檔路徑在Excel H欄、原欄位／定位在G/I欄；完整列與source SHA見 [factor_crosswalk.json](</C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/data_inventory/factor_crosswalk.json>)。
- 每個原欄名的存在不證明是操縱變因；是否controlled必須在匹配試次／protocol中另核。`microgravity`不填成精確g=0；缺失T、g或U保留Unknown。

## 多結論比較

- **共同結論：** source表用不同quantity描述液滴縮減、光學／化學／熱場位置與相位端點；這些量可以並列研究，但不能互換定義。
- **不同結論：** 每條source series保留原x／y units、原列與block；表內Experiment/Model的壓力、時間網格、D0和邊界定義未必匹配。
- **是否使用相同資料：** 同一CSV內是exact source-table subsets；對物理burn／其他論文仍為shared_investigation_unjoined或Unknown。ReadMe給fuel／figure不是exact trial-ID。
- **衝突或未解差異：** 單位按unit audit分已核與仍null；未提供的方程／solver／property state保持Unknown，不暗補常數或做自選配對。

## 消防洞見

| 預防／偵測／撲滅 | 洞見 | 依據結論 | 直接支持或新增假說 | 缺少的判別實驗 |
|---|---|---|---|---|
| 預防 | 本分支可用來檢查「相同燃料名稱是否仍有不同初始狀態／輸運」；不由source-model低殘差宣告材料或艙體安全。 | C01等source curves | 作者數值／比較範圍；策略為物理假說 | exact run、溫度／成分、幾何／fiber／history匹配，獨立量測 |
| 偵測 | Df、radiance與Tmax或OH位置須各自標角色；模型Tmax與光學變暗不能直接當實測氣體溫度／火警漏報。 | 各quantity與定義限制 | 物理可觀測性邊界；尚非感測器qualification | 同步光譜／熱／物種與實際alarm channels、校準與誤差預算 |
| 撲滅／抑制 | 若來源涉及hot/cool transition，須追殘餘液體與後續反應；此table不提供藥劑注入量、抑制成功率或再燃概率。 | source endpoint／model branches | 持續燃燒監測為新增假說，無設備效能證明 | 明示intervention時序、全相位耗氧／溫度／物種與reignition labels |

## 資料缺口與文獻覆蓋

- 原檔raw strings／空白／重複點與series cells都在 [visualization_data.json](</C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/data_inventory/visualization_data.json>)；沒有以平滑圖替換原資料。
- 作者完整輸入檔、化學機構／熱力／transport／radiation資產及逐次初始場未由這份CSV提供；本地程式僅重播source output。
- 具體paper title／版本／物理頁與formula核對以專項文獻receipt為準；metadata關聯不能當已全文核對。
- CFI／PSI117文獻補充：[cfi_literature.json](</C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/literature/cfi_literature.json>)。本葉節點仍只採本次明列的來源row/series，新增source record本身不建立exact trial join。
- 不把所有PSI117資料都標為同一OpenFOAM solver；每篇模型、燃料與版本需要各自primary source binding。
- 數值與原始路徑留離線，不改原始JSON／資料／程式／live服務。
