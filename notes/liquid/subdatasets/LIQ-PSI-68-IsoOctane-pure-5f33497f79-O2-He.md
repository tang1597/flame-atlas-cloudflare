# PSI-68 / IsoOctane (pure) / O2/He

`LIQ-PSI-68-IsoOctane-pure-5f33497f79-O2-He`

## 資料身分與可追溯範圍

- 類別：Fuel configuration；架構：`CIR_MDCA_isolated_liquid_droplet`；燃料label原樣保留，混合比例basis未核時不假定mass/volume。
- 觀測分母：4筆列舉配方配置，不是4次燃燒。
- source rows：`2`。standardized physical CSV rows：`1656, 1658, 1660, 1662`。
- 存取：[liquid_subdatasets.json](</C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/data_inventory/liquid_subdatasets.json>)；[numeric fixture](</C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/data_inventory/visualization_data.json>)。
- **來源檔：** `C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-68_FLEX-2\Experimental table\PSI-68_Experimental table_Flex2.csv`
- **SHA256：** `cc57ad1bd9977aa13e7ac6c3aa618303012686e232b36c052c6a9f1a74e5f528`
- **原始儲存／版本：** `public_data_20261104_155720/01_PSI/PSI-68_FLEX-2/Experimental table/PSI-68_Experimental table_Flex2.csv`；source identity=`67929004b7b6ff8e6502ecd0`；version=`1`。
- **NASA／DOI：** https://psi.nasa.gov/physci/repo/data/investigations/PSI-68；DOI=10.60555/byp8-h018。

## 文獻結果與視覺化程式

下表把物理量的來源值、量測定義、metadata與缺口分別標示；metadata／限制列不是物理實驗結果。

