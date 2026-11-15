# PSI-117 / n-dodecane / PROCI_C12_2019_Three_Stage / Experiment_or_comparison

`PSI117-PROCI_C12_2019_Three_Stage-n-dodecane-Experiment_or_comparison`

## 資料身分與可追溯範圍

- 類別：source analyzed figure/curve block; experimental comparison or reported uncertainty block；來源已分析的實驗比較／界限曲線，不是新取點的raw measurements。
- 觀測單位是各曲線點／來源分析block，原始physical test-ID與獨立burn分母均Unknown；多個series不能加算成獨立試次。
- 本分支source series：`PSI117-PROCI_C12_2019_Three_Stage-Experiment_normalized_D2`, `PSI117-PROCI_C12_2019_Three_Stage-Experiment_normalized_flame_diameter`, `PSI117-PROCI_C12_2019_Three_Stage-Experiment_flame_diameter`, `PSI117-PROCI_C12_2019_Three_Stage-Experiment_radiance_I`, `PSI117-PROCI_C12_2019_Three_Stage-Experiment_radiance_II`, `PSI117-PROCI_C12_2019_Three_Stage-Experiment_cool_diameter_HWFM`, `PSI117-PROCI_C12_2019_Three_Stage-Experiment_cool_diameter_peak_peak`。
- **來源檔：** `C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\補下載\PSI-117\Analyzed Data\be4a795d96c94a1e_PSI-117_Analyzed Data_PROCI_C12_2019_Three_Stage.csv`
- **SHA256：** `0e7c8c7e9ea35bd139ba52c9f2118724b8cc9f251d82b9222adf03cb67317809`
- **原始儲存／版本：** `supplement_20261113/01_PSI/PSI-117/Analyzed Data/be4a795d96c94a1e_PSI-117_Analyzed Data_PROCI_C12_2019_Three_Stage.csv`；source identity=`psi:PSI-117|psi-data/PSI-117/Analyzed Data/PSI-117_Analyzed Data_PROCI_C12_2019_Three_Stage.csv|1`；version=`None`。
- **NASA／DOI：** https://psi-repo-prod.s3.amazonaws.com/psi-data/PSI-117/Analyzed%20Data/PSI-117_Analyzed%20Data_PROCI_C12_2019_Three_Stage.csv；DOI=此file registry未列；下方文獻ReadMe另列。
- ReadMe：`C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\補下載\PSI-117\Analyzed Data\72c51a58b2632547_PSI-117_Analyzed Data_ReadMe_List_of_Data.xlsx`；SHA256 `a84c138d22545ba9f59c4aa336710741dd48cf3c27823124ed04ac8f91a5f4a0`；`Sheet1!B6:K6`；對應https://doi.org/10.1016/j.proci.2018.09.015 / Fig. 7。
- ReadMe原值：fuel=n-dodecane；D0(mm)=4.5；P(atm)=2.75；XO2=0.21；XN2=0.5；第三物種=0.29。這是來源條件，不補成逐次實測。
- **強制配方／來源警示：** inventory／ReadMe將此table描述為C12、D0=4.5mm、P=2.75atm；primary paper的數值示例為C7／3atm，對照量測為FLEX1268的C12／2.75atm。來源published comparison可以保留，但這份CSV每條curve的精確provenance尚待綁定；本標題中的fuel label是ReadMe身份，**不能用來宣告此Model分支已驗證為C12／OpenFOAM或同條件驗證**。

## 文獻結果與視覺化程式

