# SMK-LOGNORMAL-INVERSE Lognormal inverse from characteristic diameters

## 公式與來源

`Dg=sqrt(d_count^3/dm); sigma_g=exp(sqrt(ln(dm/d_count)))`

- study_ids: ["PSI-102", "PSI-101"]
- report: Smoke Aerosol Measurement Experiment (SAME): Final Report
- edition: March15,2010; physicalpp15–19 correspond to printedpp5–9
- sha256: af91c96d22d93bbefbc0f2c5e1cc06e24813f532e5379b3fec9f121cccb22193
- locators: ["physicalp15Eqs1–2d", "physicalp16Eq2f,Eq3", "physicalp17Eq6", "physicalp18Eqs7–9", "physicalp19Eqs10–13", "physicalpp22–24calibrationFigs7–9"]


## 使用哪些量與單位

### 輸入

- d_count: um
- dm: um


### 輸出

- dg: um
- sigma_g: dimensionless>=1


## 對應展示程式

- physics.py::lognormal_parameters


互動入口為 `viewer.html`；圖形邏輯為 `viewer.js`。沒有 planned_functions 的條目沒有完整數值求解器，不能宣稱已算出預測。

## 比較分類與獨立性

狀態：executable_conditionally。比較角色：measurement_inversion。

- Require lognormal assumption and valid compatible moments. Parameters reconstructed fromM0/M1/M3 do not independently predict those same moments.


## 限制與消防解讀

- dm>=d_count>0; no absolute-value repair of invalid negative logarithm.
- sigma=1 is a monodisperse limit; do not evaluate an ordinary continuous PDF with ln(sigma)=0.
- SAMERAppendixFEq7ambiguoustypography is preserved; executable formula uses unambiguous SAME2010 Eqs7–10.


這個公式只能支持其觀測量與閉合假設範圍；不直接輸出警報效能、通用消防安全或產品資格。
