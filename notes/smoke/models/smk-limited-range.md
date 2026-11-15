# SMK-LIMITED-RANGE Lognormal moment fraction between detector cutoffs

## 公式與來源

`eta(D)=[ln(D/Dg)-k*ln(sigma)^2]/[sqrt(2)*ln(sigma)]; F_k(Dlo,Dhi)=0.5*[erf(eta_hi)-erf(eta_lo)]`

- study_ids: ["PSI-101"]
- report: Smoke Aerosol Measurement Experiment Re-flight (SAMER)
- edition: June2,2014 FinalReport
- sha256: 65381e2715eb7379113dd1b9c550baaa5fa5a247dba00419123143aa98ef80d6
- locators: ["AppendixFphysicalp74Eqs1–2", "physicalp75Eq6", "physicalp77calibration/density", "physicalpp28–30finite-range moments"]


## 使用哪些量與單位

### 輸入

- Dg,Dlo,Dhi: same lengthunit
- sigma_g: dimensionless>1
- k: moment order


### 輸出

- fraction: dimensionless[0,1]


## 對應展示程式

- physics.py::moment_fraction


互動入口為 `viewer.html`；圖形邏輯為 `viewer.js`。沒有 planned_functions 的條目沒有完整數值求解器，不能宣稱已算出預測。

## 比較分類與獨立性

狀態：executable_conditionally。比較角色：conditional_derived_quantity。

- A detector range fraction is not a detector voltage/alarm prediction; requires validated response/efficiency kernel to compare signals.


## 限制與消防解讀

- Momentorderk differs from characteristicdiameterp=0.5/1.5 notation.
- Cutoff corrections are not automatically valid for nonspherical/agglomerated or non-lognormal smoke.


這個公式只能支持其觀測量與閉合假設範圍；不直接輸出警報效能、通用消防安全或產品資格。