| 結論 ID | 文獻／頁或圖 | 結果與端點 | 使用的資料子集 | 公式／參數來源 | 展示程式 | 證據角色 |
|---|---|---|---|---|---|---|
| C01 | https://doi.org/10.1016/j.proci.2018.09.015；Fig. 7；CSV B/C rows 2–206 | Experiment_normalized_D2：raw numeric pairs=205；source pairs after point-specific censor=205；remaining source x=-0.200806–1.85565 s/mm2；remaining source y=0.00966184–0.997585 1 | `PSI117-PROCI_C12_2019_Three_Stage-Experiment_normalized_D2`；censor/units見下方audit | 來源experiment／comparison／bound block，不新fit | prepare_visualization.py → viewer.js；permission=`known_units_only` | source_experimental_comparison_block；不是安全閾值或獨立驗證 |
| C02 | https://doi.org/10.1016/j.proci.2018.09.015；Fig. 7；CSV F/G rows 2–138 | Experiment_normalized_flame_diameter：raw numeric pairs=137；source pairs after point-specific censor=137；remaining source x=0.00724638–0.425121 s/mm2；remaining source y=-0.157895–23.7895 1 | `PSI117-PROCI_C12_2019_Three_Stage-Experiment_normalized_flame_diameter`；censor/units見下方audit | 來源experiment／comparison／bound block，不新fit | prepare_visualization.py → viewer.js；permission=`known_units_only` | source_experimental_comparison_block；不是安全閾值或獨立驗證 |
| C03 | https://doi.org/10.1016/j.proci.2018.09.015；Fig. 7；CSV I/J rows 2–94 | Experiment_flame_diameter：raw numeric pairs=93；source pairs after point-specific censor=93；remaining source x=0.00241546–0.422705 s/mm2；remaining source y=-0.0526316–5.42105 mm | `PSI117-PROCI_C12_2019_Three_Stage-Experiment_flame_diameter`；censor/units見下方audit | 來源experiment／comparison／bound block，不新fit | prepare_visualization.py → viewer.js；permission=`known_units_only` | source_experimental_comparison_block；不是安全閾值或獨立驗證 |
| C04 | https://doi.org/10.1016/j.proci.2018.09.015；Fig. 7；CSV M/N rows 2–364 | Experiment_radiance_I：raw numeric pairs=363；source pairs after point-specific censor=363；remaining source x=-0.195652–2.00725 s/mm2；remaining source y=1.84979–62.8182 W | `PSI117-PROCI_C12_2019_Three_Stage-Experiment_radiance_I`；censor/units見下方audit | 來源experiment／comparison／bound block，不新fit | prepare_visualization.py → viewer.js；permission=`known_units_only` | source_experimental_comparison_block；不是安全閾值或獨立驗證 |
| C05 | https://doi.org/10.1016/j.proci.2018.09.015；Fig. 7；CSV Q/R rows 2–225 | Experiment_radiance_II：raw numeric pairs=224；source pairs after point-specific censor=224；remaining source x=-0.099839–1.99678 s/mm2；remaining source y=0.987816–26.391 W | `PSI117-PROCI_C12_2019_Three_Stage-Experiment_radiance_II`；censor/units見下方audit | 來源experiment／comparison／bound block，不新fit | prepare_visualization.py → viewer.js；permission=`known_units_only` | source_experimental_comparison_block；不是安全閾值或獨立驗證 |
| C06 | https://doi.org/10.1016/j.proci.2018.09.015；Fig. 7；CSV U/V rows 2–119 | Experiment_cool_diameter_HWFM：raw numeric pairs=118；source pairs after point-specific censor=118；remaining source x=0.431562–1.54589 s/mm2；remaining source y=0–33.4256 Unknown / 未核 | `PSI117-PROCI_C12_2019_Three_Stage-Experiment_cool_diameter_HWFM`；censor/units見下方audit | 來源experiment／comparison／bound block，不新fit | prepare_visualization.py → viewer.js；permission=`blocked_pending_missing_units` | source_experimental_comparison_block；不是安全閾值或獨立驗證 |
| C07 | https://doi.org/10.1016/j.proci.2018.09.015；Fig. 7；CSV X/Y rows 2–159 | Experiment_cool_diameter_peak_peak：raw numeric pairs=158；source pairs after point-specific censor=158；remaining source x=0.434783–1.5781 s/mm2；remaining source y=-0.121107–19.8616 Unknown / 未核 | `PSI117-PROCI_C12_2019_Three_Stage-Experiment_cool_diameter_peak_peak`；censor/units見下方audit | 來源experiment／comparison／bound block，不新fit | prepare_visualization.py → viewer.js；permission=`blocked_pending_missing_units` | source_experimental_comparison_block；不是安全閾值或獨立驗證 |
| C08 | ReadMe file-specific row；原CSV各block | 同一表裡實驗與模型各自有x坐標；不同P／time row不作paired trial | 同table跨分支 | 不插值、不新fit、不拿K當分子D | prepare_visualization.py保留source axes | **comparison／identifiability限制，非物理結果** |
| C09 | 原欄定義／待綁primary方法 | 光學Df、D_OHm、D_Tmax、Tmax與Ddrop不是同一邊界／溫度角色 | 同table多quantity | Tmax是模型量時不叫thermometry；radiance W不當W/m² heatflux | 分量／分角色顯示 | **量測／模型定義，非新物理結果** |