| 結論 ID | 文獻／頁或圖 | 結果與端點 | 使用的資料子集 | 公式／參數來源 | 展示程式 | 證據角色 |
|---|---|---|---|---|---|---|
| C01 | 原燃料配置表source row 2 | 此O2/He分支列O2=0.17, 0.21, 0.25, 0.3；4個選項 | 同一燃料source row的recipe expansion | 無response fit | 無專用viewer case | **metadata／設計，非物理結果** |
| C02 | 同一配置列 | D0、P與U是範圍／選項，名義25°C不是逐次T | 尚無test-id/Y | 不計K、熄滅機率或濃度門檻 | prepare_visualization.py尚無此配置series | **限制，非物理結果** |
| C03 | FLEX2-SRD2010 pp43–44；FLEX2-DOD | 研究需求與資料組織不等於完成試驗 | 規劃與歷史檔案結構 | Gr/Re²為條件尺度需求，非每次量測g | physics_models.py無填入缺state | **planning／schema** |

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
| 二氧化碳濃度 | `物理參數!C186:I186`；G186=`CO2`；原定位 `line 1, column 4` | E186=未由欄名確認；原分類D186=量測或條件值 | 稀釋氣初始設定與燃燒產物應變值必須分開。 | 僅供結論來源／條件核對；未建立數值trial join |
| 其他氣體組成／濃度 | `物理參數!C187:I187`；G187=`Ambient Gas Mixture`；原定位 `line 1, column 3` | E187=未由欄名確認；原分類D187=條件或分析量 | 初始成分／來源分析量需按欄定義；不因分類名稱當實測。 | 僅供結論來源／條件核對；未建立數值trial join |
| 壓力 | `物理參數!C188:I188`；G188=`FCU_MP_PT16(PSIA)；FCU_MP_PT17(PSIA)；FCU_MP_PT28(PSIA)；FCU_MP_PT29(PSIA)；FCU_PT16_INDEX_0(PSIA)；FCU_PT16_INDEX_1(PSIA)；FCU_PT16_INDEX_2(PSIA)；FCU_PT16_INDEX_3(PSIA)；F…（完整原欄見crosswalk）`；原定位 `line 1, column 2` | E188=PSIA；原分類D188=量測或設定 | 環境初始／設定條件；原摘要之absolute ambient已核時才使用；單一欄名不能證明因果操縱。 | 僅供結論來源／條件核對；未建立數值trial join |
| 壓力 | `物理參數!C189:I189`；G189=`Ambient Pressure (atm)`；原定位 `line 1, column 5` | E189=atm；原分類D189=量測或設定 | 環境初始／設定條件；原摘要之absolute ambient已核時才使用；單一欄名不能證明因果操縱。 | 僅供結論來源／條件核對；未建立數值trial join |
| 壓力 | `物理參數!C190:I190`；G190=`Chamber pressure data was not collected at 30Hz`；原定位 `line 1, column 1` | E190=未由欄名確認；原分類D190=量測或設定 | 環境初始／設定條件；原摘要之absolute ambient已核時才使用；單一欄名不能證明因果操縱。 | 僅供結論來源／條件核對；未建立數值trial join |
| 尺寸／幾何 | `物理參數!C191:I191`；G191=`TP_PARAMETER_NEEDLE_DISPENSE_POSITION_1(N/A)；TP_PARAMETER_NEEDLE_DISPENSE_POSITION_2(N/A)；TP_PARAMETER_IGNITER_IGNITION_POSITION_1(N/A)；TP_PARAMETER_IGNITER_IGNITION…（完整原欄見crosswalk）`；原定位 `line 1, column 29` | E191=N/A（來源未給物理單位）；原分類D191=儀器設定／控制參數 | 逐欄核對硬體、液滴、座標、指令的角色；不可generic diameter。 | 僅供結論來源／條件核對；未建立數值trial join |
| 尺寸／幾何 | `物理參數!C192:I192`；G192=`ZOOM_POSITION(N/A)；FOCUS_POSITION(N/A)；MEMORY_LAST_ACCESS_POSITION(N/A)；SHUTTER_POSITION(N/A)；IRIS_POSITION(N/A)；BRIGHT_POSITION(N/A)；EXPOSURE_COMP_POSITION(N/A)；LLL…（完整原欄見crosswalk）`；原定位 `line 1, column 2` | E192=N/A（來源未給物理單位）；原分類D192=裝置或樣本條件 | 逐欄核對硬體、液滴、座標、指令的角色；不可generic diameter。 | 僅供結論來源／條件核對；未建立數值trial join |
| 尺寸／幾何 | `物理參數!C193:I193`；G193=`WaveLength`；原定位 `line 3, column 10` | E193=未由欄名確認；原分類D193=裝置或樣本條件 | 逐欄核對硬體、液滴、座標、指令的角色；不可generic diameter。 | 僅供結論來源／條件核對；未建立數值trial join |
| 影像／光譜設定 | `物理參數!C194:I194`；G194=`IPSU_TP_CAMERA(N/A)；DCM_MP_CAM_PIXEL_OFFSET(N/A)；DCM_MP_CAM_FRAME_RATE(N/A)；COLOR_CAMERA_SETUP(N/A)；COLOR_CAMERA_ILLUMINATION_LIGHT_RELAY_ON_OFF(N/A)；COLOR_CAMERA_IL…（完整原欄見crosswalk）`；原定位 `line 1, column 2` | E194=N/A（來源未給物理單位）；原分類D194=儀器設定或影像座標 | 量測條件／光學設定，不是物理應變值。 | 僅供結論來源／條件核對；未建立數值trial join |
| 影像／光譜設定 | `物理參數!C195:I195`；G195=`Frames per Second；IPSU1 images are very dark until ignition - Melani Smajdek suggests that possibly the illumination was not configured properly for this test point；…（完整原欄見crosswalk）`；原定位 `line 8` | E195=未由欄名確認；原分類D195=儀器設定或影像座標 | 量測條件／光學設定，不是物理應變值。 | 僅供結論來源／條件核對；未建立數值trial join |
| 氧濃度 | `物理參數!C196:I196`；G196=`Oxygen Mole Fraction；O2`；原定位 `line 1, column 4` | E196=未由欄名確認；原分類D196=量測或條件值 | 初始氣氛或列舉配方選項；各物種basis/scope分開。 | 僅供結論來源／條件核對；未建立數值trial join |
| 流速／通風 | `物理參數!C197:I197`；G197=`TP_PARAMETER_DISPENSER_VELOCITY_1(N/A)；TP_PARAMETER_DISPENSER_VELOCITY_2(N/A)；TP_PARAMETER_FIBER_INDEXING_VELOCITY(N/A)；TP_PARAMETER_FLOW_NOZZLE_1_SPEED(N/A)；TP_PARA…（完整原欄見crosswalk）`；原定位 `line 1, column 37` | E197=N/A（來源未給物理單位）；原分類D197=儀器設定／控制參數 | 設定／相對流速或原始通道待核；液滴漂移、風扇顯示、燃料供應不混用。 | 僅供結論來源／條件核對；未建立數值trial join |
| 流速／通風 | `物理參數!C198:I198`；G198=`FLOW_NOZZLE_1_SPEED(N/A)；FLOW_NOZZLE_2_SPEED(N/A)`；原定位 `line 1, column 19` | E198=N/A（來源未給物理單位）；原分類D198=量測或設定 | 設定／相對流速或原始通道待核；液滴漂移、風扇顯示、燃料供應不混用。 | 僅供結論來源／條件核對；未建立數值trial join |
| 流速／通風 | `物理參數!C199:I199`；G199=`Flow Velocity (cm/s)`；原定位 `line 1, column 7` | E199=cm/s；原分類D199=量測或設定 | 設定／相對流速或原始通道待核；液滴漂移、風扇顯示、燃料供應不混用。 | 僅供結論來源／條件核對；未建立數值trial join |
| 液滴直徑／面積 | `物理參數!C200:I200`；G200=`Initial Droplet Diameter (mm)`；原定位 `line 1, column 2` | E200=mm；原分類D200=影像／來源分析量 | D0是初始狀態；D(t)、熄滅D與影像面積是應變／來源影像分析；不是火焰尺寸。 | 僅供結論來源／條件核對；未建立數值trial join |
| 溫度 | `物理參數!C201:I201`；G201=`Ambient Temperature (C)`；原定位 `line 1, column 6` | E201=C；原分類D201=量測或設定 | 環境氣體、初始液體、火焰／表面、點火器與property reference分開；儀器時序不是溫度。 | 僅供結論來源／條件核對；未建立數值trial join |
| 溫度 | `物理參數!C202:I202`；G202=`FCU_MP_TM1(Deg C)；FCU_MP_TM2(Deg C)；FCU_MP_TM3(Deg C)；FCU_MP_TM4(Deg C)`；原定位 `line 1, column 6` | E202=Deg C；原分類D202=量測或設定 | 環境氣體、初始液體、火焰／表面、點火器與property reference分開；儀器時序不是溫度。 | 僅供結論來源／條件核對；未建立數值trial join |
| 溫度 | `物理參數!C203:I203`；G203=`FCU_MP_TM1(NA)；FCU_MP_TM2(NA)；FCU_MP_TM3(NA)；FCU_MP_TM4(NA)`；原定位 `line 1, column 6` | E203=N/A（來源未給物理單位）；原分類D203=量測或設定 | 環境氣體、初始液體、火焰／表面、點火器與property reference分開；儀器時序不是溫度。 | 僅供結論來源／條件核對；未建立數值trial join |
| 溫度 | `物理參數!C204:I204`；G204=`RR/FG Ave PSIA Ave DegC`；原定位 `line 34, column 14` | E204=未由欄名確認；原分類D204=量測或設定 | 環境氣體、初始液體、火焰／表面、點火器與property reference分開；儀器時序不是溫度。 | 僅供結論來源／條件核對；未建立數值trial join |
| 熱通量／輻射 | `物理參數!C205:I205`；G205=`RADIOMETER_100HZ_FRAME_MILLISECONDS(N/A)`；原定位 `line 1, column 6` | E205=N/A（來源未給物理單位）；原分類D205=量測通道或來源分析量 | 原始電壓／訊號、W輻射功率及W/m²通量須逐欄校準，不能直接替換。 | 僅供結論來源／條件核對；未建立數值trial join |
| 熱通量／輻射 | `物理參數!C206:I206`；G206=`NARROW_BAND_RADIOMETER_SAMPLE_00(VDC)；NARROW_BAND_RADIOMETER_SAMPLE_01(VDC)；NARROW_BAND_RADIOMETER_SAMPLE_02(VDC)；NARROW_BAND_RADIOMETER_SAMPLE_03(VDC)；NARROW_BAND_R…（完整原欄見crosswalk）`；原定位 `line 1, column 9` | E206=VDC；原分類D206=量測通道或來源分析量 | 原始電壓／訊號、W輻射功率及W/m²通量須逐欄校準，不能直接替換。 | 僅供結論來源／條件核對；未建立數值trial join |
| 熱通量／輻射 | `物理參數!C207:I207`；G207=`NARROW_BAND_RADIOMETER_SAMPLE_00(Watt/cm2)；NARROW_BAND_RADIOMETER_SAMPLE_01(Watt/cm2)；NARROW_BAND_RADIOMETER_SAMPLE_02(Watt/cm2)；NARROW_BAND_RADIOMETER_SAMPLE_03(Wat…（完整原欄見crosswalk）`；原定位 `line 1, column 9` | E207=Watt/cm2；原分類D207=量測通道或來源分析量 | 原始電壓／訊號、W輻射功率及W/m²通量須逐欄校準，不能直接替換。 | 僅供結論來源／條件核對；未建立數值trial join |
| 熱通量／輻射 | `物理參數!C208:I208`；G208=`Radiometer Time；RADIOMETER_100HZ_FRAME_TIME(GMT)`；原定位 `line 34, column 3` | E208=未由欄名確認；原分類D208=量測通道或來源分析量 | 原始電壓／訊號、W輻射功率及W/m²通量須逐欄校準，不能直接替換。 | 僅供結論來源／條件核對；未建立數值trial join |
| 燃燒／點火／老化時間 | `物理參數!C209:I209`；G209=`TP_PARAMETER_BURN_TO_COMPLETION_TIME(N/A)`；原定位 `line 1, column 56` | E209=N/A（來源未給物理單位）；原分類D209=儀器設定／控制參數 | protocol/history及postevent response分開，熱焰／冷焰／可見端點不混。 | 僅供結論來源／條件核對；未建立數值trial join |
| 硬體電壓／電流／功率 | `物理參數!C210:I210`；G210=`ICM_LASER_CURRENT(Adc)`；原定位 `line 1, column 22` | E210=Adc；原分類D210=原始訊號或狀態 | 儀器／硬體原始通道或控制；不自動代表燃燒熱釋放。 | 僅供結論來源／條件核對；未建立數值trial join |
| 硬體電壓／電流／功率 | `物理參數!C211:I211`；G211=`POWER(N/A)`；原定位 `line 1, column 30` | E211=N/A（來源未給物理單位）；原分類D211=原始訊號或狀態 | 儀器／硬體原始通道或控制；不自動代表燃燒熱釋放。 | 僅供結論來源／條件核對；未建立數值trial join |
| 點火功率／電壓／電流 | `物理參數!C212:I212`；G212=`TP_PARAMETER_IGNITER_ON_TIME(N/A)`；原定位 `line 1, column 54` | E212=N/A（來源未給物理單位）；原分類D212=儀器設定／控制參數 | 點火設定／history；電壓或電流不自動等於熱功率。 | 僅供結論來源／條件核對；未建立數值trial join |
| 點火功率／電壓／電流 | `物理參數!C213:I213`；G213=`TP_PARAMETER_IGNITER_WATTAGE(Watts)`；原定位 `line 1, column 55` | E213=Watts；原分類D213=儀器設定／控制參數 | 點火設定／history；電壓或電流不自動等於熱功率。 | 僅供結論來源／條件核對；未建立數值trial join |
| 點火功率／電壓／電流 | `物理參數!C214:I214`；G214=`IGNITER_CURRENT_MONITOR(Adc)`；原定位 `line 1, column 21` | E214=Adc；原分類D214=量測或設定 | 點火設定／history；電壓或電流不自動等於熱功率。 | 僅供結論來源／條件核對；未建立數值trial join |
| 點火功率／電壓／電流 | `物理參數!C215:I215`；G215=`IGNITER_POWER_ENABLE(N/A)；IGNITER_POWER_STATUS(N/A)`；原定位 `line 1, column 14` | E215=N/A（來源未給物理單位）；原分類D215=量測或設定 | 點火設定／history；電壓或電流不自動等於熱功率。 | 僅供結論來源／條件核對；未建立數值trial join |
| 點火功率／電壓／電流 | `物理參數!C216:I216`；G216=`IGNITER_VOLTAGE_MONITOR_1(Vdc)；IGNITER_VOLTAGE_MONITOR_2(Vdc)`；原定位 `line 1, column 17` | E216=Vdc；原分類D216=量測或設定 | 點火設定／history；電壓或電流不自動等於熱功率。 | 僅供結論來源／條件核對；未建立數值trial join |
| 點火功率／電壓／電流 | `物理參數!C217:I217`；G217=`IGNITER_WATTAGE(Watts)`；原定位 `line 1, column 13` | E217=Watts；原分類D217=量測或設定 | 點火設定／history；電壓或電流不自動等於熱功率。 | 僅供結論來源／條件核對；未建立數值trial join |
| 點火功率／電壓／電流 | `物理參數!C218:I218`；G218=`Igniter On Time (milliseconds): 1300 Igniter Wattage: 8.03；Igniter On Time (milliseconds): 1500 Igniter Wattage: 1.92`；原定位 `RDTST01!R2C1` | E218=milliseconds；原分類D218=量測或設定 | 點火設定／history；電壓或電流不自動等於熱功率。 | 僅供結論來源／條件核對；未建立數值trial join |
| 點火功率／電壓／電流 | `物理參數!C219:I219`；G219=`HFRHR, HIBMS and Color Camera images/FCI files start at 2 seconds before the igniter on time.；Ignition Time；IGNITER_POWER_STATUS`；原定位 `line 30, column 2` | E219=未由欄名確認；原分類D219=量測或設定 | 點火設定／history；電壓或電流不自動等於熱功率。 | 僅供結論來源／條件核對；未建立數值trial join |

