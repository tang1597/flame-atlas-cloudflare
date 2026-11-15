# RELATED PSI-142 / data ID 1 / cool diffusion flame extinction limits, no ozone

`RELATED-PSI142-data-ID-1`

## 資料身分與可追溯範圍

- **RELATED機制資料，不是核心液態／液滴physical trials。** 濃縮／室溫可液化燃料名稱不證明此裝置以液滴或液相供應；ground counterflow／premixed architecture與ISS MDCA分開。
- 觀測單位是來源圖表點、空間profile或limit series；numeric-bearing rows=41；工作表dimensions=[53, 5]；verified independent tests=Unknown，不加進564列。
- **來源檔：** `C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\補下載\PSI-142\Analyzed Data\6dbe702e6abad060_PSI-142_Analyzed Data_PSI data summary Princeton with links.xlsx`
- **SHA256：** `b6324538ff12cc07061bd0931dfc3e1cd458cd2eee4747c477c728791aca2ee0`
- **原始儲存／版本：** `supplement_20261113/01_PSI/PSI-142/Analyzed Data/6dbe702e6abad060_PSI-142_Analyzed Data_PSI data summary Princeton with links.xlsx`；source identity=`psi:PSI-142|psi-data/PSI-142/Analyzed Data/PSI-142_Analyzed Data_PSI data summary Princeton with links.xlsx|1`；version=`None`。
- **NASA／DOI：** https://psi-curation-prod.s3.amazonaws.com/legacy/Filestreamdb/116733/PSI%20data%20summary%20Princeton%20with%20links.xlsx；DOI=10.60555/80qf-vj95。
- 文獻索引：`data summary!B4:E4` → C.B. Reuter et al. / Combustion and Flame 179 (2017) 23–32；Figure 4；cool diffusion flame extinction limits, no ozone。這是source workbook索引，非本輪已讀該全文的聲明。
- 主要worksheet標籤：`C4`=nC14; `D4`=Yf; `E4`=aCFE (1/s); `C13`=nC12; `D13`=Yf; `E13`=aCFE (1/s); `C23`=nC10; `D23`=Yf; `E23`=aCFE (1/s); `C33`=nC8; `D33`=Yf; `E33`=aCFE (1/s); `C43`=nC7; `D43`=Yf; `E43`=aCFE (1/s)。

## 文獻結果與視覺化程式

| 結論 ID | 文獻／頁或圖 | 結果與端點 | 使用的資料子集 | 公式／參數來源 | 展示程式 | 證據角色 |
|---|---|---|---|---|---|---|
| C01 | data summary指定Figure 4；data ID 1 D/E多燃料block | 來源aCFE值有41個finite點；範圍42.97–129.66 s⁻¹ | 各fuel block原儲存格，不視為相同試次 | strain-limit來源response；Yf的basis須全文核 | 目前沒有PSI142 viewer case | **source-reported limit points**；非液滴Y |
| C02 | DataID1/2/3的workbook descriptions | 無ozone與cool diffusion端點不同；不能直接合併成通用滅火濃度 | 同物理workbook但原實驗對照ID未join | 需混合／溫度／噴口間距／strain定義 | 不生成placeholder曲線 | **endpoint定義／可比性限制** |

### 真實程式與展示範圍

