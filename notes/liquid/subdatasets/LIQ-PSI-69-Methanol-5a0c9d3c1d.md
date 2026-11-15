# PSI-69 / Methanol / source_summary_test_table

`LIQ-PSI-69-Methanol-5a0c9d3c1d`

## 資料身分與可追溯範圍

- 類別：Test；架構：`CIR_MDCA_isolated_liquid_droplet`；燃料label原樣保留，混合比例basis未核時不假定mass/volume。
- 觀測分母：157筆試次摘要列；unique reported test-id=157，verified independent physical tests仍Unknown。
- source rows：`2, 3, 4, 5, 6, 7, 11, 12, 14, 15, 16, 17, 18, 21, 22, 23, 26, 27, 30, 31, 34, 35, 37, 38, 39, 41, 42, 45, 46, 47, 49, 55, 56, 59, 60, 61, 62, 66, 67, 68, 69, 72, 76, 77, 78, 79, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 98, 99, 100, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 122, 123, 124, 125, 126, 127, 128, 129, 141, 142, 143, 144, 145, 146, 147, 148, 152, 153, 154, 158, 159, 160, 161, 162, 163, 164, 165, 167, 168, 169, 170, 171, 177, 178, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 200, 201, 202, 203, 204, 216, 217, 218, 219, 220, 221, 222, 223, 224, 226, 227, 228, 240, 241, 242, 243, 245, 246, 247, 248, 249, 252, 253, 254, 255, 256, 257, 258, 263, 264, 265, 266, 267, 272, 273`。standardized physical CSV rows：`1663, 1664, 1665, 1666, 1667, 1668, 1669, 1670, 1671, 1672, 1673, 1674, 1675, 1676, 1677, 1678, 1679, 1680, 1681, 1682, 1683, 1684, 1685, 1686, 1687, 1688, 1689, 1690, 1691, 1692, 1693, 1694, 1695, 1696, 1697, 1698, 1699, 1700, 1701, 1702, 1703, 1704, 1705, 1706, 1707, 1708, 1709, 1710, 1711, 1712, 1713, 1714, 1715, 1716, 1717, 1718, 1719, 1720, 1721, 1722, 1723, 1724, 1725, 1726, 1727, 1728, 1729, 1730, 1731, 1732, 1733, 1734, 1735, 1736, 1737, 1738, 1739, 1740, 1741, 1742, 1743, 1744, 1745, 1746, 1747, 1748, 1749, 1750, 1751, 1752, 1753, 1754, 1755, 1756, 1757, 1758, 1759, 1760, 1761, 1762, 1763, 1764, 1765, 1766, 1767, 1768, 1769, 1770, 1771, 1772, 1773, 1774, 1775, 1776, 1777, 1778, 1779, 1780, 1781, 1782, 1783, 1784, 1785, 1786, 1787, 1788, 1789, 1790, 1791, 1792, 1793, 1794, 1795, 1796, 1797, 1798, 1799, 1800, 1801, 1802, 1803, 1804, 1805, 1806, 1807, 1808, 1809, 1810, 1811, 1812, 1813, 1814, 1815, 1816, 1817, 1818, 1819`。
- 存取：[liquid_subdatasets.json](</C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/data_inventory/liquid_subdatasets.json>)；[numeric fixture](</C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/data_inventory/visualization_data.json>)。
- **來源檔：** `C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\01_實驗資料\第一批下載\PSI-69_FLEX\Experimental table\PSI-69_Experimental table_FLEX.csv`
- **SHA256：** `37c88ce8ae9391b7544ff630a45ce87543d04d317cdbfbed104fe7d5c27e1b96`
- **原始儲存／版本：** `public_data_20261104_155720/01_PSI/PSI-69_FLEX/Experimental table/PSI-69_Experimental table_FLEX.csv`；source identity=`6792be99b7b6ff8e65037e3a`；version=`1`。
- **NASA／DOI：** https://psi.nasa.gov/physci/repo/data/investigations/PSI-69；DOI=10.60555/mbq8-0451。

## 文獻結果與視覺化程式

下表把物理量的來源值、量測定義、metadata與缺口分別標示；metadata／限制列不是物理實驗結果。