- 每列原檔路徑在Excel H欄、原欄位／定位在G/I欄；完整列與source SHA見 [factor_crosswalk.json](</C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/data_inventory/factor_crosswalk.json>)。
- 每個原欄名的存在不證明是操縱變因；是否controlled必須在匹配試次／protocol中另核。`microgravity`不填成精確g=0；缺失T、g或U保留Unknown。

### 此子集的數值可用性

| 標準欄位 | finite／總列 | source zero | min–max（標準單位） |
|---|---|---|---|
| `std_pressure_Pa` | 0/4 | 0 | Unknown / 未核–Unknown / 未核 Pa |
| `std_oxygen_fraction` | 4/4 | 0 | 0.17–0.3 mole fraction [1] |
| `std_ambient_temperature_K` | 4/4 | 0 | 298.15–298.15 K |

這是來源值分布與可用性，沒有新回歸或控制其他變因；數值範圍不是安全操作範圍。

### 文獻審核紀錄與資料關係

完整受限範圍見 [FLEX/FLEX2 review JSON](</C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/literature/flex_flex2_literature.json>)（本次讀到16筆review_records；metadata、選頁全文與remote indexed-only狀態分開）。

- **FLEX2-SRD2010 — Science Requirements Document: Fundamental Studies in Droplet Combustion and Flame Extinguishment in Microgravity (FLEX-2)**；DOI/NTRS=未列；官方URL=未列。
  - edition SHA=3ea215485f65c4c08fd86b5d74f0bf4435d45b2e2d5e4ac6c33820316175e562；來源 `C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\03_其他文件\其他研究文件_正文類型待確認\第一批下載\PSI-68_FLEX-2\Science Documents\PSI-68_Science Documents_FLEX-2 SRD Final.pdf`；已讀physical pages=[1, 9, 10, 11, 12, 13, 14, 15, 16, 43, 44]；範圍：selected original pages; source SHA verified。
  - 試次關係：unknown；本子集不因燃料同名自動配對。
