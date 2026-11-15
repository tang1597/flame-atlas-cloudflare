# PSI-39 / C12H26 / source_summary_test_table

`LIQ-PSI-39-C12H26-a0f3edb383`

## 資料身分與可追溯範圍

- 類別：Test；架構：`CIR_MDCA_isolated_liquid_droplet`；燃料label原樣保留，混合比例basis未核時不假定mass/volume。
- 觀測分母：79筆試次摘要列；unique reported test-id=79，verified independent physical tests仍Unknown。
- source rows：`2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81`。standardized physical CSV rows：`1383, 1384, 1385, 1386, 1387, 1388, 1389, 1390, 1391, 1392, 1393, 1394, 1395, 1396, 1397, 1398, 1399, 1400, 1401, 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410, 1411, 1412, 1413, 1414, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1422, 1423, 1424, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1432, 1433, 1434, 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1442, 1443, 1444, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461`。
- 存取：[liquid_subdatasets.json](</C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/data_inventory/liquid_subdatasets.json>)；[numeric fixture](</C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/data_inventory/visualization_data.json>)。
- **來源檔：** `C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\03_其他文件\其他研究文件_正文類型待確認\第一批下載\PSI-39_CFI\Science Documents\PSI-39_Science Documents_CFI_DataSummary_Spreadsheet_Jan2021.xlsx`
- **SHA256：** `a5b04b6a32bda764a9b367e491cc46b78ad0af0ac6b5e723e63b57abdb1d7dd8`
- **原始儲存／版本：** `public_data_20261104_155720/01_PSI/PSI-39_CFI/Science Documents/PSI-39_Science Documents_CFI_DataSummary_Spreadsheet_Jan2021.xlsx`；source identity=`683f4b7cda33c6f4c4cec615`；version=`2`。
- **NASA／DOI：** https://psi.nasa.gov/physci/repo/data/investigations/PSI-39；DOI=10.60555/m6pj-a914。

## 文獻結果與視覺化程式

下表把物理量的來源值、量測定義、metadata與缺口分別標示；metadata／限制列不是物理實驗結果。

| 結論 ID | 文獻／頁或圖 | 結果與端點 | 使用的資料子集 | 公式／參數來源 | 展示程式 | 證據角色 |
|---|---|---|---|---|---|---|
| C01 | CFI工作簿DATA；各sourceCell見fixture | 熱焰來源Khot有73/79個finite值，範圍6.2e-08–1.703e-06 m²/s | 本燃料子集原DATA rows | 來源D²分析參數；沒有新fit | 無專用summary viewer；prepare_visualization.py只載指定source curves | **來源分析應變量**，不是物性或熱測量 |
| C02 | CFI工作簿DATA；各sourceCell見fixture | 冷焰來源Kcool有64/79個finite值，範圍3.1e-07–8.06e-07 m²/s | 本燃料子集原DATA rows | 來源D²分析參數；沒有新fit | 無專用summary viewer；prepare_visualization.py只載指定source curves | **來源分析應變量**，不是物性或熱測量 |
| C03 | CFI DATA::Dext,cool；Master Sheet/Comments需並看 | 冷焰端點直徑有60值，其中source zero=15；zero及缺值不自動當燃料耗盡 | 同上；extrapolation／分析完成旗標另存 | postevent端點；不是氧擴散係數 | 無新增閾值圖 | **來源數值＋censoring限制** |

### 真實程式與展示範圍

