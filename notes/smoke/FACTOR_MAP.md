# 煙霧因子與使用者 Excel 對照

總表是參數索引；各試次的設定、量測、來源計算和感測器狀態仍以原始來源定位。

## 參考 Excel 與盤點範圍

- path: C:\Users\User\Downloads\NASA_實驗目的_燃料_環境_物理參數總表_20261114.xlsx
- sha256: fac357147ff98acf3a2f76b2ddd88d2fbab9a500159cc5ca360bb2d3a236dae1
- role: secondary field-discovery reference, not raw data

## 使用者 Excel 實驗總覽

| 研究／位置 | 名稱 | 目的 | 材料 | 環境 | 因子索引 | 原表限制 |
| --- | --- | --- | --- | --- | --- | --- |
| PSI-101 / 實驗總覽 row28 | SAME-R | 研究煙霧顆粒尺寸、成長、老化與偵測器反應，改進粒子診斷。 | Kapton、Teflon、silicone、lampwick、Pyrell 等過熱材料，依試次核對。 | ISS 微重力；可控加熱、入口氣流、稀釋、混合與老化。 | 光電／離子偵測訊號、其他氣體組成／濃度、壓力、密度、尺寸／幾何、影像／光譜設定、流速／通風、溫度、燃燒／點火／老化時間、硬體電壓／電流／功率、粒子數濃度、粒子質量濃度、粒徑／粒子分布、質量流率、質量／質量損失、風扇／流量顯示設定、體積流量／MFC | 偵測器電壓、濃度量測與衍生粒徑分開；須保留通電／自測、背景、稀釋及公式異常。 |
| PSI-102 / 實驗總覽 row29 | SAME | 研究低重力煙霧粒徑分布與輸運，量測偵測器反應及材料質量損失。 | Teflon、Kapton、Silicone Rubber、Lampwick、Dibutyl Phthalate。 | ISS 微重力；受控過熱、5／10 cm/s 等原表氣流、取樣與老化。 | 光電／離子偵測訊號、其他氣體組成／濃度、壓力、尺寸／幾何、影像／光譜設定、流速／通風、溫度、燃燒／點火／老化時間、硬體電壓／電流／功率、粒子數濃度、粒子質量濃度、粒徑／粒子分布、質量流率、質量／質量損失、風扇／流量顯示設定、體積流量／MFC | 原表 8 列含材料條件摘要；工作簿可能混合 log、graph 與數據。 |

## 使用者 Excel 物理參數的精確定位

分類欄以下保留參考Excel原值，不表示已驗證物理分類。表頭核對只證明欄位身份，不證明儀器已校正。