- **FLEX2-DOD — FLEX-2 Description of Data**；DOI/NTRS=未列；官方URL=未列。
  - edition SHA=e4a0ccea1a5a08aa60f6346055b43a382fd0ebbce4fb6fe9ae6983d08fbba56c；來源 `C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\03_其他文件\其他研究文件_正文類型待確認\第一批下載\PSI-68_FLEX-2\Science Documents\PSI-68_Science Documents_FLEX-2 DoD.docx`；已讀physical pages=[]；範圍：All nonempty text paragraphs of short DOCX read; no fabricated PDF pages。
  - 試次關係：group organization only；本子集不因燃料同名自動配對。
- **FLEX2-HARDWARE — FLEX-2 Hardware Presentation**；DOI/NTRS=未列；官方URL=未列。
  - edition SHA=fe807d053060d2c90f09804d8b2f0ff06082d0c1f01a277fb5f7d7718cb167c3；來源 `C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\03_其他文件\簡報與海報\第一批下載\PSI-68_FLEX-2\Engineering Documents\PSI-68_Engineering Documents_FLEX-2 Hardware Presentation.ppt`；已讀physical pages=[]；範圍：SHA-bound selected-page/legacy-PPT audit reused from specified prior receipt; not new full-document read。
  - 試次關係：explicit source labels only; no inferred fuel/D0-based raw join；本子集不因燃料同名自動配對。
