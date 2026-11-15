# SMK-MOMENT-RATIOS Moment-ratio characteristic diameters

## 公式與來源

`M_k=integral D^k f_N(D)dD; d_count=M1/M0; d_average_mass=(M3/M0)^(1/3)`

- study_ids: ["PSI-102", "PSI-101"]
- report: Smoke Aerosol Measurement Experiment (SAME): Final Report
- edition: March15,2010; physicalpp15–19 correspond to printedpp5–9
- sha256: af91c96d22d93bbefbc0f2c5e1cc06e24813f532e5379b3fec9f121cccb22193
- locators: ["physicalp15Eqs1–2d", "physicalp16Eq2f,Eq3", "physicalp17Eq6", "physicalp18Eqs7–9", "physicalp19Eqs10–13", "physicalpp22–24calibrationFigs7–9"]


## 使用哪些量與單位

### 輸入

- m0: particles/cm3
- m1: um/cm3 after explicit conversion
- m3: um3/cm3


### 輸出

- d_count: um
- dm: um


## 對應展示程式

- physics.py::moment_diameters


互動入口為 `viewer.html`；圖形邏輯為 `viewer.js`。沒有 planned_functions 的條目沒有完整數值求解器，不能宣稱已算出預測。

## 比較分類與獨立性

狀態：executable_after_unit_calibration_range_gate。比較角色：measurement_inversion。

- Requires compatible calibrated same-sample moments. Not a prediction of moments from material/flow.


## 限制與消防解讀

- No lognormal assumption required for the two diameter ratios.
- M3 is a size moment, not a mass concentration until density/geometric conversion is supplied.
- d_average_mass is cube-mean diameter, not mass-weighted meanD43.


這個公式只能支持其觀測量與閉合假設範圍；不直接輸出警報效能、通用消防安全或產品資格。