- [physics_models.py](</C:/Users/User/Documents/ChatGPT/Nasa Hackathon/research/liquid_combustion/physics_models.py>)：`d2_history`只用明示D0²/K做條件重建；`classical_burning_constant`需要匹配物性與氧質量分率；`cool_stage_rate`含effective NTC參數，不是測得火焰溫度。
- [prepare_visualization.py](</C:/Users/User/Documents/ChatGPT/Nasa Hackathon/research/liquid_combustion/prepare_visualization.py>)：保留各source block的x軸與實驗／來源模型角色；重播已發表數值，不是執行作者原solver。
- [web/viewer.js](</C:/Users/User/Documents/ChatGPT/Nasa Hackathon/research/liquid_combustion/web/viewer.js>)；入口 [http://127.0.0.1:8808/](http://127.0.0.1:8808/)。
- 本子集尚無對應的獨立viewer case；以上是已存在的程式／入口，不是聲稱52個葉節點都已繪圖。缺圖不以示意量測或placeholder替代。
- 本文件產出沒有fit/train、反推係數或重跑作者模型；輸入缺件時不生成理論數值。

### 與最終文獻receipt相連的結論（不外推至未配對試次）

| 結論 ID | 文獻／頁或圖 | 結果與端點 | 使用的資料子集 | 公式／參數來源 | 展示程式 | 證據角色 |
|---|---|---|---|---|---|---|
| C04 | CFI-REPORT2020 physicalp6；CFI receipt CC01 | backlight liquid diameter、UV OH*、color及radiometer是不同量測，不以一張黑暗影像證明反應停止 | 此CFI campaign方法；本燃料每個timepoint尚未join | D²／phase定義，不重跑分析 | physics_models.py::d2_history僅條件式；無summary專用case | **觀測方法＋source interpretation**；不是安全判定 |
| C05 | CFI-DIETRICH2024 public Fig1/3/4/5 captions；全文未取得 | source文獻把低溫燃燒、輻射、液滴／火焰尺寸及高壓warm/reignition分開；不能以同fuel宣告same-data | caption named FLEX1240/1250/1230/1256/1260/1261；本CSV逐列未join | 詳細／analytical model身份各別；不把effective NTC T當沸點 | source-model replay；不生新預測 | **作者結論／部分caption範圍** |
| C06 | CFI-DODECANE-KINETICS2020 primary3page text；CFI receipt CC07 | Heptane chemistry配dodecane物性會過度預測Dce；source step4是校準妥協，不是獨立驗證 | 原論文比較；未與本子集每列配對 | 不轉移heptane係數，不反推kinetics | 無完整原code／state，僅列式與缺件 | **作者模型不匹配結果**；適用原文domain |

- Source report p7的dodecanol文字與campaign/caption dodecane身份不一致，保留source conflict；不暗改成另一種液體。
- FLEX1268的final-report caption條件與ThreeStage deck不同：report physicalp8寫3atm／12%O2／50%N2／29%He，deck physicalp15–16寫2.75atm／21.6%O2／50.2%N2／28.2%He；本葉不選其中一版本消除差異。

### 最終CFI／PSI117文獻binding（保留review程度）

專項receipt：[cfi_literature.json](</C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/literature/cfi_literature.json>)；SHA256 `87d764f52cb27ffea8c7889aa71746057f0cacbd1dfe8a82f72328f55135b403`。這些是文獻來源與適用範圍，未取得exact archived test mapping者不提升成same-data。

- **CFI-REPORT2020 — Cool Flame Investigation (CFI): Science Final Report**；DOI/NTRS=Unknown；官方URL=https://psi.ndc.nasa.gov/mpglobal/api/athena/file/9919378/?inline=1&log=1。
  - review狀態=`all_13_physical_pages_text_reviewed`；physical pages=[1, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13]；edition SHA=e15158689180314583917200a071730d3aed9088e1ae689b847bd416674010f9；local source `C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\03_其他文件\研究報告與書章\第一批下載\PSI-39_CFI\Reports\PSI-39_Reports_CFI Science Final Report.pdf`。
  - dataset mapping=`source_campaign_ranges_not_exact_row_join`；trial IDs=None。
- **CFI-DIETRICH2024 — Low Temperature n-Dodecane Droplet Combustion Experiments Aboard the International Space Station**；DOI/NTRS=10.1007/s12217-024-10115-x；官方URL=https://link.springer.com/article/10.1007/s12217-024-10115-x。
  - review狀態=`publisher_abstract_data_availability_and_public_figure_captions_reviewed_fulltext_not_obtained`；physical pages=[]；edition SHA=None；local source `未取得local全文`。
  - dataset mapping=`Fig3_caption_named_tests_no_CSV_row_join`；trial IDs=['FLEX1240', 'FLEX1250', 'FLEX1230', 'FLEX1256', 'FLEX1260', 'FLEX1261']。
- **CFI-ASPECTS2015 — Aspects of Cool-Flame Supported Droplet Combustion in Microgravity**；DOI/NTRS=20160000344；官方URL=https://ntrs.nasa.gov/api/citations/20160000344/downloads/20160000344.pdf。
  - review狀態=`20_slide_text_review_and_p13_equation_visually_verified`；physical pages=[1, 4, 9, 13, 14, 15, 16, 17]；edition SHA=302c8a9bcb5a847db044a6bd87f0319431132f5bbd506ae47837b41930b66aab；local source `C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\03_其他文件\簡報與海報\第一批下載\PSI-39_CFI\Presentations\PSI-39_Presentations_Aspects of Cool-Flame Supported Droplet Combustion in Microgravity_CFI.pdf`。
  - dataset mapping=`unknown`；trial IDs=None。
- **CFI-DODECANE-KINETICS2020 — Cool-flame dodecane-droplet extinction diameters**；DOI/NTRS=10.1016/j.combustflame.2019.10.036；官方URL=https://par.nsf.gov/servlets/purl/10176660。
  - review狀態=`3page_NSF_primary_text_reviewed_no_local_payload`；physical pages=[1, 2, 3]；edition SHA=None；local source `未取得local全文`。
  - dataset mapping=`unknown`；trial IDs=None。
- 未取得全文者只依receipt明示的primary abstract／captions／metadata範圍；不把slide、conference與journal版混成同一edition。
- 沒有複製英文直接引句；維持既有quote ledger。

## 因子與試驗目的

本節引用使用者Excel `C:\Users\User\Downloads\NASA_實驗目的_燃料_環境_物理參數總表_20261114.xlsx`，SHA256 `fac357147ff98acf3a2f76b2ddd88d2fbab9a500159cc5ca360bb2d3a236dae1`。來源分類是前一輪表頭盤點，不能直接升格為逐次校準量測或科學因果角色；原公式/cache未重算。

| 因子 | Excel sheet／cell與原表欄 | 單位與定義 | 操縱／控制／應變／未確立 | 結論使用方式 |
|---|---|---|---|---|
| 一氧化碳濃度 | `物理參數!C148:I148`；G148=`不可讀亂碼標籤；不採為CO證據`；原定位 `line 18, column 1` | E148=未由欄名確認；原分類D148=量測通道 | 索引候選，需有效原欄、單位與校準；亂碼不能證明CO量測。 | 僅供結論來源／條件核對；未建立數值trial join |
| 其他氣體組成／濃度 | `物理參數!C149:I149`；G149=`Nitrogen；Helium`；原定位 `line 1, column 7` | E149=未由欄名確認；原分類D149=條件或分析量 | 初始成分／來源分析量需按欄定義；不因分類名稱當實測。 | 僅供結論來源／條件核對；未建立數值trial join |
| 壓力 | `物理參數!C150:I150`；G150=`FCU_MP_PT16(PSIA)；FCU_MP_PT17(PSIA)；FCU_MP_PT28(PSIA)；FCU_MP_PT29(PSIA)；FCU_PT16_INDEX_0(PSIA)；FCU_PT16_INDEX_1(PSIA)；FCU_PT16_INDEX_2(PSIA)；FCU_PT16_INDEX_3(PSIA)；F…（完整原欄見crosswalk）`；原定位 `line 1, column 2` | E150=PSIA；原分類D150=量測或設定 | 環境初始／設定條件；原摘要之absolute ambient已核時才使用；單一欄名不能證明因果操縱。 | 僅供結論來源／條件核對；未建立數值trial join |
| 壓力 | `物理參數!C151:I151`；G151=`Pressure`；原定位 `line 1, column 5` | E151=未由欄名確認；原分類D151=量測或設定 | 環境初始／設定條件；原摘要之absolute ambient已核時才使用；單一欄名不能證明因果操縱。 | 僅供結論來源／條件核對；未建立數值trial join |
| 尺寸／幾何 | `物理參數!C152:I152`；G152=`TP_PARAMETER_NEEDLE_DISPENSE_POSITION_1(N/A)；TP_PARAMETER_NEEDLE_DISPENSE_POSITION_2(N/A)；TP_PARAMETER_IGNITER_IGNITION_POSITION_1(N/A)；TP_PARAMETER_IGNITER_IGNITION…（完整原欄見crosswalk）`；原定位 `line 1, column 50` | E152=N/A（來源未給物理單位）；原分類D152=儀器設定／控制參數 | 逐欄核對硬體、液滴、座標、指令的角色；不可generic diameter。 | 僅供結論來源／條件核對；未建立數值trial join |
| 尺寸／幾何 | `物理參數!C153:I153`；G153=`CFI_FILTER_POSITION_RAW(N/A)；CFI_FILTER_POSITION(N/A)；IPSUG_CAMERA_4_ROI_WIDTH(N/A)；IPSUG_CAMERA_4_WIDTH(N/A)；ZOOM_POSITION(N/A)；FOCUS_POSITION(N/A)；MEMORY_LAST_ACCE…（完整原欄見crosswalk）`；原定位 `line 1, column 21` | E153=N/A（來源未給物理單位）；原分類D153=裝置或樣本條件 | 逐欄核對硬體、液滴、座標、指令的角色；不可generic diameter。 | 僅供結論來源／條件核對；未建立數值trial join |
| 尺寸／幾何 | `物理參數!C154:I154`；G154=`CFI_CF_INTENSIFIER_PULSE_WIDTH(us)；CFI_HF_INTENSIFIER_PULSE_WIDTH(us)；CFI_PCF_INTENSIFIER_PULSE_WIDTH(us)；IPSUG_INTENS_GATE_WIDTH(us)`；原定位 `line 1, column 14` | E154=us；原分類D154=裝置或樣本條件 | 逐欄核對硬體、液滴、座標、指令的角色；不可generic diameter。 | 僅供結論來源／條件核對；未建立數值trial join |
| 尺寸／幾何 | `物理參數!C155:I155`；G155=`Width；SensorWidth；WaveLength`；原定位 `line 8` | E155=未由欄名確認；原分類D155=裝置或樣本條件 | 逐欄核對硬體、液滴、座標、指令的角色；不可generic diameter。 | 僅供結論來源／條件核對；未建立數值trial join |
| 影像／光譜設定 | `物理參數!C156:I156`；G156=`IPSU_TP_CAMERA(N/A)；COLOR_CAMERA_ILLUMINATION_LIGHT_RELAY_STATUS(N/A)；CFI_CF_INTENSIFIER_FILTER(N/A)；CFI_HF_INTENSIFIER_FILTER(N/A)；DCM_MP_CAM_PIXEL_OFFSET(N/A)；DCM_…（完整原欄見crosswalk）`；原定位 `line 1, column 2` | E156=N/A（來源未給物理單位）；原分類D156=儀器設定或影像座標 | 量測條件／光學設定，不是物理應變值。 | 僅供結論來源／條件核對；未建立數值trial join |
| 影像／光譜設定 | `物理參數!C157:I157`；G157=`PixelFormat；ExposureTimeRaw；CurrentFrameRate；Frames per Second；ColorCamTime_sec`；原定位 `line 3` | E157=未由欄名確認；原分類D157=儀器設定或影像座標 | 量測條件／光學設定，不是物理應變值。 | 僅供結論來源／條件核對；未建立數值trial join |
| 影像／光譜設定 | `物理參數!C158:I158`；G158=`IPSUG_CAMERA_4_GAIN_MODE(N/A)；IPSUG_CAMERA_4_AUTO_GAIN(N/A)；IPSUG_CAMERA_4_MAN_GAIN(N/A)`；原定位 `line 1, column 16` | E158=N/A（來源未給物理單位）；原分類D158=儀器設定／控制參數 | 量測條件／光學設定，不是物理應變值。 | 僅供結論來源／條件核對；未建立數值trial join |
| 氧濃度 | `物理參數!C159:I159`；G159=`Oxygen`；原定位 `line 1, column 6` | E159=未由欄名確認；原分類D159=量測或條件值 | 初始氣氛或列舉配方選項；各物種basis/scope分開。 | 僅供結論來源／條件核對；未建立數值trial join |
| 流速／通風 | `物理參數!C160:I160`；G160=`TP_PARAMETER_DISPENSER_VELOCITY_1(N/A)；TP_PARAMETER_DISPENSER_VELOCITY_2(N/A)；TP_PARAMETER_FIBER_INDEXING_VELOCITY(N/A)；TP_PARAMETER_FLOW_NOZZLE_1_SPEED(N/A)；TP_PARA…（完整原欄見crosswalk）`；原定位 `line 1, column 58` | E160=N/A（來源未給物理單位）；原分類D160=儀器設定／控制參數 | 設定／相對流速或原始通道待核；液滴漂移、風扇顯示、燃料供應不混用。 | 僅供結論來源／條件核對；未建立數值trial join |
| 流速／通風 | `物理參數!C161:I161`；G161=`FLOW_NOZZLE_1_SPEED(N/A)；FLOW_NOZZLE_2_SPEED(N/A)；CFI_FILTER_DEFAULT_VELOCITY(N/A)；CFI_FILTER_FAST_VELOCITY (N/A)`；原定位 `line 1, column 20` | E161=N/A（來源未給物理單位）；原分類D161=量測或設定 | 設定／相對流速或原始通道待核；液滴漂移、風扇顯示、燃料供應不混用。 | 僅供結論來源／條件核對；未建立數值trial join |
| 液滴直徑／面積 | `物理參數!C162:I162`；G162=`but no indication it was sd0 only.；DropletDiameter_mm`；原定位 `line 16, column 2` | E162=未由欄名確認；原分類D162=影像／來源分析量 | D0是初始狀態；D(t)、熄滅D與影像面積是應變／來源影像分析；不是火焰尺寸。 | 僅供結論來源／條件核對；未建立數值trial join |
| 溫度 | `物理參數!C163:I163`；G163=`FCU_MP_TM1(Deg C)；FCU_MP_TM2(Deg C)；FCU_MP_TM3(Deg C)；FCU_MP_TM4(Deg C)；IPSUG_CAMERA_4_TEMP(Deg C)；IPSUG_MOTION_4_TEMP1(Deg C)；IPSUG_MOTION_4_TEMP2(Deg C)；IPSUG_MOTI…（完整原欄見crosswalk）`；原定位 `line 1, column 6` | E163=Deg C；原分類D163=量測或設定 | 環境氣體、初始液體、火焰／表面、點火器與property reference分開；儀器時序不是溫度。 | 僅供結論來源／條件核對；未建立數值trial join |
| 溫度 | `物理參數!C164:I164`；G164=`IPSUG5-1 RR/FG Ave PSIA Ave DegC`；原定位 `line 34, column 13` | E164=未由欄名確認；原分類D164=量測或設定 | 環境氣體、初始液體、火焰／表面、點火器與property reference分開；儀器時序不是溫度。 | 僅供結論來源／條件核對；未建立數值trial join |
| 火焰幾何／延燒 | `物理參數!C165:I165`；G165=`ColorCamFlameDiameter_mm；ColorCamFlameStandoff；CoolFlameDiameterFWHM_mm；CoolFlameDiameterP2P_mm`；原定位 `line 1, column 2` | E165=未由欄名確認；原分類D165=影像／來源分析量 | 來源定義的光學或模型邊界應變；不等於液滴或熱通量。 | 僅供結論來源／條件核對；未建立數值trial join |
| 熱通量／輻射 | `物理參數!C166:I166`；G166=`RADIOMETER_100HZ_FRAME_MILLISECONDS(N/A)`；原定位 `line 1, column 6` | E166=N/A（來源未給物理單位）；原分類D166=量測通道或來源分析量 | 原始電壓／訊號、W輻射功率及W/m²通量須逐欄校準，不能直接替換。 | 僅供結論來源／條件核對；未建立數值trial join |
| 熱通量／輻射 | `物理參數!C167:I167`；G167=`LLL_NARROWBAND_RADIOMETER_THRESHOLD(VDC)；LLL_WIDEBAND_RADIOMETER_THRESHOLD(VDC)；NARROW_BAND_RADIOMETER_SAMPLE_00(VDC)；NARROW_BAND_RADIOMETER_SAMPLE_01(VDC)；NARROW_BA…（完整原欄見crosswalk）`；原定位 `line 1, column 86` | E167=VDC；原分類D167=量測通道或來源分析量 | 原始電壓／訊號、W輻射功率及W/m²通量須逐欄校準，不能直接替換。 | 僅供結論來源／條件核對；未建立數值trial join |
| 熱通量／輻射 | `物理參數!C168:I168`；G168=`Radiometer Time；RADIOMETER_100HZ_FRAME_TIME(GMT)；RadiometerTime_sec`；原定位 `line 34, column 3` | E168=未由欄名確認；原分類D168=量測通道或來源分析量 | 原始電壓／訊號、W輻射功率及W/m²通量須逐欄校準，不能直接替換。 | 僅供結論來源／條件核對；未建立數值trial join |
| 燃燒率／燃燒常數 | `物理參數!C169:I169`；G169=`�kB \u0001.g⑷[&gt;�[gR����3'���4��4m\u000f'�\u001bf�Ż=�\u0001�๽H��.�\u0007���x�S=v����\|3�\u0015�� {�SՆ~�\u0005��c��\u0018��n^VK�`；原定位 `line 14, column 3` | E169=未由欄名確認；原分類D169=計算／分析參數 | 來源分析／擬合後的D²應變量；不是O2分子擴散係數或獨立輸入。 | 僅供結論來源／條件核對；未建立數值trial join |
| 燃燒／點火／老化時間 | `物理參數!C170:I170`；G170=`TP_PARAMETER_BURN_TO_COMPLETION_TIME(N/A)`；原定位 `line 1, column 77` | E170=N/A（來源未給物理單位）；原分類D170=儀器設定／控制參數 | protocol/history及postevent response分開，熱焰／冷焰／可見端點不混。 | 僅供結論來源／條件核對；未建立數值trial join |
| 硬體電壓／電流／功率 | `物理參數!C171:I171`；G171=`ICM_LASER_CURRENT(Adc)`；原定位 `line 1, column 22` | E171=Adc；原分類D171=原始訊號或狀態 | 儀器／硬體原始通道或控制；不自動代表燃燒熱釋放。 | 僅供結論來源／條件核對；未建立數值trial join |
| 硬體電壓／電流／功率 | `物理參數!C172:I172`；G172=`POWER(N/A)`；原定位 `line 1, column 30` | E172=N/A（來源未給物理單位）；原分類D172=原始訊號或狀態 | 儀器／硬體原始通道或控制；不自動代表燃燒熱釋放。 | 僅供結論來源／條件核對；未建立數值trial join |
| 硬體電壓／電流／功率 | `物理參數!C173:I173`；G173=`CFI_HF_NARROW_THRESHOLD(VDC)；CFI_HF_WIDE_THRESHOLD(VDC)`；原定位 `line 1, column 87` | E173=VDC；原分類D173=原始訊號或狀態 | 儀器／硬體原始通道或控制；不自動代表燃燒熱釋放。 | 僅供結論來源／條件核對；未建立數值trial join |
| 硬體電壓／電流／功率 | `物理參數!C174:I174`；G174=`TotalWideBandPower_W；TotalNarrowBandPower_W`；原定位 `line 1, column 2` | E174=未由欄名確認；原分類D174=原始訊號或狀態 | 儀器／硬體原始通道或控制；不自動代表燃燒熱釋放。 | 僅供結論來源／條件核對；未建立數值trial join |
| 點火功率／電壓／電流 | `物理參數!C175:I175`；G175=`TP_PARAMETER_IGNITER_ON_TIME(N/A)`；原定位 `line 1, column 75` | E175=N/A（來源未給物理單位）；原分類D175=儀器設定／控制參數 | 點火設定／history；電壓或電流不自動等於熱功率。 | 僅供結論來源／條件核對；未建立數值trial join |
| 點火功率／電壓／電流 | `物理參數!C176:I176`；G176=`TP_PARAMETER_IGNITER_WATTAGE(Watts)`；原定位 `line 1, column 76` | E176=Watts；原分類D176=儀器設定／控制參數 | 點火設定／history；電壓或電流不自動等於熱功率。 | 僅供結論來源／條件核對；未建立數值trial join |
| 點火功率／電壓／電流 | `物理參數!C177:I177`；G177=`IGNITER_CURRENT_MONITOR(Adc)`；原定位 `line 1, column 22` | E177=Adc；原分類D177=量測或設定 | 點火設定／history；電壓或電流不自動等於熱功率。 | 僅供結論來源／條件核對；未建立數值trial join |
| 點火功率／電壓／電流 | `物理參數!C178:I178`；G178=`IGNITER_POWER_STATUS(N/A)；IGNITER_POWER_ENABLE(N/A)`；原定位 `line 1, column 9` | E178=N/A（來源未給物理單位）；原分類D178=量測或設定 | 點火設定／history；電壓或電流不自動等於熱功率。 | 僅供結論來源／條件核對；未建立數值trial join |
| 點火功率／電壓／電流 | `物理參數!C179:I179`；G179=`IGNITER_VOLTAGE_MONITOR_1(Vdc)；IGNITER_VOLTAGE_MONITOR_2(Vdc)`；原定位 `line 1, column 18` | E179=Vdc；原分類D179=量測或設定 | 點火設定／history；電壓或電流不自動等於熱功率。 | 僅供結論來源／條件核對；未建立數值trial join |
| 點火功率／電壓／電流 | `物理參數!C180:I180`；G180=`IGNITER_WATTAGE(Watts)`；原定位 `line 1, column 8` | E180=Watts；原分類D180=量測或設定 | 點火設定／history；電壓或電流不自動等於熱功率。 | 僅供結論來源／條件核對；未建立數值trial join |
| 點火功率／電壓／電流 | `物理參數!C181:I181`；G181=`HFRHR, HIBMS and Color Camera images/FCI files start at 2 seconds before the igniter on time.`；原定位 `line 30, column 2` | E181=未由欄名確認；原分類D181=量測或設定 | 點火設定／history；電壓或電流不自動等於熱功率。 | 僅供結論來源／條件核對；未建立數值trial join |

- 每列原檔路徑在Excel H欄、原欄位／定位在G/I欄；完整列與source SHA見 [factor_crosswalk.json](</C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/data_inventory/factor_crosswalk.json>)。
- 每個原欄名的存在不證明是操縱變因；是否controlled必須在匹配試次／protocol中另核。`microgravity`不填成精確g=0；缺失T、g或U保留Unknown。
- **Excel 物理參數!A148:K148特例：** G148是不可讀／亂碼，H148指RadiometerData、I148=line18 column1；它只是索引發現，**不能證明CO濃度通道存在或可用**，不得據此做CO偵測結論。

### 此子集的數值可用性

| 標準欄位 | finite／總列 | source zero | min–max（標準單位） |
|---|---|---|---|
| `std_initial_droplet_diameter_m` | 73/79 | 0 | 0.003793–0.006094 m |
| `std_hot_extinction_droplet_diameter_m` | 70/79 | 0 | 0.002773–0.006013 m |
| `std_cool_extinction_droplet_diameter_m` | 60/79 | 15 | 0–0.002972 m |
| `std_pressure_Pa` | 79/79 | 0 | 50662.5–506625 Pa |
| `std_oxygen_fraction` | 79/79 | 0 | 0.17–0.21 mole fraction [1] |
| `std_ambient_nitrogen_fraction` | 79/79 | 0 | 0.2–0.83 mole fraction [1] |
| `std_ambient_helium_fraction` | 79/79 | 57 | 0–0.59 mole fraction [1] |
| `std_ambient_temperature_K` | 0/79 | 0 | Unknown / 未核–Unknown / 未核 K |
| `std_duration_s` | 72/79 | 0 | 1.90394–21.6167 s |
| `std_hot_flame_duration_s` | 72/79 | 0 | 1.90394–21.6167 s |
| `std_hot_burning_rate_constant_m2_s` | 73/79 | 0 | 6.2e-08–1.703e-06 m²/s |
| `std_cool_burning_rate_constant_m2_s` | 64/79 | 0 | 3.1e-07–8.06e-07 m²/s |
| `std_reported_reignition_count` | 74/79 | 53 | 0–7 count |

這是來源值分布與可用性，沒有新回歸或控制其他變因；數值範圍不是安全操作範圍。

- CFI／PSI117文獻補充：[cfi_literature.json](</C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/literature/cfi_literature.json>)。本葉節點仍只採本次明列的來源row/series，新增source record本身不建立exact trial join。

## 多結論比較

- **共同結論：** 來源均把液滴初始／剩餘尺寸、相位端點與來源K視為不同quantity；不能把液滴直徑換成火焰大小。
- **不同結論：** 不同燃料、P、O2/N2/He/CO2、D0、fiber與點火history需保留；同名microgravity或同一CIR/MDCA不建立控制匹配。
- **是否使用相同資料：** 同一來源摘要表內可追source rows；對其他論文通常為shared_investigation_unjoined。上方僅在報告identifier直接命中時列exact_subset，其餘不提升成相同資料。
- **衝突或未解差異：** 未回源或未核單位、缺值、零值／extrapolation與版本差異均保留；不藉選來源消除。

## 消防洞見

| 預防／偵測／撲滅 | 洞見 | 依據結論 | 直接支持或新增假說 | 缺少的判別實驗 |
|---|---|---|---|---|
| 預防 | P、氧／稀釋成分與液滴尺度必須共同描述；本子集的K或壽命不能提供艙體通用安全閾值。 | C01–C02 | source-bounded研究條件；安全策略是新增假說 | 同配方／P／O2／D0／fiber／點火history的重複實驗與失敗樣本 |
| 偵測 | 液滴縮減、UV／可見焰與熱／化學量測須分通道，黑暗或可見焰消失不自動確認完整熄滅。 | C02–C03 | 量測端點邊界；沒有alarm qualification | 同步光學、溫度／物種／煙霧與真正警報反應，含盲點／誤報 |
| 撲滅／抑制 | 預配稀釋氣與液滴試驗不是艙體藥劑注入試驗；不給He/CO2用量、再燃機率或設備效能。 | C01–C03 | 限制＋待驗證的持續燃燒監測構想 | 確切注入時序／劑量、全相位反應、殘餘液體、再點火與通風／尺度對照 |

## 資料缺口與文獻覆蓋

- 逐次熱狀態／U／numeric g／完整物性與history缺失時，`classical_burning_constant`或`cool_stage_rate`只能列公式，不能填預設值產生理論曲線。
- 支撐fiber、FOV loss、phase/extrapolation與不完整分析需保留；CFI cool-endpoint source zero不能自動稱「已耗盡」。
- 文獻全文／選頁／metadata-only／remote lead已分開。沒有聲稱檢索完整、每個source量測有效，或所有條件都完成燃燒。
- 數值與原始路徑僅離線MD／JSON；不納入Git、不改原檔。