- **FLEX-ALKANE-D0-2013 — Effect of Varying the Initial Diameter of n-Octane and n-Decane Droplets over a Wide Range on the Spherically Symmetric Combustion Process: International Space Station and Ground-based Experiments**；DOI/NTRS=未列；官方URL=未列。
  - edition SHA=6f1f971138effa8800466e33f0a694d54329263bd5a41bae0e1a3f1856de0f0e；來源 `C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\03_其他文件\簡報與海報\第一批下載\PSI-69_FLEX\Presentations\PSI-69_Presentations_2G11-070HE-0310.pdf`；已讀physical pages=[2, 3, 4, 6, 7, 9, 10]；範圍：SHA-bound selected-page/legacy-PPT audit reused from specified prior receipt; not new full-document read。
  - 試次關係：explicit source labels only; no inferred fuel/D0-based raw join；本子集不因燃料同名自動配對。
- 本文件沒有新增英文直接引句；不重複既有quote ledger。

## 多結論比較

- **共同結論：** 配方表與規劃文件都描述燃料／氣氛／尺寸等條件；它們沒有提供這4個選項的觀測Y。
- **不同結論：** 不同燃料、P、O2/N2/He/CO2、D0、fiber與點火history需保留；同名microgravity或同一CIR/MDCA不建立控制匹配。
- **是否使用相同資料：** shared_investigation_unjoined：本來源是配置列；外部論文有operation-ID時也不能自動對應本列。
- **衝突或未解差異：** 未回源或未核單位、缺值、零值／extrapolation與版本差異均保留；不藉選來源消除。