| 研究 | Excel位置 | 參考Excel原分類 | 參考Excel原角色 | 單位原值 | 對應原始欄位／檔案 | 實際欄位核對 |
| --- | --- | --- | --- | --- | --- | --- |
| PSI-101 | 物理參數 row318; {"A": "A318", "B": "B318", "C": "C318", "D": "D318", "E": "E318", "F": "F318", "G": "G318", "H": "H318", "I": "I318", "J": "J318"} | 光電／離子偵測訊號 | 儀器原始訊號 | Volts | ISSDetectorObscurationMeasurement(Volts)；ISSDetectorScatterMeasurement(Volts)；STSDetectorMeasurement(Volts)；IonDetectorAMeasurement(Volts)；IonDetectorBMeasurement(Volts); 01_實驗資料/第一批下載/PSI-101_SAME-R/Raw Data/PSI-101_Raw Data_HKPData_gmt250_1.csv; line 1, column 22 | \[{"csv_line": 1, "column_1based": 22, "actual_header": "ISSDetectorObscurationMeasurement(Volts)", "is_one_of_reference_aliases": true, "locator_status": "original header from prior complete CSV profile"}\] |
| PSI-101 | 物理參數 row319; {"A": "A319", "B": "B319", "C": "C319", "D": "D319", "E": "E319", "F": "F319", "G": "G319", "H": "H319", "I": "I319", "J": "J319"} | 光電／離子偵測訊號 | 儀器原始訊號 | mg/m^3 | Dustrak scattering program predicted (mg/m^3); 01_實驗資料/第一批下載/PSI-101_SAME-R/Analyzed Data/PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx; SAME1 Flight Tests 8-27-09!R2C47 | \[{"target_sheet": "SAME1 Flight Tests 8-27-09", "target_cell": "AU2", "actual_header": "Dustrak scattering program   predicted (mg/m^3)", "exact_header_match": false, "locator_status": "literal source cell checked"}\] |
| PSI-101 | 物理參數 row320; {"A": "A320", "B": "B320", "C": "C320", "D": "D320", "E": "E320", "F": "F320", "G": "G320", "H": "H320", "I": "I320", "J": "J320"} | 光電／離子偵測訊號 | 儀器原始訊號 | volts | ISS Obscuration (volts)；ISS Detector Scatter (volts); 01_實驗資料/第一批下載/PSI-101_SAME-R/Analyzed Data/PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx; DBP!R2C48 | \[{"target_sheet": "DBP", "target_cell": "AV2", "actual_header": "ISS Obscuration (volts)", "exact_header_match": false, "locator_status": "literal source cell checked"}\] |
| PSI-101 | 物理參數 row321; {"A": "A321", "B": "B321", "C": "C321", "D": "D321", "E": "E321", "F": "F321", "G": "G321", "H": "H321", "I": "I321", "J": "J321"} | 光電／離子偵測訊號 | 儀器原始訊號 | 未由欄名確認 | Scattering Program Predicted geometric standard deviation；Scattering Predicted Davg mass；Number count to produce scattering alarm；Scattering to produce number alarm; 01_實驗資料/第一批下載/PSI-101_SAME-R/Analyzed Data/PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx; SAME1 Flight Tests 8-27-09!R2C49 | \[{"target_sheet": "SAME1 Flight Tests 8-27-09", "target_cell": "AW2", "actual_header": "Scattering Program Predicted geometric standard deviation", "exact_header_match": false, "locator_status": "literal source cell checked"}\] |
| PSI-101 | 物理參數 row322; {"A": "A322", "B": "B322", "C": "C322", "D": "D322", "E": "E322", "F": "F322", "G": "G322", "H": "H322", "I": "I322", "J": "J322"} | 其他氣體組成／濃度 | 儀器設定／控制參數 | mg/m3 | DustTrak A (mg/m3) Mpass_2nd offset, dilution and Gain corrected; 01_實驗資料/第一批下載/PSI-101_SAME-R/Analyzed Data/PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx; DBP!R2C67 | \[{"target_sheet": "DBP", "target_cell": "BO2", "actual_header": "DustTrak A (mg/m3) Mpass_2nd  offset, dilution and Gain corrected", "exact_header_match": false, "locator_status": "literal source cell checked"}\] |
| PSI-101 | 物理參數 row323; {"A": "A323", "B": "B323", "C": "C323", "D": "D323", "E": "E323", "F": "F323", "G": "G323", "H": "H323", "I": "I323", "J": "J323"} | 其他氣體組成／濃度 | 儀器設定／控制參數 | 未由欄名確認 | DustTrak A (mg/m3) (Drum) offset, dilution and Gain corrected; 01_實驗資料/第一批下載/PSI-101_SAME-R/Analyzed Data/PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx; Drum 8-2012!R2C59 | \[{"target_sheet": "Drum 8-2012", "target_cell": "BG2", "actual_header": "DustTrak A (mg/m3) (Drum)  offset, dilution and Gain corrected", "exact_header_match": false, "locator_status": "literal source cell checked"}\] |
| PSI-101 | 物理參數 row324; {"A": "A324", "B": "B324", "C": "C324", "D": "D324", "E": "E324", "F": "F324", "G": "G324", "H": "H324", "I": "I324", "J": "J324"} | 其他氣體組成／濃度 | 條件或分析量 | mg/m3 | DustTrak A calibratred and corrected for dilution (mg/m3)；DustTrak B calibratred and corrected for dilution (mg/m3)；DustTrak A corrected for dilution (mg/m3)；DustTrak B corrected for dilution (mg/m3); 01_實驗資料/第一批下載/PSI-101_SAME-R/Analyzed Data/PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx; DBP!R2C68 | \[{"target_sheet": "DBP", "target_cell": "BP2", "actual_header": "DustTrak A calibratred and corrected for dilution (mg/m3)", "exact_header_match": false, "locator_status": "literal source cell checked"}\] |
| PSI-101 | 物理參數 row325; {"A": "A325", "B": "B325", "C": "C325", "D": "D325", "E": "E325", "F": "F325", "G": "G325", "H": "H325", "I": "I325", "J": "J325"} | 其他氣體組成／濃度 | 條件或分析量 | 未由欄名確認 | DynamicDilutorSolenoid\[PN15\]；CommDiagADilutionSolenoid\[PN24\]；CommDiagBDilutionSolenoid\[PN27\]；Diluting A；Diluting B；Mpass_3rd offset and dilution corrected；CPC 100 nm cal, dilution corrected；CPC 600 nm cal, dilution corrected；CPC 1200 nm cal, dilution corrected；Dust Trak Dilution factor；其餘見原始欄位; 01_實驗資料/第一批下載/PSI-101_SAME-R/Raw Data/PSI-101_Raw Data_HKPData_gmt250_1.csv; line 1, column 73 | \[{"csv_line": 1, "column_1based": 73, "actual_header": "DynamicDilutorSolenoid\[PN15\]", "is_one_of_reference_aliases": true, "locator_status": "original header from prior complete CSV profile"}\] |
| PSI-101 | 物理參數 row326; {"A": "A326", "B": "B326", "C": "C326", "D": "D326", "E": "E326", "F": "F326", "G": "G326", "H": "H326", "I": "I326", "J": "J326"} | 壓力 | 量測或設定 | PSIA | MFCPressure(PSIA)；GN2MainPressure\[PN02\](PSIA)；VacuumPressure\[VR04\](PSIA)；DriveSidePressure\[BN02\](PSIA)；SampleSidePressure\[AT20\](PSIA)；GN2MainPressure\[PN02\](PSIA)/10; 01_實驗資料/第一批下載/PSI-101_SAME-R/Raw Data/PSI-101_Raw Data_HKPData_gmt250_1.csv; line 1, column 38 | \[{"csv_line": 1, "column_1based": 38, "actual_header": "MFCPressure(PSIA)", "is_one_of_reference_aliases": true, "locator_status": "original header from prior complete CSV profile"}\] |
| PSI-101 | 物理參數 row327; {"A": "A327", "B": "B327", "C": "C327", "D": "D327", "E": "E327", "F": "F327", "G": "G327", "H": "H327", "I": "I327", "J": "J327"} | 壓力 | 量測或設定 | PSIG | GN2RegulatedPressure\[PN12\](PSIG); 01_實驗資料/第一批下載/PSI-101_SAME-R/Raw Data/PSI-101_Raw Data_HKPData_gmt250_1.csv; line 1, column 42 | \[{"csv_line": 1, "column_1based": 42, "actual_header": "GN2RegulatedPressure\[PN12\](PSIG)", "is_one_of_reference_aliases": true, "locator_status": "original header from prior complete CSV profile"}\] |
| PSI-101 | 物理參數 row328; {"A": "A328", "B": "B328", "C": "C328", "D": "D328", "E": "E328", "F": "F328", "G": "G328", "H": "H328", "I": "I328", "J": "J328"} | 壓力 | 量測或設定 | 未由欄名確認 | Upstream P, psig；N2 flow (SLPM) = 0.308*(Regulated N2 pressure)^0.5283; 01_實驗資料/第一批下載/PSI-101_SAME-R/Analyzed Data/PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx; Gnd Verif. 8-2012!R42C44 | \[{"target_sheet": "Gnd Verif. 8-2012", "target_cell": "AR42", "actual_header": "Upstream P, psig", "exact_header_match": false, "locator_status": "literal source cell checked"}\] |
| PSI-101 | 物理參數 row329; {"A": "A329", "B": "B329", "C": "C329", "D": "D329", "E": "E329", "F": "F329", "G": "G329", "H": "H329", "I": "I329", "J": "J329"} | 密度 | 量測或來源分析量 | g/cc | Density (g/cc); 01_實驗資料/第一批下載/PSI-101_SAME-R/Analyzed Data/PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx; SAME1 Flight Tests 8-27-09!R2C57 | \[{"target_sheet": "SAME1 Flight Tests 8-27-09", "target_cell": "BE2", "actual_header": "Density (g/cc)", "exact_header_match": true, "locator_status": "literal source cell checked"}\] |
| PSI-101 | 物理參數 row330; {"A": "A330", "B": "B330", "C": "C330", "D": "D330", "E": "E330", "F": "F330", "G": "G330", "H": "H330", "I": "I330", "J": "J330"} | 密度 | 量測或來源分析量 | 未由欄名確認 | Particle density g/cc；density; 01_實驗資料/第一批下載/PSI-101_SAME-R/Analyzed Data/PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx; DBP!R2C82 | \[{"target_sheet": "DBP", "target_cell": "CD2", "actual_header": "Particle density g/cc", "exact_header_match": false, "locator_status": "literal source cell checked"}\] |
| PSI-101 | 物理參數 row331; {"A": "A331", "B": "B331", "C": "C331", "D": "D331", "E": "E331", "F": "F331", "G": "G331", "H": "H331", "I": "I331", "J": "J331"} | 尺寸／幾何 | 裝置或樣本條件 | #/cm3 | M0 best Diameter (#/cm3)；Mo Best Diameter (#/cm3); 01_實驗資料/第一批下載/PSI-101_SAME-R/Analyzed Data/PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx; 3-tests Compar.!R2C56 | \[{"target_sheet": "3-tests Compar.", "target_cell": "BD2", "actual_header": "M0 best Diameter (#/cm3)", "exact_header_match": false, "locator_status": "literal source cell checked"}\] |
| PSI-101 | 物理參數 row332; {"A": "A332", "B": "B332", "C": "C332", "D": "D332", "E": "E332", "F": "F332", "G": "G332", "H": "H332", "I": "I332", "J": "J332"} | 尺寸／幾何 | 裝置或樣本條件 | micro-m | Diameter of Average mass (micro-m); 01_實驗資料/第一批下載/PSI-101_SAME-R/Analyzed Data/PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx; DBP!R2C71 | \[{"target_sheet": "DBP", "target_cell": "BS2", "actual_header": "Diameter of Average mass (micro-m)", "exact_header_match": true, "locator_status": "literal source cell checked"}\] |
| PSI-101 | 物理參數 row333; {"A": "A333", "B": "B333", "C": "C333", "D": "D333", "E": "E333", "F": "F333", "G": "G333", "H": "H333", "I": "I333", "J": "J333"} | 尺寸／幾何 | 裝置或樣本條件 | micrometers | Computed arithmetic mean diameter (micrometers); 01_實驗資料/第一批下載/PSI-101_SAME-R/Analyzed Data/PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx; SAME1 Flight Tests 8-27-09!R2C42 | \[{"target_sheet": "SAME1 Flight Tests 8-27-09", "target_cell": "AP2", "actual_header": "Computed arithmetic mean diameter (micrometers)", "exact_header_match": true, "locator_status": "literal source cell checked"}\] |
| PSI-101 | 物理參數 row334; {"A": "A334", "B": "B334", "C": "C334", "D": "D334", "E": "E334", "F": "F334", "G": "G334", "H": "H334", "I": "I334", "J": "J334"} | 尺寸／幾何 | 裝置或樣本條件 | microns | Best Diameter Ion A/Ptrak Count Mean Diamter (microns)；Best Diameter Ion B/Ptrak Count Mean Diameter (microns); 01_實驗資料/第一批下載/PSI-101_SAME-R/Analyzed Data/PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx; SAME Ground Test Results!R2C39 | \[{"target_sheet": "SAME Ground Test Results", "target_cell": "AM2", "actual_header": "Best Diameter Ion A/Ptrak\nCount Mean Diamter (microns)", "exact_header_match": false, "locator_status": "literal source cell checked"}\] |
| PSI-101 | 物理參數 row335; {"A": "A335", "B": "B335", "C": "C335", "D": "D335", "E": "E335", "F": "F335", "G": "G335", "H": "H335", "I": "I335", "J": "J335"} | 尺寸／幾何 | 裝置或樣本條件 | mm/cm3 | M1 (mm/cm3)；M1 (Ion) Chamber constant based (mm/cm3); 01_實驗資料/第一批下載/PSI-101_SAME-R/Analyzed Data/PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx; 3-tests Compar.!R2C57 | \[{"target_sheet": "3-tests Compar.", "target_cell": "BE2", "actual_header": "M1 (mm/cm3)", "exact_header_match": false, "locator_status": "literal source cell checked"}\] |
| PSI-101 | 物理參數 row336; {"A": "A336", "B": "B336", "C": "C336", "D": "D336", "E": "E336", "F": "F336", "G": "G336", "H": "H336", "I": "I336", "J": "J336"} | 尺寸／幾何 | 裝置或樣本條件 | mm/cm^3 | M1 (mm/cm^3)；Ion B Mment (mm/cm^3); 01_實驗資料/第一批下載/PSI-101_SAME-R/Analyzed Data/PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx; DBP!R2C65 | \[{"target_sheet": "DBP", "target_cell": "BM2", "actual_header": "M1 (mm/cm^3)", "exact_header_match": false, "locator_status": "literal source cell checked"}\] |
| PSI-101 | 物理參數 row337; {"A": "A337", "B": "B337", "C": "C337", "D": "D337", "E": "E337", "F": "F337", "G": "G337", "H": "H337", "I": "I337", "J": "J337"} | 尺寸／幾何 | 裝置或樣本條件 | 未由欄名確認 | PositionerEnable；PositionerDirectionIn；PositionerClock；Diameter；Width；diameter equiv sphere；Position in Carousel；M0 best Diameter；Ion B Mment mm/cm^3；Ptraks vs. CPC (both units are counts/cm^3)；其餘見原始欄位; 01_實驗資料/第一批下載/PSI-101_SAME-R/Raw Data/PSI-101_Raw Data_HKPData_gmt250_1.csv; line 1, column 65 | \[{"csv_line": 1, "column_1based": 65, "actual_header": "PositionerEnable", "is_one_of_reference_aliases": true, "locator_status": "original header from prior complete CSV profile"}\] |
| PSI-101 | 物理參數 row338; {"A": "A338", "B": "B338", "C": "C338", "D": "D338", "E": "E338", "F": "F338", "G": "G338", "H": "H338", "I": "I338", "J": "J338"} | 影像／光譜設定 | 儀器設定或影像座標 | 未由欄名確認 | CameraPower；IlluminationLEDPower; 01_實驗資料/第一批下載/PSI-101_SAME-R/Raw Data/PSI-101_Raw Data_HKPData_gmt250_1.csv; line 1, column 97 | \[{"csv_line": 1, "column_1based": 97, "actual_header": "CameraPower", "is_one_of_reference_aliases": true, "locator_status": "original header from prior complete CSV profile"}\] |
| PSI-101 | 物理參數 row339; {"A": "A339", "B": "B339", "C": "C339", "D": "D339", "E": "E339", "F": "F339", "G": "G339", "H": "H339", "I": "I339", "J": "J339"} | 流速／通風 | 量測或設定 | cm/s | Inlet velocity (cm/s); 01_實驗資料/第一批下載/PSI-101_SAME-R/Experimental table/PSI-101_Experimental table_SAME-R.csv; line 1, column 5 | \[{"csv_line": 1, "column_1based": 5, "actual_header": "Inlet velocity (cm/s)", "is_one_of_reference_aliases": true, "locator_status": "literal experimental CSV header checked; index not assumed per-trial measurement"}\] |
| PSI-101 | 物理參數 row340; {"A": "A340", "B": "B340", "C": "C340", "D": "D340", "E": "E340", "F": "F340", "G": "G340", "H": "H340", "I": "I340", "J": "J340"} | 流速／通風 | 量測或設定 | cm/sec | Inlet Velocity (cm/sec); 01_實驗資料/第一批下載/PSI-101_SAME-R/Analyzed Data/PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx; DBP!R2C14 | \[{"target_sheet": "DBP", "target_cell": "N2", "actual_header": "Inlet Velocity (cm/sec)", "exact_header_match": true, "locator_status": "literal source cell checked"}\] |
| PSI-101 | 物理參數 row341; {"A": "A341", "B": "B341", "C": "C341", "D": "D341", "E": "E341", "F": "F341", "G": "G341", "H": "H341", "I": "I341", "J": "J341"} | 溫度 | 量測或設定 |  C | Sample Temperature ( C); 01_實驗資料/第一批下載/PSI-101_SAME-R/Analyzed Data/PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx; Pyrell R&T plots!R2C83 | \[{"target_sheet": "Pyrell R&T plots", "target_cell": "CE2", "actual_header": "Sample Temperature ( C)", "exact_header_match": true, "locator_status": "literal source cell checked"}\] |
| PSI-101 | 物理參數 row342; {"A": "A342", "B": "B342", "C": "C342", "D": "D342", "E": "E342", "F": "F342", "G": "G342", "H": "H342", "I": "I342", "J": "J342"} | 溫度 | 量測或設定 | DegC | GasPlumeTemperature(DegC)；MFCTemperature(DegC); 01_實驗資料/第一批下載/PSI-101_SAME-R/Raw Data/PSI-101_Raw Data_HKPData_gmt250_1.csv; line 1, column 20 | \[{"csv_line": 1, "column_1based": 20, "actual_header": "GasPlumeTemperature(DegC)", "is_one_of_reference_aliases": true, "locator_status": "original header from prior complete CSV profile"}\] |
| PSI-101 | 物理參數 row343; {"A": "A343", "B": "B343", "C": "C343", "D": "D343", "E": "E343", "F": "F343", "G": "G343", "H": "H343", "I": "I343", "J": "J343"} | 溫度 | 量測或設定 | 未由欄名確認 | Sample Temperature C；Sampel Temperature C; 01_實驗資料/第一批下載/PSI-101_SAME-R/Analyzed Data/PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx; Reduced data sheet!R2C19 | \[{"target_sheet": "Reduced data sheet", "target_cell": "S2", "actual_header": "Sample Temperature C", "exact_header_match": false, "locator_status": "literal source cell checked"}\] |
| PSI-101 | 物理參數 row344; {"A": "A344", "B": "B344", "C": "C344", "D": "D344", "E": "E344", "F": "F344", "G": "G344", "H": "H344", "I": "I344", "J": "J344"} | 燃燒／點火／老化時間 | 時序或處理條件 | Secs | ElapsedTestTime(Secs); 01_實驗資料/第一批下載/PSI-101_SAME-R/Raw Data/PSI-101_Raw Data_HKPData_gmt250_1.csv; line 1, column 5 | \[{"csv_line": 1, "column_1based": 5, "actual_header": "ElapsedTestTime(Secs)", "is_one_of_reference_aliases": true, "locator_status": "original header from prior complete CSV profile"}\] |
| PSI-101 | 物理參數 row345; {"A": "A345", "B": "B345", "C": "C345", "D": "D345", "E": "E345", "F": "F345", "G": "G345", "H": "H345", "I": "I345", "J": "J345"} | 燃燒／點火／老化時間 | 時序或處理條件 | sec | Duration (sec)；Primary aging time (sec)；Primary mixing time (sec)；Net aging time (sec)；Primary Aging Duration (sec)；Primary Mixing Duration (sec)；Secondary Aging Duration (sec)；Secondary Mixing Duration (sec)；Aging Duration (sec); 01_實驗資料/第一批下載/PSI-101_SAME-R/Experimental table/PSI-101_Experimental table_SAME-R.csv; line 1, column 7 | \[{"csv_line": 1, "column_1based": 7, "actual_header": "Duration (sec)", "is_one_of_reference_aliases": true, "locator_status": "literal experimental CSV header checked; index not assumed per-trial measurement"}\] |
| PSI-101 | 物理參數 row346; {"A": "A346", "B": "B346", "C": "C346", "D": "D346", "E": "E346", "F": "F346", "G": "G346", "H": "H346", "I": "I346", "J": "J346"} | 燃燒／點火／老化時間 | 時序或處理條件 | 未由欄名確認 | PreAge Thermal Precipitator Duration；Net Aging Duration；Primary Aging Therm Precip Duration；secondary agign thermal precip duration; 01_實驗資料/第一批下載/PSI-101_SAME-R/Analyzed Data/PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx; DBP!R2C20 | \[{"target_sheet": "DBP", "target_cell": "T2", "actual_header": "PreAge Thermal Precipitator Duration", "exact_header_match": false, "locator_status": "literal source cell checked"}\] |
| PSI-101 | 物理參數 row347; {"A": "A347", "B": "B347", "C": "C347", "D": "D347", "E": "E347", "F": "F347", "G": "G347", "H": "H347", "I": "I347", "J": "J347"} | 硬體電壓／電流／功率 | 儀器設定／控制參數 | Volts | VSOSetpoint\[PN23\](Volts)；VSOSetpoint\[PN23\](Volts)*10; 01_實驗資料/第一批下載/PSI-101_SAME-R/Raw Data/PSI-101_Raw Data_HKPData_gmt250_1.csv; line 1, column 33 | \[{"csv_line": 1, "column_1based": 33, "actual_header": "VSOSetpoint\[PN23\](Volts)", "is_one_of_reference_aliases": true, "locator_status": "original header from prior complete CSV profile"}\] |
| PSI-101 | 物理參數 row348; {"A": "A348", "B": "B348", "C": "C348", "D": "D348", "E": "E348", "F": "F348", "G": "G348", "H": "H348", "I": "I348", "J": "J348"} | 硬體電壓／電流／功率 | 原始訊號或狀態 | Volts | ProximitySensor1(Volts)；ProximitySensor2(Volts)；ProximitySensor4(Volts)；CarouselProximitySensor(Volts); 01_實驗資料/第一批下載/PSI-101_SAME-R/Raw Data/PSI-101_Raw Data_HKPData_gmt250_1.csv; line 1, column 55 | \[{"csv_line": 1, "column_1based": 55, "actual_header": "ProximitySensor1(Volts)", "is_one_of_reference_aliases": true, "locator_status": "original header from prior complete CSV profile"}\] |
| PSI-101 | 物理參數 row349; {"A": "A349", "B": "B349", "C": "C349", "D": "D349", "E": "E349", "F": "F349", "G": "G349", "H": "H349", "I": "I349", "J": "J349"} | 硬體電壓／電流／功率 | 原始訊號或狀態 | volts | STS Detector (volts)；STS Detector offset (volts)；Ion A (volts)；Ion A offset V0 (volts)；Ion A (volts) Mpass_3rd；Ion A offset V0 Mpass (volts)；Ion B (volts)；Ion B offset V0 (volts)；Ion B Delta (volts)；Ion A Mpass_3rd offset V0 (volts)；其餘見原始欄位; 01_實驗資料/第一批下載/PSI-101_SAME-R/Analyzed Data/PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx; DBP!R2C50 | \[{"target_sheet": "DBP", "target_cell": "AX2", "actual_header": "STS Detector (volts)", "exact_header_match": false, "locator_status": "literal source cell checked"}\] |
| PSI-101 | 物理參數 row350; {"A": "A350", "B": "B350", "C": "C350", "D": "D350", "E": "E350", "F": "F350", "G": "G350", "H": "H350", "I": "I350", "J": "J350"} | 硬體電壓／電流／功率 | 原始訊號或狀態 | 未由欄名確認 | PTrakPower；DustTrakAPower；DustTrakBPower；STSDetectorPower；CarouselPower；VideoPower; 01_實驗資料/第一批下載/PSI-101_SAME-R/Raw Data/PSI-101_Raw Data_HKPData_gmt250_1.csv; line 1, column 60 | \[{"csv_line": 1, "column_1based": 60, "actual_header": "PTrakPower", "is_one_of_reference_aliases": true, "locator_status": "original header from prior complete CSV profile"}\] |
| PSI-101 | 物理參數 row351; {"A": "A351", "B": "B351", "C": "C351", "D": "D351", "E": "E351", "F": "F351", "G": "G351", "H": "H351", "I": "I351", "J": "J351"} | 粒子數濃度 | 量測通道 | PtPerCC | PTrakMeasurement(PtPerCC); 01_實驗資料/第一批下載/PSI-101_SAME-R/Raw Data/PSI-101_Raw Data_HKPData_gmt250_1.csv; line 1, column 27 | \[{"csv_line": 1, "column_1based": 27, "actual_header": "PTrakMeasurement(PtPerCC)", "is_one_of_reference_aliases": true, "locator_status": "original header from prior complete CSV profile"}\] |
| PSI-101 | 物理參數 row352; {"A": "A352", "B": "B352", "C": "C352", "D": "D352", "E": "E352", "F": "F352", "G": "G352", "H": "H352", "I": "I352", "J": "J352"} | 粒子數濃度 | 量測通道 | Volts | PTrakPowerMeasurement(Volts); 01_實驗資料/第一批下載/PSI-101_SAME-R/Raw Data/PSI-101_Raw Data_HKPData_gmt250_1.csv; line 1, column 50 | \[{"csv_line": 1, "column_1based": 50, "actual_header": "PTrakPowerMeasurement(Volts)", "is_one_of_reference_aliases": true, "locator_status": "original header from prior complete CSV profile"}\] |
| PSI-101 | 物理參數 row353; {"A": "A353", "B": "B353", "C": "C353", "D": "D353", "E": "E353", "F": "F353", "G": "G353", "H": "H353", "I": "I353", "J": "J353"} | 粒子數濃度 | 量測通道 | 未由欄名確認 | PTrakMeasurement(PtPerCC)/1000 (Right Axis); 01_實驗資料/第一批下載/PSI-101_SAME-R/Analyzed Data/PSI-101_Analyzed Data_2010_210_10_lampwick_run57_a.xlsx; Sheet used to Graph!R1C7 | \[{"target_sheet": "Sheet used to Graph", "target_cell": "G1", "actual_header_or_log_cell": "PTrakMeasurement(PtPerCC)/1000 (Right Axis)", "is_one_of_reference_aliases": true, "locator_status": "literal original source target cell checked; log text distinguished from numeric trial factor"}\] |
| PSI-101 | 物理參數 row354; {"A": "A354", "B": "B354", "C": "C354", "D": "D354", "E": "E354", "F": "F354", "G": "G354", "H": "H354", "I": "I354", "J": "J354"} | 粒子質量濃度 | 量測通道 | MgPerM3 | DustTrakAMeasurement(MgPerM3)；DustTrakBMeasurement(MgPerM3); 01_實驗資料/第一批下載/PSI-101_SAME-R/Raw Data/PSI-101_Raw Data_HKPData_gmt250_1.csv; line 1, column 28 | \[{"csv_line": 1, "column_1based": 28, "actual_header": "DustTrakAMeasurement(MgPerM3)", "is_one_of_reference_aliases": true, "locator_status": "original header from prior complete CSV profile"}\] |
| PSI-101 | 物理參數 row355; {"A": "A355", "B": "B355", "C": "C355", "D": "D355", "E": "E355", "F": "F355", "G": "G355", "H": "H355", "I": "I355", "J": "J355"} | 粒子質量濃度 | 量測通道 | Volts | DustTrakAAnalogMeasurement(Volts)；DustTrakBAnalogMeasurement(Volts); 01_實驗資料/第一批下載/PSI-101_SAME-R/Raw Data/PSI-101_Raw Data_HKPData_gmt250_1.csv; line 1, column 30 | \[{"csv_line": 1, "column_1based": 30, "actual_header": "DustTrakAAnalogMeasurement(Volts)", "is_one_of_reference_aliases": true, "locator_status": "original header from prior complete CSV profile"}\] |
| PSI-101 | 物理參數 row356; {"A": "A356", "B": "B356", "C": "C356", "D": "D356", "E": "E356", "F": "F356", "G": "G356", "H": "H356", "I": "I356", "J": "J356"} | 粒子質量濃度 | 量測通道 | 未由欄名確認 | DustTrakBMeasurement(MgPerM3) (Right Axis)；Predicted mass conc. mg/m^3；Mass concentration to produce number alarm; 01_實驗資料/第一批下載/PSI-101_SAME-R/Analyzed Data/PSI-101_Analyzed Data_2010_210_10_lampwick_run57_a.xlsx; Sheet used to Graph!R1C9 | \[{"target_sheet": "Sheet used to Graph", "target_cell": "I1", "actual_header_or_log_cell": "DustTrakBMeasurement(MgPerM3) (Right Axis)", "is_one_of_reference_aliases": true, "locator_status": "literal original source target cell checked; log text distinguished from numeric trial factor"}\] |
| PSI-101 | 物理參數 row357; {"A": "A357", "B": "B357", "C": "C357", "D": "D357", "E": "E357", "F": "F357", "G": "G357", "H": "H357", "I": "I357", "J": "J357"} | 粒徑／粒子分布 | 計算／影像分析量 | micro-m | M1/M0 (micro-m)--CMD; 01_實驗資料/第一批下載/PSI-101_SAME-R/Analyzed Data/PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx; DBP!R2C70 | \[{"target_sheet": "DBP", "target_cell": "BR2", "actual_header": "M1/M0 (micro-m)--CMD", "exact_header_match": true, "locator_status": "literal source cell checked"}\] |
| PSI-101 | 物理參數 row358; {"A": "A358", "B": "B358", "C": "C358", "D": "D358", "E": "E358", "F": "F358", "G": "G358", "H": "H358", "I": "I358", "J": "J358"} | 粒徑／粒子分布 | 計算／影像分析量 | micrometers | Scattering Predicted geometric mean size (micrometers); 01_實驗資料/第一批下載/PSI-101_SAME-R/Analyzed Data/PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx; SAME1 Flight Tests 8-27-09!R2C48 | \[{"target_sheet": "SAME1 Flight Tests 8-27-09", "target_cell": "AV2", "actual_header": "Scattering Predicted geometric mean size (micrometers)", "exact_header_match": true, "locator_status": "literal source cell checked"}\] |
| PSI-101 | 物理參數 row359; {"A": "A359", "B": "B359", "C": "C359", "D": "D359", "E": "E359", "F": "F359", "G": "G359", "H": "H359", "I": "I359", "J": "J359"} | 粒徑／粒子分布 | 計算／影像分析量 | 未由欄名確認 | CommDiagASolenoid\[VR11\]；CommDiagBSolenoid\[VR12\]；Sigmagv；a.k.a Sigmagn；sqrt(2Pi)*ln(sigmag)；Lnsigmagn^2=J53*dLnD；lnsigmagn^2=p53*dLnD；Sigmagn；Hatch Choate Sigma g；CMD, M1/M0, micro-m；其餘見原始欄位; 01_實驗資料/第一批下載/PSI-101_SAME-R/Raw Data/PSI-101_Raw Data_HKPData_gmt250_1.csv; line 1, column 75 | \[{"csv_line": 1, "column_1based": 75, "actual_header": "CommDiagASolenoid\[VR11\]", "is_one_of_reference_aliases": true, "locator_status": "original header from prior complete CSV profile"}\] |
| PSI-101 | 物理參數 row360; {"A": "A360", "B": "B360", "C": "C360", "D": "D360", "E": "E360", "F": "F360", "G": "G360", "H": "H360", "I": "I360", "J": "J360"} | 質量流率 | 量測或設定 | LPM | MFCMassFlowRate(LPM); 01_實驗資料/第一批下載/PSI-101_SAME-R/Raw Data/PSI-101_Raw Data_HKPData_gmt250_1.csv; line 1, column 36 | \[{"csv_line": 1, "column_1based": 36, "actual_header": "MFCMassFlowRate(LPM)", "is_one_of_reference_aliases": true, "locator_status": "original header from prior complete CSV profile"}\] |
| PSI-101 | 物理參數 row361; {"A": "A361", "B": "B361", "C": "C361", "D": "D361", "E": "E361", "F": "F361", "G": "G361", "H": "H361", "I": "I361", "J": "J361"} | 質量／質量損失 | 量測或衍生 | Ohms | SampleResistance(Ohms); 01_實驗資料/第一批下載/PSI-101_SAME-R/Raw Data/PSI-101_Raw Data_HKPData_gmt250_1.csv; line 1, column 21 | \[{"csv_line": 1, "column_1based": 21, "actual_header": "SampleResistance(Ohms)", "is_one_of_reference_aliases": true, "locator_status": "original header from prior complete CSV profile"}\] |
| PSI-101 | 物理參數 row362; {"A": "A362", "B": "B362", "C": "C362", "D": "D362", "E": "E362", "F": "F362", "G": "G362", "H": "H362", "I": "I362", "J": "J362"} | 質量／質量損失 | 量測或衍生 | mg | Mass Loss (mg); 01_實驗資料/第一批下載/PSI-101_SAME-R/Analyzed Data/PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx; Reduced data sheet!R2C20 | \[{"target_sheet": "Reduced data sheet", "target_cell": "T2", "actual_header": "Mass Loss (mg)", "exact_header_match": true, "locator_status": "literal source cell checked"}\] |
| PSI-101 | 物理參數 row363; {"A": "A363", "B": "B363", "C": "C363", "D": "D363", "E": "E363", "F": "F363", "G": "G363", "H": "H363", "I": "I363", "J": "J363"} | 質量／質量損失 | 量測或衍生 | 未由欄名確認 | Mass Loss；Mass Loss mg；PTrack/mass loss；Ion/Mass loss；Dust Track/mass loss; 01_實驗資料/第一批下載/PSI-101_SAME-R/Analyzed Data/PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx; DBP!R2C47 | \[{"target_sheet": "DBP", "target_cell": "AU2", "actual_header": "Mass Loss", "exact_header_match": false, "locator_status": "literal source cell checked"}\] |
| PSI-101 | 物理參數 row364; {"A": "A364", "B": "B364", "C": "C364", "D": "D364", "E": "E364", "F": "F364", "G": "G364", "H": "H364", "I": "I364", "J": "J364"} | 風扇／流量顯示設定 | 儀器設定 | 未由欄名確認 | MixingFanPower；Fan problem; 01_實驗資料/第一批下載/PSI-101_SAME-R/Raw Data/PSI-101_Raw Data_HKPData_gmt250_1.csv; line 1, column 59 | \[{"csv_line": 1, "column_1based": 59, "actual_header": "MixingFanPower", "is_one_of_reference_aliases": true, "locator_status": "original header from prior complete CSV profile"}\] |
| PSI-101 | 物理參數 row365; {"A": "A365", "B": "B365", "C": "C365", "D": "D365", "E": "E365", "F": "F365", "G": "G365", "H": "H365", "I": "I365", "J": "J365"} | 體積流量／MFC | 儀器設定／控制參數 | LPM | MFCSetpoint(LPM)；MFCAnalogSetpoint\[BN19\](LPM); 01_實驗資料/第一批下載/PSI-101_SAME-R/Raw Data/PSI-101_Raw Data_HKPData_gmt250_1.csv; line 1, column 35 | \[{"csv_line": 1, "column_1based": 35, "actual_header": "MFCSetpoint(LPM)", "is_one_of_reference_aliases": true, "locator_status": "original header from prior complete CSV profile"}\] |
| PSI-101 | 物理參數 row366; {"A": "A366", "B": "B366", "C": "C366", "D": "D366", "E": "E366", "F": "F366", "G": "G366", "H": "H366", "I": "I366", "J": "J366"} | 體積流量／MFC | 量測或設定 | LPM | MFCAnalogFlowRate(LPM); 01_實驗資料/第一批下載/PSI-101_SAME-R/Raw Data/PSI-101_Raw Data_HKPData_gmt250_1.csv; line 1, column 40 | \[{"csv_line": 1, "column_1based": 40, "actual_header": "MFCAnalogFlowRate(LPM)", "is_one_of_reference_aliases": true, "locator_status": "original header from prior complete CSV profile"}\] |
| PSI-101 | 物理參數 row367; {"A": "A367", "B": "B367", "C": "C367", "D": "D367", "E": "E367", "F": "F367", "G": "G367", "H": "H367", "I": "I367", "J": "J367"} | 體積流量／MFC | 量測或設定 | SCCM | LFEFlowRate\[AT08\](SCCM); 01_實驗資料/第一批下載/PSI-101_SAME-R/Raw Data/PSI-101_Raw Data_HKPData_gmt250_1.csv; line 1, column 32 | \[{"csv_line": 1, "column_1based": 32, "actual_header": "LFEFlowRate\[AT08\](SCCM)", "is_one_of_reference_aliases": true, "locator_status": "original header from prior complete CSV profile"}\] |
| PSI-101 | 物理參數 row368; {"A": "A368", "B": "B368", "C": "C368", "D": "D368", "E": "E368", "F": "F368", "G": "G368", "H": "H368", "I": "I368", "J": "J368"} | 體積流量／MFC | 量測或設定 | 未由欄名確認 | Air Flow rate, SLPM；N2 flow rate, SLPM; 01_實驗資料/第一批下載/PSI-101_SAME-R/Analyzed Data/PSI-101_Analyzed Data_SAME, SAME-R_Results.xlsx; Gnd Verif. 8-2012!R42C45 | \[{"target_sheet": "Gnd Verif. 8-2012", "target_cell": "AS42", "actual_header": "Air Flow rate, SLPM", "exact_header_match": false, "locator_status": "literal source cell checked"}\] |
| PSI-102 | 物理參數 row369; {"A": "A369", "B": "B369", "C": "C369", "D": "D369", "E": "E369", "F": "F369", "G": "G369", "H": "H369", "I": "I369", "J": "J369"} | 光電／離子偵測訊號 | 儀器原始訊號 | Volts | ISSDetectorObscurationMeasurement(Volts)；ISSDetectorScatterMeasurement(Volts)；STSDetectorMeasurement(Volts)；IonDetectorAMeasurement(Volts)；IonDetectorBMeasurement(Volts)；ISSDetectorScatterMeasurement(Volts)right; 01_實驗資料/第一批下載/PSI-102_SAME/Analyzed Data/PSI-102_Analyzed Data_GMT255hkp.xlsx; Copy of GMT255hkp!R1C22 | \[{"target_sheet": "Copy of GMT255hkp", "target_cell": "V1", "actual_header_or_log_cell": "ISSDetectorObscurationMeasurement(Volts)", "is_one_of_reference_aliases": true, "locator_status": "literal original source target cell checked; log text distinguished from numeric trial factor"}\] |
| PSI-102 | 物理參數 row370; {"A": "A370", "B": "B370", "C": "C370", "D": "D370", "E": "E370", "F": "F370", "G": "G370", "H": "H370", "I": "I370", "J": "J370"} | 其他氣體組成／濃度 | 條件或分析量 | 未由欄名確認 | DynamicDilutorSolenoid\[PN15\]；CommDiagADilutionSolenoid\[PN24\]；CommDiagBDilutionSolenoid\[PN27\]；Dilution control enabled；Initializing DynamicDilutor；DynamicDilutor initialized; 01_實驗資料/第一批下載/PSI-102_SAME/Analyzed Data/PSI-102_Analyzed Data_GMT255hkp.xlsx; Copy of GMT255hkp!R1C73 | \[{"target_sheet": "Copy of GMT255hkp", "target_cell": "BU1", "actual_header_or_log_cell": "DynamicDilutorSolenoid\[PN15\]", "is_one_of_reference_aliases": true, "locator_status": "literal original source target cell checked; log text distinguished from numeric trial factor"}\] |
| PSI-102 | 物理參數 row371; {"A": "A371", "B": "B371", "C": "C371", "D": "D371", "E": "E371", "F": "F371", "G": "G371", "H": "H371", "I": "I371", "J": "J371"} | 壓力 | 量測或設定 | PSIA | MFCPressure(PSIA)；GN2MainPressure\[PN02\](PSIA)；VacuumPressure\[VR04\](PSIA)；DriveSidePressure\[BN02\](PSIA)；SampleSidePressure\[AT20\](PSIA); 01_實驗資料/第一批下載/PSI-102_SAME/Analyzed Data/PSI-102_Analyzed Data_GMT255hkp.xlsx; Copy of GMT255hkp!R1C38 | \[{"target_sheet": "Copy of GMT255hkp", "target_cell": "AL1", "actual_header_or_log_cell": "MFCPressure(PSIA)", "is_one_of_reference_aliases": true, "locator_status": "literal original source target cell checked; log text distinguished from numeric trial factor"}\] |
| PSI-102 | 物理參數 row372; {"A": "A372", "B": "B372", "C": "C372", "D": "D372", "E": "E372", "F": "F372", "G": "G372", "H": "H372", "I": "I372", "J": "J372"} | 壓力 | 量測或設定 | PSIG | GN2RegulatedPressure\[PN12\](PSIG); 01_實驗資料/第一批下載/PSI-102_SAME/Analyzed Data/PSI-102_Analyzed Data_GMT255hkp.xlsx; Copy of GMT255hkp!R1C42 | \[{"target_sheet": "Copy of GMT255hkp", "target_cell": "AP1", "actual_header_or_log_cell": "GN2RegulatedPressure\[PN12\](PSIG)", "is_one_of_reference_aliases": true, "locator_status": "literal original source target cell checked; log text distinguished from numeric trial factor"}\] |
| PSI-102 | 物理參數 row373; {"A": "A373", "B": "B373", "C": "C373", "D": "D373", "E": "E373", "F": "F373", "G": "G373", "H": "H373", "I": "I373", "J": "J373"} | 壓力 | 量測或設定 | 未由欄名確認 | HighVacuumPressure；LowRegulatedGN2Pressure; 01_實驗資料/第一批下載/PSI-102_SAME/Analyzed Data/PSI-102_Analyzed Data_GMT255 log.xlsx; Copy of GMT255log!R14C3 | \[{"target_sheet": "Copy of GMT255log", "target_cell": "C14", "actual_header_or_log_cell": "HighVacuumPressure", "is_one_of_reference_aliases": true, "locator_status": "literal original source target cell checked; log text distinguished from numeric trial factor"}\] |
| PSI-102 | 物理參數 row374; {"A": "A374", "B": "B374", "C": "C374", "D": "D374", "E": "E374", "F": "F374", "G": "G374", "H": "H374", "I": "I374", "J": "J374"} | 尺寸／幾何 | 裝置或樣本條件 | 未由欄名確認 | Manual positioning option in effect；PositionerEnable；PositionerDirectionIn；PositionerClock; 01_實驗資料/第一批下載/PSI-102_SAME/Analyzed Data/PSI-102_Analyzed Data_GMT256LOG.xlsx; GMT256LOG!R7C2 | \[{"target_sheet": "GMT256LOG", "target_cell": "B7", "actual_header_or_log_cell": "Manual positioning option in effect", "is_one_of_reference_aliases": true, "locator_status": "literal original source target cell checked; log text distinguished from numeric trial factor"}\] |
| PSI-102 | 物理參數 row375; {"A": "A375", "B": "B375", "C": "C375", "D": "D375", "E": "E375", "F": "F375", "G": "G375", "H": "H375", "I": "I375", "J": "J375"} | 影像／光譜設定 | 儀器設定或影像座標 | 未由欄名確認 | Light and camera turned off；CameraPower；IlluminationLEDPower；Lights! Cameras!；Exception: Not enough bytes read from camera serial port; 01_實驗資料/第一批下載/PSI-102_SAME/Analyzed Data/PSI-102_Analyzed Data_GMT255 log.xlsx; Copy of GMT255log!R5C2 | \[{"target_sheet": "Copy of GMT255log", "target_cell": "B5", "actual_header_or_log_cell": "Light and camera turned off", "is_one_of_reference_aliases": true, "locator_status": "literal original source target cell checked; log text distinguished from numeric trial factor"}\] |
| PSI-102 | 物理參數 row376; {"A": "A376", "B": "B376", "C": "C376", "D": "D376", "E": "E376", "F": "F376", "G": "G376", "H": "H376", "I": "I376", "J": "J376"} | 影像／光譜設定 | 儀器設定／控制參數 | 未由欄名確認 | Error setting camera settings; 01_實驗資料/第一批下載/PSI-102_SAME/Analyzed Data/PSI-102_Analyzed Data_GMT254HKPandLOGmultiple runs.xls; GMT254 LOG!R52C2 | \[{"target_sheet": "GMT254 LOG", "target_cell": "B52", "actual_header_or_log_cell": "Error setting camera settings", "is_one_of_reference_aliases": true, "locator_status": "literal original source target cell checked; log text distinguished from numeric trial factor"}\] |
| PSI-102 | 物理參數 row377; {"A": "A377", "B": "B377", "C": "C377", "D": "D377", "E": "E377", "F": "F377", "G": "G377", "H": "H377", "I": "I377", "J": "J377"} | 流速／通風 | 量測或設定 | cm/s | Air Flow (cm/s); 01_實驗資料/第一批下載/PSI-102_SAME/Experimental table/PSI-102_Experimental table_SAME.csv; line 1, column 3 | \[{"csv_line": 1, "column_1based": 3, "actual_header": "Air Flow (cm/s)", "is_one_of_reference_aliases": true, "locator_status": "literal experimental CSV header checked; index not assumed per-trial measurement"}\] |
| PSI-102 | 物理參數 row378; {"A": "A378", "B": "B378", "C": "C378", "D": "D378", "E": "E378", "F": "F378", "G": "G378", "H": "H378", "I": "I378", "J": "J378"} | 流速／通風 | 量測或設定 | 未由欄名確認 | SetInletVelocity(23; 01_實驗資料/第一批下載/PSI-102_SAME/Analyzed Data/PSI-102_Analyzed Data_GMT267silicon test 23 and 24 log.xlsx; GMT267silicontest23and24log!R17C3 | \[{"target_sheet": "GMT267silicontest23and24log", "target_cell": "C17", "actual_header_or_log_cell": "SetInletVelocity(23", "is_one_of_reference_aliases": true, "locator_status": "literal original source target cell checked; log text distinguished from numeric trial factor"}\] |
| PSI-102 | 物理參數 row379; {"A": "A379", "B": "B379", "C": "C379", "D": "D379", "E": "E379", "F": "F379", "G": "G379", "H": "H379", "I": "I379", "J": "J379"} | 溫度 | 量測或設定 | DegC | GasPlumeTemperature(DegC)；MFCTemperature(DegC); 01_實驗資料/第一批下載/PSI-102_SAME/Analyzed Data/PSI-102_Analyzed Data_GMT255hkp.xlsx; Copy of GMT255hkp!R1C20 | \[{"target_sheet": "Copy of GMT255hkp", "target_cell": "T1", "actual_header_or_log_cell": "GasPlumeTemperature(DegC)", "is_one_of_reference_aliases": true, "locator_status": "literal original source target cell checked; log text distinguished from numeric trial factor"}\] |
| PSI-102 | 物理參數 row380; {"A": "A380", "B": "B380", "C": "C380", "D": "D380", "E": "E380", "F": "F380", "G": "G380", "H": "H380", "I": "I380", "J": "J380"} | 溫度 | 量測或設定 | 未由欄名確認 | HighGasPlumeTemperature; 01_實驗資料/第一批下載/PSI-102_SAME/Analyzed Data/PSI-102_Analyzed Data_GMT256LOG.xlsx; GMT256LOG!R74C3 | \[{"target_sheet": "GMT256LOG", "target_cell": "C74", "actual_header_or_log_cell": "HighGasPlumeTemperature", "is_one_of_reference_aliases": true, "locator_status": "literal original source target cell checked; log text distinguished from numeric trial factor"}\] |
| PSI-102 | 物理參數 row381; {"A": "A381", "B": "B381", "C": "C381", "D": "D381", "E": "E381", "F": "F381", "G": "G381", "H": "H381", "I": "I381", "J": "J381"} | 燃燒／點火／老化時間 | 儀器設定／控制參數 | 未由欄名確認 | Setting heater duration to 1500 cycles or 40 secs；Setting heater duration to 2250 cycles or 60 secs; 01_實驗資料/第一批下載/PSI-102_SAME/Analyzed Data/PSI-102_Analyzed Data_Run 1 GMT252 testlog.xls; Copy of GMT252run1testlog!R28C2 | \[{"target_sheet": "Copy of GMT252run1testlog", "target_cell": "B28", "actual_header_or_log_cell": "Setting heater duration to 1500 cycles or 40 secs", "is_one_of_reference_aliases": true, "locator_status": "literal original source target cell checked; log text distinguished from numeric trial factor"}\] |
| PSI-102 | 物理參數 row382; {"A": "A382", "B": "B382", "C": "C382", "D": "D382", "E": "E382", "F": "F382", "G": "G382", "H": "H382", "I": "I382", "J": "J382"} | 燃燒／點火／老化時間 | 時序或處理條件 | Secs | ElapsedTestTime(Secs); 01_實驗資料/第一批下載/PSI-102_SAME/Analyzed Data/PSI-102_Analyzed Data_GMT255hkp.xlsx; Copy of GMT255hkp!R1C5 | \[{"target_sheet": "Copy of GMT255hkp", "target_cell": "E1", "actual_header_or_log_cell": "ElapsedTestTime(Secs)", "is_one_of_reference_aliases": true, "locator_status": "literal original source target cell checked; log text distinguished from numeric trial factor"}\] |
| PSI-102 | 物理參數 row383; {"A": "A383", "B": "B383", "C": "C383", "D": "D383", "E": "E383", "F": "F383", "G": "G383", "H": "H383", "I": "I383", "J": "J383"} | 燃燒／點火／老化時間 | 時序或處理條件 | minutes | Aging Duration (minutes); 01_實驗資料/第一批下載/PSI-102_SAME/Experimental table/PSI-102_Experimental table_SAME.csv; line 1, column 5 | \[{"csv_line": 1, "column_1based": 5, "actual_header": "Aging Duration (minutes)", "is_one_of_reference_aliases": true, "locator_status": "literal experimental CSV header checked; index not assumed per-trial measurement"}\] |
| PSI-102 | 物理參數 row384; {"A": "A384", "B": "B384", "C": "C384", "D": "D384", "E": "E384", "F": "F384", "G": "G384", "H": "H384", "I": "I384", "J": "J384"} | 燃燒／點火／老化時間 | 時序或處理條件 | 未由欄名確認 | SetMixingDuration(23；SetPrimaryAgingDuration(23；SetSecondaryAgingDuration(23；Test paused at 00:01:05 elapsed test time; 01_實驗資料/第一批下載/PSI-102_SAME/Analyzed Data/PSI-102_Analyzed Data_GMT267silicon test 23 and 24 log.xlsx; GMT267silicontest23and24log!R9C3 | \[{"target_sheet": "GMT267silicontest23and24log", "target_cell": "C9", "actual_header_or_log_cell": "SetMixingDuration(23", "is_one_of_reference_aliases": true, "locator_status": "literal original source target cell checked; log text distinguished from numeric trial factor"}\] |
| PSI-102 | 物理參數 row385; {"A": "A385", "B": "B385", "C": "C385", "D": "D385", "E": "E385", "F": "F385", "G": "G385", "H": "H385", "I": "I385", "J": "J385"} | 硬體電壓／電流／功率 | 儀器設定／控制參數 | Volts | VSOSetpoint\[PN23\](Volts); 01_實驗資料/第一批下載/PSI-102_SAME/Analyzed Data/PSI-102_Analyzed Data_GMT255hkp.xlsx; Copy of GMT255hkp!R1C33 | \[{"target_sheet": "Copy of GMT255hkp", "target_cell": "AG1", "actual_header_or_log_cell": "VSOSetpoint\[PN23\](Volts)", "is_one_of_reference_aliases": true, "locator_status": "literal original source target cell checked; log text distinguished from numeric trial factor"}\] |
| PSI-102 | 物理參數 row386; {"A": "A386", "B": "B386", "C": "C386", "D": "D386", "E": "E386", "F": "F386", "G": "G386", "H": "H386", "I": "I386", "J": "J386"} | 硬體電壓／電流／功率 | 儀器設定／控制參數 | 未由欄名確認 | Setting heater setpoint to 9280 or 0.885023 Ohms；Setting MaxRt to 1.103 Ohms；Setting heater setpoint to 0 or 0 Ohms；Setting MaxRt to 0.989 Ohms; 01_實驗資料/第一批下載/PSI-102_SAME/Analyzed Data/PSI-102_Analyzed Data_Run 1 GMT252 testlog.xls; Copy of GMT252run1testlog!R27C2 | \[{"target_sheet": "Copy of GMT252run1testlog", "target_cell": "B27", "actual_header_or_log_cell": "Setting heater setpoint to 9280 or 0.885023 Ohms", "is_one_of_reference_aliases": true, "locator_status": "literal original source target cell checked; log text distinguished from numeric trial factor"}\] |
| PSI-102 | 物理參數 row387; {"A": "A387", "B": "B387", "C": "C387", "D": "D387", "E": "E387", "F": "F387", "G": "G387", "H": "H387", "I": "I387", "J": "J387"} | 硬體電壓／電流／功率 | 原始訊號或狀態 | Volts | ProximitySensor1(Volts)；ProximitySensor2(Volts)；ProximitySensor4(Volts)；CarouselProximitySensor(Volts); 01_實驗資料/第一批下載/PSI-102_SAME/Analyzed Data/PSI-102_Analyzed Data_GMT255hkp.xlsx; Copy of GMT255hkp!R1C55 | \[{"target_sheet": "Copy of GMT255hkp", "target_cell": "BC1", "actual_header_or_log_cell": "ProximitySensor1(Volts)", "is_one_of_reference_aliases": true, "locator_status": "literal original source target cell checked; log text distinguished from numeric trial factor"}\] |
| PSI-102 | 物理參數 row388; {"A": "A388", "B": "B388", "C": "C388", "D": "D388", "E": "E388", "F": "F388", "G": "G388", "H": "H388", "I": "I388", "J": "J388"} | 硬體電壓／電流／功率 | 原始訊號或狀態 | 未由欄名確認 | Video recorder powered off；VideoDrawerPower(on)；PTrakPower；DustTrakAPower；DustTrakBPower；STSDetectorPower；CarouselPower；VideoPower；Video recorder powered on; 01_實驗資料/第一批下載/PSI-102_SAME/Analyzed Data/PSI-102_Analyzed Data_GMT255 log.xlsx; Copy of GMT255log!R6C2 | \[{"target_sheet": "Copy of GMT255log", "target_cell": "B6", "actual_header_or_log_cell": "Video recorder powered off", "is_one_of_reference_aliases": true, "locator_status": "literal original source target cell checked; log text distinguished from numeric trial factor"}\] |
| PSI-102 | 物理參數 row389; {"A": "A389", "B": "B389", "C": "C389", "D": "D389", "E": "E389", "F": "F389", "G": "G389", "H": "H389", "I": "I389", "J": "J389"} | 粒子數濃度 | 量測通道 | PtPerCC | PTrakMeasurement(PtPerCC)；PTrakMeasurement(PtPerCC)/1000；PTrakMeasurement(PtPerCC)right；PTrakMeasurement(PtPerCC)/100right；PTrakMeasurement(PtPerCC)/1000 right scale；PTrakMeasurement(PtPerCC)/100; 01_實驗資料/第一批下載/PSI-102_SAME/Analyzed Data/PSI-102_Analyzed Data_GMT255hkp.xlsx; Copy of GMT255hkp!R1C27 | \[{"target_sheet": "Copy of GMT255hkp", "target_cell": "AA1", "actual_header_or_log_cell": "PTrakMeasurement(PtPerCC)", "is_one_of_reference_aliases": true, "locator_status": "literal original source target cell checked; log text distinguished from numeric trial factor"}\] |
| PSI-102 | 物理參數 row390; {"A": "A390", "B": "B390", "C": "C390", "D": "D390", "E": "E390", "F": "F390", "G": "G390", "H": "H390", "I": "I390", "J": "J390"} | 粒子數濃度 | 量測通道 | PtPerCC/100 | PTrakMeasurement(PtPerCC/100) Right；PTrakMeasurement(PtPerCC/100)；PTrakMeasurement(PtPerCC/100)right; 01_實驗資料/第一批下載/PSI-102_SAME/Analyzed Data/PSI-102_Analyzed Data_DBP GMT257hkp.xls; Copy of GMT256hkp!R1C8 | \[{"target_sheet": "Copy of GMT256hkp", "target_cell": "H1", "actual_header_or_log_cell": "PTrakMeasurement(PtPerCC/100) Right", "is_one_of_reference_aliases": true, "locator_status": "literal original source target cell checked; log text distinguished from numeric trial factor"}\] |
| PSI-102 | 物理參數 row391; {"A": "A391", "B": "B391", "C": "C391", "D": "D391", "E": "E391", "F": "F391", "G": "G391", "H": "H391", "I": "I391", "J": "J391"} | 粒子數濃度 | 量測通道 | PtPerCC/1000 | PTrakMeasurement(PtPerCC/1000)right；PTrakMeasurement(PtPerCC/1000); 01_實驗資料/第一批下載/PSI-102_SAME/Analyzed Data/PSI-102_Analyzed Data_GMT262 RUN 13 teflon.xls; GMT262tefhkp!R1C23 | \[{"target_sheet": "GMT262tefhkp", "target_cell": "W1", "actual_header_or_log_cell": "PTrakMeasurement(PtPerCC/1000)right", "is_one_of_reference_aliases": true, "locator_status": "literal original source target cell checked; log text distinguished from numeric trial factor"}\] |
| PSI-102 | 物理參數 row392; {"A": "A392", "B": "B392", "C": "C392", "D": "D392", "E": "E392", "F": "F392", "G": "G392", "H": "H392", "I": "I392", "J": "J392"} | 粒子數濃度 | 量測通道 | Volts | PTrakPowerMeasurement(Volts); 01_實驗資料/第一批下載/PSI-102_SAME/Analyzed Data/PSI-102_Analyzed Data_GMT255hkp.xlsx; Copy of GMT255hkp!R1C50 | \[{"target_sheet": "Copy of GMT255hkp", "target_cell": "AX1", "actual_header_or_log_cell": "PTrakPowerMeasurement(Volts)", "is_one_of_reference_aliases": true, "locator_status": "literal original source target cell checked; log text distinguished from numeric trial factor"}\] |
| PSI-102 | 物理參數 row393; {"A": "A393", "B": "B393", "C": "C393", "D": "D393", "E": "E393", "F": "F393", "G": "G393", "H": "H393", "I": "I393", "J": "J393"} | 粒子數濃度 | 量測通道 | 未由欄名確認 | PTrakMeasurement(PtPerCC)/1000 (right)；PTrakMeasurement(PtPerCC) (right)；PTrakMeasurement(PtPerCC)/1000(right)；PTrakMeasurement(PtPerCC)/1000 (left scale)；PTrakMeasurement(PtPerCC)/1000 (Right)；PTrakMeasurement(PtPerCC/100) (left)；PTrakMeasurement(PtPerCC) (Right)；PTrakMeasurement(PtPerCC/100) (Right)；PTrakMeasurement(PtPerCC/1000) (right)；PTrakMeasurement(PtPerCC)/1000 (right scale)；其餘見原始欄位; 01_實驗資料/第一批下載/PSI-102_SAME/Analyzed Data/PSI-102_Analyzed Data_GMT263 run 14 kapton avg.xls; GMT263kaphkp!R1C25 | \[{"target_sheet": "GMT263kaphkp", "target_cell": "Y1", "actual_header_or_log_cell": "PTrakMeasurement(PtPerCC)/1000 (right)", "is_one_of_reference_aliases": true, "locator_status": "literal original source target cell checked; log text distinguished from numeric trial factor"}\] |
| PSI-102 | 物理參數 row394; {"A": "A394", "B": "B394", "C": "C394", "D": "D394", "E": "E394", "F": "F394", "G": "G394", "H": "H394", "I": "I394", "J": "J394"} | 粒子質量濃度 | 量測通道 | MgPerM3 | DustTrakAMeasurement(MgPerM3)；DustTrakBMeasurement(MgPerM3)；DustTrakBMeasurement(MgPerM3)right；DustTrakAMeasurement(MgPerM3)right；DustTrakBMeasurement(MgPerM3) right scale；DustTrakBMeasurement(MgPerM3) right; 01_實驗資料/第一批下載/PSI-102_SAME/Analyzed Data/PSI-102_Analyzed Data_GMT255hkp.xlsx; Copy of GMT255hkp!R1C28 | \[{"target_sheet": "Copy of GMT255hkp", "target_cell": "AB1", "actual_header_or_log_cell": "DustTrakAMeasurement(MgPerM3)", "is_one_of_reference_aliases": true, "locator_status": "literal original source target cell checked; log text distinguished from numeric trial factor"}\] |
| PSI-102 | 物理參數 row395; {"A": "A395", "B": "B395", "C": "C395", "D": "D395", "E": "E395", "F": "F395", "G": "G395", "H": "H395", "I": "I395", "J": "J395"} | 粒子質量濃度 | 量測通道 | Volts | DustTrakAAnalogMeasurement(Volts)；DustTrakBAnalogMeasurement(Volts); 01_實驗資料/第一批下載/PSI-102_SAME/Analyzed Data/PSI-102_Analyzed Data_GMT255hkp.xlsx; Copy of GMT255hkp!R1C30 | \[{"target_sheet": "Copy of GMT255hkp", "target_cell": "AD1", "actual_header_or_log_cell": "DustTrakAAnalogMeasurement(Volts)", "is_one_of_reference_aliases": true, "locator_status": "literal original source target cell checked; log text distinguished from numeric trial factor"}\] |
| PSI-102 | 物理參數 row396; {"A": "A396", "B": "B396", "C": "C396", "D": "D396", "E": "E396", "F": "F396", "G": "G396", "H": "H396", "I": "I396", "J": "J396"} | 粒子質量濃度 | 量測通道 | 未由欄名確認 | DustTrakAMeasurement(MgPerM3) (right)；DustTrakBMeasurement(MgPerM3) (right)；DustTrakAMeasurement(MgPerM3) (left scale)；DustTrakBMeasurement(MgPerM3) (right scale)；DustTrakAMeasurement(MgPerM3) (Right)；DustTrakBMeasurement(MgPerM3) (Right)；DustTrakAMeasurement(MgPerM3) (left)；DustTrakBMeasurement(MgPerM3)(right)；DustTrakAMeasurement(MgPerM3) (right scale); 01_實驗資料/第一批下載/PSI-102_SAME/Analyzed Data/PSI-102_Analyzed Data_GMT272lampwick31.xls; GMT272lampwick31hkp!R1C26 | \[{"target_sheet": "GMT272lampwick31hkp", "target_cell": "Z1", "actual_header_or_log_cell": "DustTrakAMeasurement(MgPerM3) (right)", "is_one_of_reference_aliases": true, "locator_status": "literal original source target cell checked; log text distinguished from numeric trial factor"}\] |
| PSI-102 | 物理參數 row397; {"A": "A397", "B": "B397", "C": "C397", "D": "D397", "E": "E397", "F": "F397", "G": "G397", "H": "H397", "I": "I397", "J": "J397"} | 粒徑／粒子分布 | 計算／影像分析量 | 未由欄名確認 | CommDiagASolenoid\[VR11\]；CommDiagBSolenoid\[VR12\]; 01_實驗資料/第一批下載/PSI-102_SAME/Analyzed Data/PSI-102_Analyzed Data_GMT255hkp.xlsx; Copy of GMT255hkp!R1C75 | \[{"target_sheet": "Copy of GMT255hkp", "target_cell": "BW1", "actual_header_or_log_cell": "CommDiagASolenoid\[VR11\]", "is_one_of_reference_aliases": true, "locator_status": "literal original source target cell checked; log text distinguished from numeric trial factor"}\] |
| PSI-102 | 物理參數 row398; {"A": "A398", "B": "B398", "C": "C398", "D": "D398", "E": "E398", "F": "F398", "G": "G398", "H": "H398", "I": "I398", "J": "J398"} | 質量流率 | 量測或設定 | LPM | MFCMassFlowRate(LPM); 01_實驗資料/第一批下載/PSI-102_SAME/Analyzed Data/PSI-102_Analyzed Data_GMT255hkp.xlsx; Copy of GMT255hkp!R1C36 | \[{"target_sheet": "Copy of GMT255hkp", "target_cell": "AJ1", "actual_header_or_log_cell": "MFCMassFlowRate(LPM)", "is_one_of_reference_aliases": true, "locator_status": "literal original source target cell checked; log text distinguished from numeric trial factor"}\] |
| PSI-102 | 物理參數 row399; {"A": "A399", "B": "B399", "C": "C399", "D": "D399", "E": "E399", "F": "F399", "G": "G399", "H": "H399", "I": "I399", "J": "J399"} | 質量流率 | 量測或設定 | 未由欄名確認 | Initializing Mass Flow Controller；Mass Flow Controller initialized; 01_實驗資料/第一批下載/PSI-102_SAME/Analyzed Data/PSI-102_Analyzed Data_GMT254HKPandLOGmultiple runs.xls; GMT254 LOG!R36C2 | \[{"target_sheet": "GMT254 LOG", "target_cell": "B36", "actual_header_or_log_cell": "Initializing Mass Flow Controller", "is_one_of_reference_aliases": true, "locator_status": "literal original source target cell checked; log text distinguished from numeric trial factor"}\] |
| PSI-102 | 物理參數 row400; {"A": "A400", "B": "B400", "C": "C400", "D": "D400", "E": "E400", "F": "F400", "G": "G400", "H": "H400", "I": "I400", "J": "J400"} | 質量／質量損失 | 量測或衍生 | Ohms | SampleResistance(Ohms); 01_實驗資料/第一批下載/PSI-102_SAME/Analyzed Data/PSI-102_Analyzed Data_GMT255hkp.xlsx; Copy of GMT255hkp!R1C21 | \[{"target_sheet": "Copy of GMT255hkp", "target_cell": "U1", "actual_header_or_log_cell": "SampleResistance(Ohms)", "is_one_of_reference_aliases": true, "locator_status": "literal original source target cell checked; log text distinguished from numeric trial factor"}\] |
| PSI-102 | 物理參數 row401; {"A": "A401", "B": "B401", "C": "C401", "D": "D401", "E": "E401", "F": "F401", "G": "G401", "H": "H401", "I": "I401", "J": "J401"} | 質量／質量損失 | 量測或衍生 | mg/min | Weight loss rate (mg/min); 01_實驗資料/第一批下載/PSI-102_SAME/Experimental table/PSI-102_Experimental table_SAME.csv; line 1, column 4 | \[{"csv_line": 1, "column_1based": 4, "actual_header": "Weight loss rate (mg/min)", "is_one_of_reference_aliases": true, "locator_status": "literal experimental CSV header checked; index not assumed per-trial measurement"}\] |
| PSI-102 | 物理參數 row402; {"A": "A402", "B": "B402", "C": "C402", "D": "D402", "E": "E402", "F": "F402", "G": "G402", "H": "H402", "I": "I402", "J": "J402"} | 風扇／流量顯示設定 | 儀器設定 | 未由欄名確認 | MixingFanPower; 01_實驗資料/第一批下載/PSI-102_SAME/Analyzed Data/PSI-102_Analyzed Data_GMT255hkp.xlsx; Copy of GMT255hkp!R1C59 | \[{"target_sheet": "Copy of GMT255hkp", "target_cell": "BG1", "actual_header_or_log_cell": "MixingFanPower", "is_one_of_reference_aliases": true, "locator_status": "literal original source target cell checked; log text distinguished from numeric trial factor"}\] |
| PSI-102 | 物理參數 row403; {"A": "A403", "B": "B403", "C": "C403", "D": "D403", "E": "E403", "F": "F403", "G": "G403", "H": "H403", "I": "I403", "J": "J403"} | 體積流量／MFC | 儀器設定／控制參數 | LPM | MFCSetpoint(LPM)；MFCAnalogSetpoint\[BN19\](LPM); 01_實驗資料/第一批下載/PSI-102_SAME/Analyzed Data/PSI-102_Analyzed Data_GMT255hkp.xlsx; Copy of GMT255hkp!R1C35 | \[{"target_sheet": "Copy of GMT255hkp", "target_cell": "AI1", "actual_header_or_log_cell": "MFCSetpoint(LPM)", "is_one_of_reference_aliases": true, "locator_status": "literal original source target cell checked; log text distinguished from numeric trial factor"}\] |
| PSI-102 | 物理參數 row404; {"A": "A404", "B": "B404", "C": "C404", "D": "D404", "E": "E404", "F": "F404", "G": "G404", "H": "H404", "I": "I404", "J": "J404"} | 體積流量／MFC | 量測或設定 | LPM | MFCAnalogFlowRate(LPM); 01_實驗資料/第一批下載/PSI-102_SAME/Analyzed Data/PSI-102_Analyzed Data_GMT255hkp.xlsx; Copy of GMT255hkp!R1C40 | \[{"target_sheet": "Copy of GMT255hkp", "target_cell": "AN1", "actual_header_or_log_cell": "MFCAnalogFlowRate(LPM)", "is_one_of_reference_aliases": true, "locator_status": "literal original source target cell checked; log text distinguished from numeric trial factor"}\] |
| PSI-102 | 物理參數 row405; {"A": "A405", "B": "B405", "C": "C405", "D": "D405", "E": "E405", "F": "F405", "G": "G405", "H": "H405", "I": "I405", "J": "J405"} | 體積流量／MFC | 量測或設定 | SCCM | LFEFlowRate\[AT08\](SCCM); 01_實驗資料/第一批下載/PSI-102_SAME/Analyzed Data/PSI-102_Analyzed Data_GMT255hkp.xlsx; Copy of GMT255hkp!R1C32 | \[{"target_sheet": "Copy of GMT255hkp", "target_cell": "AF1", "actual_header_or_log_cell": "LFEFlowRate\[AT08\](SCCM)", "is_one_of_reference_aliases": true, "locator_status": "literal original source target cell checked; log text distinguished from numeric trial factor"}\] |
| PSI-102 | 物理參數 row406; {"A": "A406", "B": "B406", "C": "C406", "D": "D406", "E": "E406", "F": "F406", "G": "G406", "H": "H406", "I": "I406", "J": "J406"} | 體積流量／MFC | 量測或設定 | 未由欄名確認 | Zeroing the LFE；SetLFEFlowRate(23; 01_實驗資料/第一批下載/PSI-102_SAME/Analyzed Data/PSI-102_Analyzed Data_GMT256LOG.xlsx; GMT256LOG!R8C2 | \[{"target_sheet": "GMT256LOG", "target_cell": "B8", "actual_header_or_log_cell": "Zeroing the LFE", "is_one_of_reference_aliases": true, "locator_status": "literal original source target cell checked; log text distinguished from numeric trial factor"}\] |

### 原分類與實際表頭的已知差異

| 參考位置 | 實際欄位 | 可支持的量／訊號意義 | 不能照抄的解讀 |
| --- | --- | --- | --- |
| 物理參數 row392 | PTrakPowerMeasurement(Volts) | 儀器電源／狀態相關電壓訊號 | 不是粒子數濃度 |
| 物理參數 row397 | CommDiagASolenoid / CommDiagBSolenoid | 通訊／電磁閥狀態欄 | 不是粒徑分布 |
| 物理參數 row400 | SampleResistance(Ohms) | 電阻及加熱條件相關量 | 不是質量／質量損失 |
| 表頭含MFCMassFlowRate(LPM) | LPM | 依原表頭為體積流量；標準／實際體積參考狀態未知 | 不能直接當g/s；需密度、P/T與參考狀態 |

## 讀取範圍與原表疑點（非物理因子）

本節的檔案數、列數或讀取範圍不是材料／環境物理量，也不賦予單位。

| 研究 | Excel位置 | 原始儲存格內容 | 儲存格定位 |
| --- | --- | --- | --- |
| PSI-101 | 讀取範圍 row23 | {"A": "PSI-101", "B": "SAME-R", "C": 135, "D": 18010, "E": 687, "F": "{\"header_or_keys_found\": 45, \"metadata_parsed\": 1, \"xlsx_labels_scanned\": 14, \"legacy_xls_labels_scanned\": 75}", "G": "文字檔前 128 KiB；XLSX 每頁前 80 列／100 欄；XLS 每頁前 100 列／100 欄；ZIP 內可讀文字表頭", "H": "數值時序未逐值展開；二進位／媒體及無表頭數據另保留狀態"} | {"A": "A23", "B": "B23", "C": "C23", "D": "D23", "E": "E23", "F": "F23", "G": "G23", "H": "H23"} |
| PSI-102 | 讀取範圍 row24 | {"A": "PSI-102", "B": "SAME", "C": 61, "D": 6340, "E": 322, "F": "{\"header_or_keys_found\": 1, \"metadata_parsed\": 1, \"xlsx_labels_scanned\": 6, \"legacy_xls_labels_scanned\": 53}", "G": "文字檔前 128 KiB；XLSX 每頁前 80 列／100 欄；XLS 每頁前 100 列／100 欄；ZIP 內可讀文字表頭", "H": "數值時序未逐值展開；二進位／媒體及無表頭數據另保留狀態"} | {"A": "A24", "B": "B24", "C": "C24", "D": "D24", "E": "E24", "F": "F24", "G": "G24", "H": "H24"} |
| PSI-101 | 原表疑點 row41 | {"A": "PSI-101", "B": "#NUM!", "C": "#NUM!", "D": "來源公式文字／錯誤碼；保留原文，未計算", "E": "01_實驗資料/第一批下載/PSI-101_SAME-R/Analyzed Data/PSI-101_Analyzed Data_54 lampwick binneddatacorr from GWM.xlsx"} | {"A": "A41", "B": "B41", "C": "C41", "D": "D41", "E": "E41"} |
| PSI-101 | 原表疑點 row42 | {"A": "PSI-101", "B": "#DIV/0!", "C": "#DIV/0!", "D": "來源公式文字／錯誤碼；保留原文，未計算", "E": "01_實驗資料/第一批下載/PSI-101_SAME-R/Analyzed Data/PSI-101_Analyzed Data_94 Kapton aged- results.xlsx"} | {"A": "A42", "B": "B42", "C": "C42", "D": "D42", "E": "E42"} |

## 摘要工作表的原始欄位與單位

| 研究 | 工作表 | 欄／表頭儲存格 | 原始表頭 | 原始單位 |
| --- | --- | --- | --- | --- |
| PSI-101 | SAME R Results | A; A2 | Carousel | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | B; B2 | Sample Type | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | C; C2 | Sample ID | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | D; D2 | Test ID Number | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | E; E2 | Position in Carousel | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | F; F2 | SAME # | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | G; G2 | Description | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | H; H2 | GMT | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | I; I2 | Date (EST) | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | J; J2 | TEAM Test ID Number | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | K; K2 | Inlet Velocity (cm/sec) | cm/s |
| PSI-101 | SAME R Results | L; L2 | Rt/R0 | dimensionless |
| PSI-101 | SAME R Results | M; M2 | Duration (sec) | s |
| PSI-101 | SAME R Results | N; N2 | Primary Aging Duration (sec) | s |
| PSI-101 | SAME R Results | O; O2 | Primary Mixing Duration (sec) | s |
| PSI-101 | SAME R Results | P; P2 | PreAge Thermal Precipitator | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | Q; Q2 | PreAge Thermal Precipitator Duration | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | R; R2 | Net Aging  Duration | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | S; S2 | Primary Aging Therm Precip | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | T; T2 | Primary Aging Therm Precip Duration | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | U; U2 | Use STS Detector | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | V; V2 | Use Comm Diag A | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | W; W2 | Use Comm Diag B | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | X; X2 | Diluting A | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | Y; Y2 | Diluting B | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | Z; Z2 | Cyclone Inlet on CDA (MPASS) | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | AA; AA2 | Impactor Inlet on CDB | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | AB; AB2 | Use P-Trak | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | AC; AC2 | Aerosol Concentration To P-Trak | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | AD; AD2 | Aerosol Conteration to DustTrak (Not in use) | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | AE; AE2 | Secondary Diagnostics Volume %  | % |
| PSI-101 | SAME R Results | AF; AF2 | Secondary Aging Duration (sec) | s |
| PSI-101 | SAME R Results | AG; AG2 | Secondary Mixing Duration (sec) | s |
| PSI-101 | SAME R Results | AH; AH2 | STSDetector | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | AI; AI2 | Comm Diag A | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | AJ; AJ2 | Comm Diag B | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | AK; AK2 | Diluting A | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | AL; AL2 | Diluting B | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | AM; AM2 | Ues PTrak | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | AN; AN2 | Aerosol Concentration To P-Trak | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | AO; AO2 | Aerosol Conteration to DustTrak (Not in use) | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | AP; AP2 | secondary agign thermal precip duration | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | AQ; AQ2 | ISS Obscuration (volts) | V |
| PSI-101 | SAME R Results | AR; AR2 | ISS Detector Scatter (volts) | V |
| PSI-101 | SAME R Results | AS; AS2 | STS Detector (volts) | V |
| PSI-101 | SAME R Results | AT; AT2 | STS Detector offset (volts) | V |
| PSI-101 | SAME R Results | AU; AU2 | Ion A (volts) Mpass_3rd | V |
| PSI-101 | SAME R Results | AV; AV2 | Ion A offset V0 (volts) | V |
| PSI-101 | SAME R Results | AW; AW2 | Ion B (volts) | V |
| PSI-101 | SAME R Results | AX; AX2 | Ion B offset V0 (volts) | V |
| PSI-101 | SAME R Results | AY; AY2 | Ptrak (PT/cc) | #/cm^3 |
| PSI-101 | SAME R Results | AZ; AZ2 | DustTrak A (mg/m3) Mpass_2nd | mg/m^3 |
| PSI-101 | SAME R Results | BA; BA2 | DustTrak A (mg/m3) Mpass_2nd offset | mg/m^3 |
| PSI-101 | SAME R Results | BB; BB2 | DustTrak B (mg/m3) | mg/m^3 |
| PSI-101 | SAME R Results | BC; BC2 | Ion B Delta (volts) | V |
| PSI-101 | SAME R Results | BD; BD2 | M0 best Diameter (#/cm3) | #/cm^3 |
| PSI-101 | SAME R Results | BE; BE2 | M1 (mm/cm3) | mm/cm^3 |
| PSI-101 | SAME R Results | BF; BF2 |  Mpass_3rd offset and dilution corrected | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | BG; BG2 | DustTrak A (mg/m3) Mpass_2nd  offset, dilution and Gain corrected | mg/m^3 |
| PSI-101 | SAME R Results | BH; BH2 | DustTrak B calibratred and corrected for dilution (mg/m3) | mg/m^3 |
| PSI-101 | SAME R Results | BI; BI2 | M1/M0 (micro-m)--AMD | um |
| PSI-101 | SAME R Results | BJ; BJ2 | Diameter of Average mass (micro-m) | um |
| PSI-101 | SAME R Results | BK; BK2 | George's d2,1,  (micro-m) | um |
| PSI-101 | SAME R Results | BL; BL2 | MPASS 3/2 | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | BM; BM2 | Hatch Choate Sigma g | dimensionless |
| PSI-101 | SAME R Results | BN; BN2 | Hatch Choate Dg | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | BO; BO2 | CPC 100 nm cal, dilution corrected | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | BP; BP2 | CPC 600 nm cal, dilution corrected | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | BQ; BQ2 | CPC 1200 nm cal, dilution corrected | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | BR; BR2 | Ion B Mment  mm/cm^3 | mm/cm^3 |
| PSI-101 | SAME R Results | BS; BS2 | Ion B X | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | BT; BT2 | Dust Trak Cal Factor (Teom/Dusttrak) | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | BU; BU2 | MPASS Dilution factor | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | BV; BV2 | Dust Trak Dilution factor | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | BW; BW2 | Particle density g/cc | g/cm^3 |
| PSI-101 | SAME R Results | BX; BX2 | Dilution ratio for Mpass, total flow 1.68576 LPM | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | BY; BY2 | Dilution ratio for DustTrak B, total flow 1.69076 LPM | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | BZ; BZ2 | T ( C) - Eq. 2 of lrt | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | CA; CA2 | Mass Loss (mg) | mg |
| PSI-101 | SAME R Results | CB; CB2 | Test Number | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | CC; CC2 | GMT | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | CD; CD2 | Yeild: Dust Trak mass/mass lostt | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | CI; CI2 | run | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | CJ; CJ2 | material | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | CK; CK2 | AMD | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | CL; CL2 | mass1 caculated with dector 3 | Unknown（來源未提供／尚未核對） |
| PSI-101 | SAME R Results | CM; CM2 | mass2 both detectors | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME1 Flight Tests 8-27-09 | A; A2 | Carousel | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME1 Flight Tests 8-27-09 | B; B2 | Sample Type | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME1 Flight Tests 8-27-09 | C; C2 | Test ID Number | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME1 Flight Tests 8-27-09 | D; D2 | Position in Carousel | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME1 Flight Tests 8-27-09 | E; E2 | SAME # | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME1 Flight Tests 8-27-09 | F; F2 | Description | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME1 Flight Tests 8-27-09 | G; G2 | GMT | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME1 Flight Tests 8-27-09 | H; H2 | Date | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME1 Flight Tests 8-27-09 | I; I2 | Team Test ID Number | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME1 Flight Tests 8-27-09 | J; J2 | Fan problem | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME1 Flight Tests 8-27-09 | K; K2 | Flat profiles | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME1 Flight Tests 8-27-09 | L; L2 | Inlet Velocity (cm/sec) | cm/s |
| PSI-102 | SAME1 Flight Tests 8-27-09 | M; M2 | Rt/R0 | dimensionless |
| PSI-102 | SAME1 Flight Tests 8-27-09 | N; N2 | Duration (sec) | s |
| PSI-102 | SAME1 Flight Tests 8-27-09 | O; O2 | Aging Duration (sec) | s |
| PSI-102 | SAME1 Flight Tests 8-27-09 | P; P2 | Primary Mixing Duration (sec) | s |
| PSI-102 | SAME1 Flight Tests 8-27-09 | Q; Q2 | Net Aging  Duration | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME1 Flight Tests 8-27-09 | R; R2 | Diluting A | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME1 Flight Tests 8-27-09 | S; S2 | Diluting B | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME1 Flight Tests 8-27-09 | T; T2 | Impactor Inlet on CDA | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME1 Flight Tests 8-27-09 | U; U2 | Impactor Inlet on CDB | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME1 Flight Tests 8-27-09 | V; V2 | Aerosol Concentration To P-Trak | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME1 Flight Tests 8-27-09 | W; W2 | Dust Trak Aerosol Fraction ( = 1/Dilution ratio) | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME1 Flight Tests 8-27-09 | X; X2 | Mass Loss (mg) | mg |
| PSI-102 | SAME1 Flight Tests 8-27-09 | Y; Y2 | ISS Obscuration (volts) | V |
| PSI-102 | SAME1 Flight Tests 8-27-09 | Z; Z2 | ISS Detector Scatter (volts) | V |
| PSI-102 | SAME1 Flight Tests 8-27-09 | AA; AA2 | STS Detector (volts) | V |
| PSI-102 | SAME1 Flight Tests 8-27-09 | AB; AB2 | Ion B (volts) | V |
| PSI-102 | SAME1 Flight Tests 8-27-09 | AC; AC2 | Ion A offset V0 (volts) | V |
| PSI-102 | SAME1 Flight Tests 8-27-09 | AD; AD2 | Ion B offset V0 (volts) | V |
| PSI-102 | SAME1 Flight Tests 8-27-09 | AE; AE2 | Ptrak PT/cc | #/cm^3 |
| PSI-102 | SAME1 Flight Tests 8-27-09 | AF; AF2 | DustTrak A (mg/m3) | mg/m^3 |
| PSI-102 | SAME1 Flight Tests 8-27-09 | AG; AG2 | DustTrak B (mg/m3) | mg/m^3 |
| PSI-102 | SAME1 Flight Tests 8-27-09 | AH; AH2 | Ion B Delta (volts) | V |
| PSI-102 | SAME1 Flight Tests 8-27-09 | AI; AI2 | DustTrak A corrected for dilution (mg/m3) | mg/m^3 |
| PSI-102 | SAME1 Flight Tests 8-27-09 | AJ; AJ2 | DustTrak B corrected for dilution (mg/m3) | mg/m^3 |
| PSI-102 | SAME1 Flight Tests 8-27-09 | AK; AK2 | Mo Best Diameter (#/cm3) | #/cm^3 |
| PSI-102 | SAME1 Flight Tests 8-27-09 | AL; AL2 | M1 (Ion) Chamber constant based (mm/cm3) | mm/cm^3 |
| PSI-102 | SAME1 Flight Tests 8-27-09 | AM; AM2 | M3  TEOM Calibrated Corrected for Dilution | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME1 Flight Tests 8-27-09 | AN; AN2 | Real | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME1 Flight Tests 8-27-09 | AO; AO2 | Img | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME1 Flight Tests 8-27-09 | AP; AP2 | Computed arithmetic mean diameter (micrometers) | um |
| PSI-102 | SAME1 Flight Tests 8-27-09 | AQ; AQ2 | Diam Avg Mass (DAM) Teom Calibrated  (micrometers)  | um |
| PSI-102 | SAME1 Flight Tests 8-27-09 | AS; AS2 | Hatch Choate Sigma g | dimensionless |
| PSI-102 | SAME1 Flight Tests 8-27-09 | AT; AT2 | Hatch Choate Dg | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME1 Flight Tests 8-27-09 | AU; AU2 | Dustrak scattering program   predicted (mg/m^3) | mg/m^3 |
| PSI-102 | SAME1 Flight Tests 8-27-09 | AV; AV2 | Scattering Predicted geometric mean size (micrometers) | um |
| PSI-102 | SAME1 Flight Tests 8-27-09 | AW; AW2 | Scattering Program Predicted geometric standard deviation | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME1 Flight Tests 8-27-09 | AX; AX2 | TEOM sigma old version | dimensionless |
| PSI-102 | SAME1 Flight Tests 8-27-09 | AY; AY2 | TEOM dg old version | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME1 Flight Tests 8-27-09 | AZ; AZ2 | Scattering Predicted Davg mass | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME1 Flight Tests 8-27-09 | BA; BA2 | Predicted mass conc. mg/m^3 | mg/m^3 |
| PSI-102 | SAME1 Flight Tests 8-27-09 | BB; BB2 | CPC 100 nm cal, dilution corrected | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME1 Flight Tests 8-27-09 | BC; BC2 | CPC 600 nm cal, dilution corrected | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME1 Flight Tests 8-27-09 | BD; BD2 | CPC 1200 nm cal, dilution corrected | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME1 Flight Tests 8-27-09 | BE; BE2 | Density (g/cc) | g/cm^3 |
| PSI-102 | SAME1 Flight Tests 8-27-09 | BF; BF2 | Teom Cal Factor | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME1 Flight Tests 8-27-09 | BG; BG2 | Ion X | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME1 Flight Tests 8-27-09 | BH; BH2 | T ( C) - Eq. 2 of lrt | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME1 Flight Tests 8-27-09 | BI; BI2 | Mass Loss (mg) | mg |
| PSI-102 | SAME1 Flight Tests 8-27-09 | BJ; BJ2 | Test Number | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME1 Flight Tests 8-27-09 | BK; BK2 | GMT | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME1 Flight Tests 8-27-09 | BL; BL2 | Yeild: Dust Trak mass/mass lostt | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME1 Flight Tests 8-27-09 | BM; BM2 |  Fractional change in Dust Trak A corrected for Impactor | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME1 Flight Tests 8-27-09 | BN; BN2 | Dust Trak B corrected for Impactor | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME1 Flight Tests 8-27-09 | BO; BO2 | Eta 1 micron for Dustrak A | um |
| PSI-102 | SAME1 Flight Tests 8-27-09 | BP; BP2 | Eta 10 micron for Dustrak B | um |
| PSI-102 | SAME1 Flight Tests 8-27-09 | BQ; BQ2 | Dust Trak Ratios corrected for Impactors | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME1 Flight Tests 8-27-09 | BR; BR2 | Dust Trak Ratios (corrected for diltion only) | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME1 Flight Tests 8-27-09 | BS; BS2 | fractional cahnge in 10 micron dustrak | um |
| PSI-102 | SAME Ground Test Results | A; A2 | Carousel | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME Ground Test Results | B; B2 | Sample Type | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME Ground Test Results | C; C2 | Test ID Number | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME Ground Test Results | D; D2 | Position in Carousel | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME Ground Test Results | E; E2 | Description | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME Ground Test Results | F; F2 | GMT | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME Ground Test Results | G; G2 | Date | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME Ground Test Results | H; H2 | Team Test ID Number | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME Ground Test Results | I; I2 | Fan problem | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME Ground Test Results | J; J2 | Flat profiles | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME Ground Test Results | K; K2 | Inlet Velocity (cm/sec) | cm/s |
| PSI-102 | SAME Ground Test Results | L; L2 | Rt/R0 | dimensionless |
| PSI-102 | SAME Ground Test Results | M; M2 | Duration (sec) | s |
| PSI-102 | SAME Ground Test Results | N; N2 | Aging Duration (sec) | s |
| PSI-102 | SAME Ground Test Results | O; O2 | Primary Mixing Duration (sec) | s |
| PSI-102 | SAME Ground Test Results | P; P2 | Diluting A | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME Ground Test Results | Q; Q2 | Diluting B | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME Ground Test Results | R; R2 | Impactor Inlet on CDA | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME Ground Test Results | S; S2 | Impactor Inlet on CDB | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME Ground Test Results | T; T2 | Aerosol Concentration To P-Trak | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME Ground Test Results | U; U2 | Dust Trak Aerosol Fraction ( = 1/dilution ratio | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME Ground Test Results | V; V2 | ISS Obscuration (volts) | V |
| PSI-102 | SAME Ground Test Results | W; W2 | ISS Detector Scatter (volts) | V |
| PSI-102 | SAME Ground Test Results | X; X2 | STS Detector (volts) | V |
| PSI-102 | SAME Ground Test Results | Y; Y2 | Ion A (volts) 003 | V |
| PSI-102 | SAME Ground Test Results | Z; Z2 | Ion B (volts) 002 | V |
| PSI-102 | SAME Ground Test Results | AA; AA2 | Ion A offset V0 (volts) | V |
| PSI-102 | SAME Ground Test Results | AB; AB2 | Ion B offset V0 (volts) | V |
| PSI-102 | SAME Ground Test Results | AC; AC2 | Ptrak PT/cc  005 | #/cm^3 |
| PSI-102 | SAME Ground Test Results | AD; AD2 | DustTrak A (mg/m3) 003 | mg/m^3 |
| PSI-102 | SAME Ground Test Results | AE; AE2 | DustTrak B (mg/m3) 002 | mg/m^3 |
| PSI-102 | SAME Ground Test Results | AF; AF2 | Ratio B / A | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME Ground Test Results | AG; AG2 | Ion A Delta (volts) | V |
| PSI-102 | SAME Ground Test Results | AH; AH2 | Ion B Delta (volts) | V |
| PSI-102 | SAME Ground Test Results | AI; AI2 | Ion A M1 | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME Ground Test Results | AJ; AJ2 | Ion B M1 | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME Ground Test Results | AK; AK2 | M3 A TEOM Calibrated | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME Ground Test Results | AL; AL2 | M3 B TEOM Calibrated | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME Ground Test Results | AM; AM2 | Best Diameter Ion A/Ptrak Count Mean Diamter (microns) | um |
| PSI-102 | SAME Ground Test Results | AN; AN2 | Best Diameter Ion B/Ptrak Count Mean Diameter (microns) | um |
| PSI-102 | SAME Ground Test Results | AO; AO2 | DTRak A Diameter of average mass micrometers | um |
| PSI-102 | SAME Ground Test Results | AP; AP2 | DTRak B Diameter of average mass micrometers | um |
| PSI-102 | SAME Ground Test Results | AQ; AQ2 | DustTrak A corrected for dilution (mg/m3) | mg/m^3 |
| PSI-102 | SAME Ground Test Results | AR; AR2 | DustTrak B corrected for dilution (mg/m3) | mg/m^3 |
| PSI-102 | SAME Ground Test Results | AS; AS2 | Mo Best Diameter | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME Ground Test Results | AT; AT2 | CPC 100 nm cal, dilution corrected | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME Ground Test Results | AU; AU2 | CPC 600 nm cal, dilution corrected | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME Ground Test Results | AV; AV2 | CPC 1200 nm cal, dilution corrected | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME Ground Test Results | AW; AW2 | Density (g/cc) | g/cm^3 |
| PSI-102 | SAME Ground Test Results | AX; AX2 | Teom Cal Factor | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME Ground Test Results | AY; AY2 | Ion A X | Unknown（來源未提供／尚未核對） |
| PSI-102 | SAME Ground Test Results | AZ; AZ2 | Ion A X | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | A; A2 | Test sequence  | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | B; B2 | Sample Type | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | C; C2 | Sample ID | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | D; D2 | Test ID Number | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | E; E2 | Position in Carousel | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | F; F2 | SAME # | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | G; G2 | Description | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | H; H2 | GMT (In the SAME computer, not actual GMT) | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | I; I2 | Date (EST) | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | J; J2 | TEAM Test ID Number | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | K; K2 | Inlet Velocity (cm/sec) | cm/s |
| PSI-101 | Gnd Verif. 8-2012 | L; L2 | Rt/R0 | dimensionless |
| PSI-101 | Gnd Verif. 8-2012 | M; M2 | Duration (sec) | s |
| PSI-101 | Gnd Verif. 8-2012 | N; N2 | Primary Aging Duration (sec) | s |
| PSI-101 | Gnd Verif. 8-2012 | O; O2 | Primary Mixing Duration (sec) | s |
| PSI-101 | Gnd Verif. 8-2012 | P; P2 | PreAge Thermal Precipitator | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | Q; Q2 | PreAge Thermal Precipitator Duration | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | R; R2 | Net Aging  Duration | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | S; S2 | Primary Aging Therm Precip | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | T; T2 | Primary Aging Therm Precip Duration | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | U; U2 | Use STS Detector | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | V; V2 | Use Comm Diag A (Mpass) | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | W; W2 | Use Comm Diag B | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | X; X2 | Diluting A | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | Y; Y2 | Diluting B | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | Z; Z2 | Cyclone Inlet on CDA (MPASS) | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | AA; AA2 | Impactor Inlet on CDB | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | AB; AB2 | Use P-Trak | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | AC; AC2 | Aerosol Concentration To P-Trak | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | AD; AD2 | Aerosol Conteration to DustTrak (Not in use) | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | AE; AE2 | Secondary Diagnostics Volume %  | % |
| PSI-101 | Gnd Verif. 8-2012 | AF; AF2 | Secondary Aging Duration (sec) | s |
| PSI-101 | Gnd Verif. 8-2012 | AG; AG2 | Secondary Mixing Duration (sec) | s |
| PSI-101 | Gnd Verif. 8-2012 | AH; AH2 | STSDetector | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | AI; AI2 | Comm Diag A | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | AJ; AJ2 | Comm Diag B | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | AK; AK2 | Diluting A | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | AL; AL2 | Diluting B | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | AM; AM2 | Ues PTrak | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | AN; AN2 | Aerosol Concentration To P-Trak | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | AO; AO2 | Aerosol Conteration to DustTrak (Not in use) | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | AP; AP2 | secondary agign thermal precip duration | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | AQ; AQ2 | ISS Obscuration (volts) | V |
| PSI-101 | Gnd Verif. 8-2012 | AR; AR2 | ISS Detector Scatter (volts) | V |
| PSI-101 | Gnd Verif. 8-2012 | AS; AS2 | STS Detector (volts) | V |
| PSI-101 | Gnd Verif. 8-2012 | AT; AT2 | STS Detector offset (volts) | V |
| PSI-101 | Gnd Verif. 8-2012 | AU; AU2 | Ion A (volts) Mpass_3rd | V |
| PSI-101 | Gnd Verif. 8-2012 | AV; AV2 | Ion A Mpass_3rd offset V0 (volts) | V |
| PSI-101 | Gnd Verif. 8-2012 | AW; AW2 | Ion B (volts) | V |
| PSI-101 | Gnd Verif. 8-2012 | AX; AX2 | Ion B offset V0 (volts) | V |
| PSI-101 | Gnd Verif. 8-2012 | AY; AY2 | Ptrak (PT/cc) | #/cm^3 |
| PSI-101 | Gnd Verif. 8-2012 | AZ; AZ2 | DustTrak A (mg/m3) Mpass_2nd | mg/m^3 |
| PSI-101 | Gnd Verif. 8-2012 | BA; BA2 | DustTrak A (mg/m3) Mpass_2nd offset | mg/m^3 |
| PSI-101 | Gnd Verif. 8-2012 | BB; BB2 | DustTrak B (mg/m3) | mg/m^3 |
| PSI-101 | Gnd Verif. 8-2012 | BC; BC2 | Ion B Delta (volts) | V |
| PSI-101 | Gnd Verif. 8-2012 | BD; BD2 | M0 best Diameter (#/cm3) | #/cm^3 |
| PSI-101 | Gnd Verif. 8-2012 | BE; BE2 | M1 (mm/cm3) | mm/cm^3 |
| PSI-101 | Gnd Verif. 8-2012 | BF; BF2 |  Mpass_3rd offset and dilution corrected | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | BG; BG2 | DustTrak A (mg/m3) Mpass_2nd  offset, dilution and Gain corrected | mg/m^3 |
| PSI-101 | Gnd Verif. 8-2012 | BH; BH2 | DustTrak B calibratred and corrected for dilution (mg/m3) | mg/m^3 |
| PSI-101 | Gnd Verif. 8-2012 | BI; BI2 | M1/M0 (micro-m)--AMD | um |
| PSI-101 | Gnd Verif. 8-2012 | BJ; BJ2 | Diameter of Average mass (micro-m) | um |
| PSI-101 | Gnd Verif. 8-2012 | BK; BK2 | George's d2,1,  (micro-m) | um |
| PSI-101 | Gnd Verif. 8-2012 | BL; BL2 | MPASS 3/2 | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | BM; BM2 | Hatch Choate Sigma g | dimensionless |
| PSI-101 | Gnd Verif. 8-2012 | BN; BN2 | Hatch Choate Dg | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | BO; BO2 | CPC 100 nm cal, dilution corrected | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | BP; BP2 | CPC 600 nm cal, dilution corrected | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | BQ; BQ2 | CPC 1200 nm cal, dilution corrected | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | BR; BR2 | Ion B Mment  mm/cm^3 | mm/cm^3 |
| PSI-101 | Gnd Verif. 8-2012 | BS; BS2 | Ion B X | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | BT; BT2 | Dust Trak Cal Factor (Teom/Dusttrak) | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | BU; BU2 | MPASS Dilution factor | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | BV; BV2 | Dust Trak Dilution factor | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | BW; BW2 | Particle density g/cc | g/cm^3 |
| PSI-101 | Gnd Verif. 8-2012 | BX; BX2 | Dilution ratio for Mpass, total flow 1.68576 LPM | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | BY; BY2 | Dilution ratio for DustTrak B, total flow 1.69076 LPM | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | BZ; BZ2 | T ( C) - Eq. 2 of lrt | Unknown（來源未提供／尚未核對） |
| PSI-101 | Gnd Verif. 8-2012 | CA; CA2 | Mass Loss (mg) | mg |
| PSI-101 | Drum 8-2012 | A; A2 | Test sequence  | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | B; B2 | Sample Type | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | C; C2 | Sample ID | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | D; D2 | Test ID Number | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | E; E2 | Position in Carousel | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | F; F2 | SAME # | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | G; G2 | Description | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | H; H2 | GMT | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | I; I2 | Date (EST) | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | J; J2 | TEAM Test ID Number | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | K; K2 | Inlet Velocity (cm/sec) | cm/s |
| PSI-101 | Drum 8-2012 | L; L2 | Rt/R0 | dimensionless |
| PSI-101 | Drum 8-2012 | M; M2 | Duration (sec) | s |
| PSI-101 | Drum 8-2012 | N; N2 | Primary Aging Duration (sec) | s |
| PSI-101 | Drum 8-2012 | O; O2 | Primary Mixing Duration (sec) | s |
| PSI-101 | Drum 8-2012 | P; P2 | PreAge Thermal Precipitator | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | Q; Q2 | PreAge Thermal Precipitator Duration | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | R; R2 | Net Aging  Duration | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | S; S2 | Primary Aging Therm Precip | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | T; T2 | Primary Aging Therm Precip Duration | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | U; U2 | Use STS Detector | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | V; V2 | Use Drums (CDE A) | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | W; W2 | Use Comm Diag B | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | X; X2 | Diluting Drums (CDE A) | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | Y; Y2 | Diluting B | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | Z; Z2 | Cyclone Inlet on CDA (Drums) | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | AA; AA2 | Impactor Inlet on CDB | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | AB; AB2 | Use P-Trak | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | AC; AC2 | Aerosol Concentration To P-Trak | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | AD; AD2 | Aerosol Conteration to DustTrak (Not in use) | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | AE; AE2 | Secondary Diagnostics Volume %  | % |
| PSI-101 | Drum 8-2012 | AF; AF2 | Secondary Aging Duration (sec) | s |
| PSI-101 | Drum 8-2012 | AG; AG2 | Secondary Mixing Duration (sec) | s |
| PSI-101 | Drum 8-2012 | AH; AH2 | STSDetector | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | AI; AI2 | Drums (Comm Diag A) | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | AJ; AJ2 | Comm Diag B | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | AK; AK2 | Diluting Drums (CDE A) | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | AL; AL2 | Diluting B | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | AM; AM2 | Ues PTrak | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | AN; AN2 | Aerosol Concentration To P-Trak | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | AO; AO2 | Aerosol Conteration to DustTrak (Not in use) | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | AP; AP2 | secondary agign thermal precip duration | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | AQ; AQ2 | ISS Obscuration (volts) | V |
| PSI-101 | Drum 8-2012 | AR; AR2 | ISS Detector Scatter (volts) | V |
| PSI-101 | Drum 8-2012 | AS; AS2 | STS Detector (volts) | V |
| PSI-101 | Drum 8-2012 | AT; AT2 | STS Detector offset (volts) | V |
| PSI-101 | Drum 8-2012 | AU; AU2 | Ion A (volts) Drum | V |
| PSI-101 | Drum 8-2012 | AV; AV2 | Ion A offset V0 (volts)-Drum | V |
| PSI-101 | Drum 8-2012 | AW; AW2 | Ion B (volts) | V |
| PSI-101 | Drum 8-2012 | AX; AX2 | Ion B offset V0 (volts) | V |
| PSI-101 | Drum 8-2012 | AY; AY2 | Ptrak (PT/cc) | #/cm^3 |
| PSI-101 | Drum 8-2012 | AZ; AZ2 | DustTrak A (mg/m3) Drum | mg/m^3 |
| PSI-101 | Drum 8-2012 | BA; BA2 | DustTrak A (mg/m3) Drumoffset | mg/m^3 |
| PSI-101 | Drum 8-2012 | BB; BB2 | DustTrak B (mg/m3) | mg/m^3 |
| PSI-101 | Drum 8-2012 | BC; BC2 | Ion B Delta (volts) | V |
| PSI-101 | Drum 8-2012 | BD; BD2 | M0 best Diameter (#/cm3) | #/cm^3 |
| PSI-101 | Drum 8-2012 | BE; BE2 | M1 (mm/cm3) | mm/cm^3 |
| PSI-101 | Drum 8-2012 | BF; BF2 | (Drum)  offset and dilution corrected | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | BG; BG2 | DustTrak A (mg/m3) (Drum)  offset, dilution and Gain corrected | mg/m^3 |
| PSI-101 | Drum 8-2012 | BH; BH2 | DustTrak B calibratred and corrected for dilution (mg/m3) | mg/m^3 |
| PSI-101 | Drum 8-2012 | BI; BI2 | M1/M0 (micro-m)--AMD | um |
| PSI-101 | Drum 8-2012 | BJ; BJ2 | Diameter of Average mass (micro-m) | um |
| PSI-101 | Drum 8-2012 | BK; BK2 | George's d2,1,  (micro-m) | um |
| PSI-101 | Drum 8-2012 | BL; BL2 | MPASS 3/2 | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | BM; BM2 | Hatch Choate Sigma g | dimensionless |
| PSI-101 | Drum 8-2012 | BN; BN2 | Hatch Choate Dg | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | BO; BO2 | CPC 100 nm cal, dilution corrected | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | BP; BP2 | CPC 600 nm cal, dilution corrected | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | BQ; BQ2 | CPC 1200 nm cal, dilution corrected | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | BR; BR2 | Ion B Mment  mm/cm^3 | mm/cm^3 |
| PSI-101 | Drum 8-2012 | BS; BS2 | Ion B X | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | BT; BT2 | Dust Trak Cal Factor (Teom/Dusttrak) | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | BU; BU2 | MPASS Dilution factor | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | BV; BV2 | Dust Trak Dilution factor | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | BW; BW2 | Particle density g/cc | g/cm^3 |
| PSI-101 | Drum 8-2012 | BX; BX2 | Dilution ratio for Mpass, total flow 1.68576 LPM | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | BY; BY2 | Dilution ratio for DustTrak B, total flow 1.69076 LPM | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | BZ; BZ2 | T ( C) - Eq. 2 of lrt | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | CA; CA2 | Mass Loss (mg) | mg |
| PSI-101 | Drum 8-2012 | CB; CB2 | Test Number | Unknown（來源未提供／尚未核對） |
| PSI-101 | Drum 8-2012 | CC; CC2 | GMT | Unknown（來源未提供／尚未核對） |

## 固定模型與條件使用哪些來源欄

| 來源工作表 | 條件欄 | 矩／質量／密度／尺寸欄 | 感測器狀態欄 |
| --- | --- | --- | --- |
| SAME R Results | {"inlet_velocity": "K", "heater_resistance_ratio": "L", "heating_duration": "M", "primary_aging_duration": "N", "primary_mixing_duration": "O", "net_aging_duration": "R", "secondary_aging_duration": "AF", "secondary_mixing_duration": "AG", "secondary_volume_fraction": "AE"} | {"m0": "BD", "m1": "BE", "mass": "BH", "density": "BW", "d_count": "BI", "dm": "BJ", "dg": "BN", "sigma_g": "BM"} | \["U", "V", "W", "AB", "AH", "AI", "AJ", "AM"\] |
| SAME1 Flight Tests 8-27-09 | {"inlet_velocity": "L", "heater_resistance_ratio": "M", "heating_duration": "N", "primary_aging_duration": "O", "primary_mixing_duration": "P", "net_aging_duration": "Q", "mass_loss": "X"} | {"m0": "AK", "m1": "AL", "m3": "AM", "mass": "AJ", "density": "BE", "d_count": "AP", "dm": "AQ", "dg": "AT", "sigma_g": "AS"} | \[\] |
| SAME Ground Test Results | {"inlet_velocity": "K", "heater_resistance_ratio": "L", "heating_duration": "M", "primary_aging_duration": "N", "primary_mixing_duration": "O"} | {"m0": "AS", "m1": "AJ", "m3": "AL", "mass": "AR", "density": "AW", "d_count": "AN", "dm": "AP"} | \[\] |
| Gnd Verif. 8-2012 | {"inlet_velocity": "K", "heater_resistance_ratio": "L", "heating_duration": "M", "primary_aging_duration": "N", "primary_mixing_duration": "O", "net_aging_duration": "R", "secondary_aging_duration": "AF"} | {"m0": "BD", "m1": "BE", "mass": "BH", "density": "BW", "d_count": "BI", "dm": "BJ", "dg": "BN", "sigma_g": "BM"} | \["U", "V", "W", "AB", "AH", "AI", "AJ", "AM"\] |
| Drum 8-2012 | {"inlet_velocity": "K", "heater_resistance_ratio": "L", "heating_duration": "M", "primary_aging_duration": "N", "primary_mixing_duration": "O", "net_aging_duration": "R", "secondary_aging_duration": "AF"} | {"m0": "BD", "m1": "BE", "mass": "BH", "density": "BW", "d_count": "BI", "dm": "BJ", "dg": "BN", "sigma_g": "BM"} | \["U", "V", "W", "AB", "AH", "AI", "AJ", "AM"\] |

## 量的物理意義

- m0: Source calibrated/corrected particle number concentration; source label #/cm^3 where explicit.
- m1: SAME-R BE and SAME AL explicitly mm/cm^3; multiply numeric value by1000 for um/cm^3. Do not confuse diameter with this concentration moment.
- m3: Some source headers say M3 without units; source values/formulas retained with unknown unit until explicit dimensional source audit.
- density: Source particle-density lookup, not independently measured per trial. SAME-R BW uses AA146:AC150 column3.
- dm: BJ (SAME-R) and AQ (SAME flight) are cached source-derived diameters, not independent measured targets.
- closure: BD/BH/BW -> BJ is same-source algebraic closure; not external validation.
- source_errors: Original formula errors, previous-row references and stale caches retained; no Kapton90 repair.

- Power/enable/state flags must accompany sensor values. Power0 does not mean no smoke.
- A scalar source summary n/y is not a full time-resolved sensor state.
- No campaign flags transferred between Run23 and Run60.

## 遙測的實際表頭

| 原始欄號 | 表頭 | 表頭提供單位 | 角色 | 限制 |
| --- | --- | --- | --- | --- |
| 1 | TimeString | Unknown（來源未提供／尚未核對） | stored calendar/day-of-year time label | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 2 | Time | Unknown（來源未提供／尚未核對） | numeric acquisition time, seconds changes corroborated by TimeString | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 3 | RunMode | Unknown（來源未提供／尚未核對） | recorded controller/status/command field; code/polarity requires documentation | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 4 | TestNumber | Unknown（來源未提供／尚未核對） | recorded metadata/counter; exact meaning retained from header | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 5 | ElapsedTestTime(Secs) | Secs | recorded metadata/counter; exact meaning retained from header | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 6 | SampleNumber | Unknown（來源未提供／尚未核對） | recorded metadata/counter; exact meaning retained from header | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 7 | CarouselNumber | Unknown（來源未提供／尚未核對） | recorded metadata/counter; exact meaning retained from header | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 8 | DriveKBRemaining | Unknown（來源未提供／尚未核對） | recorded metadata/counter; exact meaning retained from header | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 9 | CycleCounter | Unknown（來源未提供／尚未核對） | recorded metadata/counter; exact meaning retained from header | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 10 | WatchdogReset | Unknown（來源未提供／尚未核對） | recorded metadata/counter; exact meaning retained from header | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 11 | EnetSelect | Unknown（來源未提供／尚未核對） | recorded metadata/counter; exact meaning retained from header | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 12 | EnetOverride | Unknown（來源未提供／尚未核對） | recorded metadata/counter; exact meaning retained from header | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 13 | OKStatus | Unknown（來源未提供／尚未核對） | recorded metadata/counter; exact meaning retained from header | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 14 | EventSet | Unknown（來源未提供／尚未核對） | recorded controller/status/command field; code/polarity requires documentation | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 15 | EventCode | Unknown（來源未提供／尚未核對） | recorded controller/status/command field; code/polarity requires documentation | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 16 | TestRunning | Unknown（來源未提供／尚未核對） | recorded controller/status/command field; code/polarity requires documentation | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 17 | 12VDCHeaterEnable | Unknown（來源未提供／尚未核對） | recorded controller/status/command field; code/polarity requires documentation | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 18 | HeatingInProgress | Unknown（來源未提供／尚未核對） | recorded controller/status/command field; code/polarity requires documentation | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 19 | SampleHeaterOverride | Unknown（來源未提供／尚未核對） | recorded metadata/counter; exact meaning retained from header | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 20 | GasPlumeTemperature(DegC) | DegC | recorded sensor/instrument output; physical calibration not independently established here | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 21 | SampleResistance(Ohms) | Ohms | recorded sensor/instrument output; physical calibration not independently established here | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 22 | ISSDetectorObscurationMeasurement(Volts) | Volts | recorded sensor/instrument output; physical calibration not independently established here | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 23 | ISSDetectorScatterMeasurement(Volts) | Volts | recorded sensor/instrument output; physical calibration not independently established here | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 24 | STSDetectorMeasurement(Volts) | Volts | recorded sensor/instrument output; physical calibration not independently established here | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 25 | IonDetectorAMeasurement(Volts) | Volts | recorded sensor/instrument output; physical calibration not independently established here | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 26 | IonDetectorBMeasurement(Volts) | Volts | recorded sensor/instrument output; physical calibration not independently established here | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 27 | PTrakMeasurement(PtPerCC) | PtPerCC | recorded sensor/instrument output; physical calibration not independently established here | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 28 | DustTrakAMeasurement(MgPerM3) | MgPerM3 | recorded sensor/instrument output; physical calibration not independently established here | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 29 | DustTrakBMeasurement(MgPerM3) | MgPerM3 | recorded sensor/instrument output; physical calibration not independently established here | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 30 | DustTrakAAnalogMeasurement(Volts) | Volts | recorded sensor/instrument output; physical calibration not independently established here | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 31 | DustTrakBAnalogMeasurement(Volts) | Volts | recorded sensor/instrument output; physical calibration not independently established here | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 32 | LFEFlowRate\[AT08\](SCCM) | SCCM | recorded sensor/instrument output; physical calibration not independently established here | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 33 | VSOSetpoint\[PN23\](Volts) | Volts | recorded metadata/counter; exact meaning retained from header | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 34 | ZeroLFE | Unknown（來源未提供／尚未核對） | recorded metadata/counter; exact meaning retained from header | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 35 | MFCSetpoint(LPM) | LPM | recorded metadata/counter; exact meaning retained from header | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 36 | MFCMassFlowRate(LPM) | LPM | recorded sensor/instrument output; physical calibration not independently established here | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 37 | MFCTemperature(DegC) | DegC | recorded sensor/instrument output; physical calibration not independently established here | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 38 | MFCPressure(PSIA) | PSIA | recorded sensor/instrument output; physical calibration not independently established here | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 39 | MFCAnalogSetpoint\[BN19\](LPM) | LPM | recorded metadata/counter; exact meaning retained from header | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 40 | MFCAnalogFlowRate(LPM) | LPM | recorded sensor/instrument output; physical calibration not independently established here | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 41 | GN2MainPressure\[PN02\](PSIA) | PSIA | recorded sensor/instrument output; physical calibration not independently established here | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 42 | GN2RegulatedPressure\[PN12\](PSIG) | PSIG | recorded sensor/instrument output; physical calibration not independently established here | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 43 | VacuumPressure\[VR04\](PSIA) | PSIA | recorded sensor/instrument output; physical calibration not independently established here | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 44 | DriveSidePressure\[BN02\](PSIA) | PSIA | recorded sensor/instrument output; physical calibration not independently established here | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 45 | SampleSidePressure\[AT20\](PSIA) | PSIA | recorded sensor/instrument output; physical calibration not independently established here | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 46 | ThermalPrecipitatorPreAgeChannel | Unknown（來源未提供／尚未核對） | recorded metadata/counter; exact meaning retained from header | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 47 | ThermalPrecipitatorPostAgeChannel | Unknown（來源未提供／尚未核對） | recorded metadata/counter; exact meaning retained from header | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 48 | PTrakState | Unknown（來源未提供／尚未核對） | recorded controller/status/command field; code/polarity requires documentation | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 49 | PTrakKeySelect | Unknown（來源未提供／尚未核對） | recorded controller/status/command field; code/polarity requires documentation | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 50 | PTrakPowerMeasurement(Volts) | Volts | recorded sensor/instrument output; physical calibration not independently established here | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 51 | DustTrakAState | Unknown（來源未提供／尚未核對） | recorded controller/status/command field; code/polarity requires documentation | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 52 | DustTrakAKeySelect | Unknown（來源未提供／尚未核對） | recorded controller/status/command field; code/polarity requires documentation | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 53 | DustTrakBState | Unknown（來源未提供／尚未核對） | recorded controller/status/command field; code/polarity requires documentation | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 54 | DustTrakBKeySelect | Unknown（來源未提供／尚未核對） | recorded controller/status/command field; code/polarity requires documentation | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 55 | ProximitySensor1(Volts) | Volts | proximity analog voltage; no source mapping or threshold established | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 56 | ProximitySensor2(Volts) | Volts | proximity analog voltage; no source mapping or threshold established | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 57 | ProximitySensor4(Volts) | Volts | proximity analog voltage; no source mapping or threshold established | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 58 | CarouselProximitySensor(Volts) | Volts | proximity analog voltage; no source mapping or threshold established | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 59 | MixingFanPower | Unknown（來源未提供／尚未核對） | recorded controller/status/command field; code/polarity requires documentation | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 60 | PTrakPower | Unknown（來源未提供／尚未核對） | recorded controller/status/command field; code/polarity requires documentation | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 61 | DustTrakAPower | Unknown（來源未提供／尚未核對） | recorded controller/status/command field; code/polarity requires documentation | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 62 | DustTrakBPower | Unknown（來源未提供／尚未核對） | recorded controller/status/command field; code/polarity requires documentation | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 63 | STSDetectorPower | Unknown（來源未提供／尚未核對） | recorded controller/status/command field; code/polarity requires documentation | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 64 | CarouselPower | Unknown（來源未提供／尚未核對） | recorded controller/status/command field; code/polarity requires documentation | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 65 | PositionerEnable | Unknown（來源未提供／尚未核對） | recorded controller/status/command field; code/polarity requires documentation | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 66 | PositionerDirectionIn | Unknown（來源未提供／尚未核對） | recorded controller/status/command field; code/polarity requires documentation | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 67 | PositionerClock | Unknown（來源未提供／尚未核對） | recorded controller/status/command field; code/polarity requires documentation | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 68 | GN2MainSolenoid\[PN03\] | Unknown（來源未提供／尚未核對） | recorded controller/status/command field; code/polarity requires documentation | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 69 | GateEnableSolenoid\[PN07\] | Unknown（來源未提供／尚未核對） | recorded controller/status/command field; code/polarity requires documentation | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 70 | InletGateSolenoid\[BN08\] | Unknown（來源未提供／尚未核對） | recorded controller/status/command field; code/polarity requires documentation | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 71 | OutletGateSolenoid\[BN09\] | Unknown（來源未提供／尚未核對） | recorded controller/status/command field; code/polarity requires documentation | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 72 | PistonControlSolenoid\[BN17\] | Unknown（來源未提供／尚未核對） | recorded controller/status/command field; code/polarity requires documentation | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 73 | DynamicDilutorSolenoid\[PN15\] | Unknown（來源未提供／尚未核對） | recorded controller/status/command field; code/polarity requires documentation | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 74 | PTrakSolenoid\[VR06\] | Unknown（來源未提供／尚未核對） | recorded controller/status/command field; code/polarity requires documentation | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 75 | CommDiagASolenoid\[VR11\] | Unknown（來源未提供／尚未核對） | recorded controller/status/command field; code/polarity requires documentation | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 76 | CommDiagBSolenoid\[VR12\] | Unknown（來源未提供／尚未核對） | recorded controller/status/command field; code/polarity requires documentation | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 77 | CommDiagADilutionSolenoid\[PN24\] | Unknown（來源未提供／尚未核對） | recorded controller/status/command field; code/polarity requires documentation | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 78 | CommDiagBDilutionSolenoid\[PN27\] | Unknown（來源未提供／尚未核對） | recorded controller/status/command field; code/polarity requires documentation | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 79 | PurgeSolenoid\[VM09\] | Unknown（來源未提供／尚未核對） | recorded controller/status/command field; code/polarity requires documentation | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 80 | PistonGN2Solenoid\[BN18\] | Unknown（來源未提供／尚未核對） | recorded controller/status/command field; code/polarity requires documentation | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 81 | PistonVentSolenoid\[BN20\] | Unknown（來源未提供／尚未核對） | recorded controller/status/command field; code/polarity requires documentation | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 82 | PistonVacuumSolenoid\[BN16\] | Unknown（來源未提供／尚未核對） | recorded controller/status/command field; code/polarity requires documentation | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 83 | ThermalPrecipitatorSolenoid\[VM06\] | Unknown（來源未提供／尚未核對） | recorded controller/status/command field; code/polarity requires documentation | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 84 | ThermalPrecipitatorPreAgeHeater | Unknown（來源未提供／尚未核對） | recorded metadata/counter; exact meaning retained from header | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 85 | ThermalPrecipitatorPostAgeHeater | Unknown（來源未提供／尚未核對） | recorded metadata/counter; exact meaning retained from header | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 86 | ThermalPrecipitatorPreAgeValve | Unknown（來源未提供／尚未核對） | recorded metadata/counter; exact meaning retained from header | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 87 | ThermalPrecipitatorPostAgeValve | Unknown（來源未提供／尚未核對） | recorded metadata/counter; exact meaning retained from header | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 88 | ThermalPrecipitatorPreAgeCableSense | Unknown（來源未提供／尚未核對） | recorded metadata/counter; exact meaning retained from header | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 89 | ThermalPrecipitatorPostAgeCableSense | Unknown（來源未提供／尚未核對） | recorded metadata/counter; exact meaning retained from header | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 90 | STSDetectorSelfTest | Unknown（來源未提供／尚未核對） | recorded metadata/counter; exact meaning retained from header | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 91 | STSDetectorAlarmReset | Unknown（來源未提供／尚未核對） | recorded metadata/counter; exact meaning retained from header | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 92 | STSDetectorAlarm | Unknown（來源未提供／尚未核對） | recorded metadata/counter; exact meaning retained from header | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 93 | ISSDetectorSelfTest | Unknown（來源未提供／尚未核對） | recorded metadata/counter; exact meaning retained from header | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 94 | VideoPower | Unknown（來源未提供／尚未核對） | recorded controller/status/command field; code/polarity requires documentation | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 95 | VideoRecording | Unknown（來源未提供／尚未核對） | recorded metadata/counter; exact meaning retained from header | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 96 | VideoPaused | Unknown（來源未提供／尚未核對） | recorded metadata/counter; exact meaning retained from header | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 97 | CameraPower | Unknown（來源未提供／尚未核對） | recorded controller/status/command field; code/polarity requires documentation | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |
| 98 | IlluminationLEDPower | Unknown（來源未提供／尚未核對） | recorded controller/status/command field; code/polarity requires documentation | Do not replace source codes, sentinel values or negative voltage offsets with physical zeros. |

校正狀態：Headers provide engineering units but do not establish run-specific calibration, standard flow reference state, dilution correction or sensor latency.