- [physics_models.py](</C:/Users/User/Documents/ChatGPT/Nasa Hackathon/research/liquid_combustion/physics_models.py>)：`d2_history`只用明示D0²/K做條件重建；`classical_burning_constant`需要匹配物性與氧質量分率；`cool_stage_rate`含effective NTC參數，不是測得火焰溫度。
- [prepare_visualization.py](</C:/Users/User/Documents/ChatGPT/Nasa Hackathon/research/liquid_combustion/prepare_visualization.py>)：保留各source block的x軸與實驗／來源模型角色；重播已發表數值，不是執行作者原solver。
- [web/viewer.js](</C:/Users/User/Documents/ChatGPT/Nasa Hackathon/research/liquid_combustion/web/viewer.js>)；入口 [http://127.0.0.1:8808/](http://127.0.0.1:8808/)。
- 本子集尚無對應的獨立viewer case；以上是已存在的程式／入口，不是聲稱52個葉節點都已繪圖。缺圖不以示意量測或placeholder替代。
- 本文件產出沒有fit/train、反推係數或重跑作者模型；輸入缺件時不生成理論數值。

## 因子與試驗目的

本節引用使用者Excel `C:\Users\User\Downloads\NASA_實驗目的_燃料_環境_物理參數總表_20261114.xlsx`，SHA256 `fac357147ff98acf3a2f76b2ddd88d2fbab9a500159cc5ca360bb2d3a236dae1`。來源分類是前一輪表頭盤點，不能直接升格為逐次校準量測或科學因果角色；原公式/cache未重算。

| 因子 | Excel sheet／cell與原表欄 | 單位與定義 | 操縱／控制／應變／未確立 | 結論使用方式 |
|---|---|---|---|---|
| 其他氣體組成／濃度 | `物理參數!C464:I464`；G464=`cool diffusion flame extinction limits, no ozone；cool diffusion flame extinction limits, with ozone；hot diffusion flame extinction limits, no ozone；Xf = 0.1；Xf = 0.0…（完整原欄見crosswalk）`；原定位 `data summary!R4C5` | E464=未由欄名確認；原分類D464=地面實驗／模擬來源，須按資料區分 | 初始成分／來源分析量需按欄定義；不因分類名稱當實測。 | 僅供結論來源／條件核對；未建立數值trial join |
| 尺寸／幾何 | `物理參數!C465:I465`；G465=`distance [cm]；location [cm]；distance[cm]`；原定位 `data ID 5!R3C3` | E465=cm；原分類D465=地面實驗／模擬來源，須按資料區分 | 逐欄核對硬體、液滴、座標、指令的角色；不可generic diameter。 | 僅供結論來源／條件核對；未建立數值trial join |
| 溫度 | `物理參數!C466:I466`；G466=`temperature [K]`；原定位 `data ID 5!R3C12` | E466=K；原分類D466=地面實驗／模擬來源，須按資料區分 | 環境氣體、初始液體、火焰／表面、點火器與property reference分開；儀器時序不是溫度。 | 僅供結論來源／條件核對；未建立數值trial join |

- 每列原檔路徑在Excel H欄、原欄位／定位在G/I欄；完整列與source SHA見 [factor_crosswalk.json](</C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/data_inventory/factor_crosswalk.json>)。
- 每個原欄名的存在不證明是操縱變因；是否controlled必須在匹配試次／protocol中另核。`microgravity`不填成精確g=0；缺失T、g或U保留Unknown。

### 最終CFI／PSI117文獻binding（保留review程度）

專項receipt：[cfi_literature.json](</C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/literature/cfi_literature.json>)；SHA256 `87d764f52cb27ffea8c7889aa71746057f0cacbd1dfe8a82f72328f55135b403`。這些是文獻來源與適用範圍，未取得exact archived test mapping者不提升成same-data。

- **PSI117-SEMINAR2026 — Cool Flames in Space**；DOI/NTRS=Unknown；官方URL=https://psi.nasa.gov/physci/repo/data/investigations/PSI-117。
  - review狀態=`bounded_36slide_text_review`；physical pages=[1, 8, 9, 21, 25, 31]；edition SHA=9b69c81ba20b7a9af49ca899fb7520ae8e2034f9ceadf94fc6ef22910fc417aa；local source `C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\03_其他文件\簡報與海報\第一批下載\PSI-117_research\Presentations\PSI-117_Presentations_PSI_Users_Group_Cool_Flames_in_Space_03302026.pdf`。
  - dataset mapping=`unknown`；trial IDs=None。
  - 此項只作scope／機制背景，不是本PSI142工作表原始publication的全文核對或exact same-data證明。
- 未取得全文者只依receipt明示的primary abstract／captions／metadata範圍；不把slide、conference與journal版混成同一edition。
- 沒有複製英文直接引句；維持既有quote ledger。

## 多結論比較

- **共同結論：** source索引涉及hot/cool endpoints與光學／熱場可觀測量；這些是燃燒機制研究相關量。
- **不同結論：** diffusion／premixed、with/withoutO3、fuel、fraction、strain、空間座標與endpoint各別保留；地面counterflow不是ISS孤立液滴。
- **是否使用相同資料：** 本葉為exact source-workbook sheet subset。不同sheet及publication是否partially_shared或independent尚Unknown；不因同author／fuel推定。
- **衝突或未解差異：** 未核units／coordinate direction／量測還原方法／source-run IDs保留，不能用它補冷焰液滴Y或當Earth↔space matched pair。

## 消防洞見

| 預防／偵測／撲滅 | 洞見 | 依據結論 | 直接支持或新增假說 | 缺少的判別實驗 |
|---|---|---|---|---|
| 預防 | 可以提出需同時量成分、strain／輸運與熱邊界的機制假說；不能把source extinction limit當艙體安全設定。 | C01–C02 | related mechanism，不是液滴／艙體直接驗證 | 明確fuel delivery phase、geometry、P/O2/T與重力匹配，matched trial IDs |
| 偵測 | PLIF／chemiluminescence／thermometry須區分；光學訊號可研究反應區，但尚無alarm效能證據。 | C01–C02 | 新增感測研究假說；未qualification | 校準、物種／熱同步、真實煙霧與alarm positive/negative cohort |
| 撲滅／抑制 | ozone-sensitized機理對照不是消防藥劑方案，不建議O3抑制／注入；counterflow strain limit不能當艙體通風滅火程序。 | C02 | 適用範圍限制 | 真正intervention時序／劑量／暴露／副產物與再燃量測 |

## 資料缺口與文獻覆蓋

- 全文、原始experimental IDs、量測／source-reduction／model角色、組成basis及calibration需按對應primary publication核對；本輪只讀此local工作簿與既有索引。
- DOI／physical page未在這份sheet registry給定者仍Unknown；Figure與publication string保持來源原文，不造page或DOI。
- CFI／PSI117文獻補充：[cfi_literature.json](</C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/literature/cfi_literature.json>)。本葉節點仍只採本次明列的來源row/series，新增source record本身不建立exact trial join。
- 不增加核心液態試次分母，不重跑模型，不把ground1g的此端點補成CFI冷焰Y。
- 離線來源路徑／hash留本MD，不上Git。
