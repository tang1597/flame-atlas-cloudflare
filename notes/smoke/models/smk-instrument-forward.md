# SMK-INSTRUMENT-FORWARD Raw-signal / calibrated-moment response

## 公式與來源

`S_j=integral K_j(D,material,configuration)*f_N(D)dD only as observation-operator notation; source calibration correlations are size/material dependent`

- SAME: {"study_ids": ["PSI-102", "PSI-101"], "report": "Smoke Aerosol Measurement Experiment (SAME): Final Report", "edition": "March15,2010; physicalpp15–19 correspond to printedpp5–9", "sha256": "af91c96d22d93bbefbc0f2c5e1cc06e24813f532e5379b3fec9f121cccb22193", "locators": ["physicalp15Eqs1–2d", "physicalp16Eq2f,Eq3", "physicalp17Eq6", "physicalp18Eqs7–9", "physicalp19Eqs10–13", "physicalpp22–24calibrationFigs7–9"]}
- SAMER: {"study_ids": ["PSI-101"], "report": "Smoke Aerosol Measurement Experiment Re-flight (SAMER)", "edition": "June2,2014 FinalReport", "sha256": "65381e2715eb7379113dd1b9c550baaa5fa5a247dba00419123143aa98ef80d6", "locators": ["AppendixFphysicalp74Eqs1–2", "physicalp75Eq6", "physicalp77calibration/density", "physicalpp28–30finite-range moments"]}


## 使用哪些量與單位

### 輸入

- kernel: source-fixed complete response/calibration and configuration
- PSD: same-sample compatibledistribution


### 輸出

- signal: instrument-specific volts/counts/proxy


## 對應展示程式

Unknown；此處沒有補入推測值。


互動入口為 `viewer.html`；圖形邏輯為 `viewer.js`。沒有 planned_functions 的條目沒有完整數值求解器，不能宣稱已算出預測。

## 比較分類與獨立性

狀態：unavailable_as_complete_fixed_NASA_case。比較角色：not_testable_missing_inputs。

- Need actual coefficients or response kernel, gain/dilution/size cutoffs, active-state/response mapping and unused response target. Do not fit missing coefficients.


## 限制與消防解讀

- PTrak/M1/DustTrak measurements are not interchangeable raw signals.
- DustTrakM3 needs size-dependent calibration and source report describes iterative correction; no new iterative calibration fitting authorized.
- MPASS historical fits are source empirical relations, not independently validated physical predictors.


這個公式只能支持其觀測量與閉合假設範圍；不直接輸出警報效能、通用消防安全或產品資格。