| 結論 ID | 文獻／頁或圖 | 結果與端點 | 使用的資料子集 | 公式／參數來源 | 展示程式 | 證據角色 |
|---|---|---|---|---|---|---|
| C01 | FLEX CSV；FLEX-TP2015 AppendixA.1 physicalp25；TableIX | 平均液滴D²燃燒率常數：finite 151/157，範圍2e-07–7.4e-07 m²/s | 此燃料source rows；不同end-type保留 | K是同圖像D²縮減；Dext不是火焰直徑 | Test002 sourcecase可用 | **來源實驗縮減結果**；不作因果係數 |
| C02 | FLEX CSV；FLEX-TP2015 AppendixA.1 physicalp25；TableIX | 可見焰消失時剩餘液滴直徑：finite 117/157，範圍0.0004–0.00396 m | 此燃料source rows；不同end-type保留 | K是同圖像D²縮減；Dext不是火焰直徑 | Test002 sourcecase可用 | **來源實驗縮減結果**；不作因果係數 |
| C03 | FLEX-TP2015 p25；FLEX-ISS2014 p4 | 相機的液滴等效面積、UV與可見焰邊界是不同觀測 | 本表沒有完整相機／逐時相位聯結 | 光學定義與來源擬合窗需另核 | prepare_visualization.py分通道；viewer.js顯示source role | **量測定義／限制，非新增物理結果** |
| C04 | Test002 XLS Test002!D3:D5，C57:C198/F57:F198；CSV Test#2/20CAL10 | 同一sourcecase的K為0.5356與0.60 mm²/s；D0=1.850197784與1.86mm，版本差異未解 | 一次燃燒的142 source-window frames；另有664個液滴、191UV、140可見焰source points | d2_history以各來源K/D0²重建；既有0.535579…fit receipt未重跑 | physics_models.py::d2_history；viewercase PSI69-FLEX-TEST002 | **確切同case衝突＋同源診斷**，非獨立預測 |

### 真實程式與展示範圍