### 真實程式與展示範圍

- [physics_models.py](</C:/Users/User/Documents/ChatGPT/Nasa Hackathon/research/liquid_combustion/physics_models.py>)：`d2_history`只用明示D0²/K做條件重建；`classical_burning_constant`需要匹配物性與氧質量分率；`cool_stage_rate`含effective NTC參數，不是測得火焰溫度。
- [prepare_visualization.py](</C:/Users/User/Documents/ChatGPT/Nasa Hackathon/research/liquid_combustion/prepare_visualization.py>)：保留各source block的x軸與實驗／來源模型角色；重播已發表數值，不是執行作者原solver。
- [web/viewer.js](</C:/Users/User/Documents/ChatGPT/Nasa Hackathon/research/liquid_combustion/web/viewer.js>)；入口 [http://127.0.0.1:8808/](http://127.0.0.1:8808/)。
- 目前入口有source case `PSI117-PROCI_C12_2019_Three_Stage`，請由case選單選取；不宣稱URL有未實作的case deep link。
- 本文件產出沒有fit/train、反推係數或重跑作者模型；輸入缺件時不生成理論數值。

### Series級單位與端點審核

[unit_audit.json](</C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/literature/unit_audit.json>)；SHA256 `d0804a6fd04a7847e3e55743968237a58e2dbcc31d24a68dc7ed0a7a2e422a45`；input fixture SHA=cff6dbbfd8b8f3313eed3f300416a61e33faebbbc0acda99e9faa68ff1655fd7。以下是獨立display overlay，不改原header／值。

| Series | raw units → display units | plot permission | quantity／source evidence |
|---|---|---|---|
| `PSI117-PROCI_C12_2019_Three_Stage-Experiment_normalized_D2` | s/mm2 / 1 → s/mm2 / 1 | `known_units_only` | (D/Do)2；此source block未有新primary unit證據；null仍Unknown |
| `PSI117-PROCI_C12_2019_Three_Stage-Experiment_normalized_flame_diameter` | s/mm2 / 1 → s/mm2 / 1 | `known_units_only` | Dflame/Dodrop；此source block未有新primary unit證據；null仍Unknown |
| `PSI117-PROCI_C12_2019_Three_Stage-Experiment_flame_diameter` | s/mm2 / mm → s/mm2 / mm | `known_units_only` | Dflame (mm)；此source block未有新primary unit證據；null仍Unknown |
| `PSI117-PROCI_C12_2019_Three_Stage-Experiment_radiance_I` | s/mm2 / W → s/mm2 / W | `known_units_only` | Flame Radiance (W)；此source block未有新primary unit證據；null仍Unknown |
| `PSI117-PROCI_C12_2019_Three_Stage-Experiment_radiance_II` | s/mm2 / W → s/mm2 / W | `known_units_only` | Flame Radiance (W)；此source block未有新primary unit證據；null仍Unknown |
| `PSI117-PROCI_C12_2019_Three_Stage-Experiment_cool_diameter_HWFM` | s/mm2 / Unknown / 未核 → s/mm2 / Unknown / 未核 | `blocked_pending_missing_units` | cool-flame spatial emission-profile diameter using source HWFM or peak-to-peak definition; not liquid droplet extinction diameter；此source block未有新primary unit證據；null仍Unknown |
| `PSI117-PROCI_C12_2019_Three_Stage-Experiment_cool_diameter_peak_peak` | s/mm2 / Unknown / 未核 → s/mm2 / Unknown / 未核 | `blocked_pending_missing_units` | cool-flame spatial emission-profile diameter using source HWFM or peak-to-peak definition; not liquid droplet extinction diameter；此source block未有新primary unit證據；null仍Unknown |

- 只對明確source-confirmed的Experiment_cool G7/H7原始0套censor；Model_cool J6/K6=0.03保留，其餘zero沒有全域censor規則。
- Errorbar+／−欄的bound／offset意義與confidence level尚Unknown；不是獨立試次或已校準PI。

### 最終CFI／PSI117文獻binding（保留review程度）

專項receipt：[cfi_literature.json](</C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/literature/cfi_literature.json>)；SHA256 `87d764f52cb27ffea8c7889aa71746057f0cacbd1dfe8a82f72328f55135b403`。這些是文獻來源與適用範圍，未取得exact archived test mapping者不提升成same-data。

- **PSI117-THREE2019 — Three stage cool flame droplet burning behavior of n-alkane droplets at elevated pressure conditions: Hot, warm and cool flame**；DOI/NTRS=10.1016/j.proci.2018.09.015；官方URL=https://www.sciencedirect.com/science/article/abs/pii/S1540748918306205。
  - review狀態=`primary_abstract_or_metadata_reviewed_fulltext_not_obtained`；physical pages=[]；edition SHA=None；local source `未取得local全文`。
  - dataset mapping=`source_comparative_not_exact_test`；trial IDs=None。
- **PSI117-THREEDECK2018 — Three Stage Cool Flame Droplet Burning Behavior of n-Alkane Droplets at Elevated Pressure Conditions: Hot, Warm and Cool Flame**；DOI/NTRS=Unknown；官方URL=https://psi.nasa.gov/physci/repo/data/investigations/PSI-117。
  - review狀態=`22slide_text_reviewed`；physical pages=[1, 7, 8, 9, 10, 15, 16, 21, 22]；edition SHA=99b341840ed423878c622478b3b7817729d0ccf4d772f407f860a91d66972917；local source `C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\03_其他文件\簡報與海報\補下載\PSI-117\Presentations\17a57c65bf1e1624_PSI-117_Presentations_Three_Stage_Cool_Flame_TFarouk.pdf`。
  - dataset mapping=`named_slide_tests_not_exact_model_match`；trial IDs=['FLEX1268', 'FLEX1256']。
- **CFI-REPORT2020 — Cool Flame Investigation (CFI): Science Final Report**；DOI/NTRS=Unknown；官方URL=https://psi.ndc.nasa.gov/mpglobal/api/athena/file/9919378/?inline=1&log=1。
  - review狀態=`all_13_physical_pages_text_reviewed`；physical pages=[1, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13]；edition SHA=e15158689180314583917200a071730d3aed9088e1ae689b847bd416674010f9；local source `C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\03_其他文件\研究報告與書章\第一批下載\PSI-39_CFI\Reports\PSI-39_Reports_CFI Science Final Report.pdf`。
  - dataset mapping=`source_campaign_ranges_not_exact_row_join`；trial IDs=None。
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
- **衝突或未解差異：** C12ReadMe與C7／3atm數值示例、C12FLEX1268／2.75atm量測分開；curve provenance pending。

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