## 消防洞見

| 預防／偵測／撲滅 | 洞見 | 依據結論 | 直接支持或新增假說 | 缺少的判別實驗 |
|---|---|---|---|---|
| 預防 | 這些燃料配方需要逐次資料，才能比較實際火災持續／熄滅；不能依配方表選安全燃料。 | C01–C02 | source-bounded研究條件；安全策略是新增假說 | 同配方／P／O2／D0／fiber／點火history的重複實驗與失敗樣本 |
| 偵測 | 表內沒有警報／煙訊號試驗，尚不能比較偵測器。 | C02–C03 | 量測端點邊界；沒有alarm qualification | 同步光學、溫度／物種／煙霧與真正警報反應，含盲點／誤報 |
| 撲滅／抑制 | 預配稀釋氣與液滴試驗不是艙體藥劑注入試驗；不給He/CO2用量、再燃機率或設備效能。 | C01–C03 | 限制＋待驗證的持續燃燒監測構想 | 確切注入時序／劑量、全相位反應、殘餘液體、再點火與通風／尺度對照 |

## 資料缺口與文獻覆蓋

- 逐次熱狀態／U／numeric g／完整物性與history缺失時，`classical_burning_constant`或`cool_stage_rate`只能列公式，不能填預設值產生理論曲線。
- 支撐fiber、FOV loss、phase/extrapolation與不完整分析需保留；CFI cool-endpoint source zero不能自動稱「已耗盡」。
- 文獻全文／選頁／metadata-only／remote lead已分開。沒有聲稱檢索完整、每個source量測有效，或所有條件都完成燃燒。
- 數值與原始路徑僅離線MD／JSON；不納入Git、不改原檔。