- [physics_models.py](</C:/Users/User/Documents/ChatGPT/Nasa Hackathon/research/liquid_combustion/physics_models.py>)：`d2_history`只用明示D0²/K做條件重建；`classical_burning_constant`需要匹配物性與氧質量分率；`cool_stage_rate`含effective NTC參數，不是測得火焰溫度。
- [prepare_visualization.py](</C:/Users/User/Documents/ChatGPT/Nasa Hackathon/research/liquid_combustion/prepare_visualization.py>)：保留各source block的x軸與實驗／來源模型角色；重播已發表數值，不是執行作者原solver。
- [web/viewer.js](</C:/Users/User/Documents/ChatGPT/Nasa Hackathon/research/liquid_combustion/web/viewer.js>)；入口 [http://127.0.0.1:8808/](http://127.0.0.1:8808/)。
- 目前入口有source case `PSI69-FLEX-TEST002`，請由case選單選取；不宣稱URL有未實作的case deep link。
- 本文件產出沒有fit/train、反推係數或重跑作者模型；輸入缺件時不生成理論數值。

## 因子與試驗目的

本節引用使用者Excel `C:\Users\User\Downloads\NASA_實驗目的_燃料_環境_物理參數總表_20261114.xlsx`，SHA256 `fac357147ff98acf3a2f76b2ddd88d2fbab9a500159cc5ca360bb2d3a236dae1`。來源分類是前一輪表頭盤點，不能直接升格為逐次校準量測或科學因果角色；原公式/cache未重算。

| 因子 | Excel sheet／cell與原表欄 | 單位與定義 | 操縱／控制／應變／未確立 | 結論使用方式 |
|---|---|---|---|---|
| 一氧化碳濃度 | `物理參數!C220:I220`；G220=`CO initial ambient composition; mole fraction`；原定位 `line 1, column 9` | E220=未由欄名確認；原分類D220=量測通道 | 索引候選，需有效原欄、單位與校準；亂碼不能證明CO量測。 | 僅供結論來源／條件核對；未建立數值trial join |
| 二氧化碳濃度 | `物理參數!C221:I221`；G221=`CO2；0.70 atm ambient environment. This was the first successful test after switching from the high CO2`；原定位 `line 1, column 4` | E221=未由欄名確認；原分類D221=量測或條件值 | 稀釋氣初始設定與燃燒產物應變值必須分開。 | 僅供結論來源／條件核對；未建立數值trial join |
| 光電／離子偵測訊號 | `物理參數!C222:I222`；G222=`1.0 atm ambient environment. The droplet remains within the FOV of all the cameras. This was a 'calibration' run using cabin air and the LLUV setting was not optimal…（完整原欄見crosswalk）`；原定位 `line 25, column 2` | E222=未由欄名確認；原分類D222=儀器設定／控制參數 | 儀器設定／訊號；不直接等於煙濃度或經合格認證的火警反應。 | 僅供結論來源／條件核對；未建立數值trial join |
| 其他氣體組成／濃度 | `物理參數!C223:I223`；G223=`O initial ambient composition; mole fraction；N initial ambient composition; mole fraction；He initial ambient composition; mole fraction；0.70 atm ambient environment.…（完整原欄見crosswalk）`；原定位 `line 1, column 7` | E223=未由欄名確認；原分類D223=條件或分析量 | 初始成分／來源分析量需按欄定義；不因分類名稱當實測。 | 僅供結論來源／條件核對；未建立數值trial join |
| 壓力 | `物理參數!C224:I224`；G224=`FCU_MP_PT16(PSIA)；FCU_MP_PT17(PSIA)；FCU_MP_PT28(PSIA)；FCU_MP_PT29(PSIA)；FCU_PT16_INDEX_0(PSIA)；FCU_PT16_INDEX_1(PSIA)；FCU_PT16_INDEX_2(PSIA)；FCU_PT16_INDEX_3(PSIA)；F…（完整原欄見crosswalk）`；原定位 `line 1, column 2` | E224=PSIA；原分類D224=量測或設定 | 環境初始／設定條件；原摘要之absolute ambient已核時才使用；單一欄名不能證明因果操縱。 | 僅供結論來源／條件核對；未建立數值trial join |
| 壓力 | `物理參數!C225:I225`；G225=`P16 (psia)；P17 (psia)；P28 (psia)；P29 (psia)`；原定位 `Test 009!R10C26` | E225=psia；原分類D225=量測或設定 | 環境初始／設定條件；原摘要之absolute ambient已核時才使用；單一欄名不能證明因果操縱。 | 僅供結論來源／條件核對；未建立數值trial join |
| 壓力 | `物理參數!C226:I226`；G226=`Ambient pressure; mmHg；Average PSIA`；原定位 `line 1, column 6` | E226=未由欄名確認；原分類D226=量測或設定 | 環境初始／設定條件；原摘要之absolute ambient已核時才使用；單一欄名不能證明因果操縱。 | 僅供結論來源／條件核對；未建立數值trial join |
| 尺寸／幾何 | `物理參數!C227:I227`；G227=`GAIN_POSITION(N/A)；TP_PARAMETER_NEEDLE_DISPENSE_POSITION_1(N/A)；TP_PARAMETER_NEEDLE_DISPENSE_POSITION_2(N/A)；TP_PARAMETER_IGNITER_IGNITION_POSITION_1(N/A)；TP_PARAMET…（完整原欄見crosswalk）`；原定位 `line 1, column 26` | E227=N/A（來源未給物理單位）；原分類D227=儀器設定／控制參數 | 逐欄核對硬體、液滴、座標、指令的角色；不可generic diameter。 | 僅供結論來源／條件核對；未建立數值trial join |
| 尺寸／幾何 | `物理參數!C228:I228`；G228=`ZOOM_POSITION(N/A)；FOCUS_POSITION(N/A)；MEMORY_LAST_ACCESS_POSITION(N/A)；SHUTTER_POSITION(N/A)；IRIS_POSITION(N/A)；BRIGHT_POSITION(N/A)；EXPOSURE_COMP_POSITION(N/A)`；原定位 `line 1, column 2` | E228=N/A（來源未給物理單位）；原分類D228=裝置或樣本條件 | 逐欄核對硬體、液滴、座標、指令的角色；不可generic diameter。 | 僅供結論來源／條件核對；未建立數值trial join |
| 尺寸／幾何 | `物理參數!C229:I229`；G229=`Dext (mm) =；x (mm)；y(mm)；UV diameter (mm)；D Ext (mm)；y (mm)`；原定位 `line 21, column 1` | E229=mm；原分類D229=裝置或樣本條件 | 逐欄核對硬體、液滴、座標、指令的角色；不可generic diameter。 | 僅供結論來源／條件核對；未建立數值trial join |
| 尺寸／幾何 | `物理參數!C230:I230`；G230=`The following raw image files have missing gaps；The following raw image files have gaps；1.0 atm ambient environment. There was very little droplet motion after deplo…（完整原欄見crosswalk）`；原定位 `line 1` | E230=未由欄名確認；原分類D230=裝置或樣本條件 | 逐欄核對硬體、液滴、座標、指令的角色；不可generic diameter。 | 僅供結論來源／條件核對；未建立數值trial join |
| 影像／光譜設定 | `物理參數!C231:I231`；G231=`IPSU_TP_CAMERA(N/A)；DCM_MP_CAM_PIXEL_OFFSET(N/A)；DCM_MP_CAM_FRAME_RATE(N/A)；FOCUS_NEAR_LIMIT(N/A)；AUTO_FOCUS_SENSITIVITY(N/A)；DIGITAL_ZOOM(N/A)；FOCUS_MODE(N/A)；CAMER…（完整原欄見crosswalk）`；原定位 `line 1, column 2` | E231=N/A（來源未給物理單位）；原分類D231=儀器設定或影像座標 | 量測條件／光學設定，不是物理應變值。 | 僅供結論來源／條件核對；未建立數值trial join |
| 影像／光譜設定 | `物理參數!C232:I232`；G232=`Color images；ColorCamTime_sec；at 15 frames per second；the MDCA color camera；Frames per Second；For the Color camera (IPSU4)；starting at frame 151 several frames are r…（完整原欄見crosswalk）`；原定位 `line 14` | E232=未由欄名確認；原分類D232=儀器設定或影像座標 | 量測條件／光學設定，不是物理應變值。 | 僅供結論來源／條件核對；未建立數值trial join |
| 影像／光譜設定 | `物理參數!C233:I233`；G233=`1.0 atm ambient environment. The droplet stays within the FOV of all the cameras. This is a 'calibration' run and the LLUV camera settings were not optimized. As a r…（完整原欄見crosswalk）`；原定位 `line 25, column 2` | E233=未由欄名確認；原分類D233=儀器設定／控制參數 | 量測條件／光學設定，不是物理應變值。 | 僅供結論來源／條件核對；未建立數值trial join |
| 氧濃度 | `物理參數!C234:I234`；G234=`O2；Free-floating methanol droplet burning in a 0.14/0.85 O2/N2；Fiber-supported heptane droplet burning in a 0.17/0.63 O2/N2；Fiber-supported methanol droplet burning …（完整原欄見crosswalk）`；原定位 `line 1, column 2` | E234=未由欄名確認；原分類D234=量測或條件值 | 初始氣氛或列舉配方選項；各物種basis/scope分開。 | 僅供結論來源／條件核對；未建立數值trial join |
| 流速／通風 | `物理參數!C235:I235`；G235=`TP_PARAMETER_DISPENSER_VELOCITY_1(N/A)；TP_PARAMETER_DISPENSER_VELOCITY_2(N/A)；TP_PARAMETER_FIBER_INDEXING_VELOCITY(N/A)；TP_PARAMETER_FLOW_NOZZLE_1_SPEED(N/A)；TP_PARA…（完整原欄見crosswalk）`；原定位 `line 1, column 37` | E235=N/A（來源未給物理單位）；原分類D235=儀器設定／控制參數 | 設定／相對流速或原始通道待核；液滴漂移、風扇顯示、燃料供應不混用。 | 僅供結論來源／條件核對；未建立數值trial join |
| 流速／通風 | `物理參數!C236:I236`；G236=`FLOW_NOZZLE_1_SPEED(N/A)；FLOW_NOZZLE_2_SPEED(N/A)`；原定位 `line 1, column 19` | E236=N/A（來源未給物理單位）；原分類D236=量測或設定 | 設定／相對流速或原始通道待核；液滴漂移、風扇顯示、燃料供應不混用。 | 僅供結論來源／條件核對；未建立數值trial join |
| 流速／通風 | `物理參數!C237:I237`；G237=`0.70 atm ambient environment. The droplet deploys with a relatively high (~ 6 mm/sec) NW drift velocity. The burn time is relatively short and the droplet stays with…（完整原欄見crosswalk）`；原定位 `line 25, column 2` | E237=未由欄名確認；原分類D237=量測或設定 | 設定／相對流速或原始通道待核；液滴漂移、風扇顯示、燃料供應不混用。 | 僅供結論來源／條件核對；未建立數值trial join |
| 液滴直徑／面積 | `物理參數!C238:I238`；G238=`leaving the FOV and then reapperaing for a short time before disappearing again. The glow from the igniter influences the droplet size measurement early`；原定位 `line 25, column 4` | E238=未由欄名確認；原分類D238=儀器設定／控制參數 | D0是初始狀態；D(t)、熄滅D與影像面積是應變／來源影像分析；不是火焰尺寸。 | 僅供結論來源／條件核對；未建立數值trial join |
| 液滴直徑／面積 | `物理參數!C239:I239`；G239=`(D/D0)2`；原定位 `Test 009!R10C7` | E239=D/D0；原分類D239=影像／來源分析量 | D0是初始狀態；D(t)、熄滅D與影像面積是應變／來源影像分析；不是火焰尺寸。 | 僅供結論來源／條件核對；未建立數值trial join |
| 液滴直徑／面積 | `物理參數!C240:I240`；G240=`D0 (mm) =；D0 (mm)；Extinction Diameter (mm)`；原定位 `line 18, column 1` | E240=mm；原分類D240=影像／來源分析量 | D0是初始狀態；D(t)、熄滅D與影像面積是應變／來源影像分析；不是火焰尺寸。 | 僅供結論來源／條件核對；未建立數值trial join |
| 液滴直徑／面積 | `物理參數!C241:I241`；G241=`Droplet initial diameter; mm；Visible flame extinction diameter; mm；1.0 atm (nominally air) ambient environment. The droplet stays in HiBMS FOV for most of lifetime. …（完整原欄見crosswalk）`；原定位 `line 1, column 11` | E241=未由欄名確認；原分類D241=影像／來源分析量 | D0是初始狀態；D(t)、熄滅D與影像面積是應變／來源影像分析；不是火焰尺寸。 | 僅供結論來源／條件核對；未建立數值trial join |
| 溫度 | `物理參數!C242:I242`；G242=`FCU_MP_TM1(Deg C)；FCU_MP_TM2(Deg C)；FCU_MP_TM3(Deg C)；FCU_MP_TM4(Deg C)；T1 (Deg C)；T2 (Deg C)；T3 (Deg C)；T4 (Deg C)`；原定位 `line 1, column 6` | E242=Deg C；原分類D242=量測或設定 | 環境氣體、初始液體、火焰／表面、點火器與property reference分開；儀器時序不是溫度。 | 僅供結論來源／條件核對；未建立數值trial join |
| 溫度 | `物理參數!C243:I243`；G243=`FCU_MP_TM3(DegC)；FCU_MP_TM4(DegC)`；原定位 `line 1, column 8` | E243=DegC；原分類D243=量測或設定 | 環境氣體、初始液體、火焰／表面、點火器與property reference分開；儀器時序不是溫度。 | 僅供結論來源／條件核對；未建立數值trial join |
| 溫度 | `物理參數!C244:I244`；G244=`Relative Pressure and Temperature Time (s)`；原定位 `Test 009!R10C25` | E244=s；原分類D244=量測或設定 | 環境氣體、初始液體、火焰／表面、點火器與property reference分開；儀器時序不是溫度。 | 僅供結論來源／條件核對；未建立數值trial join |
| 溫度 | `物理參數!C245:I245`；G245=`IPSU4 Ave PSIA Ave DegC；RR/FG Ave PSIA Ave DegC；Average Deg C`；原定位 `line 36, column 9` | E245=未由欄名確認；原分類D245=量測或設定 | 環境氣體、初始液體、火焰／表面、點火器與property reference分開；儀器時序不是溫度。 | 僅供結論來源／條件核對；未建立數值trial join |
| 火焰幾何／延燒 | `物理參數!C246:I246`；G246=`Flame diameter (mm)`；原定位 `Test 002!R7C19` | E246=mm；原分類D246=影像／來源分析量 | 來源定義的光學或模型邊界應變；不等於液滴或熱通量。 | 僅供結論來源／條件核對；未建立數值trial join |
| 火焰幾何／延燒 | `物理參數!C247:I247`；G247=`ColorCamFlameDiameter_mm；ColorCamFlameStandoff；the flame becomes undetectable in the LLUV midway through the burn. The LLUV flame size for this test. There is no evi…（完整原欄見crosswalk）`；原定位 `line 1, column 2` | E247=未由欄名確認；原分類D247=影像／來源分析量 | 來源定義的光學或模型邊界應變；不等於液滴或熱通量。 | 僅供結論來源／條件核對；未建立數值trial join |
| 熱通量／輻射 | `物理參數!C248:I248`；G248=`RADIOMETER_100HZ_FRAME_MILLISECONDS(N/A)`；原定位 `line 1, column 6` | E248=N/A（來源未給物理單位）；原分類D248=量測通道或來源分析量 | 原始電壓／訊號、W輻射功率及W/m²通量須逐欄校準，不能直接替換。 | 僅供結論來源／條件核對；未建立數值trial join |
| 熱通量／輻射 | `物理參數!C249:I249`；G249=`NARROW_BAND_RADIOMETER_SAMPLE_00(VDC)；NARROW_BAND_RADIOMETER_SAMPLE_01(VDC)；NARROW_BAND_RADIOMETER_SAMPLE_02(VDC)；NARROW_BAND_RADIOMETER_SAMPLE_03(VDC)；NARROW_BAND_R…（完整原欄見crosswalk）`；原定位 `line 1, column 9` | E249=VDC；原分類D249=量測通道或來源分析量 | 原始電壓／訊號、W輻射功率及W/m²通量須逐欄校準，不能直接替換。 | 僅供結論來源／條件核對；未建立數值trial join |
| 熱通量／輻射 | `物理參數!C250:I250`；G250=`NARROW_BAND_RADIOMETER_SAMPLE_00(Volts)；NARROW_BAND_RADIOMETER_SAMPLE_01(Volts)；NARROW_BAND_RADIOMETER_SAMPLE_02(Volts)；NARROW_BAND_RADIOMETER_SAMPLE_03(Volts)；NARRO…（完整原欄見crosswalk）`；原定位 `line 1, column 9` | E250=Volts；原分類D250=量測通道或來源分析量 | 原始電壓／訊號、W輻射功率及W/m²通量須逐欄校準，不能直接替換。 | 僅供結論來源／條件核對；未建立數值trial join |
| 熱通量／輻射 | `物理參數!C251:I251`；G251=`Relative Radiometer Time (s)`；原定位 `Test 002!R7C23` | E251=s；原分類D251=量測通道或來源分析量 | 原始電壓／訊號、W輻射功率及W/m²通量須逐欄校準，不能直接替換。 | 僅供結論來源／條件核對；未建立數值trial join |
| 熱通量／輻射 | `物理參數!C252:I252`；G252=`Radiometer Time；RADIOMETER_100HZ_FRAME_TIME(GMT)；NARROW_BAND_RADIOMETER_SAMPLE_00()；NARROW_BAND_RADIOMETER_SAMPLE_01()；NARROW_BAND_RADIOMETER_SAMPLE_02()；NARROW_BAND…（完整原欄見crosswalk）`；原定位 `line 35, column 3` | E252=未由欄名確認；原分類D252=量測通道或來源分析量 | 原始電壓／訊號、W輻射功率及W/m²通量須逐欄校準，不能直接替換。 | 僅供結論來源／條件核對；未建立數值trial join |
| 燃燒率／燃燒常數 | `物理參數!C253:I253`；G253=`kavg (mm2/s) =；K (mm2/s)；Burning Rate (mm2/s)`；原定位 `line 19, column 1` | E253=mm2/s；原分類D253=計算／分析參數 | 來源分析／擬合後的D²應變量；不是O2分子擴散係數或獨立輸入。 | 僅供結論來源／條件核對；未建立數值trial join |
| 燃燒率／燃燒常數 | `物理參數!C254:I254`；G254=`Burning rate; mm；high pressure ambients where we had significant deployment problems. The droplet has a high burning rate and stays in the HiBMS FOV the entire test.…（完整原欄見crosswalk）`；原定位 `line 1, column 13` | E254=未由欄名確認；原分類D254=計算／分析參數 | 來源分析／擬合後的D²應變量；不是O2分子擴散係數或獨立輸入。 | 僅供結論來源／條件核對；未建立數值trial join |
| 燃燒／點火／老化時間 | `物理參數!C255:I255`；G255=`TP_PARAMETER_BURN_TO_COMPLETION_TIME(N/A)`；原定位 `line 1, column 56` | E255=N/A（來源未給物理單位）；原分類D255=儀器設定／控制參數 | protocol/history及postevent response分開，熱焰／冷焰／可見端點不混。 | 僅供結論來源／條件核對；未建立數值trial join |
| 燃燒／點火／老化時間 | `物理參數!C256:I256`；G256=`Burn time; s；1.0 atm ambient environment. Neither the HiBMS or color camera IPSUs recorded any images for this test. The droplet burns for a short time to disruption…（完整原欄見crosswalk）`；原定位 `line 1, column 14` | E256=未由欄名確認；原分類D256=時序或處理條件 | protocol/history及postevent response分開，熱焰／冷焰／可見端點不混。 | 僅供結論來源／條件核對；未建立數值trial join |
| 硬體電壓／電流／功率 | `物理參數!C257:I257`；G257=`ICM_LASER_CURRENT(Adc)`；原定位 `line 1, column 22` | E257=Adc；原分類D257=原始訊號或狀態 | 儀器／硬體原始通道或控制；不自動代表燃燒熱釋放。 | 僅供結論來源／條件核對；未建立數值trial join |
| 硬體電壓／電流／功率 | `物理參數!C258:I258`；G258=`POWER(N/A)`；原定位 `line 1, column 30` | E258=N/A（來源未給物理單位）；原分類D258=原始訊號或狀態 | 儀器／硬體原始通道或控制；不自動代表燃燒熱釋放。 | 僅供結論來源／條件核對；未建立數值trial join |
| 點火功率／電壓／電流 | `物理參數!C259:I259`；G259=`TP_PARAMETER_IGNITER_ON_TIME(N/A)`；原定位 `line 1, column 54` | E259=N/A（來源未給物理單位）；原分類D259=儀器設定／控制參數 | 點火設定／history；電壓或電流不自動等於熱功率。 | 僅供結論來源／條件核對；未建立數值trial join |
| 點火功率／電壓／電流 | `物理參數!C260:I260`；G260=`TP_PARAMETER_IGNITER_WATTAGE(Watts)`；原定位 `line 1, column 55` | E260=Watts；原分類D260=儀器設定／控制參數 | 點火設定／history；電壓或電流不自動等於熱功率。 | 僅供結論來源／條件核對；未建立數值trial join |
| 點火功率／電壓／電流 | `物理參數!C261:I261`；G261=`IGNITER_CURRENT_MONITOR(Adc)`；原定位 `line 1, column 21` | E261=Adc；原分類D261=量測或設定 | 點火設定／history；電壓或電流不自動等於熱功率。 | 僅供結論來源／條件核對；未建立數值trial join |
| 點火功率／電壓／電流 | `物理參數!C262:I262`；G262=`IGNITER_POWER_ENABLE(N/A)；IGNITER_POWER_STATUS(N/A)`；原定位 `line 1, column 14` | E262=N/A（來源未給物理單位）；原分類D262=量測或設定 | 點火設定／history；電壓或電流不自動等於熱功率。 | 僅供結論來源／條件核對；未建立數值trial join |
| 點火功率／電壓／電流 | `物理參數!C263:I263`；G263=`IGNITER_VOLTAGE_MONITOR_1(Vdc)；IGNITER_VOLTAGE_MONITOR_2(Vdc)`；原定位 `line 1, column 17` | E263=Vdc；原分類D263=量測或設定 | 點火設定／history；電壓或電流不自動等於熱功率。 | 僅供結論來源／條件核對；未建立數值trial join |
| 點火功率／電壓／電流 | `物理參數!C264:I264`；G264=`IGNITER_WATTAGE(Watts)`；原定位 `line 1, column 13` | E264=Watts；原分類D264=量測或設定 | 點火設定／history；電壓或電流不自動等於熱功率。 | 僅供結論來源／條件核對；未建立數值trial join |
| 點火功率／電壓／電流 | `物理參數!C265:I265`；G265=`HIBMS and Color Camera images/FCI files start at 2 seconds before the igniter on time.；0.70 atm ambient environment. The droplet drifts S in the HiBMS FOV after depl…（完整原欄見crosswalk）`；原定位 `line 32, column 2` | E265=未由欄名確認；原分類D265=量測或設定 | 點火設定／history；電壓或電流不自動等於熱功率。 | 僅供結論來源／條件核對；未建立數值trial join |

- 每列原檔路徑在Excel H欄、原欄位／定位在G/I欄；完整列與source SHA見 [factor_crosswalk.json](</C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/data_inventory/factor_crosswalk.json>)。
- 每個原欄名的存在不證明是操縱變因；是否controlled必須在匹配試次／protocol中另核。`microgravity`不填成精確g=0；缺失T、g或U保留Unknown。

### 此子集的數值可用性

| 標準欄位 | finite／總列 | source zero | min–max（標準單位） |
|---|---|---|---|
| `std_initial_droplet_diameter_m` | 154/157 | 0 | 0.00161–0.00453 m |
| `std_hot_extinction_droplet_diameter_m` | 117/157 | 0 | 0.0004–0.00396 m |
| `std_pressure_Pa` | 156/157 | 0 | 70167.57–309267.9 Pa |
| `std_oxygen_fraction` | 157/157 | 0 | 0.12–0.34 mole fraction [1] |
| `std_ambient_nitrogen_fraction` | 157/157 | 0 | 0.09–0.88 mole fraction [1] |
| `std_ambient_helium_fraction` | 157/157 | 129 | 0–0.45 mole fraction [1] |
| `std_ambient_carbon_dioxide_fraction` | 157/157 | 82 | 0–0.7 mole fraction [1] |
| `std_ambient_temperature_K` | 0/157 | 0 | Unknown / 未核–Unknown / 未核 K |
| `std_duration_s` | 155/157 | 0 | 0.3–39.2 s |
| `std_burning_rate_constant_m2_s` | 151/157 | 0 | 2e-07–7.4e-07 m²/s |

這是來源值分布與可用性，沒有新回歸或控制其他變因；數值範圍不是安全操作範圍。

### 文獻審核紀錄與資料關係

完整受限範圍見 [FLEX/FLEX2 review JSON](</C:/Users/User/Documents/ChatGPT/Nasa Hackathon/output/liquid_combustion_evidence_20261115/literature/flex_flex2_literature.json>)（本次讀到16筆review_records；metadata、選頁全文與remote indexed-only狀態分開）。

- **FLEX-TP2015 — Detailed Results From the Flame Extinguishment Experiment (FLEX) March 2009 to December 2011**；DOI/NTRS=20150023456；官方URL=https://ntrs.nasa.gov/citations/20150023456。
  - edition SHA=b4f6ca983e2792c33a0b92220a791a818f426bb635b94f7fd33dc8c9c471e79d；來源 `C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\03_其他文件\研究報告與書章\第一批下載\02_NTRS_reports\FLEX\20150023456_20150023456.pdf`；已讀physical pages=[11, 25, 29, 34, 35, 160, 307]；範圍：selected original pages; source SHA verified。
  - 試次關係：exact report identifiers; selected prior report/CSV source audit reused, not global 284-to-274 reconciliation；本子集不因燃料同名自動配對。
  - **確切相同摘要子集（exact_subset）：** 報告明列identifier C13M201, H15M102在本燃料摘要ID中；其餘報告範圍與原始影格未全數join，不擴成全表same-data。
- **FLEX-ISS2014 — Droplet Combustion Experiments Aboard the International Space Station**；DOI/NTRS=10.1007/s12217-014-9372-2；官方URL=https://doi.org/10.1007/s12217-014-9372-2。
  - edition SHA=06d93043c0857dbb08b83e04f9b8f37cebfd304f685cc6de93c2f8bb517cda17；來源 `C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\02_論文全文\01_期刊論文與作者稿\Droplet Combustion Experiments Aboard the International Space Station__06d93043c0.pdf`；已讀physical pages=[1, 2, 4, 6, 9, 10]；範圍：selected original pages; source SHA verified。
  - 試次關係：unknown；本子集不因燃料同名自動配對。
- **FLEX-MEOH2013 — Methanol Droplet Combustion in Oxygen-Inert Environments in Microgravity**；DOI/NTRS=20130014061；官方URL=https://ntrs.nasa.gov/citations/20130014061。
  - edition SHA=1488bbb461f2ea0f97c2c2fab6ac0a01603a6837509ab6ac6d1ef02bbf72050b；來源 `C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\02_論文全文\02_會議論文與預印本\Methanol Droplet Combustion in Oxygen-Inert Environments in Microgravity__1488bbb461.pdf`；已讀physical pages=[1, 5, 6, 7, 9, 10]；範圍：selected original pages; source SHA verified。
  - 試次關係：paper run IDs exact; shared raw ID crosswalk not established here；本子集不因燃料同名自動配對。
- **FLEX-WATER2012 — Dynamics of Water Absorption and Evaporation During Methanol Droplet Combustion in Microgravity**；DOI/NTRS=20130010979；官方URL=https://ntrs.nasa.gov/citations/20130010979。
  - edition SHA=56e69491fe8af3a31e2f2e1732b0133d769b4de356815419d41c85651d0479d1；來源 `C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\03_其他文件\簡報與海報\第一批下載\PSI-69_FLEX\Presentations\PSI-69_Presentations_20130010979.pdf`；已讀physical pages=[3, 4, 7, 9, 10, 11, 12, 13, 14, 15]；範圍：SHA-bound selected-page/legacy-PPT audit reused from specified prior receipt; not new full-document read。
  - 試次關係：explicit source labels only; no inferred fuel/D0-based raw join；本子集不因燃料同名自動配對。
- **FLEX-OPTICAL2014 — Interpretation of Backlit Droplet Images from ISS Droplet Combustion Experiments**；DOI/NTRS=10.2478/gsr-2014-0007；官方URL=https://doi.org/10.2478/gsr-2014-0007。
  - edition SHA=a0a4a555cc5f050cc695eb29ced827e50f44d4df02beda74580b0e05f26d92c6；來源 `C:\Users\User\Documents\ChatGPT\Nasa Hackathon\NASA_同事分享包_20261114\02_論文全文\01_期刊論文與作者稿\Interpretation of Backlit Droplet Images from ISS Droplet Combustion Experiments__a0a4a555cc.pdf`；已讀physical pages=[1, 4, 5, 7, 8, 9]；範圍：selected original pages; source SHA verified。
  - 試次關係：unknown；本子集不因燃料同名自動配對。
- 本文件沒有新增英文直接引句；不重複既有quote ledger。

## 多結論比較

- **共同結論：** 來源均把液滴初始／剩餘尺寸、相位端點與來源K視為不同quantity；不能把液滴直徑換成火焰大小。
- **不同結論：** 不同燃料、P、O2/N2/He/CO2、D0、fiber與點火history需保留；同名microgravity或同一CIR/MDCA不建立控制匹配。
- **是否使用相同資料：** 同一來源摘要表內可追source rows；對其他論文通常為shared_investigation_unjoined。上方僅在報告identifier直接命中時列exact_subset，其餘不提升成相同資料。
- **衝突或未解差異：** Methanol Test002保留0.5356／0.60與D0差異；來源處理版本、擬合窗／校準未解。

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
